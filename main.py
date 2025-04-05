from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from translator import translation

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    data = request.get_json()
    text = data.get("text")
    target_lang = data.get("target_lang", "hi")
    
    trans = translation(text, target_lang)
    result = trans.translate_word()
    return {"Result": result}

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
