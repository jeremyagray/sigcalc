# ******************************************************************************
#
# sigcalc, significant figures calculations
#
# Copyright 2023 Jeremy A Gray <gray@flyquackswim.com>.
#
# All rights reserved.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# ******************************************************************************

"""sigcalc module initialization."""

from .quantity import Quantity
from .quantity import _least_significant_place
from .quantity import _most_significant_place
