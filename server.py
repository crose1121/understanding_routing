from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello_World!'

@app.route('/dojo')
def say_Dojo():
    return 'Dojo!'

@app.route('/Hi/<name>')
def say_hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<num>/<message>')
def repeat_message(num,message):
    return f"{message*int(num)}"

if __name__ == '__main__':
    app.run(debug=True)