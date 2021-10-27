from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    # test to see if it's possible to replace labware

    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '2')
    left = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    left.transfer(100, plate.wells_by_name()['A1'], plate.wells_by_name()['B1']) # 100 ul from A1 to B1
    
    # replace left with a new pipette
    left = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])
    
    left.transfer(100, plate.wells_by_name()['B1'], plate.wells_by_name()['A1']) # 100 ul from A1 to B1