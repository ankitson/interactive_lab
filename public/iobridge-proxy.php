<?php
/**
*	ioBridge Proxy that forwards calls to your ioBridge widgets
*
*	@version 1.1 July 3, 2009 - Added URL debug and "widget" select case by ioBridge Support
*	@version 1.0 June 21, 2009 - Original version Marc Fonteijn <marcfonteijn[ at ]gmail.com>
*
*	@link http://www.iobridge.net/forum/index.php/topic,447.0.html Comments & suggestions
*	@license http://creativecommons.org/licenses/GPL/2.0/ Released under a Creative Commons GNU GPL License
*/
  $widgetID = $_GET['widgetID'];
  $widget =  $_GET['widget'];
  $state = $_GET['state'];
  $value = $_GET['value'];
  $debug = $_GET['debug'];
 
  $value = urldecode($value);
 
  if ($widgetID) {
 
      $url = "http://www.iobridge.com/interface/?actionID=RM_Widget&widgetID=" . $widgetID . "&dt=" . time();
      $ch = curl_init($url);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, '1');
      $response = curl_exec($ch);
      curl_close($ch);
 
      $start = strpos($response, "www.iobridge.com/interface/?actionID=");
      if(isset($state) && $state == "0")
        $start = strpos($response, "www.iobridge.com/interface/?actionID=", $start + 1);
      $end =  strpos($response, ";", $start);
      $widgetUrl = "http://" . substr($response, $start, $end - $start - 4);
 
      if ($debug) {
 
         echo $widgetUrl;
         exit;
 
      }
  }
  else {
 
      switch ($widget) {
       case "toggle":
        $widgetUrl = "http://www.iobridge.com/interface/?actionID=RM_XXXXXXXXXXXX&sessionID=XXXXXXXXXXXXXXXXXXXX"; 
        break;
       case "analog":
        $widgetUrl = "http://www.iobridge.com/interface/?actionID=RM_XXXXXXXXXXXX&sessionID=XXXXXXXXXXXXXXXXXXXX"; 
        break;
       case "off":
        $widgetUrl = "http://www.iobridge.com/interface/?actionID=RM_XXXXXXXXXXXX&sessionID=XXXXXXXXXXXXXXXXXXXX"; 
        break;
       case "on":
        $widgetUrl = "http://www.iobridge.com/interface/?actionID=RM_XXXXXXXXXXXX&sessionID=XXXXXXXXXXXXXXXXXXXX"; 
        break;
       case "servo":
        $widgetUrl = "http://www.iobridge.com/interface/?actionID=RM_XXXXXXXXXXXX&sessionID=XXXXXXXXXXXXXXXXXXXX"; 
        break;
      }
  }
 
  if ($widgetUrl) {
 
      $widgetUrl .= "&setValue=" . urlencode($value);
 
      $ch = curl_init($widgetUrl);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, '1');
      $response = curl_exec($ch);
      $start = strpos($response, "=");
      $end =  strpos($response, ";", $start);
      echo substr($response, $start + 2, $end - $start - 3);
 
  }
?>