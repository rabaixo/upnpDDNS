
# python packages
import argparse
import sys
import pkg_resources

# package modules
from . import upnp as up
from . import DDNS

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
        "-d",
        "--DDNS",
        action="store_true",
        help="Update the IP in DDNS server.",
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
    ddns = args.DDNS
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

    if upnp:
        up.upnp()
    if ddns:
        pass





if __name__ == "__main__":
    main()

# import asyncio

# def hello_world(loop):
#     """A callback to print 'Hello World' and stop the event loop"""
#     print('Hello World')
#     loop.call_later(1, hello_world,  loop)
#     #loop.stop()

# loop = asyncio.new_event_loop()

# # Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)

# # Blocking call interrupted by loop.stop()
# try:
#     loop.run_forever()
# finally:
#     loop.close()

# import pdb;pdb.set_trace()