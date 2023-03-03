import requests
import sys
import upnpclient
import logging

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
        logging.warning("There is no router with upnp enabled.")
        sys.exit("There is no router with upnp enabled.")

    for device in devices:
        if hasattr(device, "WANIPConn1"):
            d = device
            break
    if d:
        IP = d.WANIPConn1.GetExternalIPAddress()
        if router_ip != IP["NewExternalIPAddress"]:
            try:
                resp = requests.get(api_url)
                logging.info(resp.content)
                router_ip = IP["NewExternalIPAddress"]
            except Exception as err:
                logging.error(err)

        print(f"Current IP: {IP['NewExternalIPAddress']}")
        logging.info(f"Current IP: {IP['NewExternalIPAddress']}")
        loop.call_later(120, DDNS, router_ip, api_url, loop)
    else:
        loop.stop()
        logging.warning("There is no router with upnp enabled.")
        sys.exit("There is no router with upnp enabled.")

