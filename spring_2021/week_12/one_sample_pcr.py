# list of labware and its location: in tuples!
# (labware type, code, location)
labware = [
    ("labware", "geb_96_tiprack_10ul", '11'),
    ("labware", "opentrons_96_tiprack_300ul", '10'),
    ("labware", "opentrons_96_aluminumblock_generic_pcr_strip_200ul",'8'), 
    ("labware", "opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical",'7'),
    ("labware", "opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",'9'),
    ("pipette", "p10_single", 'right', ['11']),
    ("pipette", "p50_single", 'left', ['10'])
    ]

# basic transfer: (basic transfer, volume, initial well, initial deck location, final well, final deck location, pipette)
# mix: (mix, repetitions, volume, plate, well LIST, pipette)
# distribute: (distribute, volume, initial well LIST, initial deck location, final well LIST, final deck location, pipette)
actionDetails = [
    ("basic transfer", 20.5, ['A1'], '9', ['A1'], '8', 'left'), 
    ("basic transfer", 25, ['A4'], '7', ['A1'], '8', 'left'), 
    ("basic transfer", 1, ['C1'], '9', ['A1'], '8', 'right'), 
    ("basic transfer", 1, ['B2'], '9', ['A1'], '8', 'right'),
    ("basic transfer", 2.5, ['D2'], '9', ['A1'], '8', 'right'),
    ("mix", 5, 40, '8', ['A1'], 'left')]