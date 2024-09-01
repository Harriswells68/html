from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='static/templates')
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'

@app.route("/login", methods=['GET', 'POST'])
@cross_origin(origin='*')
def index():
    question_data = {"q": "My Question"} # Return JSON if requested as JSON
    return render_template('index.html', question=(question_data))  # Otherwise, return the HTML template

@app.route("/question", methods=["OPTIONS, POST"])
@cross_origin(origin='*')
def questions():
    return jsonify({"question":"Hello?"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
