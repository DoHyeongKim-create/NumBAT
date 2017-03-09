""" Calculate a dispersion diagram of the acoustic modes
    from k_AC = 0 (forward SBS) to k_AC = 2*k_EM (backward SBS).
"""

import time
import datetime
import numpy as np
import sys
sys.path.append("../backend/")
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

import materials
import objects
import mode_calcs
import integration
import plotting
from fortran import NumBAT


# Geometric Parameters - all in nm.
wl_nm = 1550
unitcell_x = 2.5*wl_nm
unitcell_y = unitcell_x
inc_a_x = 314.7
inc_a_y = 0.9*inc_a_x
inc_shape = 'rectangular'

num_EM_modes = 20
num_AC_modes = 20
EM_ival1 = 0
EM_ival2 = EM_ival1
AC_ival = 'All'

# Use all specified parameters to create a waveguide object.
wguide = objects.Struct(unitcell_x,inc_a_x,unitcell_y,inc_a_y,inc_shape,
                        bkg_material=materials.Air,
                        inc_a_material=materials.Si,
                        lc_bkg=2, lc2=500.0, lc3=10.0)

# Expected effective index of fundamental guided mode.
n_eff = wguide.inc_a_material.n-0.1

# Calculate Electromagnetic Modes
# sim_EM_wguide = wguide.calc_EM_modes(wl_nm, num_EM_modes, n_eff)
# np.savez('wguide_data', sim_EM_wguide=sim_EM_wguide)

# Assuming this calculation is run directly after simo-tut_02
# we don't need to recalculate EM modes, but can load them in.
npzfile = np.load('wguide_data.npz')
sim_EM_wguide = npzfile['sim_EM_wguide'].tolist()


# Will scan from forward to backward SBS so need to know k_AC of backward SBS.
k_AC = 2*sim_EM_wguide.Eig_values[0]
# Number of wavevectors steps.
nu_ks = 20

plt.clf()
plt.figure(figsize=(10,6))
ax = plt.subplot(1,1,1)
for i_ac, q_ac in enumerate(np.linspace(0.0,k_AC,nu_ks)):
    sim_AC_wguide = wguide.calc_AC_modes(wl_nm, num_AC_modes, q_ac, EM_sim=sim_EM_wguide)
    prop_AC_modes = np.array([np.real(x) for x in sim_AC_wguide.Eig_values if abs(np.real(x)) > abs(np.imag(x))])
    sym_list = integration.symmetries(sim_AC_wguide)

    for i in range(len(prop_AC_modes)):
        Om = prop_AC_modes[i]*1e-9
        if sym_list[i][0] == 1 and sym_list[i][1] == 1 and sym_list[i][2] == 1:
            sym_A, = plt.plot(np.real(q_ac/k_AC), Om, 'or')
        if sym_list[i][0] == -1 and sym_list[i][1] == 1 and sym_list[i][2] == -1:
            sym_B, = plt.plot(np.real(q_ac/k_AC), Om, 'vc')
        if sym_list[i][0] == 1 and sym_list[i][1] == -1 and sym_list[i][2] == -1:
            sym_C, = plt.plot(np.real(q_ac/k_AC), Om, 'sb')
        if sym_list[i][0] == -1 and sym_list[i][1] == -1 and sym_list[i][2] == 1:
            sym_D, = plt.plot(np.real(q_ac/k_AC), Om, '^g')

    print "wavevector loop", i_ac+1, "/", nu_ks
ax.set_ylim(0,20)
ax.set_xlim(0,1)
plt.legend([sym_A, sym_B, sym_C, sym_D],['E',r'C$_2$',r'$\sigma_y$',r'$\sigma_x$'], loc='lower right')
plt.xlabel(r'Axial wavevector (normalised)')
plt.ylabel(r'Frequency (GHz)')
plt.savefig('symetrised_dispersion.pdf', bbox_inches='tight')
plt.close()
