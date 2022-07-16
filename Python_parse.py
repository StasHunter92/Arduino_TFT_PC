import serial
import json
import urllib.request
import time

pc_ip = "192.168.1.106"
pc_port = "8085"
json_file = "data.json"
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=0)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.5)
    data_arduino = arduino.readline()
    return data_arduino


while True:
    response = urllib.request.urlopen('http://' + pc_ip + ':' + pc_port + '/' + json_file)
    data = json.load(response)
    cpu_name = data['Children'][0]['Children'][1]['Text']
    cpu_temp = data['Children'][0]['Children'][1]['Children'][1]['Children'][1]['Value'].split(' ')[0]
    cpu_load = data['Children'][0]['Children'][1]['Children'][2]['Children'][0]['Value'].split(' ')[0]
    cpu_package = data['Children'][0]['Children'][1]['Children'][3]['Children'][0]['Value'].split(' ')[0]

    ram = data['Children'][0]['Children'][2]['Children'][1]['Children'][0]['Value']

    gpu_name = data['Children'][0]['Children'][3]['Text'].split('NVIDIA ')[2]
    gpu_temp = data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Value'].split(' ')[0]
    value = write_read(f'''{cpu_name}
  Power {cpu_package} W    
  Temp {cpu_temp} C    
  Load {cpu_load} %

 Ram load {ram}

 {gpu_name}
  Temp {gpu_temp} C   ''')
    time.sleep(1)
