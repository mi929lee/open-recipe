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
protocol = """from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
"""

# list of labware and its location: in tuples!
# (labware type, code, deck location)
labware = [
    ("tiprack", "protocol.load_labware('geb_96_tiprack_10ul', ", '1'),
    ("tuberack", "protocol.load_labware('opentrons_24_tuberack_nest_2ml_screwcap',",'3'), 
    ("tuberack", "protocol.load_labware('opentrons_24_tuberack_nest_0.5ml_screwcap',",'2'),
    ("pipette", "protocol.load_instrument('p10_single', ", 'right', ['1'])
    ]

# basic transfer template: (basic transfer, volume, initial well, initial deck location, final well, final deck location, pipette)
# mix template: (mix, repetitions, volume, plate, well, pipette)

# transfer 5 ul from A3 (plate 2) --> A1 (plate 2) ... then, transfer 1 ul from A1 (plate 3) --> A1 (plate 2)
actionDetails = [
    ("basic transfer", 5, ['A3'], '2', ['A1'], '2', 'right'), 
    ("basic transfer", 1, ['A1'], '3', ['A1'], '2', 'right'), 
    ("mix", 5, 5, '2', 'A1', 'right')]


def fill_template(protocol, labware, actionDetails):
    """fill in protocol"""
    
    # writes labware assignment code
    protocol += "    # assigns labware; labware are labeled by type and deck/pipette location\n"
    protocol += "        # ex: tiprack_2 is a tip rack in deck 2 & pipette_right is the pipette in the right location\n"
    for item in labware:
        # for generally all labware
        if item[0] != "pipette": 
            protocol += f"    {item[0]}_{item[2]} = {item[1]}'{item[2]}')\n"
        
        # pipette case: need to have associated tipracks --> extra parameter needed
        else: 
            protocol += f"    {item[0]}_{item[2]} = {item[1]}'{item[2]}', tip_racks=["
            
            # adding all tipracks associated with this pipette
            # item[3] is a list of deck locations of tipracks that this pipette is associated with
            for i in range(len(item[3])): 
                
                # only add a comma if the tiprack we are assigning is not the last one
                if i != len(item[3])-1:
                    protocol += f"tiprack_{item[3][i]}, "
                else:
                    protocol += f"tiprack_{item[3][i]}])\n"

    # skip line --> two blocks of code
    protocol += "\n"

    # writes robot command code
    protocol += "    # commands the robot; also, messages (about what the robot just did) are displayed after execution\n"
    for item in actionDetails:
        if item[0] == "basic transfer":
            # ex: pipette_right.transfer(5, labware_2.wells_by_name()['A3'], labware_2.wells_by_name()['A1'])
            command = f"    pipette_{item[6]}.transfer("
            command += f"{item[1]}, labware_{item[3]}.wells_by_name(){item[2]}, labware_{item[5]}.wells_by_name(){item[4]})\n"
            protocol += command

            # ex: protocol.comment('Transferred 5 ul of liquid from well A3 in deck location 2 to well A1 in deck location 2.')
            comment = f"    protocol.comment('Transferred "
            comment += f"{item[1]} ul of liquid from well {item[2][0]} in deck location {item[3]} "
            comment += f"to well {item[4][0]} in deck location {item[5]}.')\n"
            protocol += comment
        if item[0] == "mix":
            protocol += f"    pipette_{item[5]}.mix({item[1]}, {item[2]}, labware_{item[3]}.['{item[4]}'])"
    return protocol


filename_for_output_script = "protocol.py"

# create variable with the final protocol string
protocol_string = fill_template(protocol, labware, actionDetails)

# let's save it to a file...
f = open(filename_for_output_script, "w")
print(protocol_string, file=f)
f.close()
print(f"The file {filename_for_output_script} has been written.")
