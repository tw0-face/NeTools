import argparse
import net_scan as ntscan
import attacks as atk


parser = argparse.ArgumentParser()
parser.add_argument("-i", dest="interface", help="ENTER the network interface to scan (e.g. eth0)")
parser.add_argument("-r", dest="range", help="ENTER the range of IPs to scan (e.g. 192.168.1.0/24)")
args = parser.parse_args()

interface = args.interface
scan_range = args.range

print('\33[5m' + '\33[94m' + "[!] Your network is being scanned..." + '\033[0m')

ntscan.net_scanner(interface, scan_range)

target_id = int(input("Select target by id >> "))
#target_data = ntscan.x.get_string(start=target_id-1, end=target_id, fields=["IP"])
target_data = ntscan.x.get_string()
parsed_data =  table_list = [[item.strip() for item in line.split('|') if item] for line in target_data.strip().split('\n') if '+-' not in line]
target_ip = parsed_data[target_id][1]
target_mac= parsed_data[target_id][2]
atk.mac_change(interface, target_mac)

