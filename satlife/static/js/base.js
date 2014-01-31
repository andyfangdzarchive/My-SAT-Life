function choose(choice,id) {
  console.log(id);
  var tgt=$('#'+id);
  
  $.getJSON("/grammar/choose/", { pk:choice,}, function(json){
    var result=json['answer'];
    console.log(result);
    tgt.addClass("spinner");
    setTimeout(function() {
      if(result)tgt.addClass('bg-green');
      else tgt.addClass('bg-red');
    }, 1800);
  });
  
}
$('#buttons').click(function(event) {
  var tgt=$(event.target)
  

});
function setSiteCookie(cname,cvalue,exdays)
{
  var d = new Date();
  d.setTime(d.getTime()+(exdays*24*60*60*1000));
  var expires = "expires="+d.toGMTString();
  document.cookie = cname + "=" + cvalue + "; " + expires + "; PATH=/";
}
function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++) 
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}
$(document).ready( function(){ 
  if (getCookie("last")!=""){
    $('#next').append('<a href="/grammar/'+String(getCookie("last"))+'/" class="button border-fade pulse"><i class="fa fa fa-reply"></i> Previous</a>');
  }
  setSiteCookie("last",{{ grammar.pk }},365);
});