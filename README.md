# Discord UniteBot
![logo embed](https://cdn.discordapp.com/attachments/667471154365071379/716789461748416512/logo_black_smaller.png)  
Artist: [algooddevils](https://twitter.com/algooddevils) (Twitter)  
UniteBot uses the [Pint](https://pint.readthedocs.io/en/0.11/) Python library to make unit conversions at the request of Discord users. It supports any unit type that Pint supports (save for time zones, to be implemented), although not all unit types will be described below. [Here](https://github.com/hgrecco/pint/blob/master/pint/default_en.txt) is a decent outline of the unit types supported by Pint.
  
# How to Use
UniteBot's tag is `!u`.  
Ask UniteBot to convert something like this:  
`!u [value] [unit1] to [unit2] (rounder)`  
The rounder is optional and defaults to 2 decimal places.  

Example Input:  
`!u 10 m to cm`  
Output:  
`1000.0 centimeter`  

# Supported Unit Types and Help Commands
As stated before, a more comprehensive outline of the types of measurement supported by Pint, and by extension UniteBot, can be found [here](https://github.com/hgrecco/pint/blob/master/pint/default_en.txt). 

To get help from UniteBot, type:  
`!u h(elp)`  
This will return an embed outlining how to use the bot, a list of some of the unit types it supports, and how to get more specific help with each of those unit types. These unit types include:
- Time Zones  
- Angle
- Length
- Mass
- Time
- Temperature
- Area
- Volume
- Velocity
- Acceleration
- Energy
- Density

Getting help with a specific unit type is simple.  
For example, typing:  
`!u h(elp) area`  
will return the following embed:  
![area help embed](https://media.discordapp.net/attachments/667471154365071379/711695169430224907/unknown.png)  

You can also type:  
`!u sources`  
to return an embed with a list of sources used by UniteBot.  
[Pint](https://pint.readthedocs.io/en/0.11/)  
[Time Zone Data (timeanddate.com)](https://www.timeanddate.com/time/zones/)
