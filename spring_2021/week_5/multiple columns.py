from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    """transfers the same volume into each well within a column. can transfer different volumes for different columns"""

    # assigns all labware
    plate_1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) # assign plate
    plate_2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3) # assign tiprack
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    reservoir = protocol.load_labware('agilent_1_reservoir_290ml', 5)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1, tiprack_2]) # associates this pipette with this tiprack

    # transfers 360 ul each from reservoir to plate 1, wells A1 & B7
    p300.transfer(360, reservoir.wells()[0], [plate_1.wells_by_name()[well_name] for well_name in ['A1', 'B7']])
    
    column_volumes = [30, 100]
    well_volumes = []

    # creates list of well volumes from a list of column volumes
    for column in column_volumes:
        for i in range(8):
            column_index = column_volumes.index(column) # finds index of value within a list
            well_volumes.append(column_volumes[column_index])

    # print(well_volumes) --> output: [30, 30, 30, 30, 30, 30, 30, 30, 50, 50, 50, 50, 50, 50, 50, 50]

    p300.distribute( # optimized for transfer from one (or small number of) well to many locations
        well_volumes, # when transfer from well to column, need value for each well
        [plate_1.wells_by_name()[well_name] for well_name in ['A1', 'B7']], # transfer from plate 1 wells A1 & B7
        [plate_2.columns_by_name()[well_column] for well_column in ['8', '1']])
        #[plate_2.rows_by_name()[row] for row in ['A', 'C', 'E', 'D']])