function choose(choice,id) {
  console.log(id);
  var tgt=$('#'+id);
  $.getJSON("/grammar/choose/"+choice, function(json){
    var result=json['answer'];
    console.log(result);
    tgt.addClass("spinner");
    setTimeout(function() {
      if(result)tgt.addClass('bg-green');
      else tgt.addClass('bg-red');
    }, 1800);
    setTimeout(function() {
      tgt.removeClass('spinner');
    }, 2000);
  });
}

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

function renderQuestion(json)
{
  var str='<div id="question">\n';
  str+='<div style="max-width:320px;border-style: solid;border-width: 2px; padding: 4px;">\nPlease click an alphabetically labeled button to see if you are correct. Click "Hit me!" to view another random question. Click "Previous" to view the last question you saw. Click "List" to return to the question list.\n</div>';
  str+='<h4>'+json['nickname']+'</h4>';
  str+='<p class="cbstyle">';
  str+=json['question_1st'];
  str+='<span style="text-decoration: underline;">';
  str+=json['choices'][0];
  str+='</span>';
  str+=json['question_2nd'];
  str+='</p>\n';
  str+='<div id="choices">\n'
  for (var i=0;i<5;i++)
  {
    str+='<div class="display-element" class="choice">\n';
    str+='<span class="display-label">('+json['labels'][i]+')</span>\n';
    str+='<span class="display-field">'+json['choices'][i]+'</span>\n';
    str+='</div>';
  }
  str+='</div>';
  str+='<div id="buttons">';
  for (var i=0;i<5;i++)
  {
    console.log(i);
    str+='<a id="choice-'+json['labels'][i]+'" class="button border-fade" onClick='+"'"+'choose('+json['choices_id'][i];
    str+=','+'"'+"choice-"+json['labels'][i]+'"'+");'>("+json['labels'][i]+')</a>';
  }
  str+='\n</div>\n';//!buttons
  str+='</div>\n';//!question
  return str;
}
function renderHit(nextId)
{
  var str='<a href="javascript:" class="button border-fade"'
  str+='onClick="viewQuestion('+nextId+')"';
  str+='><i class="fa fa-fighter-jet"></i> Hit me!</a>';
  return str;
}
function renderList(json)
{
  var str='<div id="qlist">\n';
  str+='<a class="button border-fade easy" onClick="viewQuestion('+json['shuffle']+')"><i class="fa fa fa-random"></i> Shuffle</a>\n';
  str+="<p class='bigdeal'>Here's a list of all grammar questions avaliable:</p>\n";
  for(var i=0;i<json['count'];i++)
  {
    console.log(i);
    str+="<p class='button easy' onClick='viewQuestion("+json['pks'][i]+")'>"+ '<i class="fa fa-tasks"></i> '+json['nicks'][i]+'</p>\n';
  }
  str+='</div>\n';
  return str;
}
function rendertoList(nextId)
{
  var str='<a href="javascript:" class="button border-fade"'
  str+='onClick="viewList()"';
  str+='><i class="fa fa-list"></i> List</a>';
  return str;
}
function renderPrevious(thisId)
{
  var lastId;
  if(getCookie("last")=="")lastId=thisId;
  else lastId=getCookie("last");
  var str='<a class="button border-fade " onClick="viewQuestion('+lastId+')"><i class="fa fa fa-reply"></i> Previous</a>';
  return str;
}
function viewQuestion(id)
{
  var jqxhr = $.getJSON( "/grammar/ajax/"+id, function() {
  console.log( "Successfully registered ajax event. Loading question "+id+"." );
  })
    .done(function(json) {
      var htmldata=renderQuestion(json);
      var pastHeight=$('#main').height();
      $('#main').addClass('switch_in_out');
      setTimeout(function() {
        $('#main').empty();
        $('#main').append(htmldata);
        var currentHeight=$('#main').height();
        //$('#operations').animate({up:"+="+currentHeight-pastHeight},500);
        window.history.pushState("object or string", document.title, "/grammar/view/"+id);
        document.title = json['nickname']+" - Grammar";
      },500);
      setTimeout(function() {
        $('#main').removeClass('switch_in_out');
      },1000);
      $('#operations').empty();
      $('#operations').append(renderHit(json['next']));
      $('#operations').append(renderPrevious(id));
      $('#operations').append(rendertoList(json['next']));
    });
}
function viewList()
{
  var jqxhr = $.getJSON( "/grammar/listajax/", function() {
  console.log( "Successfully registered ajax event. Loading list." );
  })
    .done(function(json) {
      var htmldata=renderList(json);
      var pastHeight=$('#main').height();
      $('#main').addClass('switch_in_out');
      setTimeout(function() {
        $('#main').empty();
        $('#main').append(htmldata);
        var currentHeight=$('#main').height();
        //$('#operations').animate({up:"+="+currentHeight-pastHeight},500);
        window.history.pushState("object or string", document.title, "/grammar/");
        document.title = "List"+" - Grammar";
      },500);
      setTimeout(function() {
        $('#main').removeClass('switch_in_out');
      },1000);
      $('#operations').empty();
    });
}