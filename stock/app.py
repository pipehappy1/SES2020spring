from flask import Flask, render_template, request
import hashlib
import mysql.connector

app = Flask(__name__)

counter = 0

host = "127.0.0.1"
user = "yguan"
passwd = "123456"
db = "test"

@app.route('/')
def index():
    #return 'Hello world'
    return render_template('index.html')

@app.route('/v1/new-location', methods = ['POST', 'GET'])
def new_location():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        print(name, description)

        # hash it, gen qrcode, save to db
        m = hashlib.sha256()
        m.update(name.encode('utf-8'))
        m.update(description.encode('utf-8'))
        qrid = m.hexdigest()[:16]


        global host, user, passwd, db
        cnx = mysql.connector.connect(user=user, database=db, passwd=passwd, ssl_disabled=True, auth_plugin='mysql_native_password')
        cursor = cnx.cursor()
        add_location = ( "insert into location"
                         "(name, qrid, description)"
                         "values (%s, %s, %s)")
        
        cursor.execute(add_location, (name, qrid, description))
        cnx.commit()
        cursor.close()
        cnx.close()
        
        return render_template('new-location.html',
                               hidden_or_show="visible",
                               name=name,
                               description=description,
                               qr=qrid)
    else:
        return render_template('new-location.html',
                               hidden_or_show="none",
                               name="",
                               description="",
                               qr="")
    
@app.route('/v1/list-location')
def list_location():

    global host, user, passwd, db
    cnx = mysql.connector.connect(user=user, database=db, passwd=passwd, ssl_disabled=True, auth_plugin='mysql_native_password')
    cursor = cnx.cursor()
    add_location = ( "select * from location" )
    
    cursor.execute(add_location)

    items = []
    for (rid, name, qrid, description) in cursor:
        print("{}, {}, {}, {}", rid, name, qrid, description)
        an_item = dict(name=name, description=description)
        items.append(an_item)

    cursor.close()
    cnx.close()
    
    return render_template('list-location.html', items=items)

    
@app.route('/cakes')
def cakes():
    global counter
    counter += 1
    return 'There are {} Yummy cakes!'.format(counter)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
