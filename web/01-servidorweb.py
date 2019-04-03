from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return """
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
    <h1>Resumen de facturación</h1>
    <h2>Importe facturas por cliente</h2>
    <table class="table">
        <thead>
            <tr>
                <td>Codigo</td>
                <td>Nombre</td>
                <td>Importe</td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>CLIENTE NUMERO 1</td>
                <td>1235,99</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
    """
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
