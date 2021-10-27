# LABWARE
# 2 ml screwcap tube: opentrons_24_tuberack_nest_2ml_screwcap
# 0.5 ml screwcap tube: opentrons_24_tuberack_nest_0.5ml_screwcap
# 5ul & 10ul --> 'p10_single'

# executing protocol code
d = {}
d['opentrons_24_tuberack_nest_2ml_screwcap'] = "protocol.load_labware('opentrons_24_tuberack_nest_2ml_screwcap',"
d['opentrons_24_tuberack_nest_0.5ml_screwcap'] = "protocol.load_labware('opentrons_24_tuberack_nest_0.5ml_screwcap',"
d['p10_single'] = "protocol.load_instrument('p10_single', "

# boilerplate: all protocols
protocol = ["""from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
"""]

# list of labware and its location: in tuples!
# (labware type, code, location)
labware = [
    ("labware", "protocol.load_labware('geb_96_tiprack_10ul', ", '11'),
    ("labware", "protocol.load_labware('opentrons_96_tiprack_300ul', ", '10'),
    ("labware", "protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul',",'8'), 
    ("labware", "protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',",'7'),
    ("labware", "protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',",'9'),
    ("pipette", "protocol.load_instrument('p10_single', ", 'right', ['11']),
    ("pipette", "protocol.load_instrument('p50_single', ", 'left', ['10'])
    ]

# basic transfer: (basic transfer, volume, initial well, initial deck location, final well, final deck location, pipette)
# mix: (mix, repetitions, volume, plate, well LIST, pipette)
# distribute: (distribute, volume, initial well LIST, initial deck location, final well LIST, final deck location, pipette)
actionDetails = [
    ("distribute", 20.5, ['A1'], '9', ['A1', 'A2', 'A3', 'A4', 'A5'], '8', 'left'), # sterile water
    ("distribute", 25, ['A4'], '7', ['A1', 'A2', 'A3', 'A4', 'A5'], '8', 'left'), # 2x master mix
    ("distribute", 1, ['C1'], '9', ['A1', 'A2', 'A3', 'A4', 'A5'], '8', 'right'), # forward primer
    ("distribute", 1, ['B2'], '9', ['A1', 'A2', 'A3', 'A4', 'A5'], '8', 'right'), # reverse primer
    ("basic transfer", 2.5, ['D2'], '9', ['A1'], '8', 'right'), # DNA template (D2-D5)
    ("basic transfer", 2.5, ['D3'], '9', ['A2'], '8', 'right'),
    ("basic transfer", 2.5, ['D4'], '9', ['A3'], '8', 'right'),
    ("basic transfer", 2.5, ['D5'], '9', ['A4'], '8', 'right'),
    ("basic transfer", 2.5, ['A1'], '9', ['A1'], '8', 'right'), # sterile water (A1)
    ("mix", 5, 40, '8', ['A1', 'A2', 'A3', 'A4', 'A5'], 'left')]


def fill_template(protocol, labware, actionDetails):
    """fill in protocol"""
    
    # writes labware assignment code
    protocol.append("    # assigns labware; labware are labeled by type and deck/pipette location\n")
    protocol.append("        # ex: tiprack_2 is a tip rack in deck 2 & pipette_right is the pipette in the right location\n")
    for item in labware:
        # for generally all labware
        if item[0] != "pipette": 
            protocol.append(f"    {item[0]}_{item[2]} = {item[1]}'{item[2]}')\n")
        
        # pipette case: need to have associated tipracks --> extra parameter needed
        else: 
            protocol.append(f"    {item[0]}_{item[2]} = {item[1]}'{item[2]}', tip_racks=[")
            
            # adding all tipracks associated with this pipette
            # item[3] is a list of deck locations of tipracks that this pipette is associated with
            for i in range(len(item[3])): 
                
                # only add a comma if the tiprack we are assigning is not the last one
                if i != len(item[3])-1:
                    protocol.append(f"labware_{item[3][i]}, ")
                else:
                    protocol.append(f"labware_{item[3][i]}])\n")

    # skip line --> two blocks of code
    protocol.append("\n")

    # writes robot command code
    protocol.append("    # commands the robot; also, messages (about what the robot just did) are displayed after execution\n")
    for item in actionDetails:
        if item[0] == "basic transfer":
            # command
            # ex: pipette_right.transfer(5, labware_2.wells_by_name()['A3'], labware_2.wells_by_name()['A1'])
            protocol.append(f"    pipette_{item[6]}.transfer(")
            protocol.append(f"{item[1]}, labware_{item[3]}.wells_by_name(){item[2]}, labware_{item[5]}.wells_by_name(){item[4]})\n")

            # comment
            # ex: protocol.comment('Transferred 5 ul of liquid from well A3 in deck location 2 to well A1 in deck location 2.')
            protocol.append(f"    protocol.comment('Transferred ")
            protocol.append(f"{item[1]} ul of liquid from well {item[2][0]} in deck location {item[3]} ")
            protocol.append(f"to well {item[4][0]} in deck location {item[5]}.')\n")

        if item[0] == "distribute":
            # command
            # ex: pipette_left.distribute(20.5, labware_9.wells_by_name()['A1'], 
            #     [labware_8.wells_by_name()[well_name] for well_name in ['A1', 'A2', 'A3', 'A4', 'A5']])
            protocol.append(f"    pipette_{item[6]}.distribute({item[1]}, labware_{item[3]}.wells_by_name(){item[2]}, ")
            protocol.append(f"[labware_{item[5]}.wells_by_name()[well_name] for well_name in {item[4]}])\n")

            # comment
        
        if item[0] == "mix":
            for well in item[4]:
                # command
                protocol.append(f"    pipette_{item[5]}.pick_up_tip()\n") # need to pick up tip before mixing!
                protocol.append(f"    pipette_{item[5]}.mix({item[1]}, {item[2]}, labware_{item[3]}['{well}'])\n")
                protocol.append(f"    pipette_{item[5]}.drop_tip()\n")

                # comment

    protocol = "".join(protocol)
    return protocol


filename_for_output_script = "protocol.py"

# create variable with the final protocol string
protocol_string = fill_template(protocol, labware, actionDetails)

# let's save it to a file...
f = open(filename_for_output_script, "w")
print(protocol_string, file=f)
f.close()
print(f"The file {filename_for_output_script} has been written.")
