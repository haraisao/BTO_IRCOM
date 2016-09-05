#
#
#  Bit Trand One, IR COMM Control 
#
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0
#
import sys

def array2string(data):
  res=''
  for x in data:
    res += '%02x' % x
  return res


if __name__ == '__main__' :
  if sys.platform == 'win32':
    from ircom_win import *
  else:
    from irom import *

  com = ircom()

  try:
    com.open()
    data = com.recieve_ir()
    print array2string(data)
    com.close()
  except:
    print "Error"
  
