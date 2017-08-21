# Bunch of Domoticz Plugins

## Installation 
* Requires Domoticz v3.8153 or newer
* Requires Python 3
  * sudo apt-get install -y python3
  * sudo apt-get install -y python3-dev
* Requires pyarlo python library
  * wget -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py
  * python /tmp/get-pip.py
  * sudo pip install pyarlo
* Install Plugin
  * mkdir -p /home/pi/domoticz/plugins/<plugin_name>
  * wget -O /home/pi/domoticz/plugins/<plugin_name>/plugin.py https://raw.githubusercontent.com/tcellerier/domoticz-plugins/master/<plugin_name>/plugin.py
  * chmod 755 /home/pi/domoticz/plugins/<plugin_name>/plugin.py
* Restart Domoticz
  * sudo service domoticz restart
 
## Description
* Ongoing development. Stay posted.
