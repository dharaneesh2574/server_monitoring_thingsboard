

import psutil
import requests
import json
import time

THINGSBOARD_URL = "http://demo.thingsboard.io/api/v1/u0yfq5s7z9uh7v3xrczd/telemetry"
ACCESS_TOKEN = "u0yfq5s7z9uh7v3xrczd"

def get_system_utilization():
    # CPU utilization
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory utilization
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Disk usage
    disk_usage = psutil.disk_usage('/')

    # Network usage
    net_io = psutil.net_io_counters()
    bytes_sent_mb = net_io.bytes_sent / (1024 * 1024)  
    bytes_received_mb = net_io.bytes_recv / (1024 * 1024)  

    utilization = {
        'CPU Usage (%)': cpu_usage,
        'Memory Usage (%)': memory_usage,
        'Disk Usage (%)': disk_usage,  
        'Bytes Sent (MB)': bytes_sent_mb,
        'Bytes Received (MB)': bytes_received_mb
    }

    return utilization

def send_telemetry(data):
    headers = {'Content-Type': 'application/json'}
   
    try:
        response = requests.post(THINGSBOARD_URL, headers=headers, data=json.dumps(data))
       
        if response.status_code == 200:
            print("Data sent successfully!")
            print("=====================")
        
        else:
            print(f"Error sending data: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        utilization_data = get_system_utilization()
        send_telemetry(utilization_data)
       
        time.sleep(10)
