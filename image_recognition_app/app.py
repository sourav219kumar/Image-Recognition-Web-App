
from flask import Flask, render_template, request
from predict import predict_image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        filename = image.filename
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        display_path = f"{UPLOAD_FOLDER}/{filename}"

        image.save(save_path)
        prediction = predict_image(save_path)

        return render_template("index.html", prediction=prediction, image_path=display_path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

