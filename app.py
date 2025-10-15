from flask import Flask, send_from_directory, request, redirect, url_for, abort
import json
import os

# Constants
DATA_FILE = os.path.join('static', 'dpets.json')

# Ensure dpets.json exists
if not os.path.exists(DATA_FILE):
    os.makedirs('static', exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

app = Flask(__name__, static_folder='static', static_url_path='/static')


# Serve HTML pages (must be in root dir)
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

# Serve CSS/JS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(os.path.join('static', 'css'), filename)

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory(os.path.join('static', 'js'), filename)

# Serve images
@app.route('/images/<path:filename>')
def pet_images(filename):
    return send_from_directory(os.path.join('static', 'images'), filename)

# Catch common direct file/image access
@app.route('/<filename>')
def root_images(filename):
    if filename.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        return send_from_directory('.', filename)
    return "File not found", 404

# Handle form submission and always update static/dpets.json
@app.route('/submit_pet', methods=['POST'])
def submit_pet():
    with open(DATA_FILE, 'r') as f:
        try:
            pets = json.load(f)
        except Exception:
            pets = []

    new_id = max((p.get('id', 0) for p in pets), default=0) + 1

    # Optional: upload image if included
    img = request.files.get('image')
    img_path = f'static/images/{img.filename}' if img else ''
    if img:
        os.makedirs(os.path.join('static', 'images'), exist_ok=True)
        img.save(img_path)

    new_pet = {
        "id": new_id,
        "name": request.form.get('name', ''),
        "type": request.form.get('type', ''),
        "breed": request.form.get('breed', ''),
        "age": request.form.get('age', ''),
        "gender": request.form.get('gender', ''),
        "color": request.form.get('color', ''),
        "weight": request.form.get('weight', ''),
        "location": request.form.get('location', ''),
        "vaccinated": 'vaccinated' in request.form,
        "neutered": 'neutered' in request.form,
        "friendlyWith": request.form.getlist('friendlyWith'),
        "specialNeeds": request.form.get('specialNeeds', ''),
        "description": request.form.get('description', ''),
        "image": img_path,
        "status": request.form.get('status', ''),
        "owner": {
            "name": request.form.get('owner_name', ''),
            "contact": request.form.get('owner_contact', ''),
            "phone": request.form.get('owner_phone', '')
        }
    }
    pets.append(new_pet)

    with open(DATA_FILE, 'w') as f:
        json.dump(pets, f, indent=4)
    return redirect(url_for('lostfound'))

if __name__ == '__main__':
    # Always bind to 0.0.0.0 for Docker/EC2
    app.run(host="0.0.0.0", port=5000, debug=True)


