import upnpclient
import sys

def upnp(ports_list):
    """Open router ports with upnp

    Args:
        ports_list (list): dictionaries of the ports information  to open with upnp
    """
    devices = upnpclient.discover()
    try:
        d = devices[0]
    except:
        sys.exit("There is no router with upnp enabled.")

    for port in ports_list:
        resp = d.WANIPConn1.AddPortMapping(
                        NewRemoteHost = '',
                        NewExternalPort = port["ExternalPort"],
                        NewProtocol = port["Protocol"],
                        NewInternalPort = port["InternalClient"],
                        NewInternalClient = port["InternalClient"],
                        NewEnabled='1',
                        NewPortMappingDescription= port["InternalClient"],
                        NewLeaseDuration=10000
                    )
    print(resp)



