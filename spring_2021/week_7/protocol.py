from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    labware_3 = protocol.load_labware('opentrons_24_tuberack_nest_2ml_screwcap','3')
    labware_2 = protocol.load_labware('opentrons_24_tuberack_nest_0.5ml_screwcap','2')
    labware_right = protocol.load_instrument('p10_single', 'right')

