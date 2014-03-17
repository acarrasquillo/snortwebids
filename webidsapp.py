from flask import Flask, url_for, render_template, request, jsonify

app = Flask(__name__)
app.debug = True


# get the client ip and send it to the dashboard
@app.route('/', methods = ['GET'])
def index():
	ip = str(request.remote_addr)
	return render_template('index.html', ip = ip)


@app.route('/my_ip', methods = ['GET'])
def return_ip():
	return jsonify({'ip': request.remote_addr})


if __name__ == '__main__':
	app.run()