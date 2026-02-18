import psutil
whitelistPorts = [5355,3389,3242]

for c in psutil.net_connections():
    if c.laddr:
        port = c.laddr.port
        pid = c.pid

        if pid:
            process = psutil.Process(pid)

            if port not in whitelistPorts:
                print("It is a Suspicious Port :", port)