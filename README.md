# SDN Broadcast Traffic Control using POX

Course: Computer Networks

Student Name: VIJETA MADIWALAR

Controller: POX (OpenFlow v1.0)

Topology: Multi‑Switch, 4 Hosts

---

# Problem Statement

This project implements an SDN‑based Broadcast Traffic Control system using Mininet and the POX OpenFlow controller. The controller detects excessive broadcast traffic and prevents broadcast storms by dynamically installing flow rules.

The project demonstrates:

• Controller–Switch interaction using OpenFlow
• Broadcast traffic detection
• Broadcast storm prevention
• MAC learning and selective forwarding
• Flow rule installation

---

# SDN Behaviors Demonstrated

| Behavior             | Description                           |
| -------------------- | ------------------------------------- |
| Broadcast Detection  | Detects broadcast packets in network  |
| Broadcast Control    | Limits excessive broadcast traffic    |
| MAC Learning         | Learns host MAC addresses dynamically |
| Selective Forwarding | Sends packets only to required ports  |
| Flow Installation    | Controller installs rules dynamically |

---

# Network Topology

h1 ---- s1 ---- s2 ---- h3
|        |
h2       h4

## Topology Explanation

• 4 Hosts (h1, h2, h3, h4)
• 2 Switches (s1, s2)
• Remote POX Controller
• Switches connected to controller
• Broadcast traffic monitored centrally

---

# Behavior Evaluation

Broadcast traffic is generated using broadcast ping.

The controller:

• Detects broadcast packets
• Counts broadcast traffic
• Blocks excessive broadcast
• Installs flow rules

This prevents broadcast storm and improves network performance.

---

# Controller Logic

The controller listens for PacketIn events from switches.

When packet arrives:

1. Controller learns MAC address
2. Detects broadcast packet
3. Checks broadcast frequency
4. Applies control rule

Logic implemented:

If Broadcast Traffic > Limit
→ Block Broadcast

Otherwise
→ Selective Forwarding

---

# Match–Action Mechanism

Match Conditions:

• Broadcast MAC address
• Source MAC address
• Destination MAC address

Actions:

• Drop packet
• Forward packet
• Install flow rule

---

# Flow Rules

Broadcast Rule

Match: Broadcast Traffic
Action: Limit / Block

MAC Learning Rule

Match: Known Destination
Action: Forward to specific port

Default Rule

Unknown traffic forwarded to controller

---

# Setup & Installation

## Step 1 — Install Dependencies

sudo apt update
sudo apt install git python3‑pip mininet openvswitch‑switch -y

---

## Step 2 — Clone POX

cd ~
git clone [https://github.com/noxrepo/pox.git](https://github.com/noxrepo/pox.git)

---

# How to Run

## Terminal 1 — Start Controller

cd ~/pox
python3 pox.py log.level --DEBUG misc.pox_broadcast_controller

---

## Terminal 2 — Start Mininet

cd ~/broadcast‑pox
sudo python3 custom_topo.py

---

# Test Scenarios

## Scenario 1 — Basic Connectivity

pingall

Expected:

0% Packet loss

---

## Scenario 2 — Broadcast Traffic

h1 ping -b 10.0.0.255

Expected:

Broadcast detected

---

## Scenario 3 — Broadcast Storm

h1 ping -b 10.0.0.255 -i 0.01

Expected:

Controller blocks broadcast traffic

---

# Performance Analysis

Broadcast Control: Successful
Packet Loss (Broadcast): Controlled
Latency: Low

---

# Proof of Execution

Screenshots folder contains:

• Controller Output
• Ping Results
• Broadcast Detection
• Flow Installation

---

# Repository Structure

broadcast‑pox/
├── custom_topo.py
├── pox_broadcast_controller.py
├── README.md
└── screenshots/

---

# Validation

• Broadcast detected correctly
• Controller installed rules
• Network performance improved
• Packet forwarding working

---

# Conclusion

This project demonstrates Broadcast Traffic Control using SDN and POX controller.
Broadcast storms are detected and controlled using centralized SDN logic.
The controller dynamically installs flow rules to manage network traffic.

---



---

# Languages

Python — 100%

---

#Output Screenshoots


Terminal-1

<img width="852" height="471" alt="image" src="https://github.com/user-attachments/assets/46e66ffe-c1ac-4659-ae31-035e749408b1" />

Terminal -2

<img width="891" height="159" alt="image" src="https://github.com/user-attachments/assets/8c46b037-5c86-43f7-8e4a-416abe58c814" />

<img width="808" height="61" alt="image" src="https://github.com/user-attachments/assets/b6ea4a2b-e802-4991-b2e5-400ad3e5986a" />



