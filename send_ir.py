#
#
#  Bit Trand One, IR COMM Control 
#
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0
#
import sys

def getHexArray(data):
  res = []
  for i in range(7):
    st=i*2
    ed=i*2+2
    v=data[st:ed]
    if v :
      res.append(int("0x"+v, 0))
    else:
      res.append(0)
  return res


if __name__ == '__main__' :

  data = getHexArray(sys.argv[1])

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
  
