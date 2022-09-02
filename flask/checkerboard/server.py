from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eightxeight():
    return render_template('index.html', box1 = 8, box2 = 8, color1 = "red", color2= "black")

@app.route('/4')
def eightxfour():
    return render_template('index.html', box1 = 4, box2 = 8, color1 = "red", color2= "black")

@app.route('/<int:x>/<int:y>')
def xxy(x, y):
    return render_template('index.html', box1 = y, box2 = x, color1 = "red", color2= "black")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def finalboard(x, y, color1, color2):
    return render_template('index.html', box1 = y, box2 = x, color1 = color1, color2= color2)

if __name__=="__main__":
    app.run(debug=True)