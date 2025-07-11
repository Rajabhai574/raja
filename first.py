from flask import Flask , render_template 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html") 


@app.route( "/product")
def products():
    return render_template("games.html")

@app.route( "/pc")
def pc():
    return render_template("pc.html")

app.run(debug = True)