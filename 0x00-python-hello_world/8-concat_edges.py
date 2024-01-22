#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
<<<<<<< HEAD
    language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:112] + str[:6]
=======
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[105:110] + str[:6]
>>>>>>> 15a087c2df6c0dd08327cef75cd13af6569288c4
print(str)
