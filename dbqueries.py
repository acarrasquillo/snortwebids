import MySQLdb as mdb
import settings

# function to fetch a query from the db
def dbFunc(querytext):
	
	try:
		# connect with db
		con = mdb.connect(user = settings.user, passwd = settings.passwd, db = settings.db, host = settings.host)
		#create cursor
		cursor = con.cursor()
		cursor.execute(querytext)
		# execute the queryq
		answer = cursor.fetchall()
		print answer
		if con:
			con.close()
		return answer

	except mdb.Error,e:
		print "Error %d: %s" % (e.args[0], e.args[1])

# query for all the alerts in the db from the client connecting the app
def destalerts(ip):
	querytext = "select inet_ntoa(iphdr.ip_src) as src, inet_ntoa(iphdr.ip_dst) as dst, signature,sig_name, timestamp from event,iphdr,signature where(event.cid,event.sid) = (iphdr.cid,iphdr.sid) and ((inet_ntoa(ip_dst) = '%s') or (inet_ntoa(ip_src) = '%s')) and event.signature = signature.sig_id order by timestamp DESC" % (ip,ip)
	print querytext
	return dbFunc(querytext)

# query to get the sum of diferents signatures detected by the client ip

def sigsum(ip):
	querytext = "select count(*), sig_name as sig from event,iphdr,signature where(event.cid,event.sid) = (iphdr.cid,iphdr.sid) and ((inet_ntoa(ip_dst) = '%s') or (inet_ntoa(ip_src) = '%s')) and event.signature = signature.sig_id group by sig order by timestamp DESC" % (ip,ip)
	print querytext
	return dbFunc(querytext)

