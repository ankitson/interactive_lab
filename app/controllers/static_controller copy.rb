require 'uri'
require 'net/http'
class StaticController < ApplicationController
before_filter :is_first_in_queue?, :only => [:moveX, :moveY, :setLightState, :setPumpkinState, :togglePumpkinState, :toggleLightState, :setValue, :setState]
		
	def setValue(widgetID, value)
		@baseURL = "http://astrobotic.net/interactivelab/"
		@page = "iobridge-proxy.php?"
		@parameters = "widgetID=#{widgetID}"
		
		if value
			@parameters = @parameters + "&value=#{value}"
		end
		
		@request = @baseURL+@page+@parameters
		
		uri = URI.parse(@request)
		puts @request
		puts uri
		
		render :text => "Request: #{@request} Parsed URI: #{uri} Value:#{value}"
		@response = Net::HTTP.get(uri)
	end
	
	def setState(widgetID, state)
		@baseURL = "http://astrobotic.net/interactivelab/"
		@page = "iobridge-proxy.php?"
		@parameters = "widgetID=#{widgetID}"
		
		if state
			@parameters = @parameters + "&state=#{state}"
		end
		
		@request = @baseURL+@page+@parameters
		
		uri = URI.parse(@request)
		puts @request
		puts uri
		
		render :text => "Request: #{@request} Parsed URI: #{uri} State:#{state}"
		@response = Net::HTTP.get(uri)
	end
	
=begin
	def interactState(widgetID, state)
		@baseURL = "http://astrobotic.net/interactivelab/"
		@page = "iobridge-proxy.php?"
		@parameters = "widgetID=#{widgetID}"
		
		@request = @baseURL+@page+@parameters
		uri = URI.parse(URI.encode(@request))
		@response = Net::HTTP.get_response(uri)
		
		puts "RESPONSE CODE: #{@response.code}"
		
		@oldreq = @request
		@oldresp = @response
		olduri = uri
		#render :text => "Request: #{@request.inspect} URI: #{uri} State:#{state} Response: #{@response.inspect}"
		
		if state
			@parameters = @parameters + "&state=#{state}"
		end
		
		@request = @baseURL+@page+@parameters
		uri = URI.parse(URI.encode(@request))
		@response = Net::HTTP.get_response(uri)
		
		@header =
		{ "Host" => "astrobotic.net", 
			"Connection" => "keep-alive",
			"Cache-Control" => "max-age=0",
			"User-Agent" => "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2",
			"Accept" => "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Encoding" => "gzip,deflate,sdch",
			"Accept-Language" => "en-US,en;q=0.8",
			"Accept-Charset" => "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
		  #"Cookie" => "__utma=98433423.1154994353.1320327971.1320882131.1320905384.8; __utmz=98433423.1320327971.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
		}
		
		puts "HEADER: #{@header}\n"
		puts "HEADER.class: #{@header.class}\n"
		puts "HEADER.HOST: "+ @header["Host"]
		
		Net::HTTP.start(olduri.host, olduri.port) do |http|
			#@req = Net::HTTP::Get.new(olduri.request_uri)
			#@resp = http.request(@req) # Net::HTTPResponse object
			
			@newreq = Net::HTTP::Get.new(uri.request_uri)
			@newresp = http.request(@newreq)
			
			render :text => "@req: #{@req.to_hash.inspect} #{@req.class.name} <br\><br\> @resp: #{@resp.to_hash.inspect} #{@resp.code} #{@resp.message} #{@resp.class.name} <br\><br\> @newreq:#{@newreq.to_hash.inspect} #{@newreq.class.name} <br\><br\> @newresp:#{@newresp.to_hash.inspect} #{@newresp.code} #{@newresp.message} #{@newresp.class.name} <br\><br\> OLDURI: #{olduri} <br\><br\> URI: #{uri}"
		end		
				
		#render :text => "Old Request: #{@oldreq} Old Response: #{@oldresp.inspect} Code: #{@oldresp.code} Body: #{@oldresp.body} Headers: #{@oldresp.headers.inspect}  \n Request: #{@request.inspect} URI: #{uri} State:#{state} Response: #{@response.inspect} Code: #{@response.code} Body: #{@response.body} Cache-Control: #{@response['cache-control']} "

	end
=end
		
	def moveX
		interactValue("uz2ORyR5x4Mp", params[:value])
	end
	
	def moveY
		interactValue("omCjPwzHOI9b", params[:value])
	end
	
	def setLightState
		interactState("OXO0Q9H2yXME", params[:state])
	end
	
	def setPumpkinState
		interactState("aEFW7f0gplue", params[:state])
	end
	
	def setLightState(state)
		interactState("OXO0Q9H2yXME", state)
	end
	
	def setPumpkinState(state)
		interactState("aEFW7f0gplue", state)
	end
	
	def getPumpkinState
		@uri = URI.parse(URI.encode("http://astrobotic.net/interactivelab/iobridge-proxy.php?widgetID=aEFW7f0gplue"))
		@resp = Net::HTTP.get_response(@uri).body
		@retVal = (@resp == ("<b>Astropumpkin: ON</b>"))
		
		render :text => @retVal
		return @retVal
	end
	
	def getLightState
		@uri = URI.parse(URI.encode("http://astrobotic.net/interactivelab/iobridge-proxy.php?widgetID=OXO0Q9H2yXME"))
		@resp = Net::HTTP.get_response(@uri).body
		@retVal = (@resp == ("<b>Spotlight On</b>"))
		
		render :text => @retVal		
		return @retVal1
	end
	
	def togglePumpkinState
		setPumpkinState(!getPumpkinState)
	end
	
	def toggleLightState
		setLightState(!getLightState)
	end		
	
  def main
		#if @@session[:ips].nil?
			#@@session[:ips] = [request.remote_ip]
		#else
  		#@@session[:ips] << request.remote_ip
  	#end
  	#@ips = User.all.map(&:ip_address)
  	#@ips = Time.now
  	#@ips = request.inspect
  	
  	#@id = MySession.all.inspect
  end
  
  def join_queue
  	session[:time] = Time.now
  	session[:ip] = request.remote_ip
  	session[:ga_utma] = cookies["__utma"]
  	
  	m = MySession.new(:time => Time.now, :session_id => request.session_options[:id], :ga_utma => cookies["__utma"])
  	
  	m.save!
  	
  	render :text => "joined. MySession: time: "+Time.now.to_s+" session_id: "+request.session_options[:id]+" ga_utma: "+cookies["__utma"]
  	
  	#User.create!(:ip_address => request.remote_ip, :time => Time.now, :ga_utma => cookies["__utma"])
  end
  
  def is_first_in_queue?  	
  	@session_id = request.session_options[:id]
  
  	@utma = cookies["__utma"]
  
  	#Only get first session with id and utma. This should be enough to uniquely identify a visitor.
  	@session = MySession.find_by_session_id_and_ga_utma(:first, @session_id, @utma) 
  	
  	@latest_session = MySession.last(:order => 'time')
  	
  	if (@latest_session.nil?)
  		return true
  	end
  		
		#raise "No sessions stored before trying to find first in queue" unless @first_session
		
		@returnVal = (@session_id == @latest_session.session_id)
		
		return @returnVal
  end
  
  def init
  	#@@session = []
  end

end
