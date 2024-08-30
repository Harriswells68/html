from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# Display your index page
@app.route("/")
def index():
    return render_template('static/template/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5540)