from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    # assigns labware; labware are labeled by type and deck/pipette location
        # ex: tiprack_2 is a tip rack in deck 2 & pipette_right is the pipette in the right location
    labware_2 = protocol.load_labware('geb_96_tiprack_10ul', '2')
    pipette_right = protocol.load_instrument('p10_single', 'right', tip_racks=[labware_2])
    labware_1 = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '1')

    # commands the robot; also, messages (about what the robot just did) are displayed after execution
    pipette_right.transfer(5.0, labware_1.wells_by_name()['D1'], labware_1.wells_by_name()['F1'])
    protocol.comment('Transferred 5.0 ul of liquid from well D1 in deck location 1 to well F1 in deck location 1.')
    pipette_right.transfer(1.0, labware_1.wells_by_name()['E1'], labware_1.wells_by_name()['F1'])
    protocol.comment('Transferred 1.0 ul of liquid from well E1 in deck location 1 to well F1 in deck location 1.')

