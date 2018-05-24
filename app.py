from flask import  Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/signup")
def signup():
	return "<h1>WELCOME TO SIGNUP</h1>";

@app.route("/login")
def login():
	return "<h1>WELCOME TO login</h1>";
