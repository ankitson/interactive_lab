// Place your application-specific JavaScript functions and classes here
// This file is automatically included by javascript_include_tag :defaults

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

readCookie()

function arrowToggle()
{
	$(".arrowup").fadeIn('slow');
	}