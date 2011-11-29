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
  jQuery.getJSON("http://www.iobridge.com/widgets/static/id=OXO0Q9H2yXME&value=0&format=json&callback=?", function(json) {alert("JSON: "+json); });
  //jQuery.get("http://interactivelab.astrobotic.net/iobridge-proxy.php?widgetID=OXO0Q9H2yXME&state=0", function(data) { console.log("RECEIVED: "+data); });
}

function lightOff()
{
	jQuery.get("http://www.iobridge.com/widgets/static/id=OXO0Q9H2yXME&value=1");
  //jQuery.get("http://interactivelab.astrobotic.net/iobridge-proxy.php?widgetID=OXO0Q9H2yXME&state=1", function(data) { console.log("RECEIVED: "+data); });
}

function lightState()
{
	//jQuery.get("http://interactivelab.astrobotic.net/iobridge-proxy.php?widgetID=OXO0Q9H2yXME", function(data) { console.log("RECEIVED: "+data); });
}