from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
    # picks up tip and then stops the protocol

    # boilerplate (common to all tasks)
    # assigns labware to system
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    p300_single = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack1])

    # task-specific
    p300_single.pick_up_tip(tiprack1['B2'])

    # boilerplate
    # stops the protocol
    protocol.pause("The OT-2 stops here until you press resume!")

