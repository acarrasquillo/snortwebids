#!/usr/bin/python

GRAPH_PATH="/home/labuser/graphs/" 



def  printgraphs(graph,type,w,h,divid,filter=None):


   file=open(graph,'r')
   graphdata=file.read()
   graphdata=graphdata.replace("data","data%s"%(divid))
   response=""


   if type !='cpl':
	#Read the data for the graphs and the js functions to draw it from js file
	response+= graphdata


	response+="""
	var view%s = new google.visualization.DataView(data%s);
	view%s.setColumns([0,2,3]); //here you set the columns you want to display
	var net%s = new google.visualization.AreaChart(document.getElementById('%s'));
	net%s.draw(view%s, {curveType: "function",
	 width:%s, height:%s, title: graphtitle , titleX: xtitle, titleY: ytitle,
                        vAxis: {maxValue: maxvalue}}
                );


      """%(divid,divid,divid,divid,divid,divid,divid,w,h)
   else:
	
	response+=graphdata

	response+= """
	var view%s = new google.visualization.DataView(data%s);
	view%s.setColumns([0,2,3,4,5,6,7]); //here you set the columns you want to display
	    net%s = new google.visualization.AreaChart(document.getElementById('%s'))
            net%s.draw(view%s, {curveType: "function",
                        width:%s, height:%s,title: graphtitle, titleX: xtitle, titleY: ytitle,
                        vAxis: {maxValue: 10}}
                );

	"""%(divid,divid,divid,divid,divid,divid,divid,w,h)
	

   response+="\n\n"
   file.close()	
   return response

#Id, Type (all, pak, flw,col), filter(day,week,month,day), entity(device, port, Net2net),h,w(optional)
def getGraph(type,filter,entity,h, w,portlabel,tolabel,label):

	
   	if h=='default':
		h='400'
	if w=='default':
		w='750'
	graph=""
	
	if filter=='day':
		f='1d'
	elif filter=='week':
		f='1w'
	elif filter=='month':
		f='1m'
	elif filter=='year':
		f='1a'
	if entity=='device':
		#id is network id 
		#GetLabel returns the label for that id 

		graph=GRAPH_PATH+label+'_'+f
		


	elif entity=='port':
		#id is the port if (pid from the database)


		graph=GRAPH_PATH+label+'-p'+portlabel+'_'+f

	elif entity=='net2net':
		graph=GRAPH_PATH+label+'_'+tolabel+'_'+f
		
	if type=='all':
		types=['net','pak','flw','cpl']
		response=""	
		for i in range(len(types)):
			divid='viz%s'%(i+1)
			response+='#graph\n\n'+  printgraphs(graph+types[i]+'.js',types[i],w,h,divid,filter)

	else:
			graph+=type+'.js'
		
			response='#graph\n\n'+  printgraphs(graph,type,w,h,'viz1',filter)



	return response


