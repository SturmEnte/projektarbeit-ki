from flask import Flask
from flask import request
from flask import Response
from os import system

IP = "127.0.0.1"

app = Flask(__name__)

def return_file(path):
    content = ""
    with open(path, encoding="utf-8") as f:
        content = f.read()
    return content

@app.route("/interface")
def ai_request():
    r = request.args.get("r")
    g = request.args.get("g")
    b = request.args.get("b")
    input = f"{r};{g};{b}"
    
    with open("input.txt", "w") as f:
        f.write(input)
    
    system("cargo run")
    output = None
    
    with open("result.txt", "r") as f:
        output = f.readline()
    
    return output

# index page
@app.route("/")
def index():
    return return_file("website/index.html")

@app.route("/main.js")
def index_js():
    return Response(return_file("website/main.js"), mimetype="text/js")

@app.route("/style.css")
def index_css():
    return Response(return_file("website/style.css"), mimetype="text/css")

# about page
@app.route("/about-site/")
def about():
    return return_file("website/about-site/index.html")

@app.route("/about-site/style.css")
def about_css():
    return Response(return_file("website/about-site/style.css"), mimetype="text/css")


if __name__ == "__main__":
    app.run(port=3000, host=IP)