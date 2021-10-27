# LABWARE
# 2 ml screwcap tube: opentrons_24_tuberack_nest_2ml_screwcap
# 0.5 ml screwcap tube: opentrons_24_tuberack_nest_0.5ml_screwcap

# GEL PREP PROTOCOL
# add 5uL sample (from 0.2 ml PCR tube) into 0.2 mL PCR Tube A
# add 1uL of 6X dye (from 2 mL screw cap tube) into Tube A
# mix sample + dye until dye is uniform

# 5ul & 10ul --> 'p10_single'

# boilerplate: all protocols
protocol = """from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
"""

# list of labware and its location: in tuples!
labware = [
    ("protocol.load_labware('opentrons_24_tuberack_nest_2ml_screwcap',",'3'), 
    ("protocol.load_labware('opentrons_24_tuberack_nest_0.5ml_screwcap',",'2'),
    ("protocol.load_instrument('p10_single', ", 'right')]


def fill_template(protocol, labware):
    """fill in dictionary items"""
    for item in labware:
        newline = "    labware_%s = " %(item[1]) + f"{item[0]}'{item[1]}')\n"
        protocol += newline
    return protocol

filename_for_output_script = "protocol.py"

# get the "TEMPLATE STRING" & print to check if it's correct
template = fill_template(protocol, labware)

# let's save it to a file...
f = open(filename_for_output_script, "w")
print(template, file=f)
f.close()
print(f"The file {filename_for_output_script} has been written.")
