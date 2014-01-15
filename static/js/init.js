$(function() {
	$.datepicker.setDefaults({ dateFormat: 'dd-M-yy', maxDate: '+0D' });
	$("#sd").datepicker();
	$("#ed").datepicker();
	$("#tabs").tabs();

	var servers = [
		"cpc222714",
		"cpc2c215",
		"cpc2618",
		"cpc222716",
		"cpc22644",
		"cpc2a771",
		"cpc22713",
		"cpc22751",
		"cpc22772",
		"CNTD3BWEB92L",
		"CNTD3BWEB92K",
		"CNTD3BWEB92N",
		"cpc22692",
		"cpc222718",
		"cpc22716",
		"cpc22712",
		"cpc2a774",
		"cpc2a770",
		"CNTD3BWEB92S",
		"CNTD3BWEB92R",
		"CNTD3BWEB92M",
		"cpc2295",
		"cpc22750",
		"cpc22645",
		"CNTD3BWEB92B",
		"CNTD3BWEB92C",
		"cpc22717",
		"cpc2a775",
		"cpc2a776",
		"cpc2298",
		"cpc2236",
		"CNTD3BWEB92Q",
		"CNTD3BWEB92V",
		"cpc22728",
		"cpc222719",
		"cpc222717",
		"cpc22714",
		"cpc22694",
		"cpc2299",
		"cpc2c219",
		"cpc2c217",
		"cpc2636",
		"cpc22729",
		"cpc2292",
		"cpc2293",
		"cpc2294",
		"cpc22691",
		"cpc2296",
		"cpc2297",
		"cpc2290",
		"cpc2291",
		"cpc22690",
		"cpc2a777",
		"CNTD3BWEB92A",
		"cpc222731",
		"cpc22715",
		"cpc22753.lexisnexis.com",
		"CNTD3BWEB92W",
		"CNTD3BWEB92D",
		"CNTD3BWEB92P",
		"cpc22753",
		"CNTD3BWEB92J",
		"CNTD3BWEB92X",
		"cpc222732",
		"CNTD3BWEB93A",
		"cpc222734",
		"cpc222733",
		"CNTD3BWEB94A",
		"CNTD3BWEB91A",
		"CNTD3BWEB91E",
		"CNTD3BWEB91D",
		"CNTD3BWEB91C",
		"CNTD3BWEB91F",
		"CNTD3BWEB91B"
	]

 	function split( val ) { return val.split( /,\s*/ ); }
	function extractLast( term ) { return split( term ).pop(); }

	$( "#serverName" )
	// don't navigate away from the field on tab when selecting an item
	.bind( "keydown", function( event ) {
		if ( event.keyCode === $.ui.keyCode.TAB &&
		$( this ).data( "ui-autocomplete" ).menu.active ) {
			event.preventDefault();
		}
	})
	.autocomplete({
		minLength: 0,
		source: function( request, response ) {
		// delegate back to autocomplete, but extract the last term
		response( $.ui.autocomplete.filter(
		servers, extractLast( request.term ) ) );
		},
		focus: function() {
			// prevent value inserted on focus
			return false;
		},
		select: function( event, ui ) {
			var terms = split( this.value );
			// remove the current input
			terms.pop();
			// add the selected item
			terms.push( ui.item.value );
			// add placeholder to get the comma-and-space at the end
			terms.push( "" );
			this.value = terms.join( ", " );
			return false;
		}
	});
});
