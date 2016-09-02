from pywinusb import hid
import time

class ircom:
  def __init__(self):
    self.interface=3
    self.bufsize=65
    self.device = None
    self.devices = hid.HidDeviceFilter(vendor_id=0x22ea, product_id=0x001e).get_devices()
    for dev in self.devices:
      if dev.device_path.find('mi_03') > 0:
        self.device=dev
    self.init_buffer()

  def open(self):
    if not self.device :
      raise RuntimeError, 'Device not found' 

    self.device.open()
    self.device.set_raw_data_handler(self.recv_raw_data)

    self.clear_buffer()

  def close(self):
    self.device.close()

  def write(self, data):
    if not self.device :
      raise RuntimeError, 'Device not found' 

    self.init_buffer()
    for i in range(len(data)):
      self.send_buffer[i+1] = data[i]
    return self.device.send_output_report(self.send_buffer)

  def read(self):
    while 1 :
      if self.recvbuffer : 
        res=self.recvbuffer
        self.recvbuffer=None
        return res
      time.sleep(0.1)
     
  def recv_raw_data(self, data):
    self.recvbuffer = data 
    return None

  def init_buffer(self):
    self.send_buffer=[0xff] * self.bufsize
    self.send_buffer[0]=0x00
    return self.send_buffer

  def clear_buffer(self):
    self.write([0x41])
    return 

  def set_recieve_mode(self, mode=0):
    self.write([0x51, mode])
    return

  def recieve_ir(self):
    self.set_recieve_mode(0x01)
    self.read()
    while 1:
      self.write([0x50])
      res = self.read()
      if res[2] != 0:
        self.set_recieve_mode(0x00)
        return res

  def send_ir(self, data):
    data.insert(0, 0x60)
    self.write(data)
    return
