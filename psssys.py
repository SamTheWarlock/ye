from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def application():
    testvar = logic("test test")
    return testvar
if __name__ == "__main__":
    app.run()
