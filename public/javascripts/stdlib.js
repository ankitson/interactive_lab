// LCS 3021  May 6, 2003
var separator = ";";  // used for string=> multiple select list
var max_schedule_item = 10;  // used for max period of the schedule
var PAN_TILT = false;

var HelpOptionsVar = "width=480,height=420,scrollbars,toolbar,resizable,dependent=yes";
var bigsub   = "width=620,height=460,scrollbars,menubar,resizable,status,dependent=yes";
var smallsub = "width=440,height=320,scrollbars,resizable,dependent=yes";
var specialsub = "width=440,height=320,scrollbars,resizable,dependent=no";
var sersub   = "width=500,height=380,scrollbars,resizable,status,dependent=yes";
var memsub   = "width=630,height=320,scrollbars,menubar,resizable,status,dependent=yes";
var viewingWinoptions = "width=800,height=500,scrollbars=no,resizable,status";
var motionsub = "width=582,height=350,scrollbars=no,resizable=no,status,dependent=yes";
var sambasurveysub = "dialogHeight=410px; dialogWidth=520px; scroll=off; status=no; location=no";
var sambaauthsub1 = "dialogHeight=300px; dialogWidth=360px; status=no; location=no";
var sambaauthsub2 = "dialogHeight=255px; dialogWidth=360px; status=no; location=no";
var sambasurveyauthsub1 = "dialogHeight=270px; dialogWidth=360px; status=no; location=no";
var sambasurveyauthsub2 = "dialogHeight=225px; dialogWidth=360px; status=no; location=no";
var helpWinVar = null;
var glossWinVar = null;
var datSubWinVar = null;
var ValidStr = 'abcdefghijklmnopqrstuvwxyz-';
var hex_str = "ABCDEFabcdef0123456789";
var Valid_Str= 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-';
var Valid_Strs = 'abcdefghijklmnopqrstuvwxyz_\nABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-';
var Valid_Stri = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.';
var Valid_st = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
var Valid_ch = "~!#@$%^&*()_+|}{:?><,./;'[]\"`=-\\";
var Valid_Strd = Valid_st + Valid_ch;
var Valid_domain= 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-';
var timesub = "width=460,height=250,scrollbars,status,resizable";
var Valid_Number = "0123456789";

//var lang = "@h_language#";   // "@h_lang#", "us", "eu"

function openViewWin()
{
	viewWindowVar = window.open("/img/main.cgi?next_file=main.htm", "viewWin", viewingWinoptions);
//	viewWindowVar = window.open("img/main.htm", "viewWin", viewingWinoptions);
}


var restart_time = 5000; // msecs


function changeTab(url)
{
	location.href=url;
}

var showit = "block";
var hideit = "none";
function show_hide(el,shownow)  // IE & NS6; shownow = true, false
{
    if (document.all)
        document.all(el).style.display = (shownow) ? showit : hideit ;
    else if (document.getElementById)
        document.getElementById(el).style.display = (shownow) ? showit : hideit ;
}

var Vshowit = "visible";
var Vhideit = "hidden";
function setVisible(el,shownow)  // IE & NS6; shownow = true, false
{
  if (document.all)
    document.all(el).style.visibility = (shownow) ? Vshowit : Vhideit ;
  else if (document.getElementById)
   document.getElementById(el).style.visibility = (shownow) ? Vshowit : Vhideit ;
}

function showMsg()
{
	var serverAdd = "http://"  +  self.location.host + ":" + self.location.port;
	var timeoutStr ;
	
	if (msgVar == "restart")
	{
		alert(addstr(msg_restart, restart_time/1000));
//		setTimeout(timeoutStr,restart_time);
	}
	else if (msgVar == "changeIP")
	{
		alert(addstr(msg_changeIP, restart_time/1000));
		top.close();
	}
	else if(msgVar == "@" + "m" + "essage#")
		;
	else if (msgVar.length > 1) 
		alert(msgVar);
}

function closeWin(win_var)
{
	if ((win_var != null) && (win_var.closed == false)) 
		win_var.close();
}

function openHelpWin(file_name)
{
   helpWinVar = window.open(file_name,'help_win',HelpOptionsVar);
   if (helpWinVar.focus)
		setTimeout('helpWinVar.focus()',200);
}

function openGlossWin()
{
	glossWinVar = window.open('','gloss_win',GlossOptionsVar);
	if (glossWinVar.focus)
		setTimeout('glossWinVar.focus()',200);
}

var randomn = Math.round(Math.random()*1000);
function openDataSubWin(filename,win_type)
{
	closeWin(datSubWinVar);
	datSubWinVar = window.open(filename, 'datasub_win' + randomn, win_type);
	if (datSubWinVar.focus)
		setTimeout('datSubWinVar.focus()',200); 
}

function closeSubWins()
{
	closeWin(helpWinVar);
	closeWin(glossWinVar);
	closeWin(datSubWinVar);
}

function checkBlank(fieldObj, fname)
{
	var msg = "";
	if (fieldObj.value.length < 1)
		msg = addstr(msg_blank,fname);
	return msg;
}

function checkNoBlanks(fObj, fname)
{
	var space = " ";
 	if (fObj.value.indexOf(space) >= 0 )
		return addstr(msg_nospaces, fObj.value);
	else return "";
}
function checkHostName(str)
{
	var at="@";
	var dot=".";
	var dash="-";
	var unline="_";
	var lat=str.indexOf(at);
	var lstr=str.length;
	var ldot=str.indexOf(dot);
	var i;
	var aa;	
	//host name must include "." and "." can't be the first/last char.
	if (str.indexOf(dot)==-1 || str.indexOf(dot)==0 ||str.charAt(lstr-1)==".")
	{
		return false; 
	} 
	//"-" can't be the first/last char
	if(str.indexOf(dash)==0 ||str.charAt(lstr-1)=="-")
	{
		return false; 
	} 
	//"_" can't be the first/last char
	if(str.indexOf(unline)==0 ||str.charAt(lstr-1)=="_")
	{
		return false; 
	} 
	// can't include space
	if (str.indexOf(" ")!=-1)
	{		   
	    return false;
	}
	// xx-.com is invalid 	
	if(str.indexOf("-.")!=-1)
	{					
		return false;
	}
	
	// xx.-com is invalid    
	if(str.indexOf(".-")!=-1 )
	{
		return false;
	}
	// xx..com is invalid
	if(str.indexOf("..")!=-1)
	{
		 return false;
	}
	for (i=0;i<=lstr-1;i++)
	{ 
		aa=str.charAt(i) 
		if (!((aa=='.') || (aa=='-') ||(aa=='_') || (aa>='0' && aa<='9') || (aa>='a' && aa<='z') || (aa>='A' && aa<='Z')))
		{ 
			return false; 
		} 
	}
	return true;	
}
function checkDomainName(input_field, field_name,valid_char)
{
	if (checkHostName(input_field.value)==false)
				return addstr(msg_invalid,field_name,valid_char);
	return "";
}
function CheckEmail(str)
{

		var at="@";
		var dot=".";
		var dash="-";
		var lat=str.indexOf(at);
		var lstr=str.length;
		var ldot=str.indexOf(dot);
		var i;
		var aa;		
		// it must include "@", and "@" can't be the first/last chars
		if (str.indexOf(at)==-1 || str.indexOf(at)==0 || str.charAt(lstr-1)=="@")
		{ 
			return false; 
		} 
		// "-" can't be the last chars
		if(str.charAt(lstr-1)=="-")
		{ 
			return false; 
		} 
		// it must include ".", and "." can't be the first/last chars
		if (str.indexOf(dot)==-1 || str.indexOf(dot)==0 ||str.charAt(lstr-1)==".")
		{
			return false; 
		} 
		// only one "@"
		 if (str.indexOf(at,(lat+1))!=-1)
		 {
		    return false;
		 }

		// it can't be "." or "-" to the heel of "@", it can't be "@" to the heal of "."
		// xx.@xx.com, xx@-xx.com, xx@.com, are invalid		
		 if (str.substring(lat-1,lat)==dot 
		 || str.substring(lat+1,lat+2)==dot 
		 || str.substring(lat+1,lat+2)==dash)
		 {
		    return false;
		 }

		// after "@", it must include ".", between the "@" and ".", it msut be the other chars
		 if (str.indexOf(dot,(lat+2))==-1)
		 {
		    return false;
		 }
		
		// can't include space
		 if (str.indexOf(" ")!=-1)
		 {		   
		    return false;
		 }
		 /*
		 // after "@", "_" is invalid
		// xx@xx_xx.com is invalid	
			if(str.indexOf("_",lat+1)!=-1)
			{					
			 		return false;
			}
			*/
		// after "@", the "." can't be to the heel of "-"
		// xx@xx-.com is invalid	
			if(str.indexOf("-.",lat+1)!=-1)
			{					
			 		return false;
			}
		// after "@", the "-" can't be to the heel of "."
		// xx@xx.-com is invalid
			if(str.indexOf(".-",lat+1)!=-1)
			{
			 		return false;
			}		
			// after "@", the "." can't be to the heel of "."
		// xx@xx..com is invalid
			if(str.indexOf("..",lat+1)!=-1)
			{
			 		return false;
			}
	for (i=0;i<=lstr-1;i++)
	{ 
		aa=str.charAt(i) 
		if (!((aa=='.') || (aa=='@') || (aa=='-') ||(aa=='_') || (aa>='0' && aa<='9') || (aa>='a' && aa<='z') || (aa>='A' && aa<='Z')))
		{ 
				return false; 
		} 
	} 	 		
 		 return true;					
}
function checkMailAdd(input_field, field_name)
{
	//if (!(input_field.value.indexOf("@") >= 0 ))
	//	return addstr(msg_mail, field_name);
	//if (!(input_field.value.indexOf(".") >= 0 ))
	//	return addstr(msg_mail, field_name);
	if (CheckEmail(input_field.value)==false)
		return addstr(msg_mail, field_name);
	return "";
}

function checkValid(text_input_field, field_name, Valid_Str, max_size, mustFill)
{
	var error_msg= "";
	var size = text_input_field.value.length;
	var str = text_input_field.value;

	if ((mustFill) && (size != max_size) )
		return (addstr(msg_nospaces,field_name));
 	for (var i=0; i < size; i++)
  	{
    	if (!(Valid_Str.indexOf(str.charAt(i)) >= 0))
    	{
			error_msg = addstr(msg_invalid,field_name,Valid_Str);
			break;
    	}
  	}
  	return error_msg;
}

function checkInvalid(text_input_field, field_name, InvalidStr)
// check that no chars in "InvalidStr" appear in input
{
  var str = text_input_field.value;
  var error_msg = "";

  for (var i=0; i < InvalidStr.length; i++)
  {
    if (str.indexOf(InvalidStr.charAt(i)) >= 0)
    {
		 error_msg = addstr(msg_notallow,field_name,InvalidStr);
		 break;
    }
  }
  return error_msg;
}

function checkInt(text_input_field, field_name, min_value, max_value, required)
// NOTE: Doesn't allow negative numbers, required is true/false
{
	var str = text_input_field.value;
	var error_msg= "";
	

	if (text_input_field.value.length==0) // blank
	{
		if (required)
			error_msg = addstr(msg_blank,field_name);
	}
	else // not blank, check contents
	{
		for (var i=0; i < str.length; i++)
		{
			if ((str.charAt(i) < '0') || (str.charAt(i) > '9'))
				error_msg = addstr(msg_check_invalid,field_name);
		}
		if (error_msg.length < 2) // don't parse if invalid
		{

			var int_value = parseInt(str,10);
			if (int_value < min_value)
				error_msg = addstr(msg_outofrange,field_name,min_value,max_value);
			if (int_value > max_value)
				error_msg = addstr(msg_outofrange,field_name,min_value,max_value);
		}
	}
//	if (error_msg.length > 1)
//		error_msg = error_msg + "\n";
	return(error_msg);
}

function blankIP(fn) // true if 0 or blank
{
	return ( (fn.value == "") || (fn.value == "0") )
}

function checkIp(ip1,ip2,ip3,ip4,msg,null_flag)
{
	if( (null_flag == false) && blankIP(ip1) && blankIP(ip2) && blankIP(ip3) && blankIP(ip4) )
		return "";
	var errmsg =  checkInt(ip1,msg,1,255,true);

	errmsg =  (errmsg.length > 1) ? errmsg : checkInt(ip2,msg,0,255,true);
	errmsg =  (errmsg.length > 1) ? errmsg : checkInt(ip3,msg,0,255,true);
	errmsg =  (errmsg.length > 1) ? errmsg : checkInt(ip4,msg,0,255,true);
	errmsg =  (errmsg.length > 1) ? addstr(msg_validIP,msg) : "";
	return errmsg;
}


function search_string(s_string, sub_string)
{
	var i=0, j;
	var first_char = sub_string.charAt(0);
	var sub_length = sub_string.length;
	
	while (i < s_string.length)
	{
		if (s_string.charAt(i) == first_char)
		{
			j = 0;
			while ((j < sub_length) && (s_string.charAt(i+j) == sub_string.charAt(j)))
					j++;
			if (j == sub_length) // all chars match
				return(i); // match starts at i
		}
		i++;
	}
	return -1; // not found
}

function getRadioCheckedValue(radio_object)
{
	var size = radio_object.length;
	for (var i = 0; i < size; i++)
	{
		if (radio_object[i].checked == true)
			return(radio_object[i].value)
	}
	return (radio_object[0].value); // first value if nothing checked
}

function getRadioIndex(radio_object, checked_value)  
{
	var size = radio_object.length;
	for (var i = 0; i < size; i++)
	{
		if (radio_object[i].value == checked_value)
			return  i;
	}

	return  0;   // if no match
}

function getSelIndex(sel_object, sel_text,caseSensitive)
// caseSensitive: true = exact match, false = ignore case
{
	if (sel_text.length == 0)
		return 0;   //  Nothing may be valid. e.g. New SAP contain errors & returned.
	var size = sel_object.options.length;
	var match;
	for (var i = 0; i < size; i++)
	{
		if (caseSensitive)
		  match = ( (sel_object.options[i].text == sel_text) || (sel_object.options[i].value == sel_text) )
		else
		  match =  ( (sel_object.options[i].text.toLowerCase() == sel_text.toLowerCase()) || (sel_object.options[i].value.toLowerCase() == sel_text.toLowerCase()) );
		if (match)
			return(i);
	}
	return 0;  // if no match
}

function dupSelEntry(sel_object,newvalue,caseSensitive)
// check if renaming current value to existing value
// caseSensitive: true = exact match, false = ignore case
{
	var counter = 0;
	var match;
	var size = sel_object.options.length;
	var index = sel_object.selectedIndex;

	for (var i = 0; i < size; i++)
	{
		if (caseSensitive)
		  match = (sel_object.options[i].text == newvalue) ;
		else
		  match =  (sel_object.options[i].text.toLowerCase() == newvalue.toLowerCase() );
		if ((match) && (i != index))
			return true;
	}
	return false;
}

function chkSelected(selObj, err_msg)
{
    if(!(selObj.selectedIndex >= 0 ))
	{
	    alert(err_msg);
	    return false;
	}
	return true;
}
function addOption(selObj, textStr, valueStr)  // value optional
{
	if (addOption.arguments.length == 3)
		selObj.options[selObj.options.length] = new Option(textStr, valueStr);
	else
		selObj.options[selObj.options.length] = new Option(textStr, ""); // value blank
}

function delOption(sel_obj, position)
{
	for (var i = position; i < sel_obj.options.length - 1; i++)
	{
		sel_obj.options[i].text = sel_obj.options[i + 1].text;
		sel_obj.options[i].value = sel_obj.options[i + 1].value;
	}
	sel_obj.options.length = sel_obj.options.length - 1;
}

function getOptionList(sel_obj, strType)  
// return string. strType  = "text", "value" 
{
	var size = sel_obj.options.length; 
	var i; 
	var str = "";
	for(i = 0; i < sel_obj.options.length;  i++)
		str+= (strType=="value")? sel_obj.options[i].value + separator : sel_obj.options[i].text + separator; 
	return str;
}



function makeStr(strchar, strSize)
{
	var newStr = "";
	for (var i = 0; i < strSize; i++)
		newStr+= strchar;
	return newStr;
}

function ignoreSpaces(string)
{
       var temp = "";
       var first=1;
       
       string = '' + string;
       splitstring = string.split(" ");
       for(i = 0; i < splitstring.length; i++)
            if(splitstring[i]!=""){
                if(first==1){
                      if(splitstring[i]!=" "){
                          temp=splitstring[i];
                          first=0;
                      }
                }          
               else
                      temp = temp +  " " + splitstring[i];
            }          
       return temp;
}

function addstr(input_msg)
{
	var last_msg = "";
	var str_location;
	var temp_str_1 = "";
	var temp_str_2 = "";
	var str_num = 0;
	temp_str_1 = addstr.arguments[0];
	while(1)
	{
		str_location = temp_str_1.indexOf("%s");
		if(str_location >= 0)
		{
			str_num++;
			temp_str_2 = temp_str_1.substring(0,str_location);
			last_msg += temp_str_2 + addstr.arguments[str_num];
			temp_str_1 = temp_str_1.substring(str_location+2,temp_str_1.length);
			continue;
		}
		if(str_location < 0)
		{
			last_msg += temp_str_1;
			break;
		}
	}
	return last_msg;
}


function show_data(form_obj)   
// shows form information - used only for debugging
{
	var headvar = "<" + "h" + "e" + "a" + "d" + ">";
	var headend = "<" + "/" + "h" + "e" + "a" + "d" + ">";
	var bodyvar = "<" + "b" + "o" + "d" + "y" + ">";
	var form_size = form_obj.elements.length;
	var debug_win = window.open("","debug","width=540,height=360,menubar=yes,scrollbars=yes,resizable=yes");
	with(debug_win.document)
	{
		open();
		writeln('<html>' + headvar + '<title>Debugging Window</title>' + headend);
		writeln(bodyvar + '<h2>Form being submitted</h2>');
		writeln('<p>Form Name: ' + form_obj.name);
		writeln('<br>Form Action: ' + form_obj.action);
		writeln('<br>Form Target: ' + form_obj.target);
		writeln('</p><h3>Form Data</h3><p>Following table shows ALL fields, even if not submitted.</p>');
		writeln('<p><table border=1><tr bgcolor="#cccccc"><th nowrap>Field Name</th><th>Type</th><th>Value</th></tr>');
		for (var i = 0; i < form_size; i++)
		{
			writeln('<tr><td nowrap>' + form_obj.elements[i].name + '</td>');
			writeln('<td nowrap>' + form_obj.elements[i].type + '</td>');
			writeln('<td nowrap>');
			if ((form_obj.elements[i].type=="select-one") || (form_obj.elements[i].type=="select-multiple"))
				writeln('Selected item: ' + form_obj.elements[i].options[form_obj.elements[i].selectedIndex].text);			
			else 
				writeln(form_obj.elements[i].value);
			if ((form_obj.elements[i].type == "radio") && (form_obj.elements[i].checked))
						write(' (Selected)');
			if ((form_obj.elements[i].type == "checkbox") && (form_obj.elements[i].checked))
					writeln(' (Checked)');
			writeln('</td></tr>');
		}
		writeln('</table></body></html>');
		close();
	}
}


// schedule java-script library
var sch_separator			= ";";
var sch_separator_item		= ",";
var	schedule_use_action		= 0;

function select_chk_dupl(obj, value)
{
	var i;

	for (i=0; i<obj.options.length; i++) {
		if (obj.options[i].value == value) {
			alert(msg_duplicated_period);
			return true;
		}
	}
	return false;
}

function select_add_item(obj, text, value)
{
	var i;

	i = select_chk_dupl(obj, value);
	if (i) {
		return false;
	}

	if (obj.options.length >= max_schedule_item) {
		alert(msg_too_many_periods);
		return false;
	}

	obj.options[obj.options.length] = new Option(text, value);
	return true;
}

function select_del_item(obj)
{
	if (chkSelected(obj, msg_noperiod_selected)) {
		if (confirm(msg_delperiod)) {
			var length = obj.options.length -1;
			while(length >=0){
				if(obj[length].selected == true){
					obj.options[length] = null;
				}
				length--;
			}
			return true;
		}
	}
	return false;
}

function select_show_items(obj, list)
{
	var i;
	var str;

	do {
		if ((null == list) || (list.length <= 0)) {
			break;
		}

		i = list.indexOf(sch_separator);
		if (i < 0) {
			val = list;
			list = null;
		} else {
			val = list.substr(0, i);
			list = list.substr(i+1, list.length-i-1);
		}

		select_add_item(obj, "", val);
	} while(true);

	return;
}


// Browser Issue
function isNS()
{
    if(navigator.appName.indexOf("Netscape") != -1)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function isOpera()   //only good for Opera 8.54
{
    if(navigator.userAgent.indexOf("Opera") >= 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function isChrome()
{
    if(navigator.userAgent.indexOf("Chrome") >= 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function isSafari()
{
    if (navigator.userAgent.indexOf("Safari") >= 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

function isMac()
{
    if(navigator.appVersion.indexOf("Mac") != -1)
    return true;
    else return false;
}

function isWin()
{
    if(navigator.appVersion.indexOf("Win") != -1)
    return true;
    else return false;
}

function isIE()
{
    if(navigator.appName.indexOf("Microsoft Internet Explorer") != -1)
    {
        if (false == isMac() && false == isOpera() && false == isNS())
        {
            return true;
        }
    }
    return false;
}

function isOld()
{
  if(!document.getElementById)
  {
     document.getElementById = function(element)
     { return eval("document.all." + element); }
  }
}

function SupportModalDialog()
{
    if (true == isOpera())
    {
        return false;
    }

    if (true == isChrome())
    {
        return false;
    }

    return true;
}


// IP Fields
var fieldIndex = 0;
var currentField = null;
var ipfield = false;
var lastf = false;
var fstf = false;

function setfIPfield(formObj,fieldObj)
{
	ipfield = true;
	fstf = true;
	lastf = false;
	currentField = fieldObj;
	fieldObj.select();
	for (var i = 0; i < formObj.elements.length; i++)
		if (formObj.elements[i].name == fieldObj.name)
			fieldIndex = i;
}

function setIPfield(formObj,fieldObj)
{
	ipfield = true;
	fstf = false;
	lastf = false;
	currentField = fieldObj;
	fieldObj.select();
	for (var i = 0; i < formObj.elements.length; i++)
		if (formObj.elements[i].name == fieldObj.name)
			fieldIndex = i;
}

function setlIPfield(formObj,fieldObj)
{
	ipfield = true;
	fstf = false;
	lastf = true;
	currentField = fieldObj;
	fieldObj.select();
	for (var i = 0; i < formObj.elements.length; i++)
		if (formObj.elements[i].name == fieldObj.name)
			fieldIndex = i;
}

var lastkeypressed;
var keyTooBig = false;
var mustbeHEX = false;
var keysize;
var lastObj;

function chkSize(fobj)
{ 
	if(fobj.value.length > keysize)
		fobj.value = fobj.value.substr(0,keysize);
}

function keyCheck(fobj)
{	
  lastObj = fobj;
  keyTooBig = (fobj.value.length >= keysize ) ? true : false;
}

if (document.layers) document.captureEvents(Event.KEYPRESS);
document.onkeypress = checkKey;

function checkKey(evt) 
{
  evt = (evt) ? evt : ((window.event) ? window.event : null)
  if (evt) 
  lastkeypressed = (evt.keyCode) ? evt.keyCode : (evt.which ) ? evt.which : null;

  if(ipfield)
  {
	if (lastkeypressed == 46 && currentField.value.length > 0)
	{
		if(lastf == false)
		{
			ipfield = false;
	  		document.forms[0].elements[fieldIndex + 1].focus();
		}
	  	return false;
  	}
	else if (lastkeypressed == 8 && currentField.value.length == 0)
	{
		if(fstf == false)
		{
			ipfield = false;
	  		document.forms[0].elements[fieldIndex - 1].focus();
		}
	  	return false;
  	}
	else if (lastkeypressed < 48 || lastkeypressed > 57) // not numeric
		if (lastkeypressed != 8 && lastkeypressed != 9 && lastkeypressed != 13 )
			return false;
  }

  if ( (lastkeypressed != 13) && (lastkeypressed != 8) && ( keyTooBig ))
  {
  	keyTooBig = false;
  	return false;
  }
  else if (mustbeHEX)  
  {
    mustbeHEX = false;
  	if ( ((lastkeypressed > 47) && (lastkeypressed < 58 )) 
	  || ((lastkeypressed > 96) && (lastkeypressed < 103))
	  || ((lastkeypressed > 64) && (lastkeypressed < 71 ))
	  || (lastkeypressed ==  8) 
	  || (lastkeypressed == 13) )
		 return true;
  	else return false;
  }
  return true;
}

function check_validIP(ip1, ip2, ip3, ip4,min,max,notU,msg,null_flag)
{
    var errmsg = checkIp(ip1,ip2,ip3,ip4,msg,null_flag);

    if (errmsg.length == 0 && (null_flag == true || ip1.length != 0))
    {
        errmsg = check_ip_first_part(ip1,min,max,notU,msg);
    }
    return errmsg;
    
}

function isInteger(str, min_value, max_value)
{
	if(str.length == 0)
		return false;
	for (var i=0; i < str.length; i++)
	{
		if ((str.charAt(i) < '0') || (str.charAt(i) > '9'))
				return false;
	}
	var int_value = parseInt(str,10);
	if ((int_value < min_value) || (int_value > max_value))
		return false;
	return true;
}

function valid_ipv4(addr)
{
    var ip_arry=addr.split(".");
		var size = addr.length;
    if (size == 0)
    {
        return false;
    }
    if ((ip_arry.length == 4)&& (size <= 15) && (size >=7))
    {
        for(var i=0;i<ip_arry.length;i++)
        {
    	    if (!isInteger(ip_arry[i], 0, 255))
    	    {   
        	    return false;
    	    }
	    	}
	    	return true;
    }
    return false;
}

var V6_INADDRSZ = 16;
function valid_ipv6(input_str, prelen_flag)
{
  var digits = "0123456789abcdef";
  var saw_digit = false;
  var val = 0;
  var colonp = -1;
  var i = 0;
  var j = 0;
  var len;
  var letter1;
  var curtok;
  var ch;

  if ((letter1 = input_str.charAt(i)) == ':')
  {
    if ((letter1 = input_str.charAt(i++)) != ':')
    {
      return false;
    }
  }

  curtok = i;

  while (i < input_str.length)
  {
    ch = input_str.charAt(i).toLowerCase();
    i++;
    if ((len = digits.indexOf(ch)) != -1)
    {
      val <<= 4;
      val |= len;
      if (val > 0xffff)
      {
        return false;
      }
      saw_digit = true;
      continue;
    }

    if (ch == '/')
    {
			if(!prelen_flag)
			{
				return false;
			}
			else 
			{
				if(input_str.indexOf('/', i))
				{
					return false;
				}
				if(!isInteger(input_str.substring(i), 0, 128))
				{
					return false;
				}
				break;
			}
		}

    if (ch == ':')
    { 
      curtok = i;
      if (!saw_digit) 
      {
        if (colonp != -1)
        { 
          return false;
        }
        colonp = j;
				continue;
      } 
      else if (i == input_str.length) 
      {
        return false;
      }

      if ((j + 2) > V6_INADDRSZ)
      {
        return false;      
      }
      j += 2;
      val = 0;
      saw_digit = false;
      continue;
    }

    if (ch == '.'  && ((j + 4) <= V6_INADDRSZ))
    {
      //TODO: IPv4 mapped IPv6 address is not supported
      if (!valid_ipv4(input_str.substring(curtok)))
      {
        return false;
      }
      j += 4;
      saw_digit = false;
      break;
      
    }
    return false;
  }

  if (saw_digit) 
  {
    if ((j + 2) > V6_INADDRSZ)
    {
      return false;
    }
    j += 2;
  }

  if (colonp != -1) 
  {
    if (j == V6_INADDRSZ)
    {
      return false;
    }
    j = V6_INADDRSZ;
  }

  if (j != V6_INADDRSZ)
  {
    return false;
  }

  return true;
}

function checkValidipv6(fieldObj, fmsg, prelen_flag)
{
  if(!valid_ipv6(fieldObj.value, prelen_flag))
  	return addstr(msg_illegal_addr, fmsg);
	return "";
}

function checkValidAddress(fieldObj, fmsg)
{
  if (!checkHostName(fieldObj.value))
  {
  	if(!valid_ipv6(fieldObj.value, false))
  		return addstr(msg_illegal_addr, fmsg);
  }
	return "";
}

function randomString(len, string)
{
    var str = "";

    for (var i=0; i<len; i++)
    {
        str += string.charAt(Math.ceil(Math.random()*100000000)%string.length);
    }

    return str;
}

