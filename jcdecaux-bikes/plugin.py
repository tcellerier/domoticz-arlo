#
# Author: Thomas Cellerier
# Version 1.0.0, 08/2017
#
#  Plugin based on python script by tchellomello (https://github.com/tchellomello/python-arlo)
#
"""
<plugin key="arlo" name="Arlo Security Cameras" author="Thomas Cellerier" version="1.0.0" wikilink="http://www.domoticz.com/wiki/plugins/plugin.html" externallink="https://github.com/tcellerier/domoticz-plugins/">
    <params>
        <param field="Username" label="Arlo Login" width="200px" required="true" />
        <param field="Password" label="Arlo Password" width="200px" required="true" />
        <param field="Mode5" label="Notifications" width="75px">
            <options>
                <option label="True" value="True"/>
                <option label="False" value="False"  default="False" />
            </options>
        </param>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="False" />
            </options>
        </param>
    </params>
</plugin>
"""

import Domoticz
from pyarlo import PyArlo # Arlo Python library 



class BasePlugin:
    enabled = False
    def __init__(self):
        return

    # Called when the hardware is started, either after Domoticz start, hardware creation or update.
    def onStart(self):

        if Parameters["Mode6"] == "Debug":
            Domoticz.Debugging(1)
            DumpConfigToLog()

        # Arlo connexion
        arlo  = PyArlo(Parameters["Username"], Parameters["Password"])
        
        if (len(Devices) == 0):
            for index, cam in enumerate(arlo.cameras):
                Domoticz.Device(Name="Camera " + index, Unit=index, TypeName="Selector Switch", Used=1).Create()
                Options = {"LevelActions": "||||",
                  "LevelNames": "Disarmed|Armed|Scheduled|Custom",
                  "LevelOffHidden": "false",
                  "SelectorStyle": "1"}
                  // !!!! Verifier que index commence à 1 et pas 0
                Domoticz.Log("Camera " + index) #
                Devices[index].Update(BatteryLevel = XXX)

        Domoticz.Log("onStart called")

    # Called when the hardware is stopped or deleted from Domoticz.
    def onStop(self):
        Domoticz.Log("onStop called -- Nothing happens")
    # Called when connection to remote device either succeeds or fails, or when a connection is made to a listening Address:Port. Connection is the Domoticz Connection object associated with the event. Zero Status indicates success. If Status is not zero then the Description will describe the failure.
    def onConnect(self, Connection, Status, Description):
        Domoticz.Log("onConnect called -- Nothing happens")
    # Called when a single, complete message is received from the external hardware
    def onMessage(self, Connection, Data, Status, Extra):
        Domoticz.Log("onMessage called -- Nothing happens")
    # Called after the remote device is disconnected
    def onDisconnect(self, Connection):
        Domoticz.Log("onDisconnect called")

    # Called when a command is received from Domoticz. 
    def onCommand(self, Unit, Command, Level, Hue):

        if action:
            cam.mode = 'armed'
        else:
            cam.mode = 'disarmed'

        Domoticz.Log("onCommand called for Unit " + str(Unit) + ": Parameter '" + str(Command) + "', Level: " + str(Level))

    # Called when any Domoticz device generates a notification. 
    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Log("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    # Called every 'heartbeat' seconds (default 10) regardless of connection status.
    def onHeartbeat(self):
        Domoticz.Log("onHeartbeat called")



global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data, Status, Extra):
    global _plugin
    _plugin.onMessage(Connection, Data, Status, Extra)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

    # Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
