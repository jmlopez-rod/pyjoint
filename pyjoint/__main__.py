"""Command line use of pyjoint

To run pyjoint from the command line do the following:

    python -m pyjoint ...

Use the option --help for more information.

"""

import sys
import logging
import argparse
import textwrap
import pyjoint
from pyjoint.__version__ import VERSION
from pyjoint.core.error import FatalError


def parse_options():
    """Interpret the command line inputs and options. """
    desc = """
pyjoint computes the miter and tilt angles of polyhedron faces.

"""
    ver = "pyjoint %s" % VERSION
    epi = """

more info:
  http://jmlopez-rod.github.com/pyjoint

version:
  pyjoint %s

""" % VERSION
    raw = argparse.RawDescriptionHelpFormatter
    argp = argparse.ArgumentParser(formatter_class=raw, version=ver,
                                   description=textwrap.dedent(desc),
                                   epilog=textwrap.dedent(epi))
    argp.add_argument('inputfile', type=str,
                      help='input file to process')
    argp.add_argument('--debug', action='store_true', dest='debug',
                      help='printing logging messages to stderr')
    return argp.parse_args()


def main(arg):
    """Main routine. """
    logging.info("starting main routine")
    vertices, faces = pyjoint.read_data(arg.inputfile)
    print vertices
    print faces


def run():
    """Run pyjoint from the command line. """
    arg = parse_options()
    if arg.debug:
        logging.basicConfig(
            stream=sys.stderr,
            format='%(pathname)s:%(lineno)d: %(message)s',
            level=logging.DEBUG
        )
    try:
        main(arg)
    except FatalError as err:
        print err.to_json()


if __name__ == '__main__':
    run()
