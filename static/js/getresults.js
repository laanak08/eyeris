"use strict";
$(document).ready(function() {
	$("#foot").hide();
	$("#nobs").hide();

	var numResultsPerRequest = 5;
	var action = "../cgi-bin/mquerys.py";
	var query = unescape(location.search).substring(1);

//	var beginAfter = 0;
//	query = query + "&beginAfter=" + beginAfter.toString();

	// initial ajax call on page load
	query_mongodb();

	$("#moreButton").click(function(){
//		beginAfter += numResultsPerRequest;
//		query = query.replace(/beginAfter=.+?&/gi,"&beginAfter="+beginAfter.toString());
		query_mongodb();
	 });

	function query_mongodb() {
		$.ajax({
			type: "POST",
			url: action,
			data: query,
			success: function(response){
				var resp = JSON.parse( response );
				var queryStr = "<span id='theQuery'>" + resp['mquery'].slice(1,-1) + "</span>";
				var nobs = "<span id='theNobs'>" + resp['nobs'] + "</span>";

				if( $('#theQuery').length !== 0 ) $('#theQuery').remove();
				if( $('#theNobs').length !== 0 ) $('#theNobs').remove();

				populate_response_table( resp );
				$("#query").after(queryStr);
				$("#nobs").append(nobs).show();
				$("#foot").show();
			}//,
//			error: function(xhr, status, error ){
//				alert("status: " + xhr.status + " text:  " + xhr.statusText  ); 
//			}
		});
	}

	function populate_response_table( response ) {
		var td = "<td class='ui-widget-content'>";
		for(var rowNum = 0; rowNum < numResultsPerRequest; ++rowNum){
			var row = "row" + rowNum;
			if( response[row] !== undefined ) {
				var ts = td + response[row]['ts'] + "</td>";
				var hostname = td + response[row]['hostname'] + "</td>";
				var actionName = td + response[row]['actionName'] + "</td>";
				var bdto = td + response[row]['bdto'] + "</td>";
				var edto = td + response[row]['edto'] + "</td>";
				var elapsed = td + response[row]['elapsedTime'] + "</td>";
				var keyEventRec = "<td class='ui-widget-content scroll'>";
				for( rec in response[row]['record']){
					keyEventRec += rec + "=" + response[row]['record'][rec] + " ";
				}
				keyEventRec += "</td>";
				var line = "<tr>" + ts + hostname + actionName + bdto + edto + elapsed + keyEventRec + "</tr>";
				$("#resultsdata").append(line);
			}
		}
	}

});
