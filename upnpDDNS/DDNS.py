import upnpclient


def DDNS():
    devices = upnpclient.discover()
    d = devices[0]
    IP = d.WANIPConn1.GetExternalIPAddress()
    print(IP)