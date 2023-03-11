import upnpclient
import sys
import logging
import os
import socket
import datetime

def upnp(ports_list, loop):
    """Open router ports with upnp

    Args:
        ports_list (list): dictionaries of the ports information  to open with upnp
    """
    d = None
    devices = upnpclient.discover()
    if len(devices) == 0:
        logging.warning(f"{datetime.datetime.now()}: There is no router with upnp enabled.")
    print(devices)
    for device in devices:
        if hasattr(device, "WANIPConn1"):
            d = device
            break
    if d:
        IPLOCAL = get_IPLOCAL()
        for port in ports_list:
            resp = d.WANIPConn1.AddPortMapping(
                            NewRemoteHost = '',
                            NewExternalPort = port["ExternalPort"],
                            NewProtocol = port["Protocol"],
                            NewInternalPort = port["InternalPort"],
                            NewInternalClient = IPLOCAL,
                            NewEnabled='1',
                            NewPortMappingDescription= port["Description"],
                            NewLeaseDuration=port["NewLeaseDuration"]
                        )
        print(resp)
        print(IPLOCAL)
        loop.call_later(120, upnp,  ports_list, loop)
    else:
        loop.stop()
        logging.warning(f"{datetime.datetime.now()}: There is no router with upnp enabled an IP.")
        loop.call_later(120, upnp,  ports_list, loop)





def get_IPLOCAL():
    try:
        IPLOCAL= os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]

    except:
        IPLOCAL = socket.gethostbyname(socket.gethostname())

    return IPLOCAL