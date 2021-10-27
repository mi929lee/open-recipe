from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}
def pickuptip(location):

def loadplate(plate, location):
    plate = protocol.load_labware(plate, location)

def loadtiprack_1(tiprack, location):
    tiprack_1 = protocol.load_labware

def loadlabware(plate, tiprack, platelocation, tipracklocation):
    "for string arguments plate & tiprack and their respective locations, load labware"
    plate = protocol.load_labware(plate, platelocation)
    tiprack = protocol.load_labware(tiprack, tipracklocation)

def loadplate (plate, platelocation):
    "loads plate into system"
    plate = protocol.load_labware(plate, platelocation)

def loadtiprack (tiprack, tipracklocation):
    "loads tiprack into system"
    tiprack = protocol.load_labware(tiprack, tipracklocation)

def loadpipette (pipette, location, tiprack):
    pipette = protocol.load_instrument(pipette, location, tip_racks=[tiprack])

def pickuptip(pipette):
    pipette.pick_up_tip()

# def run(protocol):
#     protocol.