#
#
#  Bit Trand One, IR COMM Control 
#
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0
#

if __name__ == '__main__' :
  from ircom import *

  data = getHexArray(sys.argv[1])
  com = ircom()

  try:
    com.open()
    print data
    com.send_ir(data)
    com.close()
  except:
    print "Error"
  
