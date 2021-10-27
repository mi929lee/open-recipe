# (labware type, code, deck location)
labware = [
    ("labware", "geb_96_tiprack_10ul", '1'),
    ("labware", "opentrons_24_tuberack_nest_2ml_screwcap",'3'), 
    ("labware", "opentrons_24_tuberack_nest_0.5ml_screwcap",'2'),
    ("pipette", "p10_single", 'right', ['1'])
    ]

# basic transfer: (basic transfer, volume, initial well, initial deck location, final well, final deck location, pipette)
# mix: (mix, repetitions, volume, plate, well LIST, pipette)
# distribute: (distribute, volume, initial well LIST, initial deck location, final well LIST, final deck location, pipette)
actionDetails = [
    ("basic transfer", 5, ['A3'], '2', ['A1'], '2', 'right'), 
    ("basic transfer", 1, ['A1'], '3', ['A1'], '2', 'right'), 
    ("mix", 5, 5, '2', ['A1'], 'right')]