from flask import render_template, Flask, request
import re
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	acceptedLangage=["bash","netcat","perl","php","python","ruby"]
	ip=""
	port=""
	langage=""
	payload=""
	alert=""
	if request.method == "POST":
		ip=request.form['ip']
		port=request.form['port']
		langage=request.form['lan']
		print ip
		print port
		print langage
		if ip != "" and port != "" and langage != "": 
			if langage in acceptedLangage:
				file=open("revshell/"+langage,"r")
				for f in file:
					f= f.replace("[ip]",ip)
					f = f.replace("[port]",port)
					print f
				file.close()
		return render_template('index.html')
	else:
		return render_template('index.html')