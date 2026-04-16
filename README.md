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
# SDN Broadcast Control

This project implements broadcast traffic control using SDN.

## Features

- Broadcast detection
- Broadcast control
- MAC learning
- Flow rule installation

## Topology

4 Hosts
2 Switches

## Output

Screenshots below
<img width="852" height="471" alt="image" src="https://github.com/user-attachments/assets/46e66ffe-c1ac-4659-ae31-035e749408b1" />
<img width="891" height="159" alt="image" src="https://github.com/user-attachments/assets/8c46b037-5c86-43f7-8e4a-416abe58c814" />
<img width="808" height="61" alt="image" src="https://github.com/user-attachments/assets/b6ea4a2b-e802-4991-b2e5-400ad3e5986a" />



## Author
Vijeta Madiwalar
