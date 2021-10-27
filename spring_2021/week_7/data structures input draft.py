# LABWARE
# 2 ml screwcap tube: opentrons_24_tuberack_nest_2ml_screwcap
# 0.5 ml screwcap tube: opentrons_24_tuberack_nest_0.5ml_screwcap

# GEL PREP PROTOCOL
# add 5uL sample (from 0.2 ml PCR tube) into 0.2 mL PCR Tube A
# add 1uL of 6X dye (from 2 mL screw cap tube) into Tube A
# mix sample + dye until dye is uniform

# 5ul & 10ul --> 'p10_single'

# THINGS TO KEEP IN MIND / FIX LATER
# assigning pipettes to tipracks


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
# labware = [
#     ("opentrons_24_tuberack_nest_2ml_screwcap",'3'), 
#     ('opentrons_24_tuberack_nest_0.5ml_screwcap','2'),
#     ('p10_single', 'right')]
labware = [
    ("protocol.load_labware('opentrons_24_tuberack_nest_2ml_screwcap',",'3'), 
    ("protocol.load_labware('opentrons_24_tuberack_nest_0.5ml_screwcap',",'2'),
    ("protocol.load_instrument('p10_single', ", 'right')]

# def assignlabware(labware):
#     """add to initial boilerplate: create new boilerplate that has all assigned labware"""
for item in labware:
    newline = "labware_%s = " %(item[1]) + f"{item[0]}'{item[1]}')\n"
    protocol += newline
print(protocol)

# for item in labware:
#     hiddenVar = f"d['{item[0]}']"
#     newline = f"{hiddenVar}, '{item[1]}')\n"
#     protocol += newline
# print(protocol)
#newline = "{" + f"d['{item[0]}']" + "}, " + f"'{item[1]}')" + "\n"

# maybe have one dictionary for each type of transfer command?
basicTransfer = {}
oneToOne = {}
oneToMany = {}
distribute = {}

# tuple template: 
# (type of action, 
# volume, 
# origin well, 
# origin labware location, 
# destination well, 
# destination labware location,
# left/right pipette)
actionDetails = [(basicTransfer, 5, 'A3', '2', 'A1', '2', 'right'), (basicTransfer, 1, 'A1', '3', 'A1', '2', 'right')]
"pipette.transfer(5,"
"plate.wells_by_name()"



def fill_template(d):
    """fill in dictionary items"""

    # tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
    # p300_single = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack1])
    # p300_single.pick_up_tip(tiprack1['B2'])
    # # stops the protocol
    # protocol.pause("The OT-2 stops here until you press resume!")
    #return labware

# filename_for_output_script = "sample mini protocol.py"

# # get the "TEMPLATE STRING" & print to check if it's correct
# THE_TEMPLATE_STRING = fill_template()

# # let's save it to a file...
# f = open(filename_for_output_script, "w")
# print(THE_TEMPLATE_STRING, file=f)
# f.close()
# print(f"The file {filename_for_output_script} has been written.")
