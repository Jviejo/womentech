from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/tabla')
def hello_world():
    numero = int(request.args.get('numero'))
    detalle = list(map( lambda x :f'<tr><td>{numero}</td><td>{x}</td><td>{numero*x}</td></tr>' , range(1, 11 )))
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <title>Document</title>
    </head>
    <body>
        <table class="table">
            {''.join(detalle)}
        </table>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
