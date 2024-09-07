from flask import Flask, render_template, jsonify, request, after_this_request
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder='/workspaces/html/templates')
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'

qk={
    1:"q1",
    2:"q2",
    3:"q3",
    4:"q4"
}

ak=[]

@app.route("/", methods=['GET', 'POST'])
@cross_origin(origin='*')
def index():
    question_data = {1: qk[1]} # Return JSON if requested as JSON
    return render_template('index.html', q1=question_data)

@app.route('/answer', methods=["POST", "GET"])
@cross_origin(origin='*')
def process():
    if request.method == 'POST':
        data=(request.json)
        ak.append(list(data.items()))
        print(ak)
        return jsonify({(int(list(data.keys())[0])+1):qk[int(list(data.keys())[0])+1]})
    else:
        return jsonify({1:"We Will See It"})