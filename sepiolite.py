#
# example of using xraylib to get crystal data
#
# see: 
#       http://dx.doi.org/10.1016/j.sab.2011.09.011   (paper) 
#       https://github.com/tschoonj/xraylib/          (code) 
#       http://lvserver.ugent.be/xraylib-web          (web interface, but crystals not included!)
#



#
#  import block 
#
import xraylib
import numpy as np
import scipy.constants.codata 

#
# get crystal data for silicon crystal
#
# cryst = xraylib.Crystal_GetCrystal("Si")
#
# print(cryst)
# print(len(cryst))

# dspacing = xraylib.Crystal_dSpacing(cryst,hh,kk,ll )
# print("dspacing: %f A \n"%dspacing)
# print("name: %s  \n"%cryst['name'],type(cryst['name']))

cryst = {} # cryst.copy()


# for key in cryst:
#     if key != "cpointer":
#         cryst2[key] = cryst[key]
#
# cryst2['atom'] = cryst['atom']
cryst['name'] = b"Si"
cryst['a'] =  5.430699825286865
cryst['b'] =  5.430699825286865
cryst['c'] =  5.430699825286865
cryst['alpha'] =  90.0
cryst['beta'] =  90.0
cryst['gamma'] = 90.0
cryst['n_atom'] =  8
cryst['atom'] = [  {'x': 0.0,  'y': 0.0,  'z': 0.0,  'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.0,  'y': 0.5,  'z': 0.5,  'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.5,  'y': 0.0,  'z': 0.5,  'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.5,  'y': 0.5,  'z': 0.0,  'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.25, 'y': 0.25, 'z': 0.25, 'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.25, 'y': 0.75, 'z': 0.75, 'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.75, 'y': 0.25, 'z': 0.75, 'Zatom': 14, 'fraction': 1.0},
                   {'x': 0.75, 'y': 0.75, 'z': 0.25, 'Zatom': 14, 'fraction': 1.0}]
cryst['volume'] = 160.16493225097656


# print some info
print ("  Unit cell dimensions [A] are %f %f %f" % (cryst['a'],cryst['b'],cryst['c']))
print ("  Unit cell angles are %f %f %f" % (cryst['alpha'],cryst['beta'],cryst['gamma']))
print ("  Unit cell volume [A] is %f" % (cryst['volume']) )

for key in cryst:
    print(">>",key," = ",cryst[key])




#
# define miller indices and compute dSpacing
#

hh = 1
kk = 1
ll = 1

dspacing = xraylib.Crystal_dSpacing(cryst,hh,kk,ll )
print("dspacing: %f A \n"%dspacing)
print(len(cryst))





#
# define energy and get Bragg angle
#
ener = 12.398 # keV
braggAngle = xraylib.Bragg_angle(cryst,ener,hh,kk,ll )
print("Bragg angle: %f degrees \n"%(braggAngle*180/np.pi))


#
# get the structure factor (at a given energy)
#


debyeWaller = 1.0
rel_angle = 1.0  # ratio of (incident angle)/(bragg angle) -> we work at Bragg angle

f0 = xraylib.Crystal_F_H_StructureFactor(cryst, ener, 0, 0, 0, debyeWaller, 1.0)
fH = xraylib.Crystal_F_H_StructureFactor(cryst, ener, hh, kk, ll, debyeWaller, 1.0)
print("f0: (%f , %f) \n"%(f0.real,f0.imag))
print("fH: (%f , %f) \n"%(fH.real,fH.imag))

# #
# # convert structure factor in chi (or psi) = - classical_e_radius wavelength^2 fH /(pi volume)
# #
# codata = scipy.constants.codata.physical_constants
# codata_c, tmp1, tmp2 = codata["speed of light in vacuum"]
# codata_h, tmp1, tmp2 = codata["Planck constant"]
# codata_ec, tmp1, tmp2 = codata["elementary charge"]
# codata_r, tmp1, tmp2 = codata["classical electron radius"]
#
# ev2meter = codata_h*codata_c/codata_ec
# wavelength = ev2meter/(ener*1e3)
# print("Photon energy: %f keV \n"%ener)
# print("Photon wavelength: %f A \n"%(1e10*wavelength))
#
# volume = cryst['volume'] *1e-10*1e-10*1e-10 # volume of silicon unit cell in m^3
# cte = - codata_r * wavelength*wavelength/(np.pi * volume)
#
# chi0 = cte*f0
# chiH = cte*fH
#
# print("chi0: (%e , %e) \n"%(chi0.real,chi0.imag))
# print("chiH: (%e , %e) \n"%(chiH.real,chiH.imag))
#
#
#
