modbus-attack.sh has to be an executable and run from the Kali to the PLC

PLC server - Make sure tha tyou have the right python version at the beginning of the plc-server.py (#!/usr/bin/env python3)
Install python3-pip (sudo apt install python3-pip)
Install pymodbus (sudo pip3 install pymodbus)

======================================================================
sudo cp /home/fortinet/pymodbus.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pymodbus.service
sudo systemctl start pymodbus.service
sudo systemctl status pymodbus.service

View Logs

If the service encounters errors, view logs using:

sudo journalctl -u pymodbus.service -f
======================================================================

modbus-cli install
[sudo pip3 install umodbus colorama](https://github.com/tallakt/modbus-cli)



