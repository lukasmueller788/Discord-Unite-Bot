from pint import UnitRegistry

default_rounder = 2
ureg = UnitRegistry(autoconvert_offset_to_baseunit=True)
Q_ = ureg.Quantity

#take user input and use ureg to convert accordingly
def convertInput(args):

    #split into list so that we can get the rounder - might be more than one digit
    args = args.split()
    #get rid of the bot tag
    args.pop(0)

    #if the last input string is a digit then we have a rounder, pop it from the list
    rounder = default_rounder if not args[len(args)-1].isdigit() else int(args.pop())

    src = " ".join(args[0:args.index("to")]) #value + unit to convert
    dst = " ".join(args[args.index("to")+1:]) #desired unit 

    #default rounding to two decimals, otherwise user-input rounder
    result = round(Q_(src).to(dst), rounder)

    return result