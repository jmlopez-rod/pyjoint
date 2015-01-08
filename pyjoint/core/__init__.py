"""
Utility functions.

"""

import json
import logging
from pyjoint.core.error import FatalError


def read_data(fname):
    """Reads a json file to obtain the vertices and faces of the
    polyhedron. """
    logging.info('read_data({0})'.format(fname))
    try:
        json_fp = open(fname, 'r')
        data = json.load(json_fp)
    except Exception as err:
        msg = 'Unable to read_data from {0}'.format(fname)
        raise FatalError(msg, str(err))
    if not isinstance(data, dict):
        msg = 'Bad data in {0}'.format(fname)
        details = 'Should be a dictionary'
        raise FatalError(msg, details)
    try:
        return data['vertices'], data['faces']
    except Exception as err:
        msg = "Unable to extract the `vertices` and `faces`"
        raise FatalError(msg, repr(err))
