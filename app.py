import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def apply_filter(image_path, filter_type):
    """Aplica filtros na imagem e salva o resultado."""
    img = cv2.imread(image_path)

    if filter_type == "blur":
        img = cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_type == "sharpen":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        img = cv2.filter2D(img, -1, kernel)
    elif filter_type == "rotate":
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
        img = cv2.warpAffine(img, matrix, (w, h))

    processed_path = os.path.join(UPLOAD_FOLDER, "processed.png")
    cv2.imwrite(processed_path, img)
    return processed_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return redirect(request.url)

        file = request.files["image"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], "original.png")
            file.save(filepath)
            return render_template("index.html", uploaded_image="original.png")

    return render_template("index.html")

@app.route("/process/<filter_type>")
def process(filter_type):
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], "original.png")
    if not os.path.exists(image_path):
        return "Nenhuma imagem foi carregada!", 400

    processed_image = apply_filter(image_path, filter_type)
    return render_template("index.html", uploaded_image="original.png", processed_image="processed.png")

if __name__ == "__main__":
    app.run(debug=True)
