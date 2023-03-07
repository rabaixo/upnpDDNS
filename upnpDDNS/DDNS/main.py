
# python packages
import argparse
import sys
import pkg_resources
import socket
import asyncio
import yaml
import logging

# package modules
from . import DDNS
from . import api_DDNS

# parse_args ------------------------------------------------------------------
def parse_args():
    """Argument parser function (see argparse_):
    .. _argparse: http://newcoder.io/api/part-4/
    """

    # general parser and info
    parser = argparse.ArgumentParser(
        prog="DDNS",
        description="Update the IP in the DynDNS server.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
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

    if not ddns:
        sys.exit("Access help by running: upnpDDNS -h ")


    if ddns_conf:
        with open(ddns_conf) as file:
            ddns_conf_dict = yaml.load(file, Loader=yaml.FullLoader)
    else:
        logging.warning("Please enter the path to the DDNS configuration file.")
        sys.exit("Please enter the path to the DDNS configuration file.")

    loop = asyncio.new_event_loop()
    loop.call_soon(DDNS.DDNS, ddns_conf_dict, api_DDNS.api_url(ddns_conf_dict), loop)
    loop.run_forever()


