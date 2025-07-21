from flask import Flask, request, render_template, send_from_directory
from utils import extract_colors, save_palette_as_image
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')
PALETTE_FOLDER = os.path.join(app.static_folder, 'palettes')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PALETTE_FOLDER, exist_ok=True)

def rgb_to_hex(color):
    return '#%02x%02x%02x' % tuple(color)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(path)

        colors = extract_colors(path)
        hex_colors = [rgb_to_hex(color) for color in colors]

        palette_path = os.path.join(PALETTE_FOLDER, f'palette_{image.filename}.png')
        save_palette_as_image(colors, palette_path)

        return render_template('index.html', palette_image=f'palettes/palette_{image.filename}.png', hex_colors=hex_colors)

    return render_template('index.html', palette_image=None)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
