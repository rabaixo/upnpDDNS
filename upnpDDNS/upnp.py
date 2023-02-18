import upnpclient
import sys
import logging

def upnp(ports_list):
    """Open router ports with upnp

    Args:
        ports_list (list): dictionaries of the ports information  to open with upnp
    """
    d = None
    devices = upnpclient.discover()
    if len(devices) == 0:
        logging.warning("There is no router with upnp enabled.")
        sys.exit("There is no router with upnp enabled.")
    print(devices)
    for device in devices:
        if hasattr(device, "WANIPConn1"):
            d = device
            break
    if d:
        for port in ports_list:
            resp = d.WANIPConn1.AddPortMapping(
                            NewRemoteHost = '',
                            NewExternalPort = port["ExternalPort"],
                            NewProtocol = port["Protocol"],
                            NewInternalPort = port["InternalPort"],
                            NewInternalClient = port["InternalClient"],
                            NewEnabled='1',
                            NewPortMappingDescription= port["Description"],
                            NewLeaseDuration=10000
                        )
        print(resp)
    else:
        logging.warning("There is no router with upnp enabled an IP.")
        sys.exit("There is no router with upnp enabled an IP.")




