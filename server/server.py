from flask import Flask,request,render_template
import json,time,random
import MySQLdb as mdb 

app = Flask(__name__)
cnx = mdb.connect('localhost','root','','road')

@app.route("/bookStatus",methods = ["POST"])
def book():
	TaxiPass = {}
	TaxiPass['name'] = str(request.form['name'])
	TaxiPass['dest'] = str(request.form['dest'])
	TaxiPass['gen_id'] = str(request.form['gen_id'])
	TaxiPass['time'] = str(request.form['time'])

	try:
		cur = cnx.cursor()
		cur.execute('insert into taxi(name,dest,gen_id,time) VALUES (%s,%s,%s,%s);',(TaxiPass['name'],TaxiPass['dest'],
			TaxiPass['gen_id'],TaxiPass['time']))
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