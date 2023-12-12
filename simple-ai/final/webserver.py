from flask import Flask
from flask import request
from os import system

IP = "127.0.0.1"

app = Flask(__name__)

@app.route("/interface")
def ai_request():
    r = request.args.get("r")
    g = request.args.get("g")
    b = request.args.get("b")
    input = f"{r}\n{g}\n{b}"
    
    with open("input.txt", "w") as f:
        f.write(input)
    
    system("cargo run")
    output = None
    
    with open("result.txt", "r") as f:
        output = f.readline()
    
    return output

if __name__ == "__main__":
    app.run(port=3000, host=IP)