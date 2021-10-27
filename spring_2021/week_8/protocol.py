from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    # assigns labware; labware are labeled by type and deck/pipette location
        # ex: tiprack_2 is a tip rack in deck 2 & pipette_right is the pipette in the right location
    tiprack_1 = protocol.load_labware('geb_96_tiprack_10ul', '1')
    tuberack_3 = protocol.load_labware('opentrons_24_tuberack_nest_2ml_screwcap','3')
    tuberack_2 = protocol.load_labware('opentrons_24_tuberack_nest_0.5ml_screwcap','2')
    pipette_right = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_1])

    # commands the robot; also, messages (about what the robot just did) are displayed after execution
    pipette_right.transfer(5, labware_2.wells_by_name()['A3'], labware_2.wells_by_name()['A1'])
    protocol.comment('Transferred 5 ul of liquid from well A3 in deck location 2 to well A1 in deck location 2.')
    pipette_right.transfer(1, labware_3.wells_by_name()['A1'], labware_2.wells_by_name()['A1'])
    protocol.comment('Transferred 1 ul of liquid from well A1 in deck location 3 to well A1 in deck location 2.')

