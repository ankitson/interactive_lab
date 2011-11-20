
// public
var msg_blank = "%s can not be blank.\n";
var msg_nospaces = "Blanks or spaces are not allowed in %s\n\n";
var msg_invalid = "Invalid character or characters in %s\nValid characters are: \n%s\n";
var msg_notallow = "Invalid character or characters in %s\nThe following characters are not allowed:\n%s\n";
var msg_check_invalid = "%s must be a number.\n";
var msg_outofrange = "Invalid %s. Valid range is %s to %s \n";
var msg_validIP = "Invalid %s. Valid range is 1.0.0.0 to 255.255.255.255\n";
var msg_validMask = "Invalid %s. Valid range is 0.0.0.0 to 255.255.255.255\n";
var msg_mail = "Invalid %s. Please enter a valid e-mail address\n";
var msg_restart = "Camera must now restart. \nPlease wait %s seconds before attempting to continue";
var msg_changeIP = "Since the Camera's IP address has changed,\nthis connection must be terminated.\n\nPlease wait %s seconds for the restart to be completed,\nand then re-connect using the new IP address";
var msg_activeX = "MPEG-4 Video is only available with Microsoft Internet Explorer.\nFor Netscape users, please use the Linksys Viewer & Recorder Utility.";
var msg_connect_livevideo =  "Connecting to Live Video steam ..." ;
var msg_invalid_mask = "Invalid Netmask IP Address\n";
var msg_invalid_ip = "Invalid IP Address\n";
var msg_invalid_gw = "Invalid Gateway IP Address\n";
var msg_duplicated_period	= "Same schedule exists on the list, please set another period.\n";
var msg_too_many_periods	= "Unable to add! List contains maximum sets of schedule.\n";
var msg_name =  "User Name";
var msg_pw =  "Password";

// basic
var msg_invalidIP_with_subnet = "Invalid combination of %s and Subnet Mask.\n";
var msg_validIP_range = "Invalid %s,Only use the IP starting with %s~%s.\n";
var msg_validIP_notU = "Invalid %s. Can't use the IP starting with %s.Please specify other IP starting with %s~%s.\n";

var msg_dname = "Device Name";
var msg_hr = "Time (Hrs)";
var msg_min = "Time (Min)";
var msg_day = "Date (Day)";
var msg_year = "Date (Year)";
var msg_invalid_year = "Invalid year. Valid range is 2005 to 2037";
var msg_adm = "Admin Name";
var msg_update_hr = "Update schedule (hr)";
var msg_update_min = "Update schedule (min)";
var msg_ip_field = "IP Address";
var msg_mask_field = "Network Mask";
var msg_gateway = "Gateway IP address";
var msg_dns1 = "Primary DNS address";
var msg_dns2 = "Secondary DNS address";
var msg_need_gwdns = "Warning!\nE-mail notification, DDNS, and Network Time Protocol\ncannot work without a Gateway and DNS.\n\nClick OK to confirm current settings, or click Cancel to abort changes.";
var msg_datetime_pcsync = "Camera's Date/Time will be set to match your PC, but this will be lost on power down.\nOn start up, the Camera will use an Internet Time Server to obtain the current Date and Time.\n";
var msg_ssid = "SSID";
var msg_cname = "Camera Name";
var msg_auto_ch  = "Auto"; // channel
var msg_wiresec = "Do you want to enable wireless security ?";
var msg_keysize = "The key length is not correct.\nKeys must consist of %s hexadecimal characters";
var msg_hexkey = "The key value is not correct. \nKeys must consist of hexadecimal characters ( 0~9 or A~F )";
var msg_smallpassphase = "Passphrase must have at least one character.";
var msg_default_key = "Selected key [%s] cannot be blank.";
var msg_psk_size = "WPA Shared key must be from 8 to 63 characters in length.\n";
var msg_wep_64 = "64 Bit Key table";
var msg_wep_128 = "128 Bit Key table";

//ipv6
var msg_ip_v6 = "IPv6 address ";
var msg_mask_v6 = "IPv6 address's prefix length ";
var msg_gw_v6 = "IPv6 default gateway ";
var msg_dns1_v6 = "Primary IPv6 DNS server ";
var msg_dns2_v6 = "Secondary IPv6 DNS server ";
var msg_illegal_addr = "Illegal address in %s.\n";

// image
var msg_quality_change = "Warning!\nWhen the image quality setting is changed, all existing connections will be terminated.\nAnyone viewing the video will need to re-connect.";
var msg_res_change = "Warning!\nWhen the image size setting is changed, all existing connections will be terminated.\nAnyone viewing the video will need to re-connect.";
var msg_preview = "In this browser, click the image pane to start and stop the preview";
var msg_typechange = "Warning!\nWhen the image type setting is changed, all existing connections will be terminated.\nAnyone viewing the video will need to re-connect.";
var msg_typechange_full = "Warning!\n1) Audio is not available with this video type.\n2) When the image type is changed, all existing connections will be terminated.\nAnyone viewing the video will need to re-connect.";
var msg_overlay = "Text display";
var msg_mv_pw = "Access Code";


// Admin
var msg_adm_login = "Administrator Login Name";
var msg_admpw_login = "Administrator Login Password";
var msg_passNoMatch = "Password entries do not match.\n";
var msg_bigpw = "Please limit the password field to 64 characters";
var up_msg = "Continue upgrading the firmware?\nAll existing connections will be terminated.";
var nofile_msg = "No filename provided. Please select the correct file.";
var finish_msg = "\Firmware Upgrade completed... Camera restarting." + 
"\nPlease wait for restart to be completed before continuing.";


// user
var button_label_add = "Add User";
var button_label_update = "Update User";
var button_label_clear =  "Clear Fields";
var button_label_cancel = "Cancel";
var msg_username = "User name";
var msg_nameused ="This name is already used. Please use another name.\n";
var msg_passwd_nomatch = "Password entries do not match, please retype.\n";
var msg_dbfull = "User database is full, no more users can be added.\n";
var msg_select_user = "No user selected, please select a user from the list.\n";
var msg_del_user = "Delete user: ";
var msg_del_allusers = "Delete all users ? \n";


// ddns
var msg_ddns_hostname = "DDNS Hostname";
var msg_ddns_username = "DDNS account name";
var msg_ddns_password = "DDNS password";
var msg_selsite = "Please select a DDNS Service provider";

// options
var msg_motiondetect = "Warning!\nMotion detection can be triggered by sudden changes in lighting levels,\nas well as by moving objects.";
var msg_nomotiondetect = "Motion detection is not available with MJPEG video streams";
var msg_noaudiomotion_mjpeg = "Motion detection and audio are not available with MJPEG video streams,\nso they have been disabled.";
var	msg_ddns_username = "DDNS User Name";
var msg_ddns_email = "E-mail Address for TZO DDNS";
var msg_send_test_mail = "This will send E-mail to the recipients you have enabled and entered.";
var msg_ddns_key = "TZO Password Key";
var msg_ddns_password = "DDNS Password";
var msg_ddns_host = "DDNS Host Name";
var msg_ddns_domain = "DDNS Domain Name";
var msg_ip_sche_hr = "Check Internet IP address time (hr)";
var msg_ip_sche_min = "Check Internet IP address time (min)";
var msg_emaildest_empty = "You must specify one receiver at lease.";
var msg_emaildest1 = "E-mail address [1]";
var msg_emaildest2 = "E-mail address [2]";
var msg_emaildest3 = "E-mail address [3]";
var msg_emailsrc = "'From' E-mail address";
var msg_smtp_port = "SMTP Port Number";
var msg_smtp_server = "Outgoing Mail SMTP Server";
var msg_smtp_login = "Mail Server Account Name" ;
var msg_port = "Alternate Port Number";
var msg_smtp_port_valid_range = "SMTP Port Number is invalid.Valid range is 1~65535.\n";
//
var msg_aftp_name = "FTP Server Name";
var msg_aftp_login = "FTP Server Login name";
var msg_aftp_pw = "FTP Server Password";
var msg_in_inter = "Invaild Ftp Upload Interval"; 
var msg_ftp_port = "FTP Port Number";
var msg_ftp_path = "FTP File Path Name";
var msg_ftp_port_valid_range = "FTP Port Number is invalid.Valid range is 1024~65535 and 21.\n";

// RTP/RTSP
var msg_port_conflict = "The Alternate Port number can not be equal to the RTSP Port number.\n";
var msg_rtsp_port = "RTSP Port";
var msg_rtp_src_port = "RTP Data Port";
var msg_rtp_data_port = "Invalid RTP Data Port number. Enter an even number between 1024 and 65514.\n";
var msg_rtp_pkt_len = "Max RTP Data Packet Length";
var msg_ip_address = "IP Address";
var msg_v_port = "Video Port";
var msg_a_port = "Audio Port";
var msg_video_port = "Invalid Video Port number. Enter an even number between 1024 and 65534.\n";
var msg_audio_port = "Invalid Audio Port number. Enter an even number between 1024 and 65534.\n";
var msg_multiport_conflict = "The Video Port number can not be equal to the Audio Port number when Video Address is the same with Audio Address.\n";
var msg_rtp_time = "Time";

var msg_video_address = "Video Address";
var msg_audio_address = "Audio Address";


// event
var msg_no_option = "No option selected. Please select one from the list.\n";
var msg_eventname = "Event Name";
var msg_event_over = "It is not possible to add any more events. The maximum number of events is 10.\n";
var msg_noevent_selected = "No event selected. Please select a event from the list.\n";
var msg_delevent = "Delete selected event or events?\n";
var msg_photo_filename = "File Path Name";
var msg_no_option = "No option selected. Please select one from the list.\n";
var msg_emaildest = "E-Mail address";
var msg_e_subject = "E-Mail Subject";
var msg_delperiod = "Delete selected period or periods?\n";
var msg_noperiod_selected = "No period selected. Please select a period from the list.\n";
var msg_finish_after_start = "Invalid period. Finish time must be after start time.\n";


// status
var resetDefault_msg = "Reset to factory defaults ?\n\nClick OK to continue, or click Cancel to abort";
var restart_msg = "Restart the Camera ? \nAll existing connections will be terminated.\n\nClick OK to continue, or click Cancel to abort";


//SMB
var msg_smb_server_empty = "Warning! The server name can not be empty.\n";
var msg_smb_server_illegal_str = "server name";
var msg_smb_path_empty = "Warning! The file path can not be empty.\n";
var msg_smb_path_illegal_str = "file path";
var msg_smb_filename_prefix_empty = "Warning! The file name prefix can not be empty.\n";
var msg_smb_filename_prefix_illegal_str = "file name prefix";
var msg_smb_name = "User name";
var msg_smb_pwd = "Password";
var msg_smb_max = "Maximum size of each file";
var msg_smb_max_duration = "Maximum duration of each file";
var msg_smb_select_null = "You must select a folder to save you file.";
var msg_smb_survey_error = "Failed to survey servers/folders.";
var msg_smb_auth_null = "Username can not be blank.";
var msg_smb_path_error = "Can't survey the path, the length is more than 128 characters.";
var msg_smb_set_manual = "* Please fill in the shared folder name directly in the setting page if you cannot find your shared folder from this windows.";

