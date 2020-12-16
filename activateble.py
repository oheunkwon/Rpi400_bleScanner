import subprocess
import serial
from time import *

uart_data = serial.Serial('/dev/ttyS0', 115200)

LENGTH_LCD = 16

sleep(1)

while True:
    read_line = uart_data.readline()
    mm = read_line.decode()
    # major_dec = int(mm[1:3], 16)
    # minor_dec = int(mm[5:9], 16)
    # print(major_dec, minor_dec)
    major_dec = int(mm[1:5], 16)
    minor_dec = int(mm[5:9], 16)
    print(major_dec, minor_dec)
    mm_dec = str(major_dec) + str(minor_dec)

    subprocess.run(['sudo hciconfig hci0 up'], shell=True, check=True)
    subprocess.run(['sudo hciconfig hci0 noscan'], shell=True, check=True)

    # os.popen('sudo hciconfig hci0 up')
    # os.popen('sudo hciconfig hci0 noscan')
    cmd_str1 = 'sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 '
    cmd_uuid = '4a 4e ce 60 7e b0 11 e4 b4 a9 08 00 20 0c 9a 66 '
    cmd_major1 = mm[1:3]+' '
    cmd_major2 = mm[3:5]+' '
    cmd_minor1 = mm[5:7]+' '
    cmd_minor2 = mm[7:9]+' '
    cmd_str2 = 'C8 00'
    subprocess.run([cmd_str1 + cmd_uuid + cmd_major1 + cmd_major2 + cmd_minor1 + cmd_minor2 + cmd_str2],
                   shell=True, check=True)
    subprocess.run(['sudo hcitool -i hci0 cmd 0x08 0x0006 A0 00 A0 00 03 00 00 00 00 00 00 00 00 07 00'],
                   shell=True, check=True)
    subprocess.run(['sudo hcitool -i hci0 cmd 0x08 0x000a 01'], shell=True, check=True)
    sleep(1)
