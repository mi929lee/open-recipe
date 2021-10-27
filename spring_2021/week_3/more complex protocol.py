from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    """transfers ___"""
    plate_1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) # assign plate
    plate_2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3) # assign tiprack
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    reservoir = protocol.load_labware('agilent_1_reservoir_290', 5)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1, tiprack_2]) # associates this pipette with this tiprack

    p300.transfer(360, reservoir, plate_1.wells_by_name()['A1']) # transfers 360 ul liquid from reservoir to plate 1, well A1
    p300.transfer(
        [20, 30, 0, 50], # list of volumes to transfer
        plate_1.wells_by_name()['A1'], # transfer from plate 1 well A1
        [plate_2.columns_by_name()[well_column] for well_column in ['2', '4', '8', '12']]) # 20ul --> col 2, 30ul --> col 4, etc.