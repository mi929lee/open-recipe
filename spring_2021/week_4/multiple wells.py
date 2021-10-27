from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    """
    1. transfers 360 ul from reservoir to plate 1, well A1 (max 360 ul volume)
    2. transfers 4 different volumes of liquid from plate 1, well A1 to 4 other wells on plate 2
    """

    # assigns all labware
    plate_1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1) # assign plate
    plate_2 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3) # assign tiprack
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    reservoir = protocol.load_labware('agilent_1_reservoir_290ml', 5)
    p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack_1, tiprack_2]) # associates this pipette with this tiprack

    # transfers 360 ul from reservoir to plate 1, well A1
    p300.transfer(360, reservoir.wells()[0], plate_1.wells_by_name()['A1'])

    # transfers volume from plate 1, well A1 to random wells in plate 2
    p300.transfer(
        [20, 30, 0, 50], # list of volumes to transfer; includes skipping wells (0)
        plate_1.wells_by_name()['A1'], # transfer from plate 1 well A1
        [plate_2.wells_by_name()[well_name] for well_name in ['B1', 'C3', 'D6', 'A2']]) # transfer to these wells in plate 2