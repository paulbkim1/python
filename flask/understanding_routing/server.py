from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:names>')
def hi(names):
    print(names)
    return f"Hi {names}!"

@app.route('/repeat/<int:num>/<string:words>')
def statement(num, words):
    return words * num

# @app.route()
# def response():
#     return "Sorry!"

if __name__=="__main__":
    app.run(debug=True)