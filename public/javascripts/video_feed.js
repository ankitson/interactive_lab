function init()
{ set_Video(); }

function set_Video()
{
	var cf = document.forms[0];
	var vs = document.getElementById("v_play");

	if (vmode != "")
	{
		vs.style.display = "block";
	}
	else
	{
		vs.style.display = "none";
	}
}

/* OCX Video init */
var vmode = "mpeg"; // "";    // mpeg, jpeg, 
var iPad = '172.31.2.125';         // '172.31.2.125'
var lpp = 'YWRtaW46YWRtaW4=';          // 'YWRtaW46YWRtaW4='
var lang_str ="USA";
var brow;
var ipadd = 'robotics.linksyscam.com';

if(isIE()) { var brow = "IE"; }
if(isNS()) { var brow = "MZ"; }

if (self.location.protocol != "http:")
{
    if (ipadd.indexOf(":") > 0)
    {
        iPad = ipadd.substring(0, ipadd.indexOf(":"));
    }
}

else
{
    var temp = iPad;
    var count = 0;
    var index = 0;
    do
    {
        //alert("temp="+temp);
        index = temp.indexOf(":");
        if (index <= 0)
        {
            break;
        }
        
        count ++;
        temp = temp.substring(index+1);
    }while (index > 0);

    if (count >= 2) // ipv6
    {
        iPad = "[" + iPad +"]";
    }
    //alert("ipadd="+ipadd+", count="+count);
}
    
var dw_jpeg = 	'<object classid="'+viewer_ocx_classid+'" CODEBASE="'+viewer_ocx_codebase+'" id="'+viewer_ocx_id+'" width="640" height="524">'+
				  '<param name="Text" value="http://'+
				  ipadd+
				  '/img/mjpeg.cgi'+
				  ' '+
				  lpp+
				  ' '+
				  brow+
				  ' '+
				  lang_str+
				  '">' + 
				  '<param name="BackColor" value="12632256">'+
				  '<param name="_Version" value="65536">'+
				  '<param name="_ExtentX" value="11774">'+
				  '<param name="_ExtentY" value="6562">'+
				'</object>';

//var dw_mpeg = '&nbsp;';
var dw_mpeg = 	'<object classid="'+viewer_ocx_classid+'" CODEBASE="'+viewer_ocx_codebase+'" id="'+viewer_ocx_id+'" width="640" height="524">'+
				  '<param name="Text" value="http://'+
				  ipadd+
				  '/img/video.asf'+
				  ' '+
				  lpp+
				  ' '+
				  brow+
				  ' '+
				  lang_str+
				  '">' + 				  
				  '<param name="BackColor" value="12632256">'+
				  '<param name="_Version" value="65536">'+
				  '<param name="_ExtentX" value="11774">'+
				  '<param name="_ExtentY" value="6562">'+
				'</object>';
    
var dw_push = 	'<img border="0" alt="Video for other Platform/OS" src="http://robotics.linksyscam.com/img/video.mjpeg">'; 				  

function dw(message)
{ document.write(message); }


function doPlay() 
{
	if(vmode != "")
	{
		if(isWin())
		{
			if(isIE())
			{
				if( vmode == "jpeg" )
				{ dw(dw_jpeg); }
				else
				{ dw(dw_mpeg); } 
			}
			else
			{
				dw(dw_push); 
			}
		}
		else
		{
			dw(dw_push); 
		}
	}
	else return false; 
}
/* OCX Video End */


var is_auto_reload = true;
function reloadOnErr(obj) {
	if(!is_auto_reload)
		return;
	setTimeout("eval('obj.src = obj.src;'", 500);
}

// Admin
var is_admin = false; // set by init()
function chkAdmin()
{
	if(!is_admin)
		return confirm(msg_admin_config);
	else
		return true;
}

function doStop() 
{	
 	if(isIE())
	{
		document.LinksysMLViewer.StopPlay(); 
	}
}
