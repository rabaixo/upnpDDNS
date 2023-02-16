import upnpclient
import ports_list

def upnp():
    devices = upnpclient.discover()
    d = devices[0]

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



