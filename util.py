"""
General utility functions.
"""
def rgb_perc(red: int, green: int, blue: int) -> str:
    """
    Convert Percentages of RGB values to hex color code.
    """
    rgb_val = lambda red, green, blue: "#%02x%02x%02x" % (red, green, blue)
    perc = lambda x: int(x / 100 * 255) # inline conversion function
    red, green, blue = (perc(red), perc(green), perc(blue)) # get values
    return rgb_val(red, green, blue) # return hex value
