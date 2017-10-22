/*
 * Copyright (c) 2015, Majenko Technologies
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 *   list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice, this
 *   list of conditions and the following disclaimer in the documentation and/or
 *   other materials provided with the distribution.
 *
 * * Neither the name of Majenko Technologies nor the names of its
 *   contributors may be used to endorse or promote products derived from
 *   this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
#include "DHT.h"


#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>
#define DHTPIN D2     // what digital pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);

char ssid[20] = "";
char password[20] = "";
String userName="";
String accountPass="";
ESP8266WebServer server ( 80 );
int dID=1;
int preMinutes= millis() / 1000/60 % 60;

void handleRoot() {

	char temp[400];
	int sec = millis() / 1000;
	int min = sec / 60;
	int hr = min / 60;
  if(WiFi.status() != WL_CONNECTED){
    snprintf ( temp, 400,
"<html>\<body>\<form action='/connectToWifi'>\<input type='text' name='ssid' placeholder='WIFI ID'>\<br>\<input type='text' name='pass' placeholder='Password'>\<br>\<input type='text' name='uid' placeholder='User name'>\<br>\<input type='text' name='uPass' placeholder='User password'>\<br>\<input type='submit' value='Submit'>\<br>\</form>\<p>Current Ip: %d:%d:%d:%d</p>\<p>Uptime: %02d:%02d:%02d</p>\</body>\</html>"
,
    WiFi.localIP()[0],WiFi.localIP()[1],WiFi.localIP()[2],WiFi.localIP()[3],hr, min % 60, sec % 60
  );
  }else if(userName.length()<1){
    snprintf ( temp, 400,
"<html>\<body>\<form action='/setUpUserDetail'>\<input type='text' name='uid' placeholder='User name'>\<br>\<input type='text' name='uPass' placeholder='User password'>\<br>\<input type='submit' value='Submit'>\<br>\</form>\<p>Current Ip: %d:%d:%d:%d</p>\<p>Uptime: %02d:%02d:%02d</p>\</body>\</html>"
,
    WiFi.localIP()[0],WiFi.localIP()[1],WiFi.localIP()[2],WiFi.localIP()[3],hr, min % 60, sec % 60
  );
  }else{
    server.send(200, "text/html", "<h1>You are connected  "+userName+":"+accountPass + " "+preMinutes+ "   "+min % 60+" ___ "+(millis() / 1000/60 % 60-preMinutes)+" </h1>");
  }
	
  
	server.send ( 200, "text/html", temp );
 //server.send ( 200, "text/plain", ssid );
	//digitalWrite ( led, 0 );
}

void handleNotFound() {
	//digitalWrite ( led, 1 );
	String message = "File Not Found\n\n";
	message += "URI: ";
	message += server.uri();
	message += "\nMethod: ";
	message += ( server.method() == HTTP_GET ) ? "GET" : "POST";
	message += "\nArguments: ";
	message += server.args();
	message += "\n";

	for ( uint8_t i = 0; i < server.args(); i++ ) {
		message += " " + server.argName ( i ) + ": " + server.arg ( i ) + "\n";
	}

	server.send ( 404, "text/plain", message );
	//digitalWrite ( led, 0 );
}

void handleSpecificArg() { 

String message = "";
bool hasPara=false;
if (server.arg("ssid")== ""||server.arg("uid")== ""|| server.arg("uPass")== ""){     //Parameter not found

message = "Argument missing";

}else{     //Parameter found
 hasPara=true;
message = "Connecting to ";
message += server.arg("ssid")+",";     //Gets the value of the query parameter
message += "Please wait for 10s and unplug than plug back in the device";    //Gets the value of the query parameter

if(server.arg("ssid").length()>0){
  server.arg("ssid").toCharArray(ssid,20);
  server.arg("pass").toCharArray(password,20);
    
}else{
  hasPara=true;
  message="ssid not found";
}

}
if(hasPara){
server.send(200, "text/plain", message+userName);          //Returns the HTTP response  
ConnectToAP();
}else{
  handleNotFound();
}


}
void putdata(){
   float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
   // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    //Serial.println("Failed to read from DHT sensor!");
    server.send(200, "text/plain", "Failed to read from DHT sensor!"); 
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);


  
    String domain="http://10.0.0.107:8000/putdata";
    if (userName.length()>1){
      String suffixData="?userName="+userName+"&pass="+accountPass+"&dID="+dID+"&temp="+t+"&humi="+h;
       HTTPClient http;  //Declare an object of class HTTPClient
       http.begin(domain+suffixData);  //Specify request destination
      int httpCode = http.GET();                                                                  //Send the request
   
      if (httpCode > 0) { //Check the returning code
   
        String payload = http.getString();   //Get the request response payload
        //Serial.println(payload);                     //Print the response payload
   
      }
   
      http.end();   //Close connection
      server.send(200, "text/plain", domain+suffixData); 
    }else{
      server.send(200, "text/plain", "user name not set "+userName+" passnot set "+ accountPass+ " dID="+dID); 
    } 
  }

void ConnectToAP(){
  WiFi.begin ( ssid, password );

  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
 
  }

 }


void connectToWifi() {
  String message = "";
  bool hasPara=false;
  if (server.arg("ssid")== ""){     //Parameter not found
  
  message = "Argument missing";
  
  }else{     //Parameter found
   hasPara=true;
  message = "Connecting to ";
  message += server.arg("ssid")+",";     //Gets the value of the query parameter
  message += "Please wait for 10s and unplug than plug back in the device";    //Gets the value of the query parameter
 if(server.arg("ssid").length()>0){
    server.arg("ssid").toCharArray(ssid,20);
    server.arg("pass").toCharArray(password,20);
      
  }else{
    hasPara=true;
    message="ssid not found";
  }
  
  }
  if(hasPara){
  server.send(200, "text/plain", message+userName);          //Returns the HTTP response  
  ConnectToAP();
  }else{
    handleNotFound();
  }
 
}




void setUpUserDetail() {
  userName=server.arg("uid");
  accountPass=server.arg("uPass");
   putdata();
  
  server.send ( 200, "text/plain", "log in device" );
 
}

 
void setup ( void ) {

	if ( MDNS.begin ( "esp8266" ) ) {
		//Serial.println ( "MDNS responder started" );
	}

	server.on ( "/", handleRoot );
  server.on ( "/es", handleSpecificArg);
	server.on ( "/test.svg", drawGraph );
 server.on ( "/urltest", putdata );

server.on ( "/setUpUserDetail", setUpUserDetail );
  server.on ( "/es", handleSpecificArg);


 
	server.on ( "/inline", []() {
		server.send ( 200, "text/plain", "this works as well" );
	} );
	server.onNotFound ( handleNotFound );
	server.begin();
  dht.begin();
//	Serial.println ( "HTTP server started" );
}

void loop ( void ) {
	server.handleClient();
  if(WiFi.status() != WL_CONNECTED||( millis() / 1000/60 % 60-preMinutes)<5||userName==""||accountPass==""){
//if(WiFi.status() != WL_CONNECTED||userName==""||accountPass==""){
  
   }else{
    //sent information 
//    //http://10.0.0.107:8000/putdata?userName=myUN&pass=mypass&dID=202&temp=25&humi=50
//    String domain="http://10.0.0.107/putdata";
//    String suffixData="?userName="+userName+"&pass="+accountPass+"&dID="+dID+"&temp=25&humi=50";
//     HTTPClient http;  //Declare an object of class HTTPClient
//     http.begin(domain+suffixData);  //Specify request destination
//    int httpCode = http.GET();                                                                  //Send the request
// 
//    if (httpCode > 0) { //Check the returning code
// 
//      String payload = http.getString();   //Get the request response payload
//      //Serial.println(payload);                     //Print the response payload
//// 
//    }
// 
//    http.end();   //Close connection
putdata();
preMinutes= millis() / 1000/60 % 60;
   }
  //Serial.println ( "looped" );
 // Serial.println ( WiFi.localIP() );
}

void drawGraph() {
	String out = "";
	char temp[100];
	out += "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" width=\"400\" height=\"150\">\n";
 	out += "<rect width=\"400\" height=\"150\" fill=\"rgb(250, 230, 210)\" stroke-width=\"1\" stroke=\"rgb(0, 0, 0)\" />\n";
 	out += "<g stroke=\"black\">\n";
 	int y = rand() % 130;
 	for (int x = 10; x < 390; x+= 10) {
 		int y2 = rand() % 130;
 		sprintf(temp, "<line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" stroke-width=\"1\" />\n", x, 140 - y, x + 10, 140 - y2);
 		out += temp;
 		y = y2;
 	}
	out += "</g>\n</svg>\n";

	server.send ( 200, "image/svg+xml", out);
}
