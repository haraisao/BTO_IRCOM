#
#
#  Bit Trand One, IR COMM Control 
#
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0
#
import sys


if __name__ == '__main__' :

  data = argv(1)
  if sys.platform == 'win32':
    from ircom_win import *
  else:
    from irom import *

  com = ircom()

  try:
    com.open()
    com.send_ir(data)
    com.close()
  except:
    print "Error"
  
