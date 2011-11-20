function dw(message)
{ document.write(message); }


//Top Menu
tm01="Wireless-N Internet Home Monitoring Camera";
tm02="Home";
tm03="View Video";
tm04="Setup";
tm05="Linksys Web";
tm06="Help";
tm07="Exit";
tm08="Copyright 2009 Cisco Systems, Inc. All rights reserved.";
tm09="Advanced Configuration";
tm10="Logout";
tm11="Linksys Camera Mobile Viewer";
tm12="Linksys Camera - Live Video";

//Left Menu
lm01="Setup";
lm02="Basic";
lm03="Image";
lm04="Administration";
lm05="Users";
lm06="DDNS";
lm07="Options";
lm08="Motion Detection";
lm09="Status";
lm101="Recording";
//
lm10="Setup - Basic";
lm11="Setup - Image";
lm12="Setup - Administration";
lm13="Setup - Users";
lm14="Setup - DDNS";
lm15="Setup - Options";
lm16="Setup - Motion Detection";
lm17="Setup - Status";
lm20="Setup - SMB/CIFS";

//Buttons
bt01="Apply";
bt02="Cancel";
bt03="Help";
bt04="Continue";
bt05="Back";
bt06="Refresh";
bt07="OK";
bt08="Remove";
bt09="Delete";
bt10="Clear";
bt11="Edit";
bt12="Generate";
bt25="Add";
//
bt13="Delete All";
bt14="Clear Log";
bt15="Add User";
//
bt16="Sync with PC";
bt17="Edit Security Settings";
bt18="Update Now";
bt19="DDNS Account";
bt20="Remove Camera";
bt21="Restore Defaults";
bt22="Upgrade Firmware";
bt23="Start Upgrade";
bt24="Set Sensitivity Area";
bt28="Change";
//
bt26="Web Site";
bt27="Change";
bt30="Skip";

//Admin Help
hav001="Administration Help";
hav002="Linksys Support Page - Download Latest Viewer/Recorder Utility";
hav003="Click here to learn how to configure Port Forwarding in your Linksys Router";
hav004="Adobe website (software for viewing PDF documents)";


//User Help
huv001="User Help";
huv002="Help Links";
huv003="Linksys Support Page - Download Latest Viewer/Recorder Utility";
huv004="Adobe website (software for viewing PDF documents)";
huv005="You can view video in the two following ways:";
huv006="A. Web Browser -&nbsp;";
huv007="You can view video using Internet Explorer 6.0 or higher.&nbsp; When you click";
huv008=", an ActiveX component (ocx file) will need to be downloaded and installed on your PC. You will be prompted to install this ocx file if it is not present in your system.";
huv009="B. Linksys Viewer &amp; Recorder Utility -&nbsp;";
huv010="This utility was included on the CD-ROM that came with the Camera. You may also download it from the link above. This utility allows you to view video and schedule recordings.";
huv011="Note: The Wireless-N Internet Home Monitoring Camera supports a maximum of five users simultaneously.";




///////////////////////////////////////////////////////

/* -  Config UI Display Content - */

//Basic
bv001="Basic Settings";
bv002="Device Settings";
bv003="Network Settings";
bv004="Wireless Settings";
//
bv005="Device ID:";
bv006="Camera Name:";
bv007="Description:";
bv008="LED Operation:";
bv009="Current Date/Time:";
bv010="Time Zone:";
bv011="Adjust for daylight saving";
//
bv012="(GMT-12:00) International Date Line West";
bv013="(GMT-11:00) Midway Island, Samoa";
bv014="(GMT-10:00) Hawaii";
bv015="(GMT-09:00) Alaska";
bv016="(GMT-08:00) Pacific Time (US & Canada); Tijuana";
bv017="(GMT-07:00) Arizona";
bv018="(GMT-07:00) Chihuahua, La Paz, Mazatlan";
bv019="(GMT-07:00) Mountain Time (US & Canada)";
bv020="(GMT-06:00) Central America";
bv021="(GMT-06:00) Central Time (US & Canada)";
bv022="(GMT-06:00) Guadalajara, Mexico City,Monterrey";
bv023="(GMT-06:00) Saskatchewan";
bv024="(GMT-05:00) Bogota, Lima, Quito";
bv025="(GMT-05:00) Eastern Time (US & Canada)";
bv026="(GMT-05:00) Indiana (East)";
bv027="(GMT-04:00) Atlantic Time (Canada)";
bv028="(GMT-04:00) Caracas, La Paz";
bv029="(GMT-04:00) Santiago";
bv030="(GMT-03:30) Newfoundland";
bv031="(GMT-03:00) Brasilia";
bv032="(GMT-03:00) Buenos Aires, Georgetown";
bv033="(GMT-03:00) Greenland";
bv034="(GMT-02:00) Mid-Atlantic";
bv035="(GMT-01:00) Azores";
bv036="(GMT-01:00) Cape Verde Is.";
bv037="(GMT) Casablanca, Monrovia";
bv038="(GMT) Greenwich Mean Time: Dublin,Edinburgh,Lisbon,London";
bv039="(GMT+01:00) Amsterdam, Berlin,Bern,Rome,Stockholm,Vienna";
bv040="(GMT+01:00) Belgrade, Bratislava,Budapest,Ljubljana,Prague";
bv041="(GMT+01:00) Brussels, Copenhagen, Madrid, Paris";
bv042="(GMT+01:00) Sarajevo, Skopje, Warsaw, Zagreb";
bv043="(GMT+01:00) West Central Africa";
bv044="(GMT+02:00) Athens, Istanbul, Minsk";
bv045="(GMT+02:00) Bucharest";
bv046="(GMT+02:00) Cairo";
bv047="(GMT+02:00) Harare, Pretoria";
bv048="(GMT+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius";
bv049="(GMT+02:00) Jerusalem";
bv050="(GMT+03:00) Baghdad";
bv051="(GMT+03:00) Kuwait, Riyadh";
bv052="(GMT+03:00) Moscow, St. Petersburg, Volgograd";
bv053="(GMT+03:00) Nairobi";
bv054="(GMT+03:30) Tehran";
bv055="(GMT+04:00) Abu Dhabi, Muscat";
bv056="(GMT+04:00) Baku, Tbilisi, Yerevan";
bv057="(GMT+04:30) Kabul";
bv058="(GMT+05:00) Ekaterinburg";
bv059="(GMT+05:00) Islamabad, Karachi, Tashkent";
bv060="(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi";
bv061="(GMT+05:45) Kathmandu";
bv062="(GMT+06:00) Almaty, Novosibirsk";
bv063="(GMT+06:00) Astana, Dhaka";
bv064="(GMT+06:00) Sri Jayawardenepura";
bv065="(GMT+06:30) Rangoon";
bv066="(GMT+07:00) Bangkok, Hanoi, Jakarta";
bv067="(GMT+07:00) Krasnoyarsk";
bv068="(GMT+08:00) Beijing, Chongqing, Hong Kong, Urumqi";
bv069="(GMT+08:00) Irkutsk, Ulaan Bataar";
bv070="(GMT+08:00) Kuala Lumpur, Singapore";
bv071="(GMT+08:00) Perth";
bv072="(GMT+08:00) Taipei";
bv073="(GMT+09:00) Osaka, Sapporo, Tokyo";
bv074="(GMT+09:00) Seoul";
bv075="(GMT+09:00) Yakutsk";
bv076="(GMT+09:30) Adelaide";
bv077="(GMT+09:30) Darwin";
bv078="(GMT+10:00) Brisbane";
bv079="(GMT+10:00) Canberra, Melbourne, Sydney";
bv080="(GMT+10:00) Guam, Port Moresby";
bv081="(GMT+10:00) Hobart";
bv082="(GMT+10:00) Vladivostok";
bv083="(GMT+11:00) Magadan, Solomon Is., New Caledonia";
bv084="(GMT+12:00) Auckland, Wellington";
bv085="(GMT+12:00) Fiji, Kamchatka, Marshall Is.";
bv086="(GMT+13:00) Nuku'alofa";
//
bv087="IPv4 Configuration Type:";
bv187="IPv6 Configuration Type:";
bv188="IP Format:";
bv088="Obtain Address Automatically";
bv089="Fixed IP Address";
bv090="IPv4 Address:";
bv091="IPv4 Subnet Mask:";
bv092="IPv4 Gateway:";
bv093="IPv4 Primary DNS:";
bv094="IPv4 Secondary DNS:";
bv190="IPv6 Address:";
bv191="IPv6 Subnet prefix length:";
bv192="IPv6 Gateway:";
bv193="IPv6 Primary DNS:";
bv194="IPv6 Secondary DNS:";
bv195="IPv6 Address(es):";
bv196="IPv6 Gateway(s):";

//
bv095="SSID:";
bv096="Network Type:";
bv097="Channel No:";
bv098="Security:";
bv099="Ad-hoc";
bv100="Infrastructure";
bv101="WSC PIN Code:";
//
bv102="IPv4 only";
bv103="IPv6 only";
bv104="IPv4 and IPv6";
bv105="IP Version:";
//
bvv001="Enable";
bvv002="Disable";
//Wsecurity.htm
bwv001="Wireless Security";
bwv002="Security Mode:";
bwv003="WPA2 Personal";
bwv004="TX Key:";
bwv005="WEP Encryption:";
bwv006="64 Bit Keys (10 Hex chars)";
bwv007="128 Bit Keys (26 Hex chars)";
bwv008="Passphrase:";
bwv009="Authentication:";
bwv010="Open System";
bwvv010="Shared Key";
bwv011="Shared Key:";
bwv012="Algorithm:";
bwv013="(8 to 63 characters or 64 hex characters)";
//
bwv014="Key 1:";
bwv015="Key 2:";
bwv016="Key 3:";
bwv017="Key 4:";
//
bwvv002="Disable";


//DDNS
dv001="DDNS Settings";
 //
dv026="Enable DDNS";
dv027="Service Provider:";
dv029="DynDNS";
dv030="TZO";
dv031="DDNS";
//
dv033="Domain Name:";
dv034="E-Mail Address:";
dv035="TZO Key:";
dv036="Update Period:";
dv037="starting at";
dv038="(hh:mm)";
dv039="Status:";
dv040="Update Now"
//
vv003="Every";
vv004="mins";
vv005="hour";
vv006="hrs";
 

//Event
ev001="Motion Detection Settings";
ev002="Schedule List";
//
ev003="New Motion Trigger Schedule";
//
ev004="Trigger Motion Detection";
ev005="Enable Motion Detection:";
ev006="";
ev007="Interval:";
ev008="Minute(s) before detecting the next motion detection.";
ev009="Action(s):";
//
ev010="Attachment Type:";
ev011="JPEG Image";
ev012="Video";
ev013="Video Format (MPEG-4):";
ev014="Pre-Capture Length:";
ev015="Post-Capture Length:";
ev016="Frame Rate:";
ev017="fps";
//
vv007="Every day";
vv008="Weekdays (Mon - Fri)";
vv009="Sunday";
vv010="Monday";
vv011="Tuesday";
vv012="Wednesday";
vv013="Thursday";
vv014="Friday";
vv015="Saturday";
vv016="Start Time:";
vv017="End Time:";
vv018="E-Mail";
vv019="FTP";
vv020="Second(s)";
vv021="(hh:mm)";


//Image
iv001="Image Settings";
iv002="Settings";
iv003="Resolution:";
iv004="Video Quality Control:";
iv005="Constant Bit Rate:";
iv0050="Kb ps";
iv0051="Mb ps";
iv006="Fixed Quality:";
iv007="Very High";
iv008="High";
iv009="Normal";
iv010="Low";
iv011="Very Low";
iv012="Max Frame Rate:";
//
iv013="Mobile Settings";
iv014="Enable Mobile Streaming";
//
iv015="Video Adjustments";
iv016="Power Line Frequency:";
iv017="(for fluorescent lighting)";
iv018="White Balance:";
iv019="Auto";
iv020="Black&White";
iv021="Brightness:";
iv022="Sharpness:";
iv023="Enable Time Stamp";
iv024="Enable Text Display";
iv025="Indoor (Incandescent)";
iv026="Fluorescent (white light)";
iv027="Fluorescent (yellow light)";
iv028="Outdoor";
//
iv029="MPEG-4 Settings";
iv030="MJPEG Settings";
iv031="Access Code:";
iv032="Enable Microphone";

iv033="Enable Low Light Sensitivity";

//Option
ov001="Options Settings";
ov0010="Index";
ov0011="Back to Top";
ov002="E-Mail Alert";
ov003="(Send E-Mail Alert when Motion Detected)";
ov004="Send To:";
ov005="(E-Mail Address)";
ov006='Show "From" as:';
ov007="Subject:";
ov008="SMTP Mail Server:";
em001="SMTP Port Number:";
em002="(1-65535)";
em003="Specify a SMTP Mail Server";
ov009="(Outgoing Mail Server)";
ov010="My Mail Server Requires Authentication";
ov011="Account Name:";
ov012="Password:";
ov013="Delay between E-Mails:";
ov014="E-Mail Video:";
ov015="Video length:";
ov016="Set Sensitivity Area";
ov017="(Discovery Only)";
ov018="Alternate Web Access Port";
ov019="(For HTTP/Web connections)";
ov020="Port Number:";
//
ov021="(E-Mail Address #1)";
ov022="(E-Mail Address #2)";
ov023="(E-Mail Address #3)";
ov0230="Test E-Mail";
ov024="UPnP";
// FTP
ov025="FTP";
ov026="FTP Server:";
ov027="Port:";
ov028="Login Name:";
ov029="Password:";
ov030="Passive Mode:";
ov031="File Path Name:";
// RTP/RTSP
ov032="RTP/RTSP";
ov033="RTSP Port:";
ov034="RTP Data Port:";
ov035="Max RTP Data Packet:";
ov036="(1024-65534)";
ov037="bytes";
// Multicast RTP/RTSP
ov038="Multicast RTP/RTSP";
ov039="IPv4 Video Address:";
ov139="IPv6 Video Address:";
ov040="Video Port:";
ov041="Time to Live:";
ov042="even values only";
ov043="IPv4 Audio Address:";
ov143="IPv6 Audio Address:";
ov044="Audio Port:";

//
vv001="Enable";
vv002="Disable";
vv021="Minutes";
vv022="Seconds";
vv023="Other";


//Password
pv001="Login";
pv002="Login Name:";
pv003="Password:";
pv004="Verify Password:";
pv005="Your password must be less than 64 characters long and it cannot contain spaces or special characters.";
pv006="Restore Factory Defaults";
pv007="Any settings you have saved will be lost when the default settings are restored.";
pv008="Firmware Upgrade";
pv009="Firmware:";
pv0010="Language";
pv_lang_list_0000="English"
pv_lang_list_0001="English-Europe"
pv_lang_list_0002="French"
pv_lang_list_0003="German"
pv_lang_list_0004="Swedish_SE"
pv_lang_list_0005="Spanish"
pv_lang_list_0006="Italian"
pv_lang_list_0007="Portugal"
pv_lang_list_0008="Denmark"
pv_lang_list_0009="Dutch"
pv_lang_list_0020="English"
pv_lang_list_0021="Simplified Chinese"
pv_lang_list_0022="Traditional Chinese"
pv_lang_list_0023="Australia English"
pv_lang_list_0024="Japanese"
pv_lang_list_0025="Korean"

//
vv024="Note:";
vv025="Caution:";
//upg_fw.htm
ufv001="Upgrade Firmware";
ufv002="The upgrade firmware file needs to be downloaded and stored on your PC.";
ufv003="Upgrade File:";
//upg_pg.htm
ufv004="Firmware Upgrade in Progress !";
ufv005="Please wait. This could take 4 to 5 minutes.";
ufv006="Progress";
ufv007="Upgrade must NOT be interrupted !";


//Status
sv001="Status Settings";
sv002="System Status";
sv003="Firmware Version:";
sv004="MAC Address:";
sv005="Log";
sv006="System Log:";
sv007="Wireless"
sv008="Ethernet"
sv009="Disable"
sv010="WEP"
sv011="WPA Personal"
sv012="WPA2 Personal"
sv013="N/A"

domain000="Domain:";
domain001="Africa";
domain002="Asia";
domain003="Australia";
domain004="Canada";
domain005="Europe";
domain006="Spain";
domain007="France";
domain008="Israel";
domain009="Japan";
domain010="Mexico";
domain011="South America";
domain012="USA";
//
vv026="Date/Time:";
vv027="Network";
vv028="Wireless";


//User
rv001="Users Settings";
rv002="User Access";
rv003="Allow access by:";
rv004="All users";
rv005="Only users in database";
rv006="User Name:";
rv007="User Password:";
rv008="Confirm Password:";

//mobile
mv01="Linksys Network Camera";
mv02="Reload";

//SMB/CIFS
smb001="Enable";
smb002="Samba Server:";
smb003="Upload Path:";
smb004="Maximum Size of Each File:";
smb005="MB";
smb006="Enable adding timestamp to files";
smb007="File Name Prefix:";
smb008="Maximum Duration:";
smb009="Define Recording Schedule";
smb010="Minutes";
smb011="Start at:";
smb012="Stop at:";
smb013="(yy:mm:dd:hh:mm.avi)";
smb014="Searching Samba Server";
smb015="Select where you want to save your recordings";
smb016="Start Recording now";
smb017="Input Username/Password";
smb018="Username:";
smb019="Password:";
smb0201="Invalid Username/Password (No Access)";
smb0202="Invalid Username/Password (No Enough Rights)";
smb021="Browse";

///////////////////////////////////////////////////////

/* -  Help Content - */
// -  Important: No translation on HTML Tags, sample list as below . . . .
// -  HTML Tags: <b>, </b>, <i>, </i>, &quot;, &nbsp;, <br>, <p>, </p>, <a>, </a>, <big>, </big>, <u>, </u>, <ul>, </ul>, <li>, </li>, <pre>, </pre>, 

//Basic
hbh01="Help - Basic";
hbh02="Device ID";
hbh03="This displays the ID for the Wireless-N Internet Home Monitoring Camera. This is used by the Setup Wizard and the Viewer and Recorder Utility to identify the Camera.";
hbh04="Camera Name";
hbh05="Enter the preferred name for the Wireless-N Internet Home Monitoring Camera.&nbsp; It must not exceed 16 alphanumeric characters.";
hbh06="Description";
hbh07="This field is used for entering a description, such as the location of the Wireless-N Internet Home Monitoring Camera.&nbsp; Entering a description will help you identify the Camera. It must not exceed 32 alphanumeric characters.";
hbh08="Current Date/Time";
hbh09="It displays the current date and time. If it's not correct, Click the &quot;Sync with PC&quot; button to let the camera use the same date and time as PC's.";
hbh10="Time Zone";
hbh11="Choose the time zone for your location from the drop-down list. <BR>If your location is currently using Daylight Savings, enable the <i>Adjust for daylight saving</i> checkbox.";
hbh120="IP Version";
hbh130="Select configuration for IP version. IPv4 only; IPv6 only; IPv4 and IPv6.";
hbh121="IPv4 Configuration Type";
hbh131="Select &quot;Obtain Address Automatically &quot; if your network has a DHCP server. <br>If you choose &quot;Fixed IP Address&quot;, you must configure the IP Address, Subnet Mask, Gateway and DNS. <p>IP Address - Assign an IP address that is unique to your local network. There's no need to purchase a separate IP address from your ISP.</p> <p>Subnet Mask - The Subnet Mask (also known as IP Mask) must be the same as the Subnet Mask set on the other devices on your Ethernet (wired) network.</p> <p>Gateway - Enter the IP address of your network's Gateway.</p> <p>DNS - The Primary DNS address is required, while the Secondary DNS is optional. Use the same value(s) as the one(s) used by PCs on your LAN. Normally, your ISP will recommend a DNS.</p>";
hbh122="IPv6 Configuration Type";
hbh132="Select &quot;Obtain Address Automatically &quot; if your network supports address autoconfiguration. <br>If you choose &quot;Fixed IP Address&quot;, you must configure the IP Address, IPv6 Subnet prefix length, Gateway and DNS. <p>IP Address - Assign an IP address that is unique to your local network.</p> <p>IPv6 Subnet prefix length - A decimal value specifying how many of the leftmost contiguous bits of the address compose the subnet prefix.</p> <p>Gateway - Enter the IP address of your network's Gateway.</p> <p>DNS - The Primary DNS address is required, while the Secondary DNS is optional. Use the same value(s) as the one(s) used by PCs on your LAN. Normally, your ISP will recommend a DNS.</p>";
hbh14="SSID";
hbh15="The SSID is the network name shared among all devices in a wireless network. The SSID must be identical for all devices in the wireless network. It is case-sensitive and must not exceed 32 alphanumeric characters, which may be any keyboard character. Make sure this setting is the same for all devices in your wireless network. For added security, Linksys recommends that you change the default SSID (<b>linksys</b>) to a unique name of your choice.";
hbh16="Network Type";
hbh17="Select Infrastructure mode if you are connecting the Wireless-N Internet Home Monitoring Camera to a network access point. Select Ad-Hoc mode if the Wireless-N Internet Home Monitoring Camera&nbsp; is connecting directly to a PC or notebook.";
hbh18="Channel No";
hbh19="Select the appropriate channel from the list provided to correspond with your network settings, between 1 and 13 (in Europe). All devices in your wireless network must use the same channel in order to function correctly.<br> Note: In Infrastructure mode, you cannot specify a channel setting on the Wireless-N Internet Home Monitoring Camera. It will automatically be configured to the station you are connecting the Wireless-N Internet Home Monitoring Camera to.";
hbh20="Security";
hbh21="It displays the current security setting for Wirelesss connections. <br>Click the <b>Edit Security Settings</b> button to configure the security settings.";
// W_Sec
hbh22="Security Mode";
hbh23="Select the desired option. All wireless clients must use the same settings as this camera. There are four wireless security mode options supported by the camera: Disable, WEP, WPA Personal, and WPA2 Personal.";
hbh24="Disable";
hbh25="This option features no security on your wireless network. Data is not encrypted before transmission.";
hbh26="WEP";
hbh27="WEP is a basic encryption method, which is not as secure as later methods such as WPA-Personal or WPA2 Personal. However, it is supported by all clients. If using WEP, select a level of WEP encryption, <b>64-bit</b> or <b>128-bit</b>. If you want to use a Passphrase, then enter it in the Passphrase field and click the <b>Generate</b> button. If you want to enter the WEP key manually, then enter it in the WEP Key 1-4 field(s). To indicate which WEP key to use, select the appropriate TX Key number.";
hbh28="WPA/WPA2 Personal";
hbh29="This method offers two encryption methods detected automatically, <b>TKIP</b> or <b>AES</b>, with dynamic encryption keys. Enter the shared key, which can have 8 to 63 characters.";
//  Select the type of encryption method you want to use, TKIP and AES. Then enter the Key Renewal period, which instructs the device how often it should change the encryption keys.
//LED 
hbh30="LED Operation";
hbh31="Enable this if you want to turn on the LED.";


//DDNS
hdh01="Help - DDNS";
hdh02="Use this feature to access the Wireless-N Internet Home Monitoring Camera from a remote location.";
hdh03='<big class="blk">ATTENTION</big> <b>- To complete the DDNS Service setup, port forwarding needs to be configured in your router.&nbsp; Click here to learn how to configure port forwarding on the Linksys Router - &nbsp;<a href="http://www.linksys.com/portfwd" class="sp" target="_blank">http://www.linksys.com/portfwd </a></b>';
hdh19="DDNS Enable/Disable";
hdh20="Enable or disable the DDNS function, as required.";
hdh21="Only enable this feature if you have registered for the DDNS Service with a DDNS Server provider.";
hdh22="Web Site<BR>Button";
hdh23="Click this button to open a new window and connect to the Web site for the selected DDNS service provider. ";
hdh24="(TZO)";
hdh25="Enter the domain name allocated to you by the DDNS Server provider. ";
hdh26="Enter the E-Mail address that is used to register the DDNS Service. ";
hdh27="Enter the TZO Key provided by the DDNS Service provider.";
hdh28="Set the schedule for checking if the Internet IP address has changed. If the IP address has changed, the DDNS Server will be notified. ";
hdh29="Service Provider";
hdh30="DDNS service provider(Only can use TZO).";
hdh31="Status";
hdh32="Display the last update result.";
hdh33="Domain Name";
hdh34="E-Mail Address";
hdh35="TZO Key";
hdh36="Update Period";
hdh37="Update Now<br>Button";
hdh38="Click this button if you wish to update now.";


//Event
heh01="Help - Motion Detection";
heh02="An trigged motion detection is a set of parameters describing how and when the camera will perform certain triggered actions, such as uploading video or snapshot files to a specified destination (E-Mail account or FTP server), according to requirements.";
heh04="<B>Notes:</B> <UL> <LI>It is important to note that adding a new motion detection trigger will stop any motion detection that is currently running. A scheduled motion detection will automatically resume, if the time is still within the scheduled period. A triggered motion detection will need to be re-triggered. <LI>The camera can be configured for up to 10 motion detections. <BR> <BR></LI></UL>";
heh05="The <B>Schedule List</B> shows all of the motion detection schedules currently configured in the  camera.";
heh06="Name";
heh07="Provide a descriptive name for the motion detection, using a maximum of 20 characters. This name will be displayed in the Motion Detection Schedule List.";
heh08="Trigger Motion Detection";
heh09="Choose the desired option for the effective time frame.";
heh10="Start Time";
heh11="Choose the desired start time using a 24 hr clock.";
heh12="End Time";
heh13="Choose the desired end time using a 24 hr clock.";
heh15="Enable Motion Detection";
heh16="Movement in a motion detection window can be used to trigger motion detections. Check to perform all of the motion detection(s) that were configured and scheduled.";
heh17="Interval";
heh18='Select the desired option for the motion detections interval. (* "0" = No Delay)';
heh19="Action(s)";
heh20='<ul> <li><b>E-Mail</b><br> If checked, an E-Mail (with "Attachment") will be delivered to the SMTP server.<li><b>FTP</b><br> If checked, an FTP upload (with "Attachment") will be activated to the FTP server. </ul>';
heh21="Attachment Type<br>(for E-Mail or FTP)";
heh22="<b>JPEG Image -</b> (MJPEG Mode Only)";
heh23="Frame Rate - Select the desired capture rate for the JPEG image(s) here.";
heh24="Pre/Post Capture - Select the desired length. The snapshot(s) of the JPEG image depends on this setting, and also the file size and degree of compression.";
heh25="<b>Video Format -</b> (MPEG-4 Mode Only)";
heh26="Video File Type - Select the desired type for the video file.";
heh27="Pre/Post Capture - Select the desired length. The size of the file depends on this setting, and also the Video size and degree of compression.";
heh28="Buttons";
heh29="Use the <i>Add</i> and <i>Clear</i> buttons to manage the schedule properties.";
heh30="Delete<BR>Button";
heh31="Use this button to delete one item in the <B>schedule list</B>";


//Image
hih01="Help - Video Image";
hih02="Resolution";
hih03="Video Quality Control";
hih04="Max Frame Rate";
hih05="<ul> <li>Constant Bit Rate: Select the desired fix bit rate. The default bit rate is set to 512 Kb ps.</li> <li>Fix Quality: Select the desired fix quality. The default fix quality is set to Normal.</li> </ul> Note: Higher image quality requires more bandwidth.";
hih06="Select the desired maximum frame rate. The default maximum frame rate is set to 10 fps.&nbsp;&nbsp;<br> Note: Higher frame rate requires more bandwidth.";
hih07="Resolution";
hih08="Fix Video Quality";
hih09="Max Frame Rate";
hih10="Select the desired video resolution format.&nbsp; The default resolution is set to 320&times;240.";
hih11="Fix Quality: Select the desired fix quality. The default fix quality is set to Normal.";
hih12="Select the desired maximum frame rate. The default maximum frame rate is set to 10 fps.&nbsp;&nbsp;<br> Note: Higher frame rate requires more bandwidth.";
hih13="Enable Mobile Streaming";
hih14="Resolution";
hih15="Video Quality Control";
hih16="Max Frame Rate";
hih17="Enable streaming video for the mobile device by checking this checkbox.";
hih18="The default resolution is set to 160x120.";
hih19="<ul> <li>Constant Bit Rate: Select the desired fix bit rate. The default bit rate is set to 32 Kb ps.</li> <li>Fix Quality: Select the desired fix quality. The default fix quality is set to Normal.</li> </ul> Note: Higher image quality requires more bandwidth.";
hih20="Select the desired maximum frame rate. The default maximum frame rate is set to 15 fps.&nbsp;&nbsp;<br> Note: Higher frame rate requires more bandwidth.";
hih21="Power line frequency";
hih22="Select the power line frequency (50Hz or 60Hz) used in your region, to improve the picture quality under fluorescent lighting.";
hih23="White Balance";
hih24="Select the suitable white balance option as you desired.";
hih25="Brightness";
hih26="If necessary, you can adjust the brightness to obtain a better image. For example, if the camera is facing a bright light, the image may be too dark. In this case, you can increase the brightness.";
hih27="Sharpness";
hih28="Select the desired option for the sharpness. You can select a Sharpness value between -3 and 3.";
hih29="Contrast";
hih30="Select the desired option for the contrast. You can select a contrast value between -3 and 3.";
hih31="Time Stamp";
hih32="Enable this feature by checking the checkbox.&nbsp; This will display the time on the video image.";
hih33="Text Display";
hih34="If you want text to be displayed on the video image, enable this feature by checking the checkbox. You can enter text up to 20 characters in length. This feature is often used to identify the Camera when multiple Cameras are installed.";
hih35="Access Code";
hih36="Set up your code for accessing the live video from camera through cell phone connection.";
hih37="Enable Microphone";
hih38="Enable microphone to receive audio by checking this checkbox. Using audio will increase the bandwidth requirements slightly.";
hih39="Enable Low Light Sensitivity";
hih40="Enable Low Light Sensitivity by checking this checkbox. User can get high quality video under low light environment.";

//Option
hoh01="Help - Options";
hoh02="Enable";
hoh03="If enabled, E-Mails are sent when motion is detected. You can include a short video with each mail by using the E-Mail Video option.<br> <b>Note:</b> Motion detection can be triggered by rapid changes in lighting levels, as well as by moving objects. For this reason, it should only be used indoors.";
hoh04="Send To";
hoh05="Enter at least one (1) E-Mail address; the 2nd and 3rd addresses are optional. The E-Mail alert will be sent to the E-Mail address or addresses specified here.";
hoh06='Show "From" as';
hoh07="Enter the E-Mail address to be shown in the <i>From</i> field when the E-Mail is received.";
hoh08="Subject";
hoh09="Enter the desired text to be shown as the subject for the E-Mail when it is received. This text can not exceed 48 alphanumeric characters.";
hoh10="SMTP Mail Server";
hoh11='Enter the address of the SMTP (Simple Mail Transport Protocol) server to be used to send E-Mail. <BR>If the SMTP Server requires a "login" in order to send mail, check the box next to <i>My Mail Server Requires Authentication</i> and enter your login name and password for the SMTP server. (This is usually the same as the POP3 server used to receive E-Mail.)';
hoh12="Test E-Mail Button";
hoh13="Click this button if you wish to have a test E-Mail with short video attached.";
hoh16="Set Sensitivity Area Button";
hoh17="Click this button to enter the motion detection sub-screen. You can set the area or areas of the video image to be examined, and adjust the sensitivity of detection for each area. <br><b>Note:</b> Motion detection can be triggered by rapid changes in lighting condition, as well as by moving objects. For this reason, it should only be used indoors.";
hoh18="UPnP";
hoh19="If Enabled, the Wireless-N Internet Home Monitoring Camera will broadcast its availability through UPnP. UPnP compatible systems such as Windows XP will then be able to detect the presence of the Wireless-N Internet Home Monitoring Camera.";
hoh20="Alternate Port";
hoh21="Enable/Disable <BR>If enabled,&nbsp; HTTP connections (from your Web Browser or the Viewer and Recorder utility) can use this port instead of port 80 (the standard HTTP port) to access the camera. <BR>If using your Web browser, you need to specify this port when you connect: <pre> http://ip_address:port_number</pre> e.g. <pre> http://203.200.34.26:1024 </pre> <p>Port Number <br>Enter the desired port, in the range 1024 to 65534. The default is 1024. <br>If you already have a Web Server on your LAN, then you should enable the Alternate Port and use this port number instead of port 80.";
// FTP
hoh22="If enabled, video clip are sent when motion is detected by using the FTP Video option.<br> <b>Note:</b> Motion detection can be triggered by rapid changes in lighting levels, as well as by moving objects. For this reason, it should only be used indoors.";
hoh23="FTP Server";
hoh24="Enter the address of the FTP Server.";
hoh25="Port";
hoh26="Enter the Port of the FTP Server to be connected.";
hoh27="Login name";
hoh28="Enter the Login name for the FTP server.";
hoh29="Password";
hoh30="Enter the password for the FTP server.";
hoh31="Passive mode";
hoh32="Check the box to enable the Passive mode feature of the FTP.";
hoh33="File Path name";
hoh34="Enter the file path/name of the FTP.";
// RTP/RTSP
hoh35="RTP/RTSP";
hoh36="RTSP Port";
hoh37="The RTSP (Real Time Streaming Protocol), a standard for connected client(s) to control streaming data (MPEG-4) over the World Wide Web. <p>If desired to change, enter the RTSP Port number (between 1024 to 65535) in the field provided. &nbsp; The default RTSP Port is <strong>554</strong>.";
hoh38="RTP Data Port";
hoh39="The RTP (Real-Time Transport Protocol), an Internet protocol used for transmitting a single real-time multimedia data such as video to a select group of connected clients. &nbsp; The RTSP uses RTP to format packets of multimedia content. <p>The Video Server's data Port number has been pre-configured and can be used for multi casting, and does not normally need to be re-configured. If a port number does need to be changed, please contact your network administrator. <p>If desired to change, enter the data Port number (between 1024 to 65514 and must be even number) in the field provided.";
hoh40="Max RTP Data Packet";
hoh41="If desired to change, enter the Max RTP Data Packet Length (between 400 to 1400 bytes) in the field provided.";
// Multicast RTP/RTSP
hoh42="Multicast RTP/RTSP";
hoh43="Video/Audio Address";
hoh44="The RTP (Real-Time Transport Protocol), an Internet protocol used for transmitting a single real-time multimedia data such as audio and video to a select group of connected clients. &nbsp; The RTSP uses RTP to format packets of multimedia content. <br>The camera's Video and Audio IP Address has been pre-configured and can be used for multicasting, and does not normally need to be re-configured. If an address does need to be changed, please contact your network administrator. <br>If desired to change, enter the Video/Audio Address in the field provided.<br>Multicast IP address settings depend on the IP version in the Basic page (IPv4 only, IPv6 only, IPv4 and IPv6).";
hoh45="Video/Audio Port";
hoh46="The camera's Video and Audio Port number has been pre-configured and can be used for multicasting, and does not normally need to be re-configured. If a port number does need to be changed, please contact your network administrator. <br>If desired to change, enter the Video/Audio Port number (between 1024 to 65534 and must be even number) in the field provided. <br>IPv4 and IPv6 use the same setting.";
hoh47="Time to Live";
hoh48="Enter a reasonable length of time (usually measured in 'hops' - the number of network routers that can be passed before the multimedia data packets arrives at its destination or is dropped.), if the packets fail to be delivered to their destination within. &nbsp; The Time to Live you entered must be in-between 1 to 255. <br>IPv4 and IPv6 use the same setting.";
//smtp port
hoh49="SMTP Port Number";
hoh50="Enter the Port of the SMTP Server to be connected.";


//hlp_samba.htm
hsmb000="Help - Recording";
hsmb001="Enable Recording";
hsmb002="Samba Server";
hsmb003="Login Name";
hsmb004="Password";
hsmb005="Upload Path";
hsmb006="File Name Prefix";
hsmb007="Maximum duration";
hsmb008="Enable adding timestamp to files";
hsmb009="Define Recording Schedule";
hsmb010="Start at";
hsmb011="Stop at";
hsmb012="Browse";

hsmb001_1="When enabled, the camera will record the video and save it to a specified folder on your Samba server.";
hsmb002_1="This is the name of the Samba server where your recording will be saved.<br>This field will be automatic populated once you select the Samba server and folder.";
hsmb003_1="This is the Samba server login name.<br>This field will be automatically populated once you select the Samba server and folder.";
hsmb004_1="This is the Samba server password.<br>This field will be automatically populated once you select the Samba server and folder.";
hsmb005_1="This is the folder on the Samba server where your recording will be saved.<br>This field will be automatically populated once you select the Samba server and folder.";
hsmb006_1="This is the file name prefix of the recorded video.";
hsmb007_1="This is the maximum length of each recorded video file.";
hsmb008_1="When enabled, the camera will append the date and time to the filename.  When disabled, the camera will save each video file using the same filename; therefore, the previous video file will be overwritten by the newest video file.";
hsmb009_1="When enabled, the camera will start to record at the specified time and/or date and continue until the specified time and/or date.";
hsmb010_1="This is the date and time when the camera starts recording video.";
hsmb011_1="This is the date and time when the camera stops recording video.";
hsmb012_1="Click Browse to search for an available Samba server and select a folder on the server to save your recording. You may be prompted to enter your user name and password for the selected Samba server.";

//Password
hph01="Help - Administration";
hph02="Login Name";
hph03="The name used to login as the Administrator. The Administrator login is required in order to change any data or settings. It should not exceed 32 alphanumeric characters and contain no spaces.";
hph04="Password";
hph05="The password for the Administrator login.&nbsp; Password should not exceed 64 alphanumeric characters.";
hph06="Verify Password";
hph07="Re-enter the password for the Administrator for password verification.";
hph08="Restore Defaults Button";
hph09="Click this button will reset the camera to it's factory default settings.";
hph10="Upgrade Firmware Button";
hph11="Click this button to upgrade the Firmware settings in the sub-screen.";
hph12="Select the desired language mode to display.";


//Status
hsh01="Help - Status";
hsh02="Firmware version";
hsh03="The version of the firmware currently installed is displayed. <br>If you have downloaded a new Firmware Upgrade file, you can click the <i>Upgrade Firmware</i> button from the Help page.&nbsp; Note: You must first be logged in to the Setup page as an administrator.";
hsh04="MAC Address";
hsh05="This displays the current MAC Address of the Wireless-N Internet Home Monitoring Camera.";
hsh06="Camera Name";
hsh07="This shows the name of the Wireless-N Internet Home Monitoring Camera.";
hsh08="Description";
hsh09="This shows the description of the Wireless-N Internet Home Monitoring Camera.";
hsh10="Date/Time";
hsh11="Displayed here is the current date and time, according to the Wireless-N Internet Home Monitoring Camera internal clock.";
hsh12="Network Type";
hsh13="Shown here is the Network Type used by the Wireless-N Internet Home Monitoring Camera.";
hsh14="IPv4 Address";
hsh15="Shown here is the IPv4 Address of the Wireless-N Internet Home Monitoring Camera.";
hsh16="IPv4 Subnet Mask";
hsh17="Shown here is Subnet Mask for the above IPv4 Address.";
hsh18="IPv4 Gateway";
hsh19="This is the IPv4 Address of the Gateway used by the Wireless-N Internet Home Monitoring Camera.";
hsh20="SSID";
hsh21="This is the wireless SSID of the Wireless-N Internet Home Monitoring Camera.";
hsh22="Channel";
hsh23="This shows the wireless channel currently used.";
hsh24="Security";
hsh25="This indicates whether wireless security is enabled or disabled.";
hsh26="System Log";
hsh27="This displays system activities.";
hsh28="Clear Log Button";
hsh29="Click the Clear Log button to erase all the entries in the System Log.";
hsh30="Domain";
hsh31="This is the wireless domain of the Wireless-N Internet Home Monitoring Camera.";
hsh32="IPv6 Address(es):";
hsh33="Shown here is(are) the IPv6 Address(es) with the subnet prefix length of the Wireless-N Internet Home Monitoring Camera.";
hsh34="IPv6 Gateway(s)";
hsh35="The IPv6 Address(es) of the Gateway(s) used by the Wireless-N Internet Home Monitoring Camera.";
hsh36="IP Version";
hsh37="The IP Version used by the Wireless-N Internet Home Monitoring Camera.";

//User
huh01="Help - Users";
huh02="User Properties";
huh03="Allow access by";
huh04="<ul> <li><b>All users</b> - This Camera can be accessed by anyone. Note: The Camera only supports up to five users simultaneously.</li> <li><b>Only users in database</b> - Allow viewing only by users in the user database. These users will be prompted to enter their User Names and Passwords when viewing video.&nbsp; Note: Only the  administrator - not users in the database - will have accessto the Setup page of the Web-based utility.</li> </ul>";
huh05="User List";
huh06="This displays all users you have entered into the User database. If you have not entered any users, this list will be empty.";
huh07="Buttons";
huh08="Use the <i>Edit</i>, <i>Delete</i>, and <i>Delete All</i> buttons to manage the user database.";
huh09="User Name";
huh10="<ul> <li>Enter the name for the user here. Spaces, punctuation, and special characters must NOT be used in the name.</li> <li>The name is case sensitive. </li> </ul>";
huh11="User Password";
huh12="The password for the user.";
huh13="Confirm Password";
huh14="Re-enter the password for the user, to ensure it is correct.";
huh15="Use the <i>Add User</i> and <i>Clear/Cancel</i> buttons to manage the user properties.";

