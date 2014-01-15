$(document).ready(function() {
	$("#foot").hide();
	var respStr = "";
	var curRespStr = "";
	var action = "../cgi-bin/mquerys.py";
	var query = unescape(location.search).substring(1);
	$.ajax({
		type: "POST",
		url: action,
		data: query,
		success: function(response){
			respStr = response;
			var resp = JSON.parse( response );
			populate_response_table( resp );
//			var queryStr = resp['mquery'];
			var nobs = resp['nobs'];
//			$("#query").after(queryStr);
			$("#nobs").append(nobs);
			$("#foot").show();
		}
	});

	function populate_response_table( response ) {
		var td = "<td class='ui-widget-content'>";
		for(var rowNum = 0; rowNum < 10; ++rowNum){
			var row = "row" + rowNum;
			if( response[row] !== undefined ) {
				var ts = td + response[row]['ts'] + "</td>";
				var hostname = td + response[row]['hostname'] + "</td>";
				var actionName = td + response[row]['actionName'] + "</td>";
				var bdto = td + response[row]['bdto'] + "</td>";
				var edto = td + response[row]['edto'] + "</td>";
				var elapsed = td + response[row]['elapsedTime'] + "</td>";
				var keyEventRec = td;
				for( rec in response[row]['record']){
					keyEventRec += rec + "=" + response[row]['record']['rec'] + " ";
				}
				keyEventRec += "</td>";
				var line = "<tr>" + ts + hostname + actionName + bdto + edto + elapsed + keyEventRec + "</tr>";
				$("#resultsdata").append(line);
			}
		}
	}

	var numResultsPerRequest = 5;
	var beginAfter = 0;
	$("#moreButton").click(function(){
		beginAfter += numResultsPerRequest;
		query += "&beginAfter=" + beginAfter;
		$.ajax({
			type: "POST",
			url: action,
			data: query,
			success: function(response){
				curRespStr = response;
				if( curRespStr == respStr ) alert("SameStr!!!");
				var resp = JSON.parse( response );
				populate_response_table( resp );
//				var queryStr = resp['mquery'];
//				var nobs = resp['nobs'];
//				$("#query").after(queryStr);
//				$("#nobs").append(nobs);
				respStr = curRespStr;
			}
		});
	});
});
