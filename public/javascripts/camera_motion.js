$(document).ready( function() {

$('#turn_left').mousedown(function()
{
    interval = setInterval( function () { moveX('uz2ORyR5x4Mp', 'CW', '20') }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_right').mousedown(function()
{
    interval = setInterval( function () { moveX('uz2ORyR5x4Mp', 'CCW', '20') }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_up').mousedown(function()
{
    interval = setInterval( function () { moveY('omCjPwzHOI9b', 'CCW', '20') }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_down').mousedown(function()
{
    interval = setInterval( function () { moveY('omCjPwzHOI9b', 'CW', '20') }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

});

function lightOn()
{
  jQuery.get("http://www.iobridge.com/widgets/static/id=aEFW7f0gplue&value=0");
  //jQuery.getJSON("http://www.iobridge.com/widgets/static/id=aEFW7f0gplue&value=0&format=json&callback=?", function(json) { console.log("lol"); });
  //jQuery.get("http://interactivelab.astrobotic.net/iobridge-proxy.php?widgetID=OXO0Q9H2yXME&state=0", function(data) { console.log("RECEIVED: "+data); });
}

function lightOff()
{
  //jQuery.getJSON("http://www.iobridge.com/widgets/static/id=aEFW7f0gplue&value=1&format=json&callback=?", function(json) { console.log("lol");});
  jQuery.get("http://www.iobridge.com/widgets/static/id=aEFW7f0gplue&value=1");
  //jQuery.get("http://interactivelab.astrobotic.net/iobridge-proxy.php?widgetID=OXO0Q9H2yXME&state=1", function(data) { console.log("RECEIVED: "+data); });
}

function lightState()
{
	//jQuery.get("http://interactivelab.astrobotic.net/iobridge-proxy.php?widgetID=OXO0Q9H2yXME", function(data) { console.log("RECEIVED: "+data); });
}

var t;
function BubbleGun1()
{
 widgetExecute('UMVH2C5rT0A2');
 widgetExecute('4EpL2Ivl6MjZ');

 t = setTimeout(BubbleGun2,2000);
}

function BubbleGun2()
{
 widgetExecute('OPSvhTDEFyCz');
 clearTimeout(t);
}