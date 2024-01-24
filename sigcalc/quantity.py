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

"""Quantity class for significant figure calculations."""

from decimal import Decimal
from decimal import getcontext
from warnings import warn

import mpmath


class Quantity:
    """A quantity for significant figure calculations."""

    def __init__(self, value, figures=None, constant=False):
        """Initialize a ``Quantity()``.

        Parameters
        ----------
        value : str
            Value of the quantity, to be converted to a ``Decimal``.
        figures : str
            Significant figures of the quantity, to be converted to a
            ``Decimal``.
        constant : bool
            Set as constant (unlimited precision), or not.
        """
        if not constant and figures is None:
            raise TypeError("`figures` should not be None for non-constants")
        elif constant:
            figures = Decimal("1")

        self.value = Decimal(str(value))

        getcontext().prec = max(
            getcontext().prec, int(figures), len(self.value.as_tuple().digits)
        )

        self.reported = self.value
        if not constant:
            self.figures = Decimal(str(figures))
        else:
            self.figures = getcontext().prec
        self._constant = constant

    # Output operations.
    def __repr__(self):
        """Represent a ``Quantity``."""
        rep = f'Quantity("{self.value}", "{self.figures}"'

        if self.constant:
            rep += f", constant={self.constant}"

        return rep + ")"

    def __format__(self, specifier):
        """Format a ``Quantity`` object.

        Format a ``Quantity`` object, rounding to significant figures
        first and then passing any format specifier through to
        ``Decimal().__format__()`` for formatting.
        """
        return format(self._round(), specifier)

    def __str__(self):
        """Stringify a ``Quantity`` object.

        Stringify a ``Quantity`` object, rounding to significant
        figures first and then using ``Decimal().__str__()`` for
        stringification.
        """
        return str(self._round())

    # Unary operations.
    def __neg__(self):
        """Negate a ``Quantity()`` object."""
        return Quantity(-self.value, self.figures, self.constant)

    def __pos__(self):
        """Return a ``Quantity()`` object."""
        return Quantity(self.value, self.figures, self.constant)

    def __abs__(self):
        """Calculate the magnitude of a ``Quantity()`` object."""
        return Quantity(abs(self.value), self.figures, self.constant)

    # Comparisons.
    def __lt__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        if isinstance(other, Quantity) and self._round() < other._round():
            return True

        return False

    def __le__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other):
        """Determine equality of two ``Quantity()`` objects."""
        if (
            isinstance(other, Quantity)
            and self._round() == other._round()
            and self.figures == other.figures
        ):
            return True

        return False

    def __ne__(self, other):
        """Determine the inequality of two ``Quantity()`` objects."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        return not self.__lt__(other) and self.__ne__(other)

    def __ge__(self, other):
        """Determine the ordering of two ``Quantity()`` objects."""
        return not self.__lt__(other) or self.__eq__(other)

    # Arithmetic operations.
    def __add__(self, other):
        """Add two ``Quantity()`` objects."""
        if isinstance(other, Quantity):
            value = self.value + other.value

            if self.constant and other.constant:
                return Quantity(value, getcontext().prec, constant=True)
            elif self.constant and not other.constant:
                least = other.value.adjusted() - other.figures + 1
            elif other.constant and not self.constant:
                least = self.value.adjusted() - self.figures + 1
            else:
                least = max(
                    self.value.adjusted() - self.figures + 1,
                    other.value.adjusted() - other.figures + 1,
                )

            most = value.adjusted()

            return Quantity(value, max(most - least + 1, 1))

        return NotImplemented

    def __sub__(self, other):
        """Subtract two ``Quantity()`` objects."""
        return self + -other

    def __mul__(self, other):
        """Multiply two ``Quantity`` objects."""
        if isinstance(other, Quantity):
            if self.constant and other.constant:
                return Quantity(
                    self.value * other.value, getcontext().prec, constant=True
                )
            elif self.constant and not other.constant:
                return Quantity(self.value * other.value, other.figures)
            elif other.constant and not self.constant:
                return Quantity(self.value * other.value, self.figures)
            else:
                return Quantity(
                    self.value * other.value, min(self.figures, other.figures)
                )

        return NotImplemented

    def __truediv__(self, other):
        """Divide two ``Quantity`` objects."""
        if isinstance(other, Quantity):
            if self.constant and other.constant:
                return Quantity(
                    self.value / other.value, getcontext().prec, constant=True
                )
            elif self.constant and not other.constant:
                return Quantity(self.value / other.value, other.figures)
            elif other.constant and not self.constant:
                return Quantity(self.value / other.value, self.figures)
            else:
                return Quantity(
                    self.value / other.value, min(self.figures, other.figures)
                )

        return NotImplemented

    def __pow__(self, other, modulo=None):
        """Calculate a power of a ``Quantity``.

        Calculate a power of a ``Quantity`` and compute the correct
        number of significant figures.  The ``__pow__`` from
        ``decimal.Decimal`` is used to calculate the value of the
        power.

        Significant figures follows "significance in, significance
        out" rule since this is (naively) multiplication.  This makes
        the assumption that the exponent will usually be an integer
        anyway and that the precision will be controlled by ``self``.

        >>> from sigcalc import Quantity
        >>> a = Quantity("2", "3")
        >>> b = Quantity("2", "3")
        >>> a**b
        Quantity("4", "3")
        >>> b = Quantity("2", "2")
        >>> a**b
        Quantity("4", "3")
        >>> a = Quantity("2", "2")
        >>> b = Quantity("2", "3")
        >>> a**b
        Quantity("4", "2")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed power and significant
            figures and constant value from the input ``Quantity``.
        """
        value = pow(self.value, other.value, modulo)

        if self.constant:
            return Quantity(
                value,
                constant=True,
            )

        return Quantity(
            value,
            self.figures,
        )

    @property
    def constant(self):
        """Mark a ``Quantity`` as a constant with unlimited precision."""
        return self._constant

    @constant.setter
    def constant(self, value):
        """Set a ``Quantity`` object's ``constant`` property.

        Set a ``Quantity`` object's ``constant`` property to value, if
        boolean.
        """
        if isinstance(value, bool):
            self._constant = value

    def _round(self):
        """Round a ``Quantity`` object ``value`` to significant figures.

        Round a ``Quantity`` object ``value`` to significant figures
        using the context rounding mode, returning a ``Decimal``.
        Return ``self.value`` unrounded if ``self.constant`` is
        ``True``.

        Returns
        -------
        Decimal
            The rounded ``value`` of the ``Quantity``.
        """
        if self.constant:
            return self.value

        place = self.value.adjusted() - self.figures + Decimal("1")
        return self.value.quantize(Decimal(f"1e{place}"))

    def round(self):  # dead: disable
        """Round a ``Quantity`` object to significant figures.

        Round a ``Quantity`` object to significant figures using the
        context rounding mode, returning a new ``Quantity`` with only
        the rounded significant figures.  Return a new ``Quantity``
        equal to ``self`` unrounded if ``self.constant`` is ``True``.

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` equal to the rounded ``self``.
        """
        if self.constant:
            return Quantity(self.value, self.figures, self.constant)

        value = self._round()
        figures = self.figures
        if value.adjusted() > self.value.adjusted():
            figures += 1

        return Quantity(value, figures, self.constant)

    # Exponential functions.

    def exp(self):
        """Calculate the base e exponential of a ``Quantity``.

        Uses the ``exp()`` function from ``decimal.Decimal`` for the
        exponential calculation and computes the significant figures
        from the significant figures of the input ``Quantity``.

        >>> from sigcalc import Quantity
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> a = Quantity("1", "3")
        >>> b = Quantity("0", "3")
        >>> a.exp()
        Quantity("2.718281828459045235360287471", "2")
        >>> import warnings
        >>> warnings.simplefilter("error")
        >>> b.exp()  # warn on ambiguous input, but return an answer
        Traceback (most recent call last):
        ...
        RuntimeWarning: ambiguous zero valued ``Quantity``:  Quantity("0", "3")
        >>> warnings.simplefilter("ignore")
        >>> b.exp()
        Quantity("1", "0")
        >>> warnings.simplefilter("error")
        >>> c = Quantity("10", "2")
        >>> c.exp()  # warn on insufficient precision, but return an answer
        Traceback (most recent call last):
        ...
        RuntimeWarning: insufficient input precision in Quantity("10", "2"): the 2 abscissa digits consume the available precision (2)
        >>> warnings.simplefilter("ignore")
        >>> c.exp()
        Quantity("22026.46579480671651695790065", "0")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed exponential and
            significant figures and constant value from the input
            ``Quantity``.

        Raises
        ------
        RuntimeWarning
            If ``self.value`` is zero, there are no significant
            figures.  Raise and return ``Quantity("1", "0")``.  Also
            raise if there are fewer significant figures than abscissa
            digits since the abscissa digits are placeholders from the
            logarithm.
        """  # noqa: E501
        # Warn on zero.
        if self.value == Decimal("0"):
            warn(f"ambiguous zero valued ``Quantity``:  {repr(self)}", RuntimeWarning)
            return Quantity("1", "0")

        value = self.value.exp()

        # Default precision for no abscissa.
        figures = self.figures

        # Constants.
        if self.constant:
            return Quantity(
                value,
                constant=self.constant,
            )

        # Chop abscissa places since they are not significant in the logarithm.
        if abs(self.value) >= Decimal("1"):
            figures = self.figures - (self.value.adjusted() + Decimal("1"))

        if figures < Decimal("1"):
            warn(
                f"insufficient input precision in {repr(self)}: "
                f"the {self.value.adjusted() + Decimal('1')} "
                f"abscissa digits consume the available precision ({self.figures})",
                RuntimeWarning,
            )
            figures = Decimal("0")

        # No abscissa.
        return Quantity(
            value,
            figures,
        )

    def exp10(self):  # dead: disable
        """Calculate the base 10 exponential of a ``Quantity``.

        Uses the ``__pow__()`` function from ``decimal.Decimal`` for
        the exponential calculation and computes the significant
        figures from the significant figures of the input
        ``Quantity``.

        >>> from sigcalc import Quantity
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> a = Quantity("1", "3")
        >>> b = Quantity("0", "3")
        >>> a.exp10()
        Quantity("10", "2")
        >>> import warnings
        >>> warnings.simplefilter("error")
        >>> b.exp10()  # warn on ambiguous input, but return an answer
        Traceback (most recent call last):
        ...
        RuntimeWarning: ambiguous zero valued ``Quantity``:  Quantity("0", "3")
        >>> warnings.simplefilter("ignore")
        >>> b.exp10()
        Quantity("1", "0")
        >>> warnings.simplefilter("error")
        >>> c = Quantity("10", "2")
        >>> c.exp10()  # warn on insufficient precision, but return an answer
        Traceback (most recent call last):
        ...
        RuntimeWarning: insufficient input precision in Quantity("10", "2"): the 2 abscissa digits consume the available precision (2)
        >>> warnings.simplefilter("ignore")
        >>> c.exp10()
        Quantity("10000000000", "0")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed exponential and
            significant figures and constant value from the input
            ``Quantity``.

        Raises
        ------
        RuntimeWarning
            If ``self.value`` is zero, there are no significant
            figures.  Raise and return ``Quantity("1", "0")``.  Also
            raise if there are fewer significant figures than abscissa
            digits since the abscissa digits are placeholders from the
            logarithm.
        """  # noqa: E501
        # Warn on zero.
        if self.value == Decimal("0"):
            warn(f"ambiguous zero valued ``Quantity``:  {repr(self)}", RuntimeWarning)
            return Quantity("1", "0")

        value = pow(Decimal("10"), self.value)

        # Default precision for no abscissa.
        figures = self.figures

        # Constants.
        if self.constant:
            return Quantity(
                value,
                constant=self.constant,
            )

        # Chop abscissa places since they are not significant in the logarithm.
        if abs(self.value) >= Decimal("1"):
            figures = self.figures - (self.value.adjusted() + Decimal("1"))

        if figures < Decimal("1"):
            warn(
                f"insufficient input precision in {repr(self)}: "
                f"the {self.value.adjusted() + Decimal('1')} "
                f"abscissa digits consume the available precision ({self.figures})",
                RuntimeWarning,
            )
            figures = Decimal("0")

        # No abscissa.
        return Quantity(
            value,
            figures,
        )

    def sqrt(self):
        """Calculate the square root of a ``Quantity``.

        Uses the ``sqrt()`` function from ``decimal.Decimal`` for the
        square root calculation and computes the significant figures
        from the significant figures of the input ``Quantity``.

        >>> from sigcalc import Quantity
        >>> a = Quantity("4", "3")
        >>> b = Quantity("9", "4")
        >>> a.sqrt()
        Quantity("2", "3")
        >>> b.sqrt()
        Quantity("3", "4")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed square root and
            significant figures and constant value from the input
            ``Quantity``.
        """
        return Quantity(self.value.sqrt(), self.figures, self.constant)

    # Logarithmic functions.

    def ln(self):
        """Calculate the natural logarithm of a ``Quantity``.

        Uses the ``ln()`` function from ``decimal.Decimal`` for the
        natural logarithm calculation and computes the significant
        figures from the significant figures of the input
        ``Quantity``.

        >>> from sigcalc import Quantity
        >>> a = Quantity("2", "3")
        >>> b = Quantity("3", "3")
        >>> a.ln()
        Quantity("0.6931471805599453094172321215", "3")
        >>> b.ln()
        Quantity("1.098612288668109691395245237", "4")

        Beware the usual problems with computing logarithms, as raised
        by the ``decimal`` module.  Precision is gained if the
        absolute value of the result is greater than or equal to one
        since the significant figures of the input determine the
        significant decimal places of the output.

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed natural logarithm,
            computed significant figures from the input and the size
            of the computed logarithm, and constant value from the
            input ``Quantity``.
        """
        value = self.value.ln()
        figures = self.figures

        if abs(value) >= Decimal("1"):
            # Significant figures includes the abscissa digits.
            figures += value.adjusted() + Decimal("1")

        if self.constant:
            return Quantity(value, constant=self.constant)

        return Quantity(value, figures)

    def log10(self):
        """Calculate the base 10 logarithm of a ``Quantity``.

        Uses the ``log10()`` function from ``decimal.Decimal`` for the
        base 10 logarithm calculation and computes the significant
        figures from the significant figures of the input
        ``Quantity``.

        >>> from sigcalc import Quantity
        >>> a = Quantity("100", "3")
        >>> a.log10()
        Quantity("2", "4")
        >>> b = Quantity("0.5", "3")
        >>> b.log10()
        Quantity("-0.3010299956639811952137388947", "3")

        Beware the usual problems with computing logarithms, as raised
        by the ``decimal`` module.  Precision is gained if the
        absolute value of the result is greater than or equal to one
        since the significant figures of the input determine the
        significant decimal places of the output.

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed base 10 logarithm,
            computed significant figures from the input and the size
            of the computed logarithm, and constant value from the
            input ``Quantity``.
        """
        value = self.value.log10()
        figures = self.figures

        if abs(value) >= Decimal("1"):
            # Significant figures includes the abscissa digits.
            figures += value.adjusted() + Decimal("1")

        if self.constant:
            return Quantity(value, constant=self.constant)

        return Quantity(value, figures)

    # Trigonometric functions and inverses.

    def sin(self):
        """Calculate the sine of a ``Quantity``.

        Uses ``mpmath.sin()`` to calculate the sine and computes the
        significant figures from the significant figures of the input
        ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> import mpmath
        >>> from sigcalc import Quantity
        >>> from sigcalc import pi
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> zero = Quantity("0", "3")
        >>> ninety = pi / Quantity("2", "3")
        >>> one_eighty = pi * Quantity("1", "3")
        >>> two_seventy = pi * Quantity("3", "3") / Quantity("2", "3")
        >>> three_sixty = pi * Quantity("2", "3")
        >>> zero.sin()
        Quantity("0.0", "3")
        >>> ninety.sin()
        Quantity("1.0", "3")
        >>> mpmath.almosteq(mpmath.mpmathify(one_eighty.sin().value), mpmath.mpmathify(Decimal("0")), 1e-25)
        True
        >>> two_seventy.sin()
        Quantity("-1.0", "3")
        >>> mpmath.almosteq(mpmath.mpmathify(three_sixty.sin().value), mpmath.mpmathify(Decimal("0")), 1e-25)
        True

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed sine and significant
            figures and constant value from the input ``Quantity``.
        """  # noqa: E501
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.sin(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def asin(self):
        """Calculate the inverse sine of a ``Quantity``.

        Uses ``mpmath.asin()`` to calculate the sine and computes the
        significant figures from the significant figures of the input
        ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> from sigcalc import Quantity
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> a = Quantity("0", "3")
        >>> b = Quantity("1", "3")
        >>> c = Quantity("-1", "3")
        >>> a.asin()
        Quantity("0.0", "3")
        >>> b.asin()
        Quantity("1.570796326794896619231321692", "3")
        >>> c.asin()
        Quantity("-1.570796326794896619231321692", "3")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed inverse sine and
            significant figures and constant value from the input
            ``Quantity``.
        """
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.asin(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def cos(self):
        """Calculate the cosine of a ``Quantity``.

        Uses ``mpmath.cos()`` to calculate the cosine and computes the
        significant figures from the significant figures of the input
        ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> from sigcalc import Quantity
        >>> from sigcalc import pi
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> zero = Quantity("0", "3")
        >>> ninety = pi / Quantity("2", "3")
        >>> one_eighty = pi * Quantity("1", "3")
        >>> two_seventy = pi * Quantity("3", "3") / Quantity("2", "3")
        >>> three_sixty = pi * Quantity("2", "3")
        >>> zero.cos()
        Quantity("1.0", "3")
        >>> mpmath.almosteq(mpmath.mpmathify(ninety.cos().value), mpmath.mpmathify(Decimal("0")), 1e-25)
        True
        >>> one_eighty.cos()
        Quantity("-1.0", "3")
        >>> mpmath.almosteq(mpmath.mpmathify(two_seventy.cos().value), mpmath.mpmathify(Decimal("0")), 1e-25)
        True
        >>> three_sixty.cos()
        Quantity("1.0", "3")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed cosine and
            significant figures and constant value from the input
            ``Quantity``.
        """  # noqa: E501
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.cos(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def acos(self):
        """Calculate the inverse cosine of a ``Quantity``.

        Uses ``mpmath.acos()`` to calculate the cosine and computes the
        significant figures from the significant figures of the input
        ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> from sigcalc import Quantity
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> a = Quantity("0", "3")
        >>> b = Quantity("1", "3")
        >>> c = Quantity("-1", "3")
        >>> a.acos()
        Quantity("1.570796326794896619231321692", "3")
        >>> b.acos()
        Quantity("0.0", "3")
        >>> c.acos()
        Quantity("3.141592653589793238462643383", "3")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed inverse cosine and
            significant figures and constant value from the input
            ``Quantity``.
        """
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.acos(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def tan(self):
        """Calculate the tangent of a ``Quantity``.

        Uses ``mpmath.tan()`` to calculate the tangent and computes the
        significant figures from the significant figures of the input
        ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> from sigcalc import Quantity
        >>> from sigcalc import pi
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> zero = Quantity("0", "3")
        >>> forty_five = pi / Quantity("4", "3")
        >>> three_fifteen = pi * Quantity("7", "3") / Quantity("4", "3")
        >>> zero.tan()
        Quantity("0.0", "3")
        >>> forty_five.tan()
        Quantity("1.0", "3")
        >>> mpmath.almosteq(mpmath.mpmathify(three_fifteen.tan().value), mpmath.mpmathify(Decimal("-1")), 1e-25)
        True

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed tangent and
            significant figures and constant value from the input
            ``Quantity``.
        """  # noqa: E501
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.tan(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def atan(self):
        """Calculate the inverse tangent of a ``Quantity``.

        Uses ``mpmath.atan()`` to calculate the tangent and computes the
        significant figures from the significant figures of the input
        ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> from sigcalc import Quantity
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> a = Quantity("0", "3")
        >>> b = Quantity("1", "3")
        >>> c = Quantity("-1", "3")
        >>> a.atan()
        Quantity("0.0", "3")
        >>> b.atan()
        Quantity("0.7853981633974483096156608458", "3")
        >>> c.atan()
        Quantity("-0.7853981633974483096156608458", "3")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed inverse tangent and
            significant figures and constant value from the input
            ``Quantity``.
        """
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.atan(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def csc(self):
        """Calculate the cosecant of a ``Quantity``.

        Uses ``mpmath.csc()`` to calculate the cosecant and computes
        the significant figures from the significant figures of the
        input ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> import mpmath
        >>> from sigcalc import Quantity
        >>> from sigcalc import pi
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> ninety = pi / Quantity("2", "3")
        >>> two_seventy = pi * Quantity("3", "3") / Quantity("2", "3")
        >>> ninety.csc()
        Quantity("1.0", "3")
        >>> two_seventy.csc()
        Quantity("-1.0", "3")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed cosecant and
            significant figures and constant value from the input
            ``Quantity``.
        """
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.csc(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def acsc(self):
        """Calculate the inverse cosecant of a ``Quantity``.

        Uses ``mpmath.acsc()`` to calculate the cosecant and computes
        the significant figures from the significant figures of the
        input ``Quantity``.  This wrapper to manages the precision of
        ``mpmath`` to compute at the required precision of the current
        ``decimal`` context.

        >>> from sigcalc import Quantity
        >>> from decimal import Decimal
        >>> from decimal import getcontext
        >>> getcontext().prec = 28
        >>> b = Quantity("1", "3")
        >>> c = Quantity("-1", "3")
        >>> b.acsc()
        Quantity("1.570796326794896619231321692", "3")
        >>> c.acsc()
        Quantity("-1.570796326794896619231321692", "3")

        Returns
        -------
        sigcalc.Quantity
            A new ``Quantity`` with the computed inverse cosecant and
            significant figures and constant value from the input
            ``Quantity``.
        """
        mpmath.mp.dps = getcontext().prec
        return Quantity(
            Decimal(
                mpmath.nstr(mpmath.acsc(mpmath.mpmathify(self.value)), mpmath.mp.dps)
            ),
            self.figures,
            self.constant,
        )

    def sec(self):  # dead: disable
        """Calculate the secant of a ``Quantity``."""
        return NotImplemented

    def asec(self):  # dead: disable
        """Calculate the inverse secant of a ``Quantity``."""
        return NotImplemented

    def cot(self):  # dead: disable
        """Calculate the cotangent of a ``Quantity``."""
        return NotImplemented

    def acot(self):  # dead: disable
        """Calculate the inverse cotangent of a ``Quantity``."""
        return NotImplemented

    # Hyperbolic functions and inverses.

    def sinh(self):  # dead: disable
        """Calculate the hyperbolic sine of a ``Quantity``."""
        return NotImplemented

    def asinh(self):  # dead: disable
        """Calculate the inverse hyperbolic sine of a ``Quantity``."""
        return NotImplemented

    def cosh(self):  # dead: disable
        """Calculate the hyperbolic cosine of a ``Quantity``."""
        return NotImplemented

    def acosh(self):  # dead: disable
        """Calculate the inverse hyperbolic cosine of a ``Quantity``."""
        return NotImplemented

    def tanh(self):  # dead: disable
        """Calculate the hyperbolic tangent of a ``Quantity``."""
        return NotImplemented

    def atanh(self):  # dead: disable
        """Calculate the inverse tangent of a ``Quantity``."""
        return NotImplemented

    def csch(self):  # dead: disable
        """Calculate the hyperbolic cosecant of a ``Quantity``."""
        return NotImplemented

    def acsch(self):  # dead: disable
        """Calculate the inverse hyperbolic cosecant of a ``Quantity``."""
        return NotImplemented

    def sech(self):  # dead: disable
        """Calculate the hyperbolic secant of a ``Quantity``."""
        return NotImplemented

    def asech(self):  # dead: disable
        """Calculate the inverse hyperbolic secant of a ``Quantity``."""
        return NotImplemented

    def coth(self):  # dead: disable
        """Calculate the hyperbolic cotangent of a ``Quantity``."""
        return NotImplemented

    def acoth(self):  # dead: disable
        """Calculate the inverse hyperbolic cotangent of a ``Quantity``."""
        return NotImplemented
