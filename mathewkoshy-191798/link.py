from flask import Flask, render_template, request
from flask_mysqldb import MySQL
build = Flask(__name__)


build.config['MYSQL_HOST'] = 'localhost'
build.config['MYSQL_USER'] = 'root'
build.config['MYSQL_PASSWORD'] = 'root'
build.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(build)


@build.route('/', methods=['GET', 'POST'])
def page1():
    if request.method == "POST":
        info = request.form
        txt1 = info['data1']
        txt2 = info['data2']
        txt3 = info['data3']
        txt4 = info['data4']

        connect = mysql.connection.cursor()
        connect.execute("INSERT INTO abc(Fullname, UID , Company, Email) VALUES (%s, %s, %s, %s)", (txt1, txt2, txt3, txt4))
        mysql.connection.commit()
        connect.close()
        return render_template('ust2.html', res1=txt1, res2=txt2, res3=txt3, res4=txt4)
    return render_template('ust1.html')

@build.route('/ust2')
def page2():
    return render_template('ust2.html')


if __name__ == '__main__':
    build.run()