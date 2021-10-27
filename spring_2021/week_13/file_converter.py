# import ast

# reads each line from file into a list
with open('protocol_test.txt') as f:
    # lines = [ast.literal_eval(line.rstrip()) for line in f]
    lines = [eval(line.rstrip()) for line in f]
    # print(lines)
    # print("\n")

# can work on fixing pipette + tiprack assignment later
labware = [
    ("labware", "geb_96_tiprack_10ul", '2'), 
    ("pipette", "p10_single", 'right', ['2'])]
# labware = []

# creates labware list
for task in lines:
    # labware_input = ("labware", task[2][0], task[2][1])
    labware_input = ("labware", 'biorad_96_wellplate_200ul_pcr', task[2][1])
    # print(labware_input)
    if labware_input not in labware: labware.append(labware_input)
print(f"labware = {labware}")


# creates action details list
actionDetails = []
for task in lines:
    action = []
    if task[0] == "transfer": 
        action.append("basic transfer")
        action.append(task[1]) # volume
        action.append([f"{task[2][2][1]}{task[2][2][0]}"]) # source well
        action.append(task[2][1]) # source deck
        action.append([f"{task[3][2][1]}{task[3][2][0]}"]) # final well
        action.append(task[3][1]) # final deck
        action.append('right') # fix --> no hard code
    actionDetails.append(tuple(action))
print(f"actionDetails = {actionDetails}")

