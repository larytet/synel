# synel

A Python script which records entry/exit time on Synel time and attendance WEB front end https://harmony.synel.co.il/eharmonynew
The goal is to allow automatic entry of the time using cron or triggered by exterenal events, like connection to WiFi. 

The script is based on Selenium WEBdriver and requires relevant Python modules

Run the script without arguments to see the usage.


Important notes. 

Synel has an API supporting automatic entry. Messaging (SMS) is one of the supported interfaces. If you do not have access to such API this the choice of your employer and not a a limitation of the Synel product.  

I think that the handshake between the Synel's client side device and the server is trivial. If you have physical access to the device it is not going to be very hard to connect a packet analyzer and reverse engineer the protocol.  
