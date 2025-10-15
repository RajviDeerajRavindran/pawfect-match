from flask import Flask, send_from_directory, request, redirect, url_for, abort, Response
import json
import os
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY

DATA_FILE = 'dpets.json'
app = Flask(__name__, static_folder='static', static_url_path='/static')

# Ensure dpets.json exists
if not os.path.isfile(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')

@app.before_request
def before_request():
    request.start_time = __import__('time').time()

@app.after_request
def after_request(response):
    request_latency = __import__('time').time() - request.start_time
    REQUEST_LATENCY.observe(request_latency)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.endpoint or 'unknown').inc()
    return response

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain')

@app.route('/health')
def health_check():
    return 'OK', 200

# Serve HTML pages (ensure these files exist in your app root)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/adopt.html')
def adopt():
    return send_from_directory('.', 'adopt.html')

@app.route('/strays.html')
def strays():
    return send_from_directory('.', 'strays.html')

@app.route('/lostfound.html')
def lostfound():
    return send_from_directory('.', 'lostfound.html')

@app.route('/about.html')
def about():
    return send_from_directory('.', 'about.html')

# Serve CSS and JS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

# Serve images
@app.route('/images/<path:filename>')
def pet_images(filename):
    return send_from_directory('images', filename)

# Handle form submission
@app.route('/submit_pet', methods=['POST'])
def submit_pet():
    # Load pet list; create if file missing or empty
    try:
        with open(DATA_FILE, 'r') as f:
            pets = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pets = []

    new_id = max((p['id'] for p in pets), default=0) + 1

    # Optional: upload image if included
    img = request.files.get('image')
    img_path = f'images/{img.filename}' if img else ''
    if img:
        os.makedirs('images', exist_ok=True)
        img.save(img_path)

    new_pet = {
        "id": new_id,
        "name": request.form['name'],
        "type": request.form['type'],
        "breed": request.form['breed'],
        "age": request.form['age'],
        "gender": request.form['gender'],
        "color": request.form['color'],
        "weight": request.form['weight'],
        "location": request.form['location'],
        "vaccinated": 'vaccinated' in request.form,
        "neutered": 'neutered' in request.form,
        "friendlyWith": request.form.getlist('friendlyWith'),
        "specialNeeds": request.form['specialNeeds'],
        "description": request.form['description'],
        "image": img_path,
        "status": request.form['status'],
        "owner": {
            "name": request.form['owner_name'],
            "contact": request.form['owner_contact'],
            "phone": request.form['owner_phone']
        }
    }
    pets.append(new_pet)
    with open(DATA_FILE, 'w') as f:
        json.dump(pets, f, indent=4)
    return redirect(url_for('lostfound'))

# Catch-all route for direct file access/images
@app.route('/<filename>')
def root_images(filename):
    if filename.endswith(('.jpg', '.png', '.jpeg', '.gif', '.webp', '.svg')):
        return send_from_directory('.', filename)
    abort(404)

if __name__ == "__main__":
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(host="0.0.0.0", port=5000, debug=True)


