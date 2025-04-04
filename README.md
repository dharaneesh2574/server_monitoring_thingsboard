# System Monitoring and Telemetry Submission

A Python script that monitors system resources (CPU, memory, disk, and network usage) and sends the data to ThingsBoard IoT platform at regular intervals.

## Features

- Real-time monitoring of system resources:
  - CPU utilization percentage
  - Memory usage percentage
  - Disk usage percentage
  - Network bytes sent/received (in MB)
- Periodic data submission to ThingsBoard IoT platform
- Error handling and status logging

## Prerequisites

- Python 3.x
- Required Python packages:
  - psutil
  - requests

## Installation

1. Clone this repository or download the script
2. Install the required packages:

```bash
pip install psutil requests

