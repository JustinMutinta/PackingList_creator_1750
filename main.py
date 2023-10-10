from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1750")
def create_1750():
    return render_template('html_files/1750_Generator.html')


@app.route("/17501")
def create_17501():
    return render_template('html_files/mutinta_position_test.html')

if __name__ == '__main__':
    app.run(debug=True)