from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def port():
    return render_template("port.html")

if __name__ == '__main__':
      app.run(port=8085, host='0.0.0.0', debug=True, threaded=True)