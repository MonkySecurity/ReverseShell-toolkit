from flask import render_template, Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
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
		return render_template('index.html')
	else:
		return render_template('index.html')