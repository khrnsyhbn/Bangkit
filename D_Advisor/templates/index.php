<!DOCTYPE html>
<html>
<head>
    <title>Demo Prototype D_Advisor</title>
</head>
<body>
    <div class="logo">
        Welcome to D-Advisor!
    </div>
    <nav>
            <ul>
            <li>
                <a href="{{url_for('index')}}">Home</a> 
            </li>
            <li> | </li>
            <li>
                <a href="">Blog</a>
            </li>
            <li> | </li>
            <li>
                <a href="{{url_for('contact')}}">About Us</a>
            </li>
            <li> | </li>
            <li>
                <a href="">Our history</a>
            </li>
            <li> | </li>
            <li>
            <a href="{{url_for('contact')}}">Contact</a>
            </li>
            </ul>
        </nav>
    <!-- Mengambil nilai dari model -->

    <h2>{{judul}}</h2>
    <p>{{tanggal}}</p>
    <p>{{isi}}</p>

    <style type="text/css">        
        .logo {
            font-size: 200%;
            padding: 50px 20px;
            margin: 0 auto;
            max-width: 1000px;
        }
        body{
            font-family: Arial;
        }
        nav {
            background-color: gray;
            padding: .5em;
            top: 0;
            position: sticky;
        }
        
        nav ul {
            margin: 0;
            padding: 0;
            list-style: none;
            display: flex;
            justify-content: space-between;
        }
        
        nav a {
            color: #fff;
            text-decoration: none;
            padding: .5em 1em;
        }
    </style>
</body>
</html>
