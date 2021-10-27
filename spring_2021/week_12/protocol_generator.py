from pcr_primitive import *

# def read_input(filename):
#     """ takes in py, txt, csv, zip, or png file and reads the data """
#     f = open(filename,"r",encoding="latin1")  # r for read-only
#     all_data = f.read()
#     f.close()
#     return all_data

# # reads input from a separate file and stores in a variable
# protocol_info = read_input("input.py")
# print(protocol_info)

# boilerplate: all protocols
protocol = ["""from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

def run(protocol):
"""]

def fill_template(protocol, labware, actionDetails):
    """create a string of the protocol"""
    
    # writes labware assignment code
    protocol.append("    # assigns labware; labware are labeled by type and deck/pipette location\n")
    protocol.append("        # ex: tiprack_2 is a tip rack in deck 2 & pipette_right is the pipette in the right location\n")
    for item in labware:
        # for generally all labware
        if item[0] == "labware": 
            protocol.append(f"    {item[0]}_{item[2]} = protocol.load_labware('{item[1]}', '{item[2]}')\n")
        
        # pipette case: need to have associated tipracks --> extra parameter needed
        if item[0] == "pipette": 
            protocol.append(f"    {item[0]}_{item[2]} = protocol.load_instrument('{item[1]}', '{item[2]}', tip_racks=[")
            
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
                
        if item[0] == "pick up tip":
            # command
            # ex: pipette_left.pick_up_tip(labware_10['A1'])
            # ex: pipette_left.pick_up_tip()
            if len(item) == 4:
                protocol.append(f"    pipette_{item[3]}.pick_up_tip(labware_{item[2]}{item[1]})\n")
            if len(item) == 2:
                protocol.append(f"    pipette_{item[1]}.pick_up_tip()\n")
            
            # comment

        if item[0] == "drop tip":
            # command
            # ex: pipette_left.drop_tip(labware_10['A1'])
            # ex: pipette_left.drop_tip()
            if len(item) == 4:
                protocol.append(f"    pipette_{item[3]}.drop_tip(labware_{item[2]}{item[1]})\n")
            if len(item) == 2:
                protocol.append(f"    pipette_{item[1]}.drop_tip()\n")
            
            # comment

        if item[0] == "aspirate":
            # command
            # ex: pipette_right.aspirate(50, labware_1['A1'], rate=2.0)
            # ex: pipette_right.aspirate(50)
            protocol.append(f"    pipette_{item[4]}.aspirate({item[1]}")
            if item[2] != [] and item[3] != '':
                protocol.append(f", labware_{item[3]}{item[2]}")
            if item[5] != 'default':
                protocol.append(f", rate={item[5]}")
            protocol.append(")\n")

        if item[0] == "dispense":
            # command
            # ex: pipette_right.dispense(50, labware_1['A1'], rate=2.0)
            # ex: pipette_right.dispense(50)
            protocol.append(f"    pipette_{item[4]}.dispense({item[1]}")
            if item[2] != [] and item[3] != '':
                protocol.append(f", labware_{item[3]}{item[2]}")
            if item[5] != 'default':
                protocol.append(f", rate={item[5]}")
            protocol.append(")\n")

    protocol = "".join(protocol)
    return protocol


filename_for_output_script = "protocol.py"

# create variable with the final protocol string
protocol_string = fill_template(protocol, labware, actionDetails)

# save the protocol into a separate file
f = open(filename_for_output_script, "w") # w for write
print(protocol_string, file=f)
f.close()
print(f"The file {filename_for_output_script} has been written.")
