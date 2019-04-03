from flask import Flask
from flask import request
import math
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello world"
@app.route('/area')
def area():
    return str(int(request.args.get('radio')) ** 2 * math.pi)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
