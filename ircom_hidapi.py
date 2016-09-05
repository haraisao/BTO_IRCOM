#
#
#  Bit Trand One, IR COMM Control 
#  This program require 'python-hidapi'
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0

import hid

def find_ircom(n):
  try:
    devices = hid.enumerate()
    for lst in devices:
      if lst['vendor_id'] == 0x22ea and lst['product_id'] == 0x01e and lst['interface_number'] == n:
        return lst['path']
  except:
    print "ERROR"
    return None
  return None

def open_ircom(n=3):
  try:
    h = hid.device()
    path = find_ircom(n)
    if path :
      h.open_path(path) 
      return h 
  except:
    print "ERROR"

  return None

def clear_buffer(h):
  try:
    cmd=0x41
    h.write([0x00, cmd, 0xff])
    h.read(64)
    return True
  except:
    print "ERROR"

  return False

def set_recieve_mode(h, mode=0x01, ext=0):
  try:
    cmd=0x51
    if ext == 1: cmd=0x53
    h.write([0x00, cmd, mode])
    val = h.read(64)
    return val
  except IOError, ex:
    print "ERROR"
  return None


def recieve_ir(h, ext=0):
  try:
    clear_buffer(h)
    cmd=0x50
    if ext == 1: cmd=0x52
    set_recieve_mode(h, 0x01, ext)
    while 1 :
      h.write([0x00, cmd])
      val = h.read(64)
      if val[0] == cmd and val[1] != 0:
        res = val
        set_recieve_mode(h, 0x00, ext)
        return res
  except IOError, ex:
    print "ERROR"
  return None

def send_ir(h,data, ext=0):
  try:
    clear_buffer(h)
    len=7
    cmd=0x60
    if ext == 1:
      len=35
      cmd=0x61
    sendbuf=[0x00,cmd]
    for i in range(len):
      sendbuf.append(data[i+1]) 

    h.write(sendbuf)
    clear_buffer(h)
  except IOError, ex:
    print "ERROR"
  return None

