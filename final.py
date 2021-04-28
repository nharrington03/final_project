from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask import request, flash

import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route("/home")
def welcome_page():
    return render_template("finalWelcome.html")

@app.route('/register')
def new_contact():
    return render_template('finalform.html')

@app.route("/addrec", methods=["POST"])
def addrec():
    if request.method == "POST":
        name = request.form["name"]
        StuID = request.form["StuID"]
        class1 = request.form["class1"]
        class2 = request.form["class2"]
        class3 = request.form["class3"]

        with sql.connect("finaldatabase.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO classes (name, StuID, class1, class2, class3) VALUES (?, ?, ?, ?, ?)", [name, StuID, class1, class2, class3])
        con.commit()

        return render_template('success.html')

@app.route('/classlist')
def list_data():
    con = sql.connect('finaldatabase.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('SELECT * FROM classes')

    rows = cur.fetchall()
    return render_template('finallist.html', rows = rows)


#def create_database():
 #   conn = sqlite3.connect("finaldatabase.db")
  #  conn.execute("CREATE TABLE classes (name TEXT, StuID TEXT, class1 TEXT, class2 TEXT, class3 TEXT)")
   # conn.close()

#create_database()


if __name__ == '__main__':
    app.run(debug=True)