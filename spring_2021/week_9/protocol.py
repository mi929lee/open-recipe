from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    # assigns labware; labware are labeled by type and deck/pipette location
        # ex: tiprack_2 is a tip rack in deck 2 & pipette_right is the pipette in the right location
    labware_11 = protocol.load_labware('geb_96_tiprack_10ul', '11')
    labware_10 = protocol.load_labware('opentrons_96_tiprack_300ul', '10')
    labware_8 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','8')
    labware_7 = protocol.load_labware('opentrons_10_tuberack_falcon)4x50ml_6x15ml_conical','7')
    labware_9 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap','9')
    pipette_right = protocol.load_instrument('p10_single', 'right', tip_racks=[labware_11])
    pipette_left = protocol.load_instrument('p50_single', 'left', tip_racks=[labware_10])

    # commands the robot; also, messages (about what the robot just did) are displayed after execution
    pipette_right.transfer(20.5, labware_2.wells_by_name()['A3'], labware_2.wells_by_name()['A1'])
    protocol.comment('Transferred 20.5 ul of liquid from well A3 in deck location 2 to well A1 in deck location 2.')
    pipette_right.transfer(1, labware_3.wells_by_name()['A1'], labware_2.wells_by_name()['A1'])
    protocol.comment('Transferred 1 ul of liquid from well A1 in deck location 3 to well A1 in deck location 2.')
    pipette_right.mix(5, 5, labware_2['A1'])
