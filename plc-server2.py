#!/usr/bin/env python3
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.payload import BinaryPayloadBuilder, Endian
from pymodbus.client import ModbusTcpClient

import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# --------------------------------------------------------------------------- #
# Configure the service logging
# --------------------------------------------------------------------------- #

def run_payload_server():
    # Initialize Data Block
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100)
    )
    context = ModbusServerContext(slaves=store, single=True)

    # Replace BinaryPayloadBuilder with modern client methods
    client = ModbusTcpClient('127.0.0.1')
    
    # Example payload creation
    payload = client.convert_to_registers(12345, byteorder=Endian.LITTLE, wordorder=Endian.BIG)
    log.info(f"Generated payload: {payload}")

    # Configure the server identity
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName = 'Pymodbus Server'
    identity.MajorMinorRevision = '3.8.0'

    # Start the TCP server
    log.info("Starting Modbus TCP server...")
    StartTcpServer(context, identity=identity, address=("localhost", 5020))


if __name__ == "__main__":
    run_payload_server()