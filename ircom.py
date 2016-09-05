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

def array2string(data):
  res=''
  for x in data:
    res += '%02x' % x
  return res


if sys.platform == 'win32':
  from ircom_win import *
else:
  from ircom_pyusb import *
