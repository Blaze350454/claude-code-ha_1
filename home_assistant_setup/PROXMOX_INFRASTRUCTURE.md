# Proxmox Infrastructure Documentation

## Proxmox Host
- **Node Name:** proxmox
- **IP Address:** 192.168.2.100
- **Network:** 192.168.2.0/24
- **Bridge:** vmbr0
- **Physical NIC:** eno1 (e4:54:e8:71:77:1f)
- **CPU Usage:** 0.66%
- **Memory:** 5.66 GiB / 31.13 GiB (6 cores)

## Storage
| Name | Type | Status | Total | Used | Available | Usage % |
|------|------|--------|-------|------|-----------|---------|
| local | dir | active | 96.4 GB | 14.6 GB | 76.8 GB | 15.21% |
| local-lvm | lvmthin | active | 794 GB | 38 GB | 756 GB | 4.79% |

## Running Containers (LXC)

### VMID 100 - esphome
- **Type:** LXC Container
- **Status:** Running
- **Purpose:** ESPHome (ESP32/ESP8266 firmware management)

### VMID 102 - mosquitto
- **Type:** LXC Container
- **Status:** Running
- **Purpose:** MQTT Broker (message bus for IoT devices)

### VMID 104 - vscode-server
- **Type:** LXC Container
- **Status:** Running
- **Purpose:** VS Code Server (web-based code editing)

### VMID 105 - backup-server
- **Type:** LXC Container
- **Status:** Stopped
- **Purpose:** Backup server

## Running Virtual Machines (VM)

### VMID 101 - home-assistant ⭐
- **Type:** Virtual Machine (KVM/QEMU)
- **Status:** Running
- **CPU:** 4 cores (host passthrough)
- **Memory:** 8192 MB (8 GB)
- **Boot Disk:** 64 GB (local-lvm:vm-101-disk-0)
- **IP Address:** 192.168.2.151
- **Network:** virtio NIC (BC:24:11:B2:67:A7) on vmbr0
- **Machine Type:** Q35
- **OS Type:** Linux 2.6+ kernel
- **Guest Agent:** Enabled
- **UUID:** 64645df9-2eb7-4530-9e0a-494de5e15f6e

**USB Passthrough Devices:**
- **usb0:** 0951:1666 (Kingston - likely USB Zigbee/Z-Wave stick)
- **usb1:** 0b05:190e (ASUS - likely Bluetooth adapter)

**Purpose:** Ubuntu VM running Docker containers

**Installation Type:** Home Assistant Container (NOT Home Assistant OS)
- **OS:** Ubuntu Linux
- **Container 1:** Home Assistant (Docker)
- **Container 2:** Matter Server (Docker)
- **No Supervisor:** Cannot use add-ons (different from HAOS)
- **GitHub Integration:** Must be done via Ubuntu host with Git CLI

## Network Configuration

### Main Bridge (vmbr0)
- **IP:** 192.168.2.100/24
- **Connected to:** eno1 (physical NIC)
- **Purpose:** Main network bridge for all VMs/containers

### Docker Network
- **Interface:** docker0
- **IP:** 172.17.0.1/16
- **Purpose:** Internal Docker networking on Proxmox host

### Virtual Interfaces
- `veth102i0` - Container 102 (mosquitto)
- `veth100i0` - Container 100 (esphome)
- `veth104i0` - Container 104 (vscode-server)
- `tap101i0` - VM 101 (home-assistant)

All containers/VMs are bridged to vmbr0, meaning they're on the same 192.168.2.0/24 network.

## Architecture Summary

```
Proxmox Host (192.168.2.100)
├── vmbr0 Bridge (192.168.2.0/24)
│   ├── VM 101: Home Assistant (192.168.2.151) [8GB RAM, 64GB disk]
│   ├── LXC 100: ESPHome
│   ├── LXC 102: Mosquitto MQTT
│   ├── LXC 104: VS Code Server
│   └── LXC 105: Backup Server (stopped)
└── docker0 (172.17.0.1/16)
    └── Docker containers (if any)
```

## Home Assistant Installation Type

Based on the VM setup, you're likely running **Home Assistant OS** (HAOS), which is:
- A full operating system optimized for HA
- Includes Supervisor (for add-ons)
- Easier for backups and updates
- Perfect for GitHub integration via add-ons

## GitHub Integration Options

Given your setup, best options are:

1. **Git Pull Add-on** (Recommended)
   - Official HA add-on
   - Easy to install via Supervisor
   - Auto-pull from GitHub

2. **SSH & Git Add-on**
   - Manual control
   - Can push/pull from HA

3. **VS Code Server Add-on**
   - You already have vscode-server LXC
   - Could use HA's built-in VS Code add-on instead
   - Git integration built-in

## Next Steps
1. Get VM config: `qm config 101`
2. Choose GitHub integration method
3. Set up repository and workflow

---

**Note:** Awaiting VM config to complete documentation
