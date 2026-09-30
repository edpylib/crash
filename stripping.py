#!/usr/bin/env python3
#so the # hash and the ! bang are instrutions to the kernel to invoke the interprator specified in the absolute path
                                      #
#we can srip caracters and white spaces from strings  using functions
#named  block of code designed for a specific operation
dirty_name = "  Bro has the hiccups  " #white spaces at the beninging :) and end
name = dirty_name.strip()
print(dirty_name)
print(name)

#we can pass what caharacters to strip
sampuli = " !#@Brayo mtapeli@!# "
#an error turns ot the space  should also be passed in the arguements or  it wont be stripped and if it comes first like in our case no stripping will be done
thamburi = sampuli.strip("@!# ") #pass arguments as string ama interpreter inathani ni text
print(thamburi)

#we could strip to the right or left only 
print(sampuli.lstrip("!@# "))
print(sampuli.rstrip("!@# "))
 
#the strip() function remose escape characters  \t \n when nthn is specified as an arguement
grape = "\n\tGrapes baba,  kula fruits"
print(grape)
grapes = grape.strip()
print(grapes)

#strip is used for characters now prefixes and suffixes 
url = "https://brian.box.nest.com"
ur =url.removeprefix("https://")
print(ur)
u  = ur.removesuffix("nest.com")
print(u)
