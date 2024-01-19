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

"""sigcalc constants."""

from decimal import Decimal

from .quantity import Quantity

pi = Quantity(
    Decimal("3.1415926535897932384626433832795028841971"),
    constant=True,
)

e = Quantity(
    Decimal("2.7182818284590452353602874713526624977572"),
    constant=True,
)
