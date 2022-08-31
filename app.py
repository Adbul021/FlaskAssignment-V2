from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "flash message"


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapplication'
mysql = MySQL(app)


@app.route('/')
def index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    cur.close()

    return render_template("index.html", user = data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":

        flash("User Data has been successfully Added!")

        id = request.form['id']
        user = request.form['user']
        number = request.form['number']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (id, user, number) VALUES (%s, %s, %s)", (id, user, number))
        mysql.connection.commit()
        return redirect (url_for('index'))



@app.route('/update', methods = ['POST','GET'])
def update():

    if request.method == 'POST':

        number = request.form['number']

        cur = mysql.connection.cursor()
        cur.execute("""
                UPDATE user
               SET number = %s

            """, (number))
        flash("User Data has been Updated Successfully!")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(debug=True)
