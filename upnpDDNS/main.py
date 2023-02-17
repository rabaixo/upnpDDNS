
# python packages
import argparse
import sys
import pkg_resources
import socket
import asyncio
import yaml

# package modules
from . import upnp as up
from . import DDNS
from . import ports_list
from . import api_DDNS

# parse_args ------------------------------------------------------------------
def parse_args():
    """Argument parser function (see argparse_):
    .. _argparse: http://newcoder.io/api/part-4/
    """

    # general parser and info
    parser = argparse.ArgumentParser(
        prog="upnpDDNS",
        description="Update the IP in the DynDNS server and open the necessary ports.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-u",
        "--upnp",
        action="store_true",
        help="Open ports with upnp.",
    )

    parser.add_argument(
        "-uc",
        "--upnp_conf",
        nargs="?",
        default=None,
        help="Upnp configuration file.",
    )

    parser.add_argument(
        "-d",
        "--DDNS",
        action="store_true",
        help="Update the IP in DDNS server.",
    )

    parser.add_argument(
        "-dc",
        "--DDNS_conf",
        nargs="?",
        default=None,
        help="DDNS configration file.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="package version.",
        required=False,
    )

    args = parser.parse_args()

    return args
# --------------------------------------------------------------------------- #
# main ------------------------------------------------------------------------
def main():
    """Read data using argparse_ package and execute the
    :func:`scengenref.scengenref.scengenref`.
    .. _argparse: http://newcoder.io/api/part-4/
    """
    # =========================================================================
    # Load input
    # -------------------------------------------------------------------------
    args = parse_args()
    upnp = args.upnp
    upnp_conf = args.upnp_conf
    ddns = args.DDNS
    ddns_conf = args.DDNS_conf

    version = args.version


    if version:
        try:
            package_info = pkg_resources.get_distribution("upnpDDNS")
        except pkg_resources.DistributionNotFound:
            sys.exit(1)
        print(package_info.version)
        sys.exit(0)

    if not upnp and not ddns:
        sys.exit("Access help by running: upnpDDNS -h ")

    if upnp_conf:
        with open(upnp_conf) as file:
            upnp_conf_dict = yaml.load(file, Loader=yaml.FullLoader)
        for item in upnp_conf_dict:
            item["InternalClient"] = ports_list.IPLOCAL
    else:
        upnp_conf_dict = ports_list


    if upnp:
        up.upnp(upnp_conf_dict)
    if ddns:
        if ddns_conf:
            with open(ddns_conf) as file:
                ddns_conf_dict = yaml.load(file, Loader=yaml.FullLoader)
        else:
            sys.exit("Please enter the path to the DDNS configuration file.")
        router_ip = socket.gethostbyname(ddns_conf_dict["zone"])
        loop = asyncio.new_event_loop()
        loop.call_soon(DDNS.DDNS, router_ip, api_DDNS.api_url(ddns_conf_dict), loop)
        loop.run_forever()


