import os
import socket

try:
    IPLOCAL= os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]

except:
    IPLOCAL = socket.gethostbyname(socket.gethostname())


# un argumento de entrada
ports_list = [
                {
                    "ExternalPort": 9898,
                    "Protocol": 'TCP',
                    "InternalPort": 80,
                    "InternalClient": IPLOCAL,
                    "Description":'HTTP server'
                },
                {
                    "ExternalPort": 1194,
                    "Protocol": 'UDP',
                    "InternalPort": 1194,
                    "InternalClient": IPLOCAL,
                    "Description": 'Vpn server'
                },
                {
                    "ExternalPort": 8989,
                    "Protocol": 'UDP',
                    "InternalPort": 22,
                    "InternalClient": IPLOCAL,
                    "Description": 'Vpn server'
                },

            ]