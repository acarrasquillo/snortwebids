function GraphView(glabel, gtype, gfilter, gentity, gportlabel, gtolabel, gwidth, gheight, gadmin, gvgraphs, guid, gsid, gremote){

//$('#graphbutton').click(function (){

      $.ajax({

                       url: '/',
                       type: 'POST',
                       data: {label:glabel,
			      type: gtype,
			      filter: gfilter,
			      entity: gentity,
			      portlabel: gportlabel,
			      tolabel: gtolabel,
			      h:gheight,
			      w: gwidth,
			      views: 'default'
				
				 },

                       success: function(res){
                               //location.reload();
                               //
                               //
                              	var response = res;

            			var graphs = response.split("#graph");
				if (graphs.length <= 1) {


					title= "The Ip " + glabel + " is not being monitored\n" 
                			document.getElementById("content").innerHTML += "<div class='col-md-6 col-md-offset-3'><h1 class='pull-left'>"+title+"</h1></div>";


				}

				else {
            			var title = "";


                		if(gentity == "device"){

                    				title = glabel+" Interface Graphs by "+gfilter.charAt(0).toUpperCase() + gfilter.slice(1);

                    				views = 'default';

                			}

               			 else if(gentity == "port"){

                    			title = glabel+" Port "+gportlabel+" Graphs by "+gfilter.charAt(0).toUpperCase() + gfilter.slice(1);

                    			views = 'default';

                			}

                		else if(gentity == "net2net"){

                    			title = glabel+" to "+gtolabel+" Graphs by "+gfilter.charAt(0).toUpperCase() + gfilter.slice(1);

                    			views = 'default';

               		 	}
				
                		document.getElementById("content").innerHTML += "<div class='col-md-6 col-md-offset-3'><h1 class='pull-left'>"+title+"</h1></div>";


            			src = document.createElement('script');

            			for(i=1; i<graphs.length;i++){


                    			document.getElementById("content").innerHTML += "<div class='thumbnail graph-thumb col-md-6 col-md-offset-3'><div class='graph' id='viz"+i+"'></div></div></center>";

                    			src.innerHTML += graphs[i];

               			 }		


            			document.body.appendChild(src);
                       }
		}

               });

	}


//    });


