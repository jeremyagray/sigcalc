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

"""Quantity class for significant figure calculations."""

from decimal import Decimal
from decimal import getcontext


class Quantity:
    """A quantity for significant figure calculations."""

    def __init__(self, value, figures, constant=False):
        """Initialize a ``Quantity()``.

        Parameters
        ----------
        value : str
            Value of the quantity, to be converted to a ``Decimal``.
        figures : str
            Significant figures of the quantity, to be converted to a
            ``Decimal``.
        constant : boolean
            Set as constant (unlimited precision), or not.
        """
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
        Quantity
            A new ``Quantity`` equal to the rounded ``self``.
        """
        if self.constant:
            return Quantity(self.value, self.figures, self.constant)

        return Quantity(self._round(), self.figures, self.constant)

    # Exponential functions.

    def exp(self):
        """Calculate the base e exponential of a ``Quantity``.

        Uses the ``exp()`` function from ``decimal.Decimal`` for the
        exponential calculation and computes the significant figures
        from the significant figures of the input ``Quantity``.

        >>> from sigcalc import Quantity
        >>> a = Quantity("1", "3")
        >>> b = Quantity("0", "3")
        >>> a.exp()
        Quantity("2.718281828459045235360287471", "3")
        >>> b.exp()
        Quantity("1", "3")

        Returns
        -------
        Quantity
            A new ``Quantity`` with the computed exponential and
            significant figures and constant value from the input
            ``Quantity``.
        """
        return Quantity(self.value.exp(), self.figures, self.constant)

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
        Quantity
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
        Quantity
            A new ``Quantity`` with the computed natural logarithm,
            computed significant figures from the input and the size
            of the computed logarithm, and constant value from the
            input ``Quantity``.
        """
        x = Quantity(self.value.ln(), self.figures, self.constant)

        if abs(x.value) < 1:
            # Significant figures is only the mantissa.
            pass
        else:
            # Significant figures includes the abscissa digits as well.
            x.figures += x.value.adjusted() + 1

        return x

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
        Quantity
            A new ``Quantity`` with the computed base 10 logarithm,
            computed significant figures from the input and the size
            of the computed logarithm, and constant value from the
            input ``Quantity``.
        """
        x = Quantity(self.value.log10(), self.figures, self.constant)

        if abs(x.value) < 1:
            # Significant figures is only the mantissa.
            pass
        else:
            # Significant figures includes the abscissa digits as well.
            x.figures += x.value.adjusted() + 1

        return x

    # Trigonometric functions and inverses.

    def sin(self):  # dead: disable
        """Calculate the sine of a ``Quantity``."""
        return NotImplemented

    def asin(self):  # dead: disable
        """Calculate the inverse sine of a ``Quantity``."""
        return NotImplemented

    def cos(self):  # dead: disable
        """Calculate the cosine of a ``Quantity``."""
        return NotImplemented

    def acos(self):  # dead: disable
        """Calculate the inverse cosine of a ``Quantity``."""
        return NotImplemented

    def tan(self):  # dead: disable
        """Calculate the tangent of a ``Quantity``."""
        return NotImplemented

    def atan(self):  # dead: disable
        """Calculate the inverse tangent of a ``Quantity``."""
        return NotImplemented

    def csc(self):  # dead: disable
        """Calculate the cosecant of a ``Quantity``."""
        return NotImplemented

    def acsc(self):  # dead: disable
        """Calculate the inverse cosecant of a ``Quantity``."""
        return NotImplemented

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
