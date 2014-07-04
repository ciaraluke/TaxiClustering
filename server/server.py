from flask import Flask,request,render_template
import json,time,random
import MySQLdb as mdb
from pygeocoder import Geocoder 
from QuadTreeCluster import *
#PyGeo location
app = Flask(__name__)
cnx = mdb.connect('localhost','root','','road')

@app.route("/admin")
def admin():
	try:
		cur = cnx.cursor()
		data = cur.execute('select * from taxi')
		rows = cur.fetchall()

		cluster = QuadTree({'x':0,'y':0,'width':18,'height':24},0)
		
		
		for entries in rows:
			address = Geocoder.geocode(entries[1])
			data = {

				'Address':entries[1],
				'x':address.coordinates[0],
				'y':address.coordinates[1]
			}
			cluster.insert(data)

		post = []
		post.extend(cluster.getAllobjects())
		cluster.clear()
		return render_template("/admin/index.html" ,posts = post)
	
	except Exception as e:
		print "WHAT THE FUCK IS WRONG => {0}".format(e)
		return render_template('/admin/index.html',posts=json.dumps({'nirvik':'Best'}))

@app.route("/bookStatus",methods = ["POST"])
def book():
	TaxiPass = {}
	TaxiPass['name'] = str(request.form['name'])
	TaxiPass['dest'] = str(request.form['dest'])
	TaxiPass['gen_id'] = str(request.form['gen_id'])
	TaxiPass['time'] = str(request.form['time'])
	TaxiPass['status'] = "False"
	try:
		cur = cnx.cursor()
		cur.execute('insert into taxi(name,dest,gen_id,time,status) VALUES (%s,%s,%s,%s,%s);',(TaxiPass['name'],TaxiPass['dest'],
			TaxiPass['gen_id'],TaxiPass['time'],TaxiPass['status']))
		cnx.commit()
		cur.close()
		return json.dumps(TaxiPass)
	except Exception as e:
		print e
		return 'The problem is '+str(e)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8000,debug=True)
