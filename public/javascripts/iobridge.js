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


function moveX(widgetID, direction, distance)
{
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
