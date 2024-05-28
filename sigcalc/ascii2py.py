# ******************************************************************************
#
# sigcalc, significant figures calculations
#
# Copyright 2023-2024 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""Convert NIST constants ASCII data to python."""

import re
import sys


def _load(fn):
    """Load a file and return the constants data only.

    Parameters
    ----------
    fn : str
        Path to file containing data

    Returns
    -------
    constants :
        Constant data.
    """
    constants = []

    with open(fn, "r") as f:
        line = f.readline()
        while not re.match(r"^-+$", line):
            line = f.readline()

        for line in f.readlines():
            parts = re.split(r"\s{2,}", line.strip("\n"))
            constant = re.sub(r"[ -/]+", "_", parts[0])
            value = re.sub(r"( |\.\.\.)", "", parts[1])
            uncertainty = re.sub(r" ", "", parts[2])
            unit = parts[3]
            constants.append(
                {
                    "name": constant,
                    "value": value,
                    "uncertainty": uncertainty,
                    "unit": unit,
                }
            )

    return constants


def convert(fn):
    """Convert NIST constants ASCII data to python.

    Parameters
    ----------
    fn : str
        Path to file containing data

    Returns
    -------
    int :
        Zero for success, error code otherwise.
    """
    constants = _load(fn)
    code = ""
    imports = ""
    docs = ""

    for c in constants:
        if c["uncertainty"] == "(exact)":
            code += rf'''{c["name"]} = Quantity(
    Decimal("{c["value"]}"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

'''
        else:
            code += rf'''{c["name"]} = Quantity.from_decimal(
    "{c["value"]}",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

'''

        imports += f'from .physical_constants import {c["name"]}\n'
        docs += f'   sigcalc.{c["name"]}\n'

    print(code)
    print(imports)
    print(docs)


if __name__ == "__main__":
    sys.exit(convert(sys.argv[1]))
