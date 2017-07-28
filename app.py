from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect('http://google.com')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')