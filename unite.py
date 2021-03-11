from pint import UnitRegistry
from textwrap import dedent
import tz_convert

default_rounder = 2
ureg = UnitRegistry(autoconvert_offset_to_baseunit=True)
Q_ = ureg.Quantity

#take user input and use ureg to convert accordingly
def convertInput(args):

    #time zone conversion
    if ':' in args:
        args = args.upper().split()
        args.pop(0)

        target = args[len(args)-1]

        given = []
        #hour
        given.append(int(args[0].split(':')[0]))
        #minute
        given.append(int(args[0].split(':')[1]))

        #need to check if AM or PM is being used
        #have [00:00, AM/PM, TZ1, 'to', TZ2]
        #need [hour, minute, TZ1, AM/PM]
        if 'AM' in args or 'PM' in args:
            try:
                #TZ1
                given.append(args[2])
                #AM/PM
                given.append(args[1])
            except:
                return "Invalid command."
        #otherwise assume 24 hour time
        #have [00:00, TZ1, 'to', TZ2]
        #need [hour, minute, TZ1, '24']
        else:
            try:
                #TZ1
                given.append(args[1])
                given.append('24')
            except:
                return "Invalid command."

        try:
            return tz_convert.convert(given, target)
        except:
            return "Invalid command."

        

    #split into list so that we can get the rounder - might be more than one digit
    args = args.split()
    #get rid of the bot tag
    args.pop(0)

    #if the last input string is a digit then we have a rounder, pop it from the list
    rounder = default_rounder if not args[len(args)-1].isdigit() else int(args.pop())

    try:
        src = " ".join(args[0:args.index("to")]) #value + unit to convert
        dst = " ".join(args[args.index("to")+1:]) #desired unit
    except:
        return "Invalid command."

    #default rounding to two decimals, otherwise user-input rounder
    result = round(Q_(src).to(dst), rounder)

    return result