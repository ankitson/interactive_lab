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
		
		puts "IN SET STATE"
		
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
			
	def moveX
		setValue("uz2ORyR5x4Mp", params[:value])
	end
	
	def moveY
		setValue("omCjPwzHOI9b", params[:value])
	end		
	
	def setLightState
		setState("OXO0Q9H2yXME", params[:state])
	end
	
	def setPumpkinState
		setState("aEFW7f0gplue", params[:state])
	end
	
	def setLightState(state)
		setState("OXO0Q9H2yXME", state)
	end
	
	def setPumpkinState(state)
		setState("aEFW7f0gplue", state)
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
	
	def getValue(widgetID)
	end
	
	def getX
		getValue("uz2ORyR5x4Mp")
	end
	
	def getY
		getValue("omCjPwzHOI9b")
	end	
	
	def togglePumpkinState
		setPumpkinState(!getPumpkinState)
	end
	
	def toggleLightState
		setLightState(!getLightState)
	end		

  def join_queue
  	session[:time] = Time.now
  	session[:ip] = request.remote_ip
  	session[:ga_utma] = cookies["__utma"]
  	
  	@exists = true;
  	#m = MySession.new(:time => Time.now, :session_id => request.session_options[:id], :ga_utma => cookies["__utma"])
  	#m.save!
		m = MySession.find_by_session_id_and_ga_utma(request.session_options[:id], cookies["__utma"])
		
		if m.nil?
			@exists = false;
			m = MySession.new(:time => Time.now, :session_id => request.session_options[:id], :ga_utma => cookies["__utma"])
  		m.save!
  	end
  	
  	
  	
  	render :text => "joined. MySession: time: "+Time.now.to_s+" session_id: "+request.session_options[:id]+" ga_utma: "+cookies["__utma"]+"Exists?: "+@exists.to_s 	
  end
  
  def position_in_queue
  	@session_id = request.session_options[:id]
  	@utma = cookies["__utma"]
  	
  	@session = MySession.find_by_session_id_and_ga_utma(:first, @session_id, @utma) 
  	@all_sessions = MySession.all(:order => 'time')
  	
  	@index = @all_sessions.index(@session)
  	
  	render :text => "INDEX: #{@index} <br><br> ALL_SESSIONS: #{@all_sessions.inspect.map{|x| x.inspect}}"
  	
  	return @index
  end
  
  def is_first_in_queue?  	
  	puts "IN FIRST IN QUEUE"
  	
  	@session_id = request.session_options[:id]
  	@utma = cookies["__utma"]
  
  	#Only get first session with id and utma. This should be enough to uniquely identify a visitor.
  	@session = MySession.find_by_session_id_and_ga_utma(:first, @session_id, @utma) 
  	@latest_session = MySession.last(:order => 'time')
  	
  	if (@latest_session.nil?) #If first in queue is called without join_queue ever being called
  		return true
  	end
  		
		@returnVal = (@session_id == @latest_session.session_id)
		
		return @returnVal
  end
  
end
