from flask import Flask

app = Flask("abc")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"