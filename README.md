# Bunch of Domoticz Plugins

## Description
* Plugins to manage new types of device in Domoticz
  * jcdecaux-bikes: JCDecaux Bike sharing systems)
	* Works for all JCDecaux systems
	  * France: Velib, Le vélo, Vélo'V, Velam, VéloCité, Velo2, Cristolib, vélOstan'lib, Bicloo, cy-clic, Vélô
	  * Spain: Tusbic, SEVICI, Valenbisi
	  * Sweden: Göteborg, Lundahoj, Cyclocity
      * Belgium: villo, Li bia velo
      * Ireland: dublinbikes
	  * Lithuania: Cyclocity
	  * Luxembourg: Veloh
	  * Norway: Bysykkel
	  * Russia: Veli'k
	  * Slovenia: Bicikelj
	  * Japan: cyclocity
	  * Australia: CityCycle
	  * etc.
    * Show how many available bikes and bike stands for a station
	* After a parameter update, delete the device. A new one will come up.
  * Arlo (Wireless security cameras) -- in development
    * Manage Arlo modes (armed, disarmed, schedule, custom)
	* Get battery level


## Installation 
* Requires Domoticz v3.8153 or newer
* Requires Python 3
  * sudo apt-get install -y python3 python3-dev python3-pip
* Requires pyarlo python library (with pip)
  * sudo pip3 install pyarlo
* Install a Plugin
  * mkdir -p /home/pi/domoticz/plugins/<plugin_name>
  * wget -O /home/pi/domoticz/plugins/<plugin_name>/plugin.py https://raw.githubusercontent.com/tcellerier/domoticz-plugins/master/<plugin_name>/plugin.py
  * chmod 755 /home/pi/domoticz/plugins/<plugin_name>/plugin.py
* Restart Domoticz
  * sudo service domoticz restart
* Add the device
  * In Domoticz, go to Setup > Hardware, find the Hardware Type, set up the parameters and click Add.


## Update plugin
  * wget -O /home/pi/domoticz/plugins/<plugin_name>/plugin.py https://raw.githubusercontent.com/tcellerier/domoticz-plugins/master/<plugin_name>/plugin.py
  * chmod 755 /home/pi/domoticz/plugins/<plugin_name>/plugin.py
  * sudo service domoticz restart
