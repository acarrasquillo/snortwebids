from flask import Flask, url_for, render_template, request, jsonify
import dbqueries as queries

app = Flask(__name__)
app.debug = True



# get the client ip and send it to the dashboard
@app.route('/', methods = ['GET'])
def index():
	ip = str(request.remote_addr)
	dstalerts = queries.destalerts(ip)
	return render_template('index.html', dstalerts = dstalerts, ip = ip, alertsnum = len(dstalerts))


@app.route('/my_ip', methods = ['GET'])
def return_ip():
	return jsonify({'ip': request.remote_addr})


if __name__ == '__main__':
	app.run(host="0.0.0.0")