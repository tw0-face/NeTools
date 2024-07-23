# NeTools

NeTools is a project I started to be a network swiss army knife for linux, it uses scapt in the backend

# Features

- [x] Network scanner (MAC & OS detection)
- [x] MAC spoofing

# Demo 
![alt text](NeTools.gif)

# Installation

1. Install `nmap` with your system package manager
    - for Ubuntu/Debian `apt install nmap`
2. Clone the repo `git clone https://github.com/tw0-face/NeTools.git`
3. `cd NeTools`
4. `pip install -r requirements.txt`
5. `python net_tools.py -i $interface -r $scan_range` 
    - replace the interface and the range with yours, you can check your interface with `ifconfig`