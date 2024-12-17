#!/usr/bin/env python3
from pymodbus.server import StartTcpServer  # Updated import
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.payload import BinaryPayloadBuilder, Endian
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

    # Correct usage of BinaryPayloadBuilder
    builder = BinaryPayloadBuilder(byteorder=Endian.LITTLE, wordorder=Endian.BIG)
    builder.add_32bit_uint(12345)  # Example: Add a 32-bit unsigned integer to the payload
    payload = builder.to_registers()
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
