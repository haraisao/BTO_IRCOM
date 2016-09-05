#
#
#  Bit Trand One, IR COMM Control 
#  This program require 'PyUSB 1.0'
#  Copyright (C) 2016 Isao Hara, All Right Reserved
#  License : MIT License 1.0
#
import usb.core
import array

class ircom:
  def __init__(self):
    self.interface=3
    self.write_endpoint=0x04
    self.read_endpoint=0x84
    self.max_bufsize=64
    self.init_buffer()
    self.device = usb.core.find(idVendor=0x22ea, idProduct=0x001e)

  def open(self):
    if not self.device :
      self.device = usb.core.find(idVendor=0x22ea, idProduct=0x001e)
      if not self.device:
        raise RuntimeError, 'Device not found' 

    self.device.reset()
    if self.device.is_kernel_driver_active(self.interface):
      self.device.detach_kernel_driver(self.interface)

    self.clear_buffer()

  def close(self):
    del self.device
    self.device = None

  def write(self, data, timeout=1000):
    if not self.device :
      raise RuntimeError, 'Device not found' 

    return self.device.write(self.write_endpoint, data, timeout)

  def read(self, size, timeout=1000):
    if not self.device :
      raise RuntimeError, 'Device not found' 

    return self.device.read(self.read_endpoint, size, timeout)

  def init_buffer(self):
    self.send_buffer=array.array('B', '\xff'* self.max_bufsize)
    return self.send_buffer

  def clear_buffer(self):
    self.init_buffer()
    self.send_buffer[0]=0x41
    self.write(self.send_buffer)
    return self.read(self.max_bufsize)

  def set_recieve_mode(self, mode=0):
    self.init_buffer()
    self.send_buffer[0]=0x51
    self.send_buffer[1]=mode
    self.write(self.send_buffer)
    return self.read(self.max_bufsize)

  def recieve_ir(self):
    self.set_recieve_mode(0x01)
    self.send_buffer[0]=0x50
    self.send_buffer[1]=0xff
    while 1:
      self.write(self.send_buffer)
      res = self.read(self.max_bufsize)
      if res[1] != 0:
        self.set_recieve_mode(0x00)
        return res[1:8]

  def send_ir(self, data):
    self.init_buffer()
    self.send_buffer[0]=0x60
    for i in range(len(data)):
      self.send_buffer[i+1]=data[i]

    self.write(self.send_buffer)
    return

if __name__ == '__main__' :
  Com = ircom()
  try:
    Com.init()
  except:
    print "Error in init"
  
