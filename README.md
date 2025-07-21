# 🎨 AI Color Palette Generator

A Flask-based web application that uses AI to generate aesthetic color palettes from uploaded images.

## 🌐 Live Demo

🚀 [View Live App on Render](https://ai-color-palette-generator-project.onrender.com/)

## 📂 Project Structure

AI-color-palette-generator

├── api/

│ ├── index.py # Main Flask app

│ ├── utils.py # Palette extraction logic

│ ├── requirements.txt # Python dependencies

│

├── static/

│ ├── css/ # Styles and background images

│ ├── uploads/ # Uploaded user images (excluded from Git)

│ └── palettes/ # Generated palettes (excluded from Git)

│

├── templates/

│ └── index.html # Main HTML template

│

├── .gitignore

└── README.md


---

## 🛠️ Features

- 🔼 Upload any image
- 🎨 Automatically generate a matching aesthetic color palette
- 🧠 Uses AI (KMeans clustering) to extract dominant colors
- 💾 Saves uploaded images and generated palettes
- 🖌️ Beautiful frontend interface with custom CSS

---

## 🚀 Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-color-palette-generator.git
cd ai-color-palette-generator
```
2. Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3.Install Dependencies
```
cd api
pip install -r requirements.txt
```
4. Create .env file (optional for local dev)
```
PORT=5000
```
5. Run the App
```
python index.py
Visit http://localhost:5000
```
🧠 Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS (custom)
AI: KMeans clustering (scikit-learn, OpenCV)
Hosting: Render.com

🧹 .gitignore
```
__pycache__/
.env
/static/uploads/
/static/palettes/
```
📸 Sample Usage
Upload an image (JPG, PNG, etc.)
The app processes the image and generates a 5-color palette.
Palette is displayed and saved in static/palettes/.

🤝 Contributions
```
PRs and issues welcome! Feel free to fork and enhance the project.
```
📜 License
```
MIT License
```
👤 Author
Name: Nehal Gupta

GitHub: @beingnehallish


### ✅ To Complete:
```
- Replace `https://<your-app-name>.onrender.com` with your actual Render URL
- Replace GitHub username link if you're publishing
```
