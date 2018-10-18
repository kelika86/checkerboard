from flask import Flask, render_template
app = Flask(__name__)



@app.route('/<x>/<y>')
def index(x,y):
    x=int(x)
    y=int(x)
    return render_template("checkerboard.html", x=x, y=y)



app.run(debug=True)