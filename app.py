# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
    

@app.route("/keshav")
def hello_world_fancy():
    greetings = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction of Keshav</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            font-size: 16px;
            line-height: 1.6;
            color: #555;
        }
        .highlight {
            font-weight: bold;
            color: #007bff;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Introduction of Keshav</h1>
        <p>Hello, I would like to introduce my brother <span class="highlight">Keshav</span>.</p>
        <p>Keshav is a dedicated and hard-working individual. After completing his Bachelor of Science (<span class="highlight">BSc</span>), he joined <span class="highlight">Wipro</span>, one of the leading companies in the IT industry.</p>
        <p>At Wipro, Keshav has been contributing to various projects, showcasing his skills, knowledge, and passion for technology. He is continuously growing and learning in his career, always striving for excellence.</p>
        <p>We are all very proud of his accomplishments and the positive impact he is making in his field.</p>
        
        <div class="footer">
            <p>Created with love for Keshav!</p>
        </div>
    </div>

</body>
</html>

    """
    return greetings



@app.route("/testpage")
def testpage():
    greetings = """
    <html>
    <body>

    <h1>This is a test page</h1>

    </body>
    </html>
    """
    return greetings

@app.route("/testpagelovely")
def testpage1():
    greetings = """
    <html>
    <body>

    <h1>This is a test page 1 by lovely</h1>

    </body>
    </html>
    """
    return greetings

@app.route("/lovestory")
def testpage2():
    greetings = """
    <html>
    <body>

   <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Love Story</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #ffb6c1;
            text-align: center;
            padding: 20px;
        }
        header h1 {
            color: #fff;
            font-size: 2.5em;
            margin: 0;
        }
        .story-container {
            padding: 30px;
            max-width: 900px;
            margin: 0 auto;
        }
        .couple-photo {
            display: block;
            margin: 30px auto;
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .story-text {
            font-size: 1.2em;
            line-height: 1.6;
            color: #444;
        }
        .highlight {
            color: #ff6f61;
            font-weight: bold;
        }
        footer {
            background-color: #ffb6c1;
            text-align: center;
            padding: 15px;
            margin-top: 50px;
        }
        footer p {
            color: #fff;
            font-size: 1em;
            margin: 0;
        }
    </style>
</head>
<body>

    <header>
        <h1>Our Love Story</h1>
    </header>

    <div class="story-container">
        <img src="https://c1.wallpaperflare.com/preview/109/930/459/love-sunset-young-couple-girl-romantic.jpg" alt="Couple Photo" class="couple-photo">
        
        <div class="story-text">
            <p>Once upon a time, there was a girl named <span class="highlight">Neha</span> who believed in love stories that came from the heart. Neha had always dreamt of meeting someone who could make her laugh, someone who would stand by her through thick and thin, and someone who would understand her soul.</p>

            <p>Then, one fateful day, she met a boy who changed everything. His name was <span class="highlight">Jackson</span>. From the moment they spoke, Neha felt something special, as if their hearts had been connected long before they had met. Their conversations were endless, and every moment they spent together felt like magic.</p>

            <p>As time passed, their bond grew stronger. They shared memories, dreams, and deep conversations under the stars. Neha knew that this was the love she had always dreamed of — a love full of passion, laughter, and understanding.</p>

            <p>And so, Neha and <span class="highlight">Jackson</span> began their journey together, a journey filled with love, joy, and endless possibilities. Together, they discovered the true meaning of love — it's not just about the grand gestures, but the little things that make life beautiful.</p>

            <p>Today, their love continues to grow, stronger with each passing day. They are inseparable, and their hearts will forever beat as one.</p>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 Neha & Jackson | All Rights Reserved</p>
    </footer>

</body>
</html>
    """
    return greetings