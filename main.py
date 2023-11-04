from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from PdfManipulator import PdfManipulator
app = Flask(__name__)

test = []

@app.route("/")
def hello():
    return "REMEMBER TO ADD /1750 OR /HOME OR /RESULTS TO GET STARTED"


@app.route("/1750", methods=["GET", "POST"])
def create_1750():
    test.clear()
    conn = sqlite3.connect('PackingListCreator.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    data = cur.fetchall()
    cur.close()
    return render_template('html_files/1750_Generator.html', data = data, test = test)


@app.route("/results", methods=["POST"])
@app.route("/results")
def show_results():
    to_add = request.form.getlist('label1')
    for item in to_add:
        test.append(item)

    username = request.form.get("PersonPacking")
    container = request.form.get("ContainerName")

    new_object = PdfManipulator(username, container)
    new_object.fill_in_pdf(test)

    pdf_output = new_object.output_pdf_location()

    return render_template('html_files/results.html', test = test, pdf_output = pdf_output)


@app.route("/home")
def home():
    return render_template('html_files/home.html')


if __name__ == '__main__':
    app.run(debug=True)