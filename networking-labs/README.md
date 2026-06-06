# Corporate LAN Network Topology & Subnetting Lab

## 📋 Overview
This module demonstrates the architectural design and configuration of a resilient, secure corporate network environment. It highlights core networking concepts required for both enterprise data center environments and modern hybrid-cloud network operations, including IP subnetting, VLAN segmentation, and inter-VLAN routing.



## 🏗️ Architecture Design
The lab models a standard enterprise branch network split into distinct security zones using Virtual Local Area Networks (VLANs). This prevents broadcast storms and enforces security boundaries between department traffic.

### Network Specifications:
* **Core Network Address Space:** `192.168.10.0 /24`
* **Routing Protocol:** Inter-VLAN Routing (Router-on-a-Stick configuration)
* **Gateway Device:** Cisco ISR 4300 Series Router
* **Switching Infrastructure:** Cisco Catalyst 2960 Layer 2 Switch

---

## 🔢 Subnetting & IP Addressing Schema
The primary `/24` block has been subnetworked to provide optimized host allocation while minimizing address waste:

| Department Space | VLAN ID | Subnet Mask | Default Gateway | Usable IP Range | Purpose |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Management** | VLAN 10 | `255.255.255.192` (/26) | `192.168.10.1` | `192.168.10.2` - `192.168.10.62` | Network switches, PDUs, console servers |
| **Data Center / Ops** | VLAN 20 | `255.255.255.192` (/26) | `192.168.10.65` | `192.168.10.66` - `192.168.10.126` | Local bare-metal servers & storage arrays |
| **Corporate Workstations** | VLAN 30 | `255.255.255.128` (/25) | `192.168.10.129` | `192.168.10.130` - `192.168.10.254` | End-user devices and client hardware |

---

## 🛠️ Core Device Configurations (Cisco IOS CLI)

### 1. Layer 2 Switch VLAN Implementation
These commands segment the physical switch ports into their respective logical broadcast domains:

```cisco
! Create VLANs
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name Management
Switch(config-vlan)# vlan 20
Switch(config-vlan)# name Data_Center_Ops
Switch(config-vlan)# vlan 30
Switch(config-vlan)# name Corporate_Users
Switch(config-vlan)# exit

! Assign Ports to Corporate User VLAN
Switch(config)# interface range fastEthernet 0/1 - 24
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 30
Switch(config-if-range)# exit

! Configure 802.1Q Trunk Port linking to Core Router
Switch(config)# interface gigabitEthernet 0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# description Uplink_to_Core_Router

Router# configure terminal
Router(config)# interface gigabitEthernet 0/0
Router(config-if)# no shutdown
Router(config-if)# exit

! Subinterface for Management (VLAN 10)
Router(config)# interface gigabitEthernet 0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.192

! Subinterface for Data Center Ops (VLAN 20)
Router(config)# interface gigabitEthernet 0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.10.65 255.255.255.192

! Subinterface for Corporate Workstations (VLAN 30)
Router(config)# interface gigabitEthernet 0/0.30
Router(config-subif)# encapsulation dot1Q 30
Router(config-subif)# ip address 192.168.10.129 255.255.255.128
Router(config-subif)# end
Router# copy running-config startup-config