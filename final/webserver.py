from flask import Flask
from flask import request
from flask import Response
from os import system, chdir, path
import os

IP = "127.0.0.1"

app = Flask(__name__)

def return_file(path):
    content = ""
    mimetype = "text/plain"
    
    if path[-3:] == "css":
        mimetype = "text/css"
    elif path[-2:] == "js":
        mimetype = "text/js"
    elif path[-4:] == "html":
        mimetype = "text/html"

    with open(path, encoding="utf-8") as f:
        content = f.read()
    
    return Response(content, mimetype=mimetype)

def return_apk(path):
    content = ""
    mimetype = "application/webassembly"

    with open(path, "rb") as f:
        content = f.read()
    
    return Response(content, mimetype=mimetype)

## overview
@app.route("/")
def index():
    return return_file("index/index.html")

@app.route("/style.css")
def index_css():
    return return_file("index/style.css")

## color ai

# interface
@app.route("/interface")
def ai_request():
    r = request.args.get("r")
    g = request.args.get("g")
    b = request.args.get("b")
    input = f"{r};{g};{b}"
    
    chdir("color-ai")

    with open("input.txt", "w") as f:
        f.write(input)
    
    if os.name == "nt" and path.exists("color_ai.exe"): # Windows
        system("color_ai.exe")
    elif os.name == "posix" and path.exists("color_ai"): # Linux
        system("color_ai")
    else:
        system("cargo run")

    output = None
    
    with open("result.txt", "r") as f:
        output = f.readline()
    
    chdir("..")
    
    return output

# index page
@app.route("/color-ai/")
def color_index():
    return return_file("color-ai/website/index.html")

@app.route("/color-ai/main.js")
def color_index_js():
    return return_file("color-ai/website/main.js")

@app.route("/color-ai/style.css")
def color_index_css():
    return return_file("color-ai/website/style.css")

# about page
# @app.route("/color-ai/about-site/")
# def color_about():
#     return return_file("color-ai/website/about-site/index.html")

# @app.route("/color-ai/about-site/style.css")
# def color_about_css():
#     return return_file("color-ai/website/about-site/style.css")

## game ai

# index page
@app.route("/game-ai/")
def game_index():
    return return_file("game-ai/web/index.html")

@app.route("/game-ai/final.apk")
def game_index_apk():
    return return_apk("game-ai/web/final.apk")

if __name__ == "__main__":
    app.run(port=3000, host=IP)