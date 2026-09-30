#!/usr/bin/env python3
#shebang
#the backlash is the escape speciial character... how then do we output a backlash?

#domain expansion double backlash
print("The dir to the wallet is c:\\user\\bank\\wallet")
     #the output obviously print with single strokes  ;)

#the boring way to doit is uese the raw string character  which tells the interprator to inetrprate \ as a string
print(r"c:\usr\bank\wallet")
     

#tripple quotes  >>used to create multi line strings without initiating escape sequences 

print("""The guy hit the \n for a new line 
He wrote commas all over it's his thing now
""")

"""He even learnt aboyt docstrings"""
 
#and finally  emojis  unicode escape sequences 
print("smile \u263A")
