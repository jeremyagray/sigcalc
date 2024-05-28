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

"""sigcalc module initialization."""

from .constants import e
from .constants import pi
from .physical_constants import Angstrom_star
from .physical_constants import Avogadro_constant
from .physical_constants import Bohr_magneton
from .physical_constants import Bohr_magneton_in_eV_T
from .physical_constants import Bohr_magneton_in_Hz_T
from .physical_constants import Bohr_magneton_in_inverse_meter_per_tesla
from .physical_constants import Bohr_magneton_in_K_T
from .physical_constants import Bohr_radius
from .physical_constants import Boltzmann_constant
from .physical_constants import Boltzmann_constant_in_eV_K
from .physical_constants import Boltzmann_constant_in_Hz_K
from .physical_constants import Boltzmann_constant_in_inverse_meter_per_kelvin
from .physical_constants import Compton_wavelength
from .physical_constants import Copper_x_unit
from .physical_constants import Faraday_constant
from .physical_constants import Fermi_coupling_constant
from .physical_constants import Hartree_energy
from .physical_constants import Hartree_energy_in_eV
from .physical_constants import Josephson_constant
from .physical_constants import Loschmidt_constant_273_15_K_100_kPa_
from .physical_constants import Loschmidt_constant_273_15_K_101_325_kPa_
from .physical_constants import Molybdenum_x_unit
from .physical_constants import Newtonian_constant_of_gravitation
from .physical_constants import Newtonian_constant_of_gravitation_over_h_bar_c
from .physical_constants import Planck_constant
from .physical_constants import Planck_constant_in_eV_Hz
from .physical_constants import Planck_length
from .physical_constants import Planck_mass
from .physical_constants import Planck_mass_energy_equivalent_in_GeV
from .physical_constants import Planck_temperature
from .physical_constants import Planck_time
from .physical_constants import Rydberg_constant
from .physical_constants import Rydberg_constant_times_c_in_Hz
from .physical_constants import Rydberg_constant_times_hc_in_eV
from .physical_constants import Rydberg_constant_times_hc_in_J
from .physical_constants import Sackur_Tetrode_constant_1_K_100_kPa_
from .physical_constants import Sackur_Tetrode_constant_1_K_101_325_kPa_
from .physical_constants import Stefan_Boltzmann_constant
from .physical_constants import Thomson_cross_section
from .physical_constants import W_to_Z_mass_ratio
from .physical_constants import Wien_frequency_displacement_law_constant
from .physical_constants import Wien_wavelength_displacement_law_constant
from .physical_constants import alpha_particle_electron_mass_ratio
from .physical_constants import alpha_particle_mass
from .physical_constants import alpha_particle_mass_energy_equivalent
from .physical_constants import alpha_particle_mass_energy_equivalent_in_MeV
from .physical_constants import alpha_particle_mass_in_u
from .physical_constants import alpha_particle_molar_mass
from .physical_constants import alpha_particle_proton_mass_ratio
from .physical_constants import alpha_particle_relative_atomic_mass
from .physical_constants import alpha_particle_rms_charge_radius
from .physical_constants import atomic_mass_constant
from .physical_constants import atomic_mass_constant_energy_equivalent
from .physical_constants import atomic_mass_constant_energy_equivalent_in_MeV
from .physical_constants import atomic_mass_unit_electron_volt_relationship
from .physical_constants import atomic_mass_unit_hartree_relationship
from .physical_constants import atomic_mass_unit_hertz_relationship
from .physical_constants import atomic_mass_unit_inverse_meter_relationship
from .physical_constants import atomic_mass_unit_joule_relationship
from .physical_constants import atomic_mass_unit_kelvin_relationship
from .physical_constants import atomic_mass_unit_kilogram_relationship
from .physical_constants import atomic_unit_of_1st_hyperpolarizability
from .physical_constants import atomic_unit_of_2nd_hyperpolarizability
from .physical_constants import atomic_unit_of_action
from .physical_constants import atomic_unit_of_charge
from .physical_constants import atomic_unit_of_charge_density
from .physical_constants import atomic_unit_of_current
from .physical_constants import atomic_unit_of_electric_dipole_mom_
from .physical_constants import atomic_unit_of_electric_field
from .physical_constants import atomic_unit_of_electric_field_gradient
from .physical_constants import atomic_unit_of_electric_polarizability
from .physical_constants import atomic_unit_of_electric_potential
from .physical_constants import atomic_unit_of_electric_quadrupole_mom_
from .physical_constants import atomic_unit_of_energy
from .physical_constants import atomic_unit_of_force
from .physical_constants import atomic_unit_of_length
from .physical_constants import atomic_unit_of_mag_dipole_mom_
from .physical_constants import atomic_unit_of_mag_flux_density
from .physical_constants import atomic_unit_of_magnetizability
from .physical_constants import atomic_unit_of_mass
from .physical_constants import atomic_unit_of_momentum
from .physical_constants import atomic_unit_of_permittivity
from .physical_constants import atomic_unit_of_time
from .physical_constants import atomic_unit_of_velocity
from .physical_constants import characteristic_impedance_of_vacuum
from .physical_constants import classical_electron_radius
from .physical_constants import conductance_quantum
from .physical_constants import conventional_value_of_ampere_90
from .physical_constants import conventional_value_of_coulomb_90
from .physical_constants import conventional_value_of_farad_90
from .physical_constants import conventional_value_of_henry_90
from .physical_constants import conventional_value_of_Josephson_constant
from .physical_constants import conventional_value_of_ohm_90
from .physical_constants import conventional_value_of_volt_90
from .physical_constants import conventional_value_of_von_Klitzing_constant
from .physical_constants import conventional_value_of_watt_90
from .physical_constants import deuteron_electron_mag_mom_ratio
from .physical_constants import deuteron_electron_mass_ratio
from .physical_constants import deuteron_g_factor
from .physical_constants import deuteron_mag_mom_
from .physical_constants import deuteron_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import deuteron_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import deuteron_mass
from .physical_constants import deuteron_mass_energy_equivalent
from .physical_constants import deuteron_mass_energy_equivalent_in_MeV
from .physical_constants import deuteron_mass_in_u
from .physical_constants import deuteron_molar_mass
from .physical_constants import deuteron_neutron_mag_mom_ratio
from .physical_constants import deuteron_proton_mag_mom_ratio
from .physical_constants import deuteron_proton_mass_ratio
from .physical_constants import deuteron_relative_atomic_mass
from .physical_constants import deuteron_rms_charge_radius
from .physical_constants import electron_charge_to_mass_quotient
from .physical_constants import electron_deuteron_mag_mom_ratio
from .physical_constants import electron_deuteron_mass_ratio
from .physical_constants import electron_g_factor
from .physical_constants import electron_gyromag_ratio
from .physical_constants import electron_gyromag_ratio_in_MHz_T
from .physical_constants import electron_helion_mass_ratio
from .physical_constants import electron_mag_mom_
from .physical_constants import electron_mag_mom_anomaly
from .physical_constants import electron_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import electron_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import electron_mass
from .physical_constants import electron_mass_energy_equivalent
from .physical_constants import electron_mass_energy_equivalent_in_MeV
from .physical_constants import electron_mass_in_u
from .physical_constants import electron_molar_mass
from .physical_constants import electron_muon_mag_mom_ratio
from .physical_constants import electron_muon_mass_ratio
from .physical_constants import electron_neutron_mag_mom_ratio
from .physical_constants import electron_neutron_mass_ratio
from .physical_constants import electron_proton_mag_mom_ratio
from .physical_constants import electron_proton_mass_ratio
from .physical_constants import electron_relative_atomic_mass
from .physical_constants import electron_tau_mass_ratio
from .physical_constants import electron_to_alpha_particle_mass_ratio
from .physical_constants import electron_to_shielded_helion_mag_mom_ratio
from .physical_constants import electron_to_shielded_proton_mag_mom_ratio
from .physical_constants import electron_triton_mass_ratio
from .physical_constants import electron_volt
from .physical_constants import electron_volt_atomic_mass_unit_relationship
from .physical_constants import electron_volt_hartree_relationship
from .physical_constants import electron_volt_hertz_relationship
from .physical_constants import electron_volt_inverse_meter_relationship
from .physical_constants import electron_volt_joule_relationship
from .physical_constants import electron_volt_kelvin_relationship
from .physical_constants import electron_volt_kilogram_relationship
from .physical_constants import elementary_charge
from .physical_constants import elementary_charge_over_h_bar
from .physical_constants import fine_structure_constant
from .physical_constants import first_radiation_constant
from .physical_constants import first_radiation_constant_for_spectral_radiance
from .physical_constants import hartree_atomic_mass_unit_relationship
from .physical_constants import hartree_electron_volt_relationship
from .physical_constants import hartree_hertz_relationship
from .physical_constants import hartree_inverse_meter_relationship
from .physical_constants import hartree_joule_relationship
from .physical_constants import hartree_kelvin_relationship
from .physical_constants import hartree_kilogram_relationship
from .physical_constants import helion_electron_mass_ratio
from .physical_constants import helion_g_factor
from .physical_constants import helion_mag_mom_
from .physical_constants import helion_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import helion_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import helion_mass
from .physical_constants import helion_mass_energy_equivalent
from .physical_constants import helion_mass_energy_equivalent_in_MeV
from .physical_constants import helion_mass_in_u
from .physical_constants import helion_molar_mass
from .physical_constants import helion_proton_mass_ratio
from .physical_constants import helion_relative_atomic_mass
from .physical_constants import helion_shielding_shift
from .physical_constants import hertz_atomic_mass_unit_relationship
from .physical_constants import hertz_electron_volt_relationship
from .physical_constants import hertz_hartree_relationship
from .physical_constants import hertz_inverse_meter_relationship
from .physical_constants import hertz_joule_relationship
from .physical_constants import hertz_kelvin_relationship
from .physical_constants import hertz_kilogram_relationship
from .physical_constants import hyperfine_transition_frequency_of_Cs_133
from .physical_constants import inverse_fine_structure_constant
from .physical_constants import inverse_meter_atomic_mass_unit_relationship
from .physical_constants import inverse_meter_electron_volt_relationship
from .physical_constants import inverse_meter_hartree_relationship
from .physical_constants import inverse_meter_hertz_relationship
from .physical_constants import inverse_meter_joule_relationship
from .physical_constants import inverse_meter_kelvin_relationship
from .physical_constants import inverse_meter_kilogram_relationship
from .physical_constants import inverse_of_conductance_quantum
from .physical_constants import joule_atomic_mass_unit_relationship
from .physical_constants import joule_electron_volt_relationship
from .physical_constants import joule_hartree_relationship
from .physical_constants import joule_hertz_relationship
from .physical_constants import joule_inverse_meter_relationship
from .physical_constants import joule_kelvin_relationship
from .physical_constants import joule_kilogram_relationship
from .physical_constants import kelvin_atomic_mass_unit_relationship
from .physical_constants import kelvin_electron_volt_relationship
from .physical_constants import kelvin_hartree_relationship
from .physical_constants import kelvin_hertz_relationship
from .physical_constants import kelvin_inverse_meter_relationship
from .physical_constants import kelvin_joule_relationship
from .physical_constants import kelvin_kilogram_relationship
from .physical_constants import kilogram_atomic_mass_unit_relationship
from .physical_constants import kilogram_electron_volt_relationship
from .physical_constants import kilogram_hartree_relationship
from .physical_constants import kilogram_hertz_relationship
from .physical_constants import kilogram_inverse_meter_relationship
from .physical_constants import kilogram_joule_relationship
from .physical_constants import kilogram_kelvin_relationship
from .physical_constants import lattice_parameter_of_silicon
from .physical_constants import lattice_spacing_of_ideal_Si_220_
from .physical_constants import luminous_efficacy
from .physical_constants import mag_flux_quantum
from .physical_constants import molar_gas_constant
from .physical_constants import molar_mass_constant
from .physical_constants import molar_mass_of_carbon_12
from .physical_constants import molar_Planck_constant
from .physical_constants import molar_volume_of_ideal_gas_273_15_K_100_kPa_
from .physical_constants import molar_volume_of_ideal_gas_273_15_K_101_325_kPa_
from .physical_constants import molar_volume_of_silicon
from .physical_constants import muon_Compton_wavelength
from .physical_constants import muon_electron_mass_ratio
from .physical_constants import muon_g_factor
from .physical_constants import muon_mag_mom_
from .physical_constants import muon_mag_mom_anomaly
from .physical_constants import muon_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import muon_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import muon_mass
from .physical_constants import muon_mass_energy_equivalent
from .physical_constants import muon_mass_energy_equivalent_in_MeV
from .physical_constants import muon_mass_in_u
from .physical_constants import muon_molar_mass
from .physical_constants import muon_neutron_mass_ratio
from .physical_constants import muon_proton_mag_mom_ratio
from .physical_constants import muon_proton_mass_ratio
from .physical_constants import muon_tau_mass_ratio
from .physical_constants import natural_unit_of_action
from .physical_constants import natural_unit_of_action_in_eV_s
from .physical_constants import natural_unit_of_energy
from .physical_constants import natural_unit_of_energy_in_MeV
from .physical_constants import natural_unit_of_length
from .physical_constants import natural_unit_of_mass
from .physical_constants import natural_unit_of_momentum
from .physical_constants import natural_unit_of_momentum_in_MeV_c
from .physical_constants import natural_unit_of_time
from .physical_constants import natural_unit_of_velocity
from .physical_constants import neutron_Compton_wavelength
from .physical_constants import neutron_electron_mag_mom_ratio
from .physical_constants import neutron_electron_mass_ratio
from .physical_constants import neutron_g_factor
from .physical_constants import neutron_gyromag_ratio
from .physical_constants import neutron_gyromag_ratio_in_MHz_T
from .physical_constants import neutron_mag_mom_
from .physical_constants import neutron_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import neutron_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import neutron_mass
from .physical_constants import neutron_mass_energy_equivalent
from .physical_constants import neutron_mass_energy_equivalent_in_MeV
from .physical_constants import neutron_mass_in_u
from .physical_constants import neutron_molar_mass
from .physical_constants import neutron_muon_mass_ratio
from .physical_constants import neutron_proton_mag_mom_ratio
from .physical_constants import neutron_proton_mass_difference
from .physical_constants import neutron_proton_mass_difference_energy_equivalent
from .physical_constants import neutron_proton_mass_difference_energy_equivalent_in_MeV
from .physical_constants import neutron_proton_mass_difference_in_u
from .physical_constants import neutron_proton_mass_ratio
from .physical_constants import neutron_relative_atomic_mass
from .physical_constants import neutron_tau_mass_ratio
from .physical_constants import neutron_to_shielded_proton_mag_mom_ratio
from .physical_constants import nuclear_magneton
from .physical_constants import nuclear_magneton_in_eV_T
from .physical_constants import nuclear_magneton_in_inverse_meter_per_tesla
from .physical_constants import nuclear_magneton_in_K_T
from .physical_constants import nuclear_magneton_in_MHz_T
from .physical_constants import proton_charge_to_mass_quotient
from .physical_constants import proton_Compton_wavelength
from .physical_constants import proton_electron_mass_ratio
from .physical_constants import proton_g_factor
from .physical_constants import proton_gyromag_ratio
from .physical_constants import proton_gyromag_ratio_in_MHz_T
from .physical_constants import proton_mag_mom_
from .physical_constants import proton_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import proton_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import proton_mag_shielding_correction
from .physical_constants import proton_mass
from .physical_constants import proton_mass_energy_equivalent
from .physical_constants import proton_mass_energy_equivalent_in_MeV
from .physical_constants import proton_mass_in_u
from .physical_constants import proton_molar_mass
from .physical_constants import proton_muon_mass_ratio
from .physical_constants import proton_neutron_mag_mom_ratio
from .physical_constants import proton_neutron_mass_ratio
from .physical_constants import proton_relative_atomic_mass
from .physical_constants import proton_rms_charge_radius
from .physical_constants import proton_tau_mass_ratio
from .physical_constants import quantum_of_circulation
from .physical_constants import quantum_of_circulation_times_2
from .physical_constants import reduced_Compton_wavelength
from .physical_constants import reduced_muon_Compton_wavelength
from .physical_constants import reduced_neutron_Compton_wavelength
from .physical_constants import reduced_Planck_constant
from .physical_constants import reduced_Planck_constant_in_eV_s
from .physical_constants import reduced_Planck_constant_times_c_in_MeV_fm
from .physical_constants import reduced_proton_Compton_wavelength
from .physical_constants import reduced_tau_Compton_wavelength
from .physical_constants import second_radiation_constant
from .physical_constants import shielded_helion_gyromag_ratio
from .physical_constants import shielded_helion_gyromag_ratio_in_MHz_T
from .physical_constants import shielded_helion_mag_mom_
from .physical_constants import shielded_helion_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import shielded_helion_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import shielded_helion_to_proton_mag_mom_ratio
from .physical_constants import shielded_helion_to_shielded_proton_mag_mom_ratio
from .physical_constants import shielded_proton_gyromag_ratio
from .physical_constants import shielded_proton_gyromag_ratio_in_MHz_T
from .physical_constants import shielded_proton_mag_mom_
from .physical_constants import shielded_proton_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import shielded_proton_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import shielding_difference_of_d_and_p_in_HD
from .physical_constants import shielding_difference_of_t_and_p_in_HT
from .physical_constants import speed_of_light_in_vacuum
from .physical_constants import standard_acceleration_of_gravity
from .physical_constants import standard_atmosphere
from .physical_constants import standard_state_pressure
from .physical_constants import tau_Compton_wavelength
from .physical_constants import tau_electron_mass_ratio
from .physical_constants import tau_energy_equivalent
from .physical_constants import tau_mass
from .physical_constants import tau_mass_energy_equivalent
from .physical_constants import tau_mass_in_u
from .physical_constants import tau_molar_mass
from .physical_constants import tau_muon_mass_ratio
from .physical_constants import tau_neutron_mass_ratio
from .physical_constants import tau_proton_mass_ratio
from .physical_constants import triton_electron_mass_ratio
from .physical_constants import triton_g_factor
from .physical_constants import triton_mag_mom_
from .physical_constants import triton_mag_mom_to_Bohr_magneton_ratio
from .physical_constants import triton_mag_mom_to_nuclear_magneton_ratio
from .physical_constants import triton_mass
from .physical_constants import triton_mass_energy_equivalent
from .physical_constants import triton_mass_energy_equivalent_in_MeV
from .physical_constants import triton_mass_in_u
from .physical_constants import triton_molar_mass
from .physical_constants import triton_proton_mass_ratio
from .physical_constants import triton_relative_atomic_mass
from .physical_constants import triton_to_proton_mag_mom_ratio
from .physical_constants import unified_atomic_mass_unit
from .physical_constants import vacuum_electric_permittivity
from .physical_constants import vacuum_mag_permeability
from .physical_constants import von_Klitzing_constant
from .physical_constants import weak_mixing_angle
from .quantity import Quantity
