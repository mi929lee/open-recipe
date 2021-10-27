from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

name = ''
location = 0

def run(protocol, name, location):
    plate = protocol.load_labware(name, location) 