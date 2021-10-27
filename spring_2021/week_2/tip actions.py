from opentrons import protocol_api
metadata = {'apiLevel': '2.9'}

#https://docs.opentrons.com/v2/new_atomic_commands.html

def run(protocol, well_location):
    """pick up tip"""
    pipette.pick_up_tip(tiprack[well_location]) #assume that we labeled a state of the pipette --> pipette = protocol.load_instrument('p300_single_gen2', mount='left)
    # can associate tip with a certain tiprack --> right = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack1, tiprack2])
        #if so, use pipette.pick_up_tip()

def run(protocol, well_location):
    """drop tip into a well on the tiprack"""
    pipette.drop_tip(tiprack[well_location])

def run(protocol):
    """drop tip into fixed track on the deck"""
    pipette.drop_tip()

def run(protocol): #what's the point of returning tips???
    """returns the tip to the location that it picked the tip from"""
    pipette.return_tip() #i'm not sure if it needs the pick up tip function directly before it...
    #in version 2.2 or above, after returning the tip, when pipette.pick_up_tip() called, the next tip (another well) is picked up
        #this is assuming there is a tip rack that is associated with it
    #there's a function to reset the tip you want to pick up from

def run(protocol, volume, location, well, speed):
    """aspirates volume in µL, where to aspirate from, and how fast to aspirate liquid"""
    pipette.aspirate(volume, plate[well], rate=speed) #aspirate = how much pipette takes up into the tip