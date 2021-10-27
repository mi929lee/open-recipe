from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    """transfers ___"""

    # assigns all labware
    plate_1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) # assign plate
    plate_2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3) # assign tiprack
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    reservoir = protocol.load_labware('agilent_1_reservoir_290ml', 5)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1, tiprack_2]) # associates this pipette with this tiprack

    # transfers 360 ul each from reservoir to plate 1, wells A1 & B7
    p300.transfer(360, reservoir.wells()[0], [plate_1.wells_by_name()[well_name] for well_name in ['A1', 'B7']])

    ####
    p300.distribute( # optimized for transfer from one (or small number of) well to many locations
        [20, 30, 0, 50, 10, 60, 10, 10, 
        10, 10, 20, 5, 30, 100, 40, 200], # when transfer from well to column, need value for each well
        [plate_1.wells_by_name()[well_name] for well_name in ['A1', 'B7']], # transfer from plate 1 wells A1 & B7
        [plate_2.columns_by_name()[well_column] for well_column in ['8', '1']])
        #[plate_2.rows_by_name()[row] for row in ['A', 'C', 'E', 'D']])