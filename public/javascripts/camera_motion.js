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
    interval = setInterval( function () { moveY('omCjPwzHOI9b', 'CCW', '100') }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

$('#turn_down').mousedown(function()
{
    interval = setInterval( function () { moveY('omCjPwzHOI9b', 'CW', '40') }, 150);
}).mouseup(function()
{
    clearInterval(interval);
});

});
