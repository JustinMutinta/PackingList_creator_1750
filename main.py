from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

test = []


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/1750", methods=["GET", "POST"])
def create_1750():
    test.clear()
    conn = sqlite3.connect('/Users/justinmutinta/Documents/Python/PackingList_creator_1750_from_BidDawg/python_files/DatabaseManagement/PackingListCreator.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    data = cur.fetchall()
    cur.close()
    if request.method == "POST":
        to_add = request.form.getlist('label1')
        for item in to_add:
            test.append(item)
    return render_template('html_files/1750_Generator.html', data = data, test = test)


@app.route("/results")
def show_results():
    return render_template('html_files/results.html', test = test)

@app.route("/home")
def home():
    return render_template('html_files/home.html')

if __name__ == '__main__':
    app.run(debug=True)