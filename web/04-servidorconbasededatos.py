from flask import Flask
from flask import request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")

app = Flask(__name__)
def lineaDetalle(row):
    linea =  f"""
     <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td class="text-right">{str(round(row[2],2))}</td>
    </tr>
    """
    return linea
def cliente(codigo):
    cur = conn.cursor()
    try:
        cur.execute("select * from customers where customerid = %s", (codigo,))
    except psycopg2.DatabaseError as error:
       return 'no puedo ...'
    row = cur.fetchone()
    return row
@app.route('/')
def hello_world():
    return "hello world"

@app.route('/facturas')
def facturas():
    codigo = request.args.get('codigo')
    cli = cliente(codigo)
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
<body class="container">
    <h1>Facturas del cliente {codigo}: {cli[1]}</h1>
    <h2>Lista de facturas</h2>
    <table class="table">
        <thead>
            <tr>
                <td>Codigo</td>
                <td>Fecha</td>
                <td>Importe</td>
            </tr>
        </thead>
        <tbody>
            
        </tbody>
    </table>
</body>
</html>
"""
@app.route('/clientes')
def datos():
    cur = conn.cursor()
    try:
        cur.execute("""select c.CUSTOMERID, c.COMPANYNAME,
                        sum( UNITPRICE * QUANTITY * (1- DISCOUNT)) importe
                        FROM CUSTOMERS c
                        INNER JOIN ORDERS o
                        INNER JOIN ORDER_DETAILS d
                            on o.ORDERID = d.ORDERID
                            on c.CUSTOMERID = o.CUSTOMERID
                    group by c.CUSTOMERID, c.COMPANYNAME
                    order by c.COMPANYNAME"""
                    )
    except:
       return 'no puedo ...'
    rows = cur.fetchall()
    detalle = ''
    for i in rows:
        detalle += lineaDetalle(i)
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
<body class="container">
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
            {detalle}
        </tbody>
    </table>
</body>
</html>
"""
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
