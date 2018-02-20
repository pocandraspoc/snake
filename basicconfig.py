"""
Basic configuration holder objects
https://github.com/kdart/pycopia/blob/master/core/pycopia/basicconfig.py
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import sys, os
import warnings

if sys.version_info.major == 3:
	def execfile(fn, glbl, loc):
		exec(open(fn).read(),
			glbl,
			loc)
else: #Python 2
	execfile == execfile
		pass