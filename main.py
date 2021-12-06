from flask import Flask
from summary_gen import generate_summary
import flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/summary/<string:n>")
def gen(n):
    val=generate_summary(n)
    return flask.jsonify(summary=val)

if __name__=="__main__":
    app.run(debug=True)
