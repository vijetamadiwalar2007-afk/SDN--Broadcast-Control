# Broadcast Traffic Control using POX SDN

## Project Description
This project implements Broadcast Traffic Control using POX SDN Controller. 
The controller detects broadcast traffic, limits excessive broadcast, performs MAC learning and installs flow rules.

## Tools Used
- POX Controller
- Mininet
- OpenFlow
- Ubuntu Virtual Machine

## Network Topology
- 2 Switches (s1, s2)
- 4 Hosts (h1, h2, h3, h4)

## Features
- Broadcast Detection
- Broadcast Traffic Control
- MAC Learning
- Flow Rule Installation
- Selective Forwarding

## How to Run

### Start Controller
cd ~/pox
python3 pox.py log.level --DEBUG misc.pox_broadcast_controller

### Start Mininet
cd ~/broadcast-pox
sudo python3 custom_topo.py

### Test
pingall
h1 ping -b 10.0.0.255 -i 0.01

## Output
Broadcast traffic detected and controlled successfully.

## Author
Vijeta Madiwalar
