from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, welcome to my small website!"

if __name__ == '__main__':
    app.run(debug=True)
