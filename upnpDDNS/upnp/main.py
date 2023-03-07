
# python packages
import argparse
import sys
import pkg_resources
import asyncio
import yaml
import logging


# package modules
from . import upnp as up
from . import ports_list

# parse_args ------------------------------------------------------------------
def parse_args():
    """Argument parser function (see argparse_):
    .. _argparse: http://newcoder.io/api/part-4/
    """

    # general parser and info
    parser = argparse.ArgumentParser(
        prog="upnp",
        description="Open the necessary ports.",
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

    version = args.version


    if version:
        try:
            package_info = pkg_resources.get_distribution("upnpDDNS")
        except pkg_resources.DistributionNotFound:
            sys.exit(1)
        print(package_info.version)
        sys.exit(0)

    if not upnp:
        sys.exit("Access help by running: upnpDDNS -h ")

    if upnp_conf:
        with open(upnp_conf) as file:
            upnp_conf_dict = yaml.load(file, Loader=yaml.FullLoader)
    else:
        upnp_conf_dict = ports_list


    loop = asyncio.new_event_loop()
    loop.call_soon(up.upnp, upnp_conf_dict, loop)
    loop.run_forever()


