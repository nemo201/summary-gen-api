from flask import Flask
from summary_gen import generate_summary 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/summary/<string:n>")
def gen(n):
    return generate_summary(n)

if __name__=="__main__":
    app.run(debug=True)
