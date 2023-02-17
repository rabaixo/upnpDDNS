import upnpclient
import requests
import sys


def DDNS(router_ip, api_url, loop):
    """Update IP on DDNS server when IP changes

    Args:
        router_ip (str): External IP of router
        api_url (str): DDNS API URL
        loop (asyncio.unix_eventsasyncio.unix_events): Check ip every 5 min
    """
    devices = upnpclient.discover()
    try:
        d = devices[0]

    except:
        sys.exit("There is no router with upnp enabled.")

    IP = d.WANIPConn1.GetExternalIPAddress()
    if router_ip == IP["NewExternalIPAddress"]:
        try:
            resp = requests.get(api_url)
            print(resp.content)
        except Exception as err:
            print(err)
    else:
        loop.call_later(300, DDNS, router_ip, api_url, loop)
    print(IP)