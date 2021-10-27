from opentrons import protocol_api

metadata = {'apilevel': '2.9'}

#not really sure if we can add arguments to this? in the examples given, they only have the 'protocol' as argument, but i'm not even sure what this 'protocol' refers to... 
def run(protocol, name, location): #name = string, location = int
    plate=protocol.load_labware(name, location)

def run(protocol, name, location) #i'm thinking of making a separate file for each command (later) so we just pull up the appropriate file when needed
    tiprack = protocol.load_labware(name, location) #my guess: protocol is like an object and we're editing the properties it has --> the robot runs the protocol
    