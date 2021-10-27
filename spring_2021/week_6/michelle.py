#
# example script-writing script!
#

# helper function

def fill_template(d):
    """ fill a template with important stuff! """
    TEMPLATE_W_BOILERPLATE = f"""
import math

def f(x):
    print("x is", x)
    for i in range(40,{d['important_number']+1}):
        print("i is",i)
        print("moving from current location to {d['glassware1']}")
    print("x+1 is", x+1)

if __name__ == "__main__":
    f(41)
"""
    return TEMPLATE_W_BOILERPLATE


#
# Here is the start of our script-writing script
#
filename_for_output_script = "opentrons_task1.py"

# set up dictionary... probably from the AR side of things...
d = {}
d['glassware1'] = 'complicated_glassware_name1'
d['important_number'] = 42

# get the "TEMPLATE STRING"
THE_TEMPLATE_STRING = fill_template(d)

# let's make sure it looks right...
print(THE_TEMPLATE_STRING)

# let's save it to a file...
f = open(filename_for_output_script, "w")
print(THE_TEMPLATE_STRING, file=f)
f.close()
print(f"The file {filename_for_output_script} has been written.")

# complete!  (for now...)