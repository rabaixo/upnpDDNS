import requests
import sys
import upnpclient


def DDNS(router_ip, api_url, loop):
    """Update IP on DDNS server when IP changes

    Args:
        router_ip (str): External IP of router
        api_url (str): DDNS API URL
        loop (asyncio.unix_eventsasyncio.unix_events): Check ip every 5 min
    """
    d = None
    devices = upnpclient.discover()
    if len(devices) == 0:
        sys.exit("There is no router with upnp enabled.")

    for device in devices:
        d = device
        break
    if d:
        IP = d.WANIPConn1.GetExternalIPAddress()
        if router_ip != IP["NewExternalIPAddress"]:
            try:
                resp = requests.get(api_url)
                print(resp.content)
                router_ip = IP["NewExternalIPAddress"]
            except Exception as err:
                print(err)

        print(IP)
        loop.call_later(300, DDNS, router_ip, api_url, loop)
    else:
        loop.stop()
        sys.exit("There is no router with upnp enabled.")

