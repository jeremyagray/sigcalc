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

alpha_particle_electron_mass_ratio = Quantity.from_decimal(
    "7294.29954171",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_mass = Quantity.from_decimal(
    "6.6446573450e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_mass_energy_equivalent = Quantity.from_decimal(
    "5.9719201997e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "3727.3794118",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_mass_in_u = Quantity.from_decimal(
    "4.001506179129",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_molar_mass = Quantity.from_decimal(
    "4.0015061833e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_proton_mass_ratio = Quantity.from_decimal(
    "3.972599690252",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_relative_atomic_mass = Quantity.from_decimal(
    "4.001506179129",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

alpha_particle_rms_charge_radius = Quantity.from_decimal(
    "1.6785e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Angstrom_star = Quantity.from_decimal(
    "1.00001495e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_constant = Quantity.from_decimal(
    "1.66053906892e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_constant_energy_equivalent = Quantity.from_decimal(
    "1.49241808768e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_constant_energy_equivalent_in_MeV = Quantity.from_decimal(
    "931.49410372",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_electron_volt_relationship = Quantity.from_decimal(
    "9.3149410372e8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_hartree_relationship = Quantity.from_decimal(
    "3.4231776922e7",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_hertz_relationship = Quantity.from_decimal(
    "2.25234272185e23",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_inverse_meter_relationship = Quantity.from_decimal(
    "7.5130066209e14",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_joule_relationship = Quantity.from_decimal(
    "1.49241808768e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_kelvin_relationship = Quantity.from_decimal(
    "1.08095402067e13",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_mass_unit_kilogram_relationship = Quantity.from_decimal(
    "1.66053906892e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_1st_hyperpolarizability = Quantity.from_decimal(
    "3.2063612996e-53",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_2nd_hyperpolarizability = Quantity.from_decimal(
    "6.2353799735e-65",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_action = Quantity(
    Decimal("1.054571817e-34"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_charge = Quantity(
    Decimal("1.602176634e-19"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_charge_density = Quantity.from_decimal(
    "1.08120238677e12",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_current = Quantity.from_decimal(
    "6.6236182375082e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_electric_dipole_mom_ = Quantity.from_decimal(
    "8.4783536198e-30",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_electric_field = Quantity.from_decimal(
    "5.14220675112e11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_electric_field_gradient = Quantity.from_decimal(
    "9.7173624424e21",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_electric_polarizability = Quantity.from_decimal(
    "1.64877727212e-41",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_electric_potential = Quantity.from_decimal(
    "27.211386245981",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_electric_quadrupole_mom_ = Quantity.from_decimal(
    "4.4865515185e-40",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_energy = Quantity.from_decimal(
    "4.3597447222060e-18",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_force = Quantity.from_decimal(
    "8.2387235038e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_length = Quantity.from_decimal(
    "5.29177210544e-11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_mag_dipole_mom_ = Quantity.from_decimal(
    "1.85480201315e-23",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_mag_flux_density = Quantity.from_decimal(
    "2.35051757077e5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_magnetizability = Quantity.from_decimal(
    "7.8910365794e-29",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_mass = Quantity.from_decimal(
    "9.1093837139e-31",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_momentum = Quantity.from_decimal(
    "1.99285191545e-24",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_permittivity = Quantity.from_decimal(
    "1.11265005620e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_time = Quantity.from_decimal(
    "2.4188843265864e-17",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

atomic_unit_of_velocity = Quantity.from_decimal(
    "2.18769126216e6",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Avogadro_constant = Quantity(
    Decimal("6.02214076e23"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Bohr_magneton = Quantity.from_decimal(
    "9.2740100657e-24",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Bohr_magneton_in_eV_T = Quantity.from_decimal(
    "5.7883817982e-5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Bohr_magneton_in_Hz_T = Quantity.from_decimal(
    "1.39962449171e10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Bohr_magneton_in_inverse_meter_per_tesla = Quantity.from_decimal(
    "46.686447719",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Bohr_magneton_in_K_T = Quantity.from_decimal(
    "0.67171381472",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Bohr_radius = Quantity.from_decimal(
    "5.29177210544e-11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Boltzmann_constant = Quantity(
    Decimal("1.380649e-23"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Boltzmann_constant_in_eV_K = Quantity(
    Decimal("8.617333262e-5"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Boltzmann_constant_in_Hz_K = Quantity(
    Decimal("2.083661912e10"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Boltzmann_constant_in_inverse_meter_per_kelvin = Quantity(
    Decimal("69.50348004"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

characteristic_impedance_of_vacuum = Quantity.from_decimal(
    "376.730313412",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

classical_electron_radius = Quantity.from_decimal(
    "2.8179403205e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Compton_wavelength = Quantity.from_decimal(
    "2.42631023538e-12",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conductance_quantum = Quantity(
    Decimal("7.748091729e-5"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_ampere_90 = Quantity(
    Decimal("1.00000008887"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_coulomb_90 = Quantity(
    Decimal("1.00000008887"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_farad_90 = Quantity(
    Decimal("0.99999998220"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_henry_90 = Quantity(
    Decimal("1.00000001779"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_Josephson_constant = Quantity(
    Decimal("483597.9e9"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_ohm_90 = Quantity(
    Decimal("1.00000001779"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_volt_90 = Quantity(
    Decimal("1.00000010666"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_von_Klitzing_constant = Quantity(
    Decimal("25812.807"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

conventional_value_of_watt_90 = Quantity(
    Decimal("1.00000019553"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Copper_x_unit = Quantity.from_decimal(
    "1.00207697e-13",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_electron_mag_mom_ratio = Quantity.from_decimal(
    "-4.664345550e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_electron_mass_ratio = Quantity.from_decimal(
    "3670.482967655",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_g_factor = Quantity.from_decimal(
    "0.8574382335",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mag_mom_ = Quantity.from_decimal(
    "4.330735087e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "4.669754568e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "0.8574382335",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mass = Quantity.from_decimal(
    "3.3435837768e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mass_energy_equivalent = Quantity.from_decimal(
    "3.00506323491e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "1875.61294500",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_mass_in_u = Quantity.from_decimal(
    "2.013553212544",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_molar_mass = Quantity.from_decimal(
    "2.01355321466e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_neutron_mag_mom_ratio = Quantity.from_decimal(
    "-0.44820652",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_proton_mag_mom_ratio = Quantity.from_decimal(
    "0.30701220930",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_proton_mass_ratio = Quantity.from_decimal(
    "1.9990075012699",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_relative_atomic_mass = Quantity.from_decimal(
    "2.013553212544",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

deuteron_rms_charge_radius = Quantity.from_decimal(
    "2.12778e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_charge_to_mass_quotient = Quantity.from_decimal(
    "-1.75882000838e11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_deuteron_mag_mom_ratio = Quantity.from_decimal(
    "-2143.9234921",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_deuteron_mass_ratio = Quantity.from_decimal(
    "2.724437107629e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_g_factor = Quantity.from_decimal(
    "-2.00231930436092",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_gyromag_ratio = Quantity.from_decimal(
    "1.76085962784e11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_gyromag_ratio_in_MHz_T = Quantity.from_decimal(
    "28024.9513861",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_helion_mass_ratio = Quantity.from_decimal(
    "1.819543074649e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mag_mom_ = Quantity.from_decimal(
    "-9.2847646917e-24",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mag_mom_anomaly = Quantity.from_decimal(
    "1.15965218046e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "-1.00115965218046",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "-1838.281971877",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mass = Quantity.from_decimal(
    "9.1093837139e-31",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mass_energy_equivalent = Quantity.from_decimal(
    "8.1871057880e-14",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "0.51099895069",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_mass_in_u = Quantity.from_decimal(
    "5.485799090441e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_molar_mass = Quantity.from_decimal(
    "5.4857990962e-7",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_muon_mag_mom_ratio = Quantity.from_decimal(
    "206.7669881",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_muon_mass_ratio = Quantity.from_decimal(
    "4.83633170e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_neutron_mag_mom_ratio = Quantity.from_decimal(
    "960.92048",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_neutron_mass_ratio = Quantity.from_decimal(
    "5.4386734416e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_proton_mag_mom_ratio = Quantity.from_decimal(
    "-658.21068789",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_proton_mass_ratio = Quantity.from_decimal(
    "5.446170214889e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_relative_atomic_mass = Quantity.from_decimal(
    "5.485799090441e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_tau_mass_ratio = Quantity.from_decimal(
    "2.87585e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_to_alpha_particle_mass_ratio = Quantity.from_decimal(
    "1.370933554733e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_to_shielded_helion_mag_mom_ratio = Quantity.from_decimal(
    "864.05823986",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_to_shielded_proton_mag_mom_ratio = Quantity.from_decimal(
    "-658.2275856",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_triton_mass_ratio = Quantity.from_decimal(
    "1.819200062327e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt = Quantity(
    Decimal("1.602176634e-19"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_atomic_mass_unit_relationship = Quantity.from_decimal(
    "1.07354410083e-9",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_hartree_relationship = Quantity.from_decimal(
    "3.6749322175665e-2",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_hertz_relationship = Quantity(
    Decimal("2.417989242e14"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_inverse_meter_relationship = Quantity(
    Decimal("8.065543937e5"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_joule_relationship = Quantity(
    Decimal("1.602176634e-19"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_kelvin_relationship = Quantity(
    Decimal("1.160451812e4"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

electron_volt_kilogram_relationship = Quantity(
    Decimal("1.782661921e-36"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

elementary_charge = Quantity(
    Decimal("1.602176634e-19"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

elementary_charge_over_h_bar = Quantity(
    Decimal("1.519267447e15"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Faraday_constant = Quantity(
    Decimal("96485.33212"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Fermi_coupling_constant = Quantity.from_decimal(
    "1.1663787e-5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

fine_structure_constant = Quantity.from_decimal(
    "7.2973525643e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

first_radiation_constant = Quantity(
    Decimal("3.741771852e-16"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

first_radiation_constant_for_spectral_radiance = Quantity(
    Decimal("1.191042972e-16"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_atomic_mass_unit_relationship = Quantity.from_decimal(
    "2.92126231797e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_electron_volt_relationship = Quantity.from_decimal(
    "27.211386245981",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Hartree_energy = Quantity.from_decimal(
    "4.3597447222060e-18",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Hartree_energy_in_eV = Quantity.from_decimal(
    "27.211386245981",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_hertz_relationship = Quantity.from_decimal(
    "6.5796839204999e15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_inverse_meter_relationship = Quantity.from_decimal(
    "2.1947463136314e7",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_joule_relationship = Quantity.from_decimal(
    "4.3597447222060e-18",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_kelvin_relationship = Quantity.from_decimal(
    "3.1577502480398e5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hartree_kilogram_relationship = Quantity.from_decimal(
    "4.8508702095419e-35",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_electron_mass_ratio = Quantity.from_decimal(
    "5495.88527984",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_g_factor = Quantity.from_decimal(
    "-4.2552506995",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mag_mom_ = Quantity.from_decimal(
    "-1.07461755198e-26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "-1.15874098083e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "-2.1276253498",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mass = Quantity.from_decimal(
    "5.0064127862e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mass_energy_equivalent = Quantity.from_decimal(
    "4.4995394185e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "2808.39161112",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_mass_in_u = Quantity.from_decimal(
    "3.014932246932",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_molar_mass = Quantity.from_decimal(
    "3.01493225010e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_proton_mass_ratio = Quantity.from_decimal(
    "2.993152671552",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_relative_atomic_mass = Quantity.from_decimal(
    "3.014932246932",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

helion_shielding_shift = Quantity.from_decimal(
    "5.9967029e-5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_atomic_mass_unit_relationship = Quantity.from_decimal(
    "4.4398216590e-24",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_electron_volt_relationship = Quantity(
    Decimal("4.135667696e-15"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_hartree_relationship = Quantity.from_decimal(
    "1.5198298460574e-16",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_inverse_meter_relationship = Quantity(
    Decimal("3.335640951e-9"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_joule_relationship = Quantity(
    Decimal("6.62607015e-34"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_kelvin_relationship = Quantity(
    Decimal("4.799243073e-11"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hertz_kilogram_relationship = Quantity(
    Decimal("7.372497323e-51"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

hyperfine_transition_frequency_of_Cs_133 = Quantity(
    Decimal("9192631770"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_fine_structure_constant = Quantity.from_decimal(
    "137.035999177",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_atomic_mass_unit_relationship = Quantity.from_decimal(
    "1.33102504824e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_electron_volt_relationship = Quantity(
    Decimal("1.239841984e-6"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_hartree_relationship = Quantity.from_decimal(
    "4.5563352529132e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_hertz_relationship = Quantity(
    Decimal("299792458"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_joule_relationship = Quantity(
    Decimal("1.986445857e-25"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_kelvin_relationship = Quantity(
    Decimal("1.438776877e-2"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_meter_kilogram_relationship = Quantity(
    Decimal("2.210219094e-42"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

inverse_of_conductance_quantum = Quantity(
    Decimal("12906.40372"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Josephson_constant = Quantity(
    Decimal("483597.8484e9"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_atomic_mass_unit_relationship = Quantity.from_decimal(
    "6.7005352471e9",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_electron_volt_relationship = Quantity(
    Decimal("6.241509074e18"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_hartree_relationship = Quantity.from_decimal(
    "2.2937122783969e17",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_hertz_relationship = Quantity(
    Decimal("1.509190179e33"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_inverse_meter_relationship = Quantity(
    Decimal("5.034116567e24"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_kelvin_relationship = Quantity(
    Decimal("7.242970516e22"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

joule_kilogram_relationship = Quantity(
    Decimal("1.112650056e-17"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_atomic_mass_unit_relationship = Quantity.from_decimal(
    "9.2510872884e-14",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_electron_volt_relationship = Quantity(
    Decimal("8.617333262e-5"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_hartree_relationship = Quantity.from_decimal(
    "3.1668115634564e-6",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_hertz_relationship = Quantity(
    Decimal("2.083661912e10"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_inverse_meter_relationship = Quantity(
    Decimal("69.50348004"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_joule_relationship = Quantity(
    Decimal("1.380649e-23"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kelvin_kilogram_relationship = Quantity(
    Decimal("1.536179187e-40"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_atomic_mass_unit_relationship = Quantity.from_decimal(
    "6.0221407537e26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_electron_volt_relationship = Quantity(
    Decimal("5.609588603e35"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_hartree_relationship = Quantity.from_decimal(
    "2.0614857887415e34",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_hertz_relationship = Quantity(
    Decimal("1.356392489e50"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_inverse_meter_relationship = Quantity(
    Decimal("4.524438335e41"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_joule_relationship = Quantity(
    Decimal("8.987551787e16"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

kilogram_kelvin_relationship = Quantity(
    Decimal("6.509657260e39"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

lattice_parameter_of_silicon = Quantity.from_decimal(
    "5.431020511e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

lattice_spacing_of_ideal_Si_220_ = Quantity.from_decimal(
    "1.920155716e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Loschmidt_constant_273_15_K_100_kPa_ = Quantity(
    Decimal("2.651645804e25"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Loschmidt_constant_273_15_K_101_325_kPa_ = Quantity(
    Decimal("2.686780111e25"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

luminous_efficacy = Quantity(
    Decimal("683"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

mag_flux_quantum = Quantity(
    Decimal("2.067833848e-15"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_gas_constant = Quantity(
    Decimal("8.314462618"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_mass_constant = Quantity.from_decimal(
    "1.00000000105e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_mass_of_carbon_12 = Quantity.from_decimal(
    "12.0000000126e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_Planck_constant = Quantity(
    Decimal("3.990312712e-10"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_volume_of_ideal_gas_273_15_K_100_kPa_ = Quantity(
    Decimal("22.71095464e-3"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_volume_of_ideal_gas_273_15_K_101_325_kPa_ = Quantity(
    Decimal("22.41396954e-3"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

molar_volume_of_silicon = Quantity.from_decimal(
    "1.205883199e-5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Molybdenum_x_unit = Quantity.from_decimal(
    "1.00209952e-13",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_Compton_wavelength = Quantity.from_decimal(
    "1.173444110e-14",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_electron_mass_ratio = Quantity.from_decimal(
    "206.7682827",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_g_factor = Quantity.from_decimal(
    "-2.00233184123",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mag_mom_ = Quantity.from_decimal(
    "-4.49044830e-26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mag_mom_anomaly = Quantity.from_decimal(
    "1.16592062e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "-4.84197048e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "-8.89059704",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mass = Quantity.from_decimal(
    "1.883531627e-28",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mass_energy_equivalent = Quantity.from_decimal(
    "1.692833804e-11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "105.6583755",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_mass_in_u = Quantity.from_decimal(
    "0.1134289257",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_molar_mass = Quantity.from_decimal(
    "1.134289258e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_neutron_mass_ratio = Quantity.from_decimal(
    "0.1124545168",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_proton_mag_mom_ratio = Quantity.from_decimal(
    "-3.183345146",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_proton_mass_ratio = Quantity.from_decimal(
    "0.1126095262",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

muon_tau_mass_ratio = Quantity.from_decimal(
    "5.94635e-2",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_action = Quantity(
    Decimal("1.054571817e-34"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_action_in_eV_s = Quantity(
    Decimal("6.582119569e-16"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_energy = Quantity.from_decimal(
    "8.1871057880e-14",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_energy_in_MeV = Quantity.from_decimal(
    "0.51099895069",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_length = Quantity.from_decimal(
    "3.8615926744e-13",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_mass = Quantity.from_decimal(
    "9.1093837139e-31",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_momentum = Quantity.from_decimal(
    "2.73092453446e-22",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_momentum_in_MeV_c = Quantity.from_decimal(
    "0.51099895069",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_time = Quantity.from_decimal(
    "1.28808866644e-21",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

natural_unit_of_velocity = Quantity(
    Decimal("299792458"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_Compton_wavelength = Quantity.from_decimal(
    "1.31959090382e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_electron_mag_mom_ratio = Quantity.from_decimal(
    "1.04066884e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_electron_mass_ratio = Quantity.from_decimal(
    "1838.68366200",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_g_factor = Quantity.from_decimal(
    "-3.82608552",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_gyromag_ratio = Quantity.from_decimal(
    "1.83247174e8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_gyromag_ratio_in_MHz_T = Quantity.from_decimal(
    "29.1646935",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mag_mom_ = Quantity.from_decimal(
    "-9.6623653e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "-1.04187565e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "-1.91304276",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mass = Quantity.from_decimal(
    "1.67492750056e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mass_energy_equivalent = Quantity.from_decimal(
    "1.50534976514e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "939.56542194",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_mass_in_u = Quantity.from_decimal(
    "1.00866491606",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_molar_mass = Quantity.from_decimal(
    "1.00866491712e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_muon_mass_ratio = Quantity.from_decimal(
    "8.89248408",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_proton_mag_mom_ratio = Quantity.from_decimal(
    "-0.68497935",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_proton_mass_difference = Quantity.from_decimal(
    "2.30557461e-30",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_proton_mass_difference_energy_equivalent = Quantity.from_decimal(
    "2.07214712e-13",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_proton_mass_difference_energy_equivalent_in_MeV = Quantity.from_decimal(
    "1.29333251",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_proton_mass_difference_in_u = Quantity.from_decimal(
    "1.38844948e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_proton_mass_ratio = Quantity.from_decimal(
    "1.00137841946",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_relative_atomic_mass = Quantity.from_decimal(
    "1.00866491606",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_tau_mass_ratio = Quantity.from_decimal(
    "0.528779",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

neutron_to_shielded_proton_mag_mom_ratio = Quantity.from_decimal(
    "-0.68499694",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Newtonian_constant_of_gravitation = Quantity.from_decimal(
    "6.67430e-11",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Newtonian_constant_of_gravitation_over_h_bar_c = Quantity.from_decimal(
    "6.70883e-39",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

nuclear_magneton = Quantity.from_decimal(
    "5.0507837393e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

nuclear_magneton_in_eV_T = Quantity.from_decimal(
    "3.15245125417e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

nuclear_magneton_in_inverse_meter_per_tesla = Quantity.from_decimal(
    "2.54262341009e-2",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

nuclear_magneton_in_K_T = Quantity.from_decimal(
    "3.6582677706e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

nuclear_magneton_in_MHz_T = Quantity.from_decimal(
    "7.6225932188",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_constant = Quantity(
    Decimal("6.62607015e-34"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_constant_in_eV_Hz = Quantity(
    Decimal("4.135667696e-15"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_length = Quantity.from_decimal(
    "1.616255e-35",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_mass = Quantity.from_decimal(
    "2.176434e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_mass_energy_equivalent_in_GeV = Quantity.from_decimal(
    "1.220890e19",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_temperature = Quantity.from_decimal(
    "1.416784e32",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Planck_time = Quantity.from_decimal(
    "5.391247e-44",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_charge_to_mass_quotient = Quantity.from_decimal(
    "9.5788331430e7",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_Compton_wavelength = Quantity.from_decimal(
    "1.32140985360e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_electron_mass_ratio = Quantity.from_decimal(
    "1836.152673426",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_g_factor = Quantity.from_decimal(
    "5.5856946893",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_gyromag_ratio = Quantity.from_decimal(
    "2.6752218708e8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_gyromag_ratio_in_MHz_T = Quantity.from_decimal(
    "42.577478461",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mag_mom_ = Quantity.from_decimal(
    "1.41060679545e-26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "1.52103220230e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "2.79284734463",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mag_shielding_correction = Quantity.from_decimal(
    "2.56715e-5",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mass = Quantity.from_decimal(
    "1.67262192595e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mass_energy_equivalent = Quantity.from_decimal(
    "1.50327761802e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "938.27208943",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_mass_in_u = Quantity.from_decimal(
    "1.0072764665789",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_molar_mass = Quantity.from_decimal(
    "1.00727646764e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_muon_mass_ratio = Quantity.from_decimal(
    "8.88024338",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_neutron_mag_mom_ratio = Quantity.from_decimal(
    "-1.45989802",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_neutron_mass_ratio = Quantity.from_decimal(
    "0.99862347797",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_relative_atomic_mass = Quantity.from_decimal(
    "1.0072764665789",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_rms_charge_radius = Quantity.from_decimal(
    "8.4075e-16",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

proton_tau_mass_ratio = Quantity.from_decimal(
    "0.528051",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

quantum_of_circulation = Quantity.from_decimal(
    "3.6369475467e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

quantum_of_circulation_times_2 = Quantity.from_decimal(
    "7.2738950934e-4",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_Compton_wavelength = Quantity.from_decimal(
    "3.8615926744e-13",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_muon_Compton_wavelength = Quantity.from_decimal(
    "1.867594306e-15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_neutron_Compton_wavelength = Quantity.from_decimal(
    "2.1001941520e-16",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_Planck_constant = Quantity(
    Decimal("1.054571817e-34"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_Planck_constant_in_eV_s = Quantity(
    Decimal("6.582119569e-16"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_Planck_constant_times_c_in_MeV_fm = Quantity(
    Decimal("197.3269804"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_proton_Compton_wavelength = Quantity.from_decimal(
    "2.10308910051e-16",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

reduced_tau_Compton_wavelength = Quantity.from_decimal(
    "1.110538e-16",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Rydberg_constant = Quantity.from_decimal(
    "10973731.568157",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Rydberg_constant_times_c_in_Hz = Quantity.from_decimal(
    "3.2898419602500e15",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Rydberg_constant_times_hc_in_eV = Quantity.from_decimal(
    "13.605693122990",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Rydberg_constant_times_hc_in_J = Quantity.from_decimal(
    "2.1798723611030e-18",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Sackur_Tetrode_constant_1_K_100_kPa_ = Quantity.from_decimal(
    "-1.15170753496",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Sackur_Tetrode_constant_1_K_101_325_kPa_ = Quantity.from_decimal(
    "-1.16487052149",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

second_radiation_constant = Quantity(
    Decimal("1.438776877e-2"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_gyromag_ratio = Quantity.from_decimal(
    "2.0378946078e8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_gyromag_ratio_in_MHz_T = Quantity.from_decimal(
    "32.434100033",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_mag_mom_ = Quantity.from_decimal(
    "-1.07455311035e-26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "-1.15867149457e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "-2.1274977624",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_to_proton_mag_mom_ratio = Quantity.from_decimal(
    "-0.76176657721",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_helion_to_shielded_proton_mag_mom_ratio = Quantity.from_decimal(
    "-0.7617861334",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_proton_gyromag_ratio = Quantity.from_decimal(
    "2.675153194e8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_proton_gyromag_ratio_in_MHz_T = Quantity.from_decimal(
    "42.57638543",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_proton_mag_mom_ = Quantity.from_decimal(
    "1.4105705830e-26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_proton_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "1.5209931551e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielded_proton_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "2.792775648",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielding_difference_of_d_and_p_in_HD = Quantity.from_decimal(
    "1.98770e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

shielding_difference_of_t_and_p_in_HT = Quantity.from_decimal(
    "2.39450e-8",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

speed_of_light_in_vacuum = Quantity(
    Decimal("299792458"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

standard_acceleration_of_gravity = Quantity(
    Decimal("9.80665"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

standard_atmosphere = Quantity(
    Decimal("101325"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

standard_state_pressure = Quantity(
    Decimal("100000"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Stefan_Boltzmann_constant = Quantity(
    Decimal("5.670374419e-8"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_Compton_wavelength = Quantity.from_decimal(
    "6.97771e-16",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_electron_mass_ratio = Quantity.from_decimal(
    "3477.23",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_energy_equivalent = Quantity.from_decimal(
    "1776.86",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_mass = Quantity.from_decimal(
    "3.16754e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_mass_energy_equivalent = Quantity.from_decimal(
    "2.84684e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_mass_in_u = Quantity.from_decimal(
    "1.90754",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_molar_mass = Quantity.from_decimal(
    "1.90754e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_muon_mass_ratio = Quantity.from_decimal(
    "16.8170",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_neutron_mass_ratio = Quantity.from_decimal(
    "1.89115",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

tau_proton_mass_ratio = Quantity.from_decimal(
    "1.89376",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Thomson_cross_section = Quantity.from_decimal(
    "6.6524587051e-29",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_electron_mass_ratio = Quantity.from_decimal(
    "5496.92153551",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_g_factor = Quantity.from_decimal(
    "5.957924930",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mag_mom_ = Quantity.from_decimal(
    "1.5046095178e-26",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mag_mom_to_Bohr_magneton_ratio = Quantity.from_decimal(
    "1.6223936648e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mag_mom_to_nuclear_magneton_ratio = Quantity.from_decimal(
    "2.9789624650",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mass = Quantity.from_decimal(
    "5.0073567512e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mass_energy_equivalent = Quantity.from_decimal(
    "4.5003878119e-10",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mass_energy_equivalent_in_MeV = Quantity.from_decimal(
    "2808.92113668",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_mass_in_u = Quantity.from_decimal(
    "3.01550071597",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_molar_mass = Quantity.from_decimal(
    "3.01550071913e-3",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_proton_mass_ratio = Quantity.from_decimal(
    "2.99371703403",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_relative_atomic_mass = Quantity.from_decimal(
    "3.01550071597",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

triton_to_proton_mag_mom_ratio = Quantity.from_decimal(
    "1.0666399189",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

unified_atomic_mass_unit = Quantity.from_decimal(
    "1.66053906892e-27",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

vacuum_electric_permittivity = Quantity.from_decimal(
    "8.8541878188e-12",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

vacuum_mag_permeability = Quantity.from_decimal(
    "1.25663706127e-6",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

von_Klitzing_constant = Quantity(
    Decimal("25812.80745"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

weak_mixing_angle = Quantity.from_decimal(
    "0.22305",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Wien_frequency_displacement_law_constant = Quantity(
    Decimal("5.878925757e10"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

Wien_wavelength_displacement_law_constant = Quantity(
    Decimal("2.897771955e-3"),
    constant=True,
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501

W_to_Z_mass_ratio = Quantity.from_decimal(
    "0.88145",
)
"""From `CODATA Internationally Recommended 2022 Values of the Fundamental Physical Constants <https://physics.nist.gov/cuu/Constants/>`_.
"""  # noqa: E501
