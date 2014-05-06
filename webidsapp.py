from flask import Flask, url_for, render_template, request, jsonify
from MasterGrapherView import *
import dbqueries as querie
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.debug = True



# get the client ip and send it to the dashboard
@app.route('/', methods = ['GET', 'POST'])

def index():
	ip = str(request.remote_addr)
	dstalerts = querie.destalerts(ip)
	sumsig = querie.sigsum(ip)
	print sumsig

	if request.method == 'POST':
	#def graph():
		type = request.form["type"]
		filter=request.form["filter"]
		entity=request.form["entity"]
		label=request.form["label"]
		portlabel=request.form["portlabel"]
		tolabel=request.form["tolabel"]
		h = request.form["h"]
		w = request.form["w"]
		views=request.form["views"]
		#paths=views.split["#"]
		
		return getGraph(type,filter,entity,h,w,portlabel,tolabel,label)
	
	return render_template('index.html', dstalerts = dstalerts, ip = ip, alertsnum = len(dstalerts), sumsig = sumsig)

@app.route('/my_ip', methods = ['GET'])
def return_ip():
	return jsonify({'ip': request.remote_addr})

#@app.route('/graph', methods = [''])


if __name__ == '__main__':
	app.run(host="0.0.0.0")
