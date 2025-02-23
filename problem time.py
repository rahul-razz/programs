#Task - Print good morning for before noon, good afternoon for before 20 and good night for after 20 till 6 

import datetime
a=datetime.datetime.now()
Hour=int(a.strftime("%H"))
if Hour>6 and Hour<12:
    print("Good morning")
elif Hour>12 and Hour<20:
    print("Good afternoon")
else:
    print("Good night")
    
