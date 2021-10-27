#
# example for michelle!
#


def f(filename):
    """ call this with
            f("filereader_for_michelle.py") or
            f("a.txt") or
            f("data.csv") or
            f("michelle's important data.zip") or even
            f("screenshot.png")
        and it will read in - and print out - all of the data
        Note: for zip and png files, that will not be human readable data!!
    """
    f = open(filename,"r",encoding="latin1")  # Note: this encoding could be wrong!
    all_data = f.read()
    f.close()
    print("\n\nall_data is", all_data, "\n\n")
    return all_data[42:43]  # just for fun


# here is an example that really should work!  
# (It returns 'm' for me, which makes sense, since it's the michelle filereader!  :-)
result = f("filereader_for_michelle.py")
print(f"result is {result}")