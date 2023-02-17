import upnpclient
import sys

def upnp(ports_list):
    """Open router ports with upnp

    Args:
        ports_list (list): dictionaries of the ports information  to open with upnp
    """
    d = None
    devices = upnpclient.discover()
    if len(devices) == 0:
        sys.exit("There is no router with upnp enabled.")

    for device in devices:
        d = device
        break
    if d
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
        sys.exit("There is no router with upnp enabled an IP.")




