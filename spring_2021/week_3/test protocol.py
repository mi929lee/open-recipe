from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    """example code (basic transfer): moving 100 ul from one well to another"""

    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) # assign plate 
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2) # assign tiprack
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1]) # associates this pipette with this tiprack

    p300.transfer(100, plate['A1'], plate['B1']) # transfer step