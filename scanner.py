import blescan_func
import sys
import time
import log
import bluetooth._bluetooth as bluez

hostname = {
    'f1:94:ec:97:9a:b0': '01',
    'd0:43:23:cc:3f:34': '03',
    'e2:a2:99:ba:6e:4c': '04',
    'f1:89:38:a0:a1:eb': '05',
    'c5:e7:58:10:e6:42': '15',
    'd9:8f:89:8a:77:05': '16'
}


beacon_dict = {}
beacon_na_dict = {}

MAX_SCAN = 100

dev_id = 0
search_num = 0

host_list = []
host_list_str = []
host_list_na = []
host_list_na_str = []
host_name_dec = 0


class BleScanner:
    def scan(self, sock):
        global host_name_dec, host_list, host_list_str, host_list_na
        returnedList = blescan_func.parse_events(sock, MAX_SCAN)
        for beacon in returnedList:
            try:
                arr_beacon = beacon.split(',')
                arr_beacon[4] = int(arr_beacon[4]) - 256
                arr_beacon[5] = int(arr_beacon[5]) - 256
                host_name = 'NA'
                beacon_na_dict['hostname'] = host_name
                beacon_na_dict['bssid'] = arr_beacon[0]
                beacon_na_dict['uuid'] = arr_beacon[1]
                beacon_na_dict['major'] = arr_beacon[2]
                beacon_na_dict['minor'] = arr_beacon[3]
                beacon_na_dict['tx_power'] = arr_beacon[4]
                beacon_na_dict['rssi'] = arr_beacon[5]
                host_list_na.append(dict(beacon_na_dict))
            except:
                log.get_log("ScanLogger").error("exception...")


def main():
    try:
        sock = bluez.hci_open_dev(dev_id)
        log.get_log("ScanLogger").info("1.ble thread started")
    except:
        log.get_log("ScanLogger").error("error accessing bluetooth device...")
        sys.exit(1)

    blescan_func.hci_le_set_scan_parameters(sock)
    blescan_func.hci_enable_le_scan(sock)

    ble = BleScanner()
    while True:
        global search_num, host_list, host_list_na, host_list_str, host_list_na_str
        search_num = search_num + 1
        str_search_start = "-----" + str(
            search_num) + "번째 SCAN [hostname: BSSID, UUID, MAJOR, MINOR, TX power, RSSI]-----"

        ble.scan(sock)
        host_list_na_sorted = sorted(host_list_na, key=(lambda beacon_na_data: beacon_na_data['bssid']))

        log.get_log("ScanLogger").info(str_search_start)
        for i in range(len(host_list_na)):
            host_list_na_str = list({host_list_na['bssid']: host_list_na for host_list_na in host_list_na_sorted}.values())

        for i in range(len(host_list_na_str)):

            host_list_na_values = list(host_list_na_str[i].values())
            log.get_log("ScanLogger").info(host_list_na_values)

        host_list.clear()
        host_list_na.clear()
        time.sleep(1)


if __name__ == '__main__':
    main()


