def square(s):
    return s * s
print"""<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Bangun Geometri</title>
</head>
<body>
    <style>
        table td{
            padding: 10px 0;
        }
        img{
            margin: 0 10px;
        }
        tr td:nth-child(1){
            width:40%;
        }
        tr td:nth-child(2){
            width:10%;
        }
        tr td:nth-child(3){
            width:30%;
        }
    </style>
    <img style="float:left;" src="../we.jpg" width="400" alt="image">
    <h1>Bangun Geometri</h1>
    <table>
        <tr>
            <td>Nama Bangun</td>
            <td>:</td>
            <td>Persegi</td>
        </tr>
        <tr>
            <td>Dimensi</td>
            <td>:</td>
            <td>2D</td>
        </tr>
        <tr>
            <td>Rumus luas</td>
            <td>:</td>
            <td>s x s<td>
        </tr>
        <tr>
            <td>Parameter 1</td>
            <td>:</td>
            <td>"""
print 4
print """</td>
        </tr>
        <tr>
            <td>Luas</td>
            <td>:</td>
            <td>"""
print square(4)
print """</td>
        </tr>
    </table>
</body>
</html>
"""
