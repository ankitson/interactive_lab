       $(function() {
           $('img[data-hover]').hover(function() {
               $(this).attr('tmp', $(this).attr('src')).attr('src', $(this).attr('data-hover')).attr('data-hover', $(this).attr('tmp')).removeAttr('tmp');
           }).each(function() {
               $('<img />').attr('src', $(this).attr('data-hover'));
           });;
       });


function refreshLightStatus() {
         $.getJSON("http://iobridge.com/api/feed/key=mki3VDGTahaPyhUZD6&callback=?", {mimeType: 'application/json'}, 
                   function(data){
                     if (data["module"]["status"] != "Online") {
                       $('#light_status').css('display','none');
                     } else {
                       var light_status = data.module.channels[1].AnalogInput;
                       light_status = 900;
                       if(light_status >= 800) {
                         $('#light_status').css('background', 'url(images/HighbayOpen.png)').css('display', 'block').css('background-size', '125px 125px');
                       } else {
                         $('#light_status').css('background', 'url(images/HighbayClosed.png)').css('display', 'block').css('background-size', '125px 125px');
                       	}
                     }
                   });
         }

var refreshId = setInterval(refreshLightStatus , 10000);
refreshLightStatus();

$(document).ready( function() {

$('#turn_left').mousedown(function()
{
    interval = setInterval( function () { moveX('uz2ORyR5x4Mp', 'CW', '20'); }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_right').mousedown(function()
{
    interval = setInterval( function () { moveX('uz2ORyR5x4Mp', 'CCW', '20'); }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_up').mousedown(function()
{
    interval = setInterval( function () { moveY('omCjPwzHOI9b', 'CCW', '100'); }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_down').mousedown(function()
{
    interval = setInterval( function () { moveY('omCjPwzHOI9b', 'CW', '40'); }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

});


function moveX(widgetID, direction, distance)
{
	console.log("MOVEX");
  distance = parseInt(distance);
  console.log("MOVEX distance: "+distance);
  console.log("WIDGET iD: "+widgetID);
  console.log("widgetGetString "+widgetGetString);
  console.log("widgetGetString(widgetID) "+widgetGetString(widgetID));
  current = parseInt(widgetGetString(widgetID));
  console.log("MOVEX current: "+current);

  if (direction == "CCW") {
       distance = current-distance;
  }
  else {
       distance = current+distance;
  }

   widgetSetString(widgetID, distance);

   current = Math.round(29 - (current - 800) * 60 / 500);

   //document.getElementById("ServoPosition").innerHTML = current + "&#176;";
}


function moveY(widgetID, direction, distance){

  distance = parseInt(distance);
  current = parseInt(widgetGetString(widgetID));

  if (direction == "CCW") {
       distance = current-distance;
  }
  else {
       distance = current+distance;
  }

   widgetSetString(widgetID, distance);

   current = Math.round(29 - (current - 800) * 60 / 500);

   //document.getElementById("ServoPosition").innerHTML = current + "&#176;";
}

function moveServo(widgetID, direction, distance){

 distance = parseInt(distance);
 current = parseInt(widgetGetString(widgetID));

 if (direction == "CCW") {
     distance = current-distance;
 }
 else {
     distance = current+distance;
 }

 widgetSetString(widgetID, distance);

 current = Math.round(29 - (current - 800) * 60 / 500);

 //document.getElementById("ServoPosition").innerHTML = current + "°";
}

//<script type="text/javascript">document.write(unescape("%3Cscript src='" + "http://www.iobridge.com/widgets/io.js? uz2ORyR5x4Mp' type='text/javascript'%3E%3C/script%3E"));</script>
//<script type="text/javascript">document.write(unescape("%3Cscript src='" + "http://www.iobridge.com/widgets/io.js? omCjPwzHOI9b' type='text/javascript'%3E%3C/script%3E"));</script>
