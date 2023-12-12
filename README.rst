.. *****************************************************************************
..
.. sigcalc, significant figures calculations
..
.. Copyright 2023 Jeremy A Gray <gray@flyquackswim.com>.
..
.. All rights reserved.
..
.. SPDX-License-Identifier: GPL-3.0-or-later
..
.. *****************************************************************************

sigcalc
=======

Sigcalc is a python module for expressing quantities with significant
figures and performing calculations on quantities based on the rules
of significant figures.

..
   .. image:: https://badge.fury.io/py/sigcalc.svg
      :target: https://badge.fury.io/py/sigcalc
      :alt: PyPI Version
   .. image:: https://readthedocs.org/projects/sigcalc/badge/?version=latest
      :target: https://sigcalc.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

Installation
------------

Install sigcalc with pip::

  pip install sigcalc

or with poetry::

  poetry add sigcalc

``sigcalc`` depends on the internal ``decimal`` module for arithmetic
and ``mpmath`` (https://mpmath.org/) for transcendental and other
functions.

Usage
-----

Import the ``Quantity`` class:

>>> from sigcalc import Quantity

Create ``Quantity`` objects as necessary:

>>> a = Quantity("3.14", "3")
>>> b = Quantity("2.72", "3")

Arithmetic for ``Quantity`` objects is implemented on the usual magic
methods:

>>> a + b
Quantity("5.86", "3")
>>> a - b
Quantity("0.42", "2")
>>> a * b
Quantity("8.5408", "3")
>>> a / b
Quantity("1.154411764705882352941176471", "3")
>>> abs(a)
Quantity("3.14", "3")
>>> -a
Quantity("-3.14", "3")
>>> +a
Quantity("3.14", "3")

Note that ``__floordiv__`` is not implemented as it is not useful for
significant figures calculations.

>>> a // b
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for //: 'Quantity' and 'Quantity'

Rounding and output are tied together.  Typically, rounding is
unnecessary except for output but is available:

>>> a = Quantity("3.14", "2")
>>> a.round()
Quantity("3.1", "2")
>>> a
Quantity("3.14", "2")

Rounding constants has no effect:

>>> a = Quantity("3.145", "3", constant=True)
>>> a.round()
Quantity("3.145", "28", constant=True)

String output uses the underlying ``decimal`` module's string output
after rounding to the correct significant figures:

>>> from decimal import ROUND_HALF_EVEN
>>> a = Quantity("3.145", "3")
>>> b = Quantity("3.145", "3", rounding=ROUND_HALF_EVEN)
>>> str(a)
'3.15'
>>> str(b)
'3.14'

The rounding mode should be one of the modes available in ``decimal``.

Likewise with formatting:

>>> format(a, ".2e")
'3.15e+0'
>>> format(b, ".2e")
'3.14e+0'

The transcendental and exponential functions will be implemented as
wrappers around the appropriate functions from ``decimal`` and
``mpmath``, calculating results based on the ``value`` of a
``Quantity`` with the correct significant figures.

References
----------

``sigcalc`` implements significant figures calculations as commonly
described in high school and undergraduate chemistry and physics
textbooks, examples of which may be found at:

1. `Significant Figures at Wikipedia <https://en.wikipedia.org/wiki/Significant_figures>`_
2. `Significance Arithmetic at Wikipedia <https://en.wikipedia.org/wiki/Significance_arithmetic>`_
3. Myers, R.T.; Tocci, S.; Oldham, K.B., Holt Chemistry, Holt, Rinehart and Winston: 2006.

Calculating with significant figures is not a substitute for
repetition of measurements and proper statistical analysis.

Copyright and License
---------------------

SPDX-License-Identifier: `GPL-3.0-or-later <https://spdx.org/licenses/GPL-3.0-or-later.html>`_

sigcalc, significant figures calculations

Copyright (C) 2023 `Jeremy A Gray <gray@flyquackswim.com>`_.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.

Author
------

`Jeremy A Gray <gray@flyquackswim.com>`_
