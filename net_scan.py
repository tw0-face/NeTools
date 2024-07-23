#!/usr/bin/env python3
import scapy.all as scapy
import nmap3
from mac_vendor_lookup import MacLookup
from prettytable import PrettyTable
import os
import argparse

CBLINK = '\33[5m'
CBLUE2 = '\33[94m'
CEND = '\033[0m'
CGREEN2 = '\33[92m'

x = PrettyTable()
print('\33[5m' + '\33[94m' + "[!] Updating Mac list..." + '\033[0m')
MacLookup().update_vendors()


def _default_command(self):
    """
    Returns the default nmap command
    that will be chained with all others
    eg nmap -oX -
    """
    if self.as_root:
        return self.default_command_privileged()
    return self.default_args.format(nmap=self.nmaptool, outarg="-oX")

nmap3.default_command = _default_command


def net_scanner(interface, scan_range):
    ans_list = scapy.arping(net=scan_range, iface=interface, verbose=False)[0]
    column_names = ["ID", "IP", "MAC", "OS", "Vendor"]
    id = []
    ip = []
    mac = []
    os_list = []
    vendor_list = []
    for element in ans_list:
        ip.append(element[1].psrc)
        mac.append(element[1].hwsrc)
    for n in range(len(ip)):
        id.append(str(n + 1))
        os_list.append(os_detect(ip[n]))
        vendor_list.append(vendor_detect(mac[n]))

    x.add_column(column_names[0], id)
    x.add_column(column_names[1], ip)
    x.add_column(column_names[2], mac)
    x.add_column(column_names[3], os_list)
    x.add_column(column_names[4], vendor_list)
    os.system('clear')
    print(x)
    print(CGREEN2 + "[+] Scan completed successfully" + CEND)


def os_detect(ip):
    try:
        nmap = nmap3.Nmap()
        os_results = nmap.nmap_os_detection(str(ip))[0]['osclass']['osfamily']
        return os_results
    except IndexError:
        return " --- "


def vendor_detect(mac):
    try:
        return MacLookup().lookup(str(mac))
    except KeyError:
        return " --- "


#net_scanner(interface, scan_range)
