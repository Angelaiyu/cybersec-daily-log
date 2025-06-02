import subprocess

ips = ["8.8.8.8", "114.114.114.114", "192.168.1.1"]

for ip in ips:
    print(f"Pinging {ip}...")
    result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    if "TTL=" in result.stdout:
        print(f"{ip} 存活")
    else:
        print(f"{ip} 不可达")
