#
#
#  Bit Trand One, IR COMM Control 
#
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0
#

if __name__ == '__main__' :
  from ircom import *
  com = ircom()

  try:
    com.open()
    data = com.recieve_ir()
    print data
    print array2string(data)
    com.close()
  except:
    print "Error"
  
