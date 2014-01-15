$().ready(function(){
 $(".jtable th").each(function(){

  $(this).addClass("ui-state-default");

  });
 $(".jtable td").each(function(){

  $(this).addClass("ui-widget-content");

  });
  /*
 $(".jtable tr").hover(
     function()
     {
      $(this).children("td").addClass("ui-state-hover");
     },
     function()
     {
      $(this).children("td").removeClass("ui-state-hover");
     }
    );*/
 $(".jtable tr").click(function(){

   $(this).children("td").toggleClass("ui-state-highlight");
  });


 $('#column-selector').buttonset();
 $('#column-selector input:checkbox').removeAttr('checked');
 $('#column-selector').buttonset('refresh');

 $("#column-selector input").click(function(){
 	ncol = this.id.substr(3);
 	$('td:nth-child(' + ncol + '),th:nth-child(' + ncol + ')').toggle();
 });


});
