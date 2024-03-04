import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"  
redirect_ip = "127.0.0.1"
blocked_sites = ["www.example.com"] 

while True:
    # Define working hours (24-hour format)
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)  
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)  

    if start_time <= dt.now() <= end_time:
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in blocked_sites:
                if site in content:
                    pass
                else:
                    file.write(redirect_ip + " " + site + "\n")
        print("Websites blocked during working hours.")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in blocked_sites):
                    file.write(line)
            file.truncate()
        print("Websites unblocked outside working hours.")

    time.sleep(5)  