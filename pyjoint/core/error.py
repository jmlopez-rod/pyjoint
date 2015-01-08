"""
The error module contains the FatalError exception. This exception
should be thrown if you do not except to catch it for reasons other
than to terminate the program in a graceful manner.

"""

import json
from inspect import currentframe, getframeinfo


class FatalError(Exception):
    """Exception to be raised in case of a fatal error. """

    def __init__(self, msg, details):
        Exception.__init__(self)
        self.error = msg
        self.details = details
        self.location = '{0}:{1}'
        cfr = currentframe()
        fname = getframeinfo(cfr.f_back).filename
        lineno = cfr.f_back.f_lineno
        self.location = self.location.format(fname, lineno)

    def __str__(self):
        return self.error

    def to_json(self):
        """Return a json string with a message. """
        err = {
            'error': self.error,
            'reason': self.details,
            'location': self.location
        }
        return json.dumps(err, indent=2, separators=(',', ': '))
