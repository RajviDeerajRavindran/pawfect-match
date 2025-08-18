from flask import Flask, send_from_directory, request, redirect, url_for
import json

app = Flask(__name__, static_folder='')

DATA_FILE = 'dpets.json'

# Serve HTML pages
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/adopt.html')
def adopt():
    return send_from_directory('', 'adopt.html')

@app.route('/strays.html')
def strays():
    return send_from_directory('', 'strays.html')

@app.route('/lostfound.html')
def lostfound():
    return send_from_directory('', 'lostfound.html')

@app.route('/about.html')
def about():
    return send_from_directory('', 'about.html')

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

@app.route('/<filename>')
def root_images(filename):
    if filename.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        return send_from_directory('', filename)
    return "File not found", 404

# Handle form submission
@app.route('/submit_pet', methods=['POST'])
def submit_pet():
    with open(DATA_FILE, 'r') as f:
        pets = json.load(f)

    new_id = max(p['id'] for p in pets) + 1 if pets else 1

    # Optional: upload image if included
    img = request.files.get('image')
    img_path = f'images/{img.filename}' if img else ''
    if img:
        img.save(f'images/{img.filename}')

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

if __name__ == '__main__':
    app.run(debug=True)
