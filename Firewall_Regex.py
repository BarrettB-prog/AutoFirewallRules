import requests, csv, subprocess, re

#regex pattern for validating IPv4 addresses. Ensures no RCE
ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist_aggressive.csv")

#remove existing firewall rule named 'BadIP' if it exists
subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule", "name=BadIP"], shell=False)

#read CSV data while skipping commented lines (#)
mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.text.splitlines()))

for row in mycsv:
    if len(row) > 1:
        ip = row[1].strip()  # Rem

        # Validate IP using regex
        if ip_pattern.match(ip):
            print(f"Blocking IP: {ip}")
            subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule", f"name=BadIP", "dir=out", "action=block", f"remoteip={ip}"],
            shell=False)
        else:
            print(f"Skipping invalid entry: {ip}")
