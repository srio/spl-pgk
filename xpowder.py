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
import numpy

import scipy.constants.codata
import matplotlib.pyplot as plt


codata = scipy.constants.codata.physical_constants
codata_c, tmp1, tmp2 = codata["speed of light in vacuum"]
codata_h, tmp1, tmp2 = codata["Planck constant"]
codata_ec, tmp1, tmp2 = codata["elementary charge"]
codata_r, tmp1, tmp2 = codata["classical electron radius"]

ev2meter = codata_h*codata_c/codata_ec






def structure_silicon():
    cryst = {} # cryst.copy()

    cryst['name']   = b"Si"
    cryst['a']      =  5.430699825286865
    cryst['b']      =  5.430699825286865
    cryst['c']      =  5.430699825286865
    cryst['alpha']  = 90.0
    cryst['beta']   =  90.0
    cryst['gamma']  = 90.0
    cryst['n_atom'] =  8
    cryst['atom']   = [  {'x': 0.0,  'y': 0.0,  'z': 0.0,  'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.0,  'y': 0.5,  'z': 0.5,  'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.5,  'y': 0.0,  'z': 0.5,  'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.5,  'y': 0.5,  'z': 0.0,  'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.25, 'y': 0.25, 'z': 0.25, 'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.25, 'y': 0.75, 'z': 0.75, 'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.75, 'y': 0.25, 'z': 0.75, 'Zatom': 14, 'fraction': 1.0, 'label':'Si'},
                       {'x': 0.75, 'y': 0.75, 'z': 0.25, 'Zatom': 14, 'fraction': 1.0, 'label':'Si'}]
    cryst['volume'] = 160.16493225097656

    return cryst

def structure_info(cryst):
    txt = ""
    txt += "name: %s\n"   %  (cryst['name']  )
    txt += "a: %f\n"      %  (cryst['a']     )
    txt += "b: %f\n"      %  (cryst['b']     )
    txt += "c: %f\n"      %  (cryst['c']     )
    txt += "alpha: %f\n"  %  (cryst['alpha'] )
    txt += "beta: %f\n"   %  (cryst['beta']  )
    txt += "gamma: %f\n"  %  (cryst['gamma'] )
    txt += "n_atom: %d\n" %  (cryst['n_atom'])
    txt += "volume: %f\n" %  (cryst['volume'])
    for atom in cryst['atom']:
        txt += "Z=%2d f:%3.1f xyz=(%5.3f, %5.3f, %5.3f)   %s \n"%(atom['Zatom'],atom['fraction'],
                    atom['x'],atom['y'],atom['z'],atom['label'])


    return txt

def structure_sepiolite():
    cryst = {} # cryst.copy()

    cryst['name'] = b"Sepiolite"
    cryst['a'] =  13.4
    cryst['b'] =  26.8
    cryst['c'] =  5.28
    cryst['alpha'] = 90.0
    cryst['beta'] =  90.0
    cryst['gamma'] = 90.0
    cryst['n_atom'] =  132
    cryst['atom'] = [
        {'Zatom':12     ,'fraction': 1.000 ,'x':     0.000 ,'y':   0.02800 ,'z':    0.2500,'label':'          Mg1'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.4720 ,'z':    0.2500,'label':'          Mg1'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':     0.000 ,'y':    0.9720 ,'z':    0.7500,'label':'          Mg1'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.5280 ,'z':    0.7500,'label':'          Mg1'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':     0.000 ,'y':    0.9160 ,'z':    0.2500,'label':'          Mg2'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.5840 ,'z':    0.2500,'label':'          Mg2'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    -0.000 ,'y':   0.08400 ,'z':    0.7500,'label':'          Mg2'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.4160 ,'z':    0.7500,'label':'          Mg2'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':     0.000 ,'y':    0.1400 ,'z':    0.2500,'label':'          Mg3'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.3600 ,'z':    0.2500,'label':'          Mg3'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':     0.000 ,'y':    0.8600 ,'z':    0.7500,'label':'          Mg3'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.6400 ,'z':    0.7500,'label':'          Mg3'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':     0.000 ,'y':    0.8040 ,'z':    0.2500,'label':'          Mg4'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.6960 ,'z':    0.2500,'label':'          Mg4'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    -0.000 ,'y':    0.1960 ,'z':    0.7500,'label':'          Mg4'},
        {'Zatom':12     ,'fraction': 1.000 ,'x':    0.5000 ,'y':    0.3040 ,'z':    0.7500,'label':'          Mg4'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2080 ,'y':   0.02800 ,'z':    0.5625,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7920 ,'y':   0.02800 ,'z':    0.9375,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7080 ,'y':    0.4720 ,'z':    0.9375,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2920 ,'y':    0.4720 ,'z':    0.5625,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7920 ,'y':    0.9720 ,'z':    0.4375,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2080 ,'y':    0.9720 ,'z':   0.06250,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2920 ,'y':    0.5280 ,'z':   0.06250,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7080 ,'y':    0.5280 ,'z':    0.4375,'label':'          Si1'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2080 ,'y':    0.1400 ,'z':    0.5625,'label':'          Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7920 ,'y':    0.1400 ,'z':    0.9375,'label':'          Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7080 ,'y':    0.3600 ,'z':    0.9375,'label':'          Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2920 ,'y':    0.3600 ,'z':    0.5625,'label':'          Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7920 ,'y':    0.8600 ,'z':    0.4375,'label':'         Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2080 ,'y':    0.8600 ,'z':   0.06250,'label':'         Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2920 ,'y':    0.6400 ,'z':   0.06250,'label':'         Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7080 ,'y':    0.6400 ,'z':    0.4375,'label':'         Si2'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2080 ,'y':    0.1960 ,'z':   0.06250,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7920 ,'y':    0.1960 ,'z':    0.4375,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7080 ,'y':    0.3040 ,'z':    0.4375,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2920 ,'y':    0.3040 ,'z':  0.06250 ,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7920 ,'y':    0.8040 ,'z':   0.9375 ,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2080 ,'y':    0.8040 ,'z':   0.5625 ,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.2920 ,'y':    0.6960 ,'z':   0.5625 ,'label':'         Si3'},
        {'Zatom':14     ,'fraction': 1.000 ,'x':    0.7080 ,'y':    0.6960 ,'z':   0.9375 ,'label':'         Si3'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.2500  ,'y':   0.2500  ,'z':  0.06250 ,'label':'       O1_O3'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.7500  ,'y':   0.2500  ,'z':   0.4375 ,'label':'       O1_O3'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.7500  ,'y':   0.7500  ,'z':   0.9375 ,'label':'       O1_O3'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.2500  ,'y':   0.7500  ,'z':   0.5625 ,'label':'       O1_O3'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08400  ,'y':  0.02800  ,'z':   0.5620 ,'label':'       O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9160  ,'y': 0.02800   ,'z':  0.9380  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.5840  ,'y':  0.4720   ,'z':  0.9380  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.4160  ,'y':  0.4720   ,'z':  0.5620  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9160  ,'y':  0.9720   ,'z':  0.4380  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08400  ,'y':  0.9720   ,'z': 0.06200  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.4160  ,'y':  0.5280   ,'z': 0.06200  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5840   ,'y':  0.5280   ,'z':  0.4380  ,'label':'      O2_O4'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08400  ,'y':   0.1400  ,'z':   0.5620 ,'label':'       O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9160  ,'y':   0.1400  ,'z':   0.9380 ,'label':'       O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.5840  ,'y':   0.3600  ,'z':   0.9380 ,'label':'       O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.4160  ,'y':   0.3600  ,'z':   0.5620 ,'label':'      O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.9160   ,'y':  0.8600   ,'z':  0.4380  ,'label':'      O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.08400   ,'y':  0.8600   ,'z': 0.06200  ,'label':'      O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.4160   ,'y':  0.6400   ,'z': 0.06200  ,'label':'      O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5840   ,'y':  0.6400   ,'z': 0.4380   ,'label':'     O3_O5'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.08400   ,'y':  0.1960   ,'z': .06200   ,'label':'     O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.9160   ,'y':  0.1960   ,'z': 0.4380   ,'label':'     O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5840   ,'y':  0.3040   ,'z': 0.4380   ,'label':'     O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.4160   ,'y':  0.3040   ,'z': .06200   ,'label':'     O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.9160   ,'y':  0.8040   ,'z': 0.9380   ,'label':'     O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.08400   ,'y':  0.8040   ,'z': 0.5620   ,'label':'     O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.4160   ,'y':  0.6960   ,'z': 0.5620   ,'label':'    O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5840   ,'y':  0.6960   ,'z': 0.9380   ,'label':'    O4_O6'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.2400   ,'y':   0.000   ,'z': 0.3120   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.7600   ,'y':   0.000   ,'z': 0.1880   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.7400   ,'y':  0.5000   ,'z': 0.1880   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.2600   ,'y': 0.5000    ,'z': 0.3120   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.7600   ,'y':  0.000    ,'z': 0.6880   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.2400   ,'y':  0.000    ,'z': 0.8120   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.2600   ,'y': 0.5000    ,'z': 0.8120   ,'label':'    O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.7400   ,'y': 0.5000    ,'z': 0.6880   ,'label':'     O5_O7'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2400    ,'y': 0.08400   ,'z': 0.5620   ,'label':'   O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7600    ,'y': 0.08400   ,'z': 0.9380   ,'label':'   O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7400    ,'y': 0.4160    ,'z': 0.9380   ,'label':'     O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2600    ,'y': 0.4160    ,'z': 0.5620   ,'label':'     O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7600    ,'y': 0.9160    ,'z': 0.4380   ,'label':'     O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2400    ,'y': 0.9160    ,'z': 0.06200  ,'label':'  O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2600    ,'y': 0.5840    ,'z': 0.06200  ,'label':'  O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7400    ,'y': 0.5840    ,'z': 0.4380   ,'label':'     O6_O8'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2400    ,'y': 0.1680    ,'z': 0.3120   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7600    ,'y': 0.1680    ,'z': 0.1880   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7400    ,'y': 0.3320    ,'z': 0.1880   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2600    ,'y': 0.3320    ,'z': 0.3120   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7600    ,'y': 0.8320    ,'z': 0.6880   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2400    ,'y': 0.8320    ,'z': 0.8120   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.2600    ,'y': 0.6680    ,'z': 0.8120   ,'label':'     O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.7400    ,'y': 0.6680    ,'z': 0.6880   ,'label':'    O7_O9'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.2400   ,'y':  0.1680   ,'z':  0.8120  ,'label':'     O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.7600   ,'y':  0.1680   ,'z':  0.6880  ,'label':'    O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.7400  ,'y':   0.3320  ,'z':   0.6880 ,'label':'      O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.2600  ,'y':   0.3320  ,'z':   0.8120 ,'label':'     O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.7600  ,'y':   0.8320  ,'z':   0.1880 ,'label':'     O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.2400  ,'y':   0.8320  ,'z':   0.3120 ,'label':'     O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.2600  ,'y':   0.6680  ,'z':   0.3120 ,'label':'     O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.7400  ,'y':   0.6680  ,'z':   0.1880 ,'label':'     O8_O10'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08400  ,'y':  0.08400  ,'z': 0.06200  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9160  ,'y':  0.08400  ,'z':  0.4380  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.5840  ,'y':   0.4160  ,'z':  0.4380  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.4160  ,'y':   0.4160  ,'z': 0.06200  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9160  ,'y':   0.9160  ,'z':  0.9380  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08400  ,'y':   0.9160  ,'z':  0.5620  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.4160  ,'y':   0.5840  ,'z':  0.5620  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.5840  ,'y':   0.5840  ,'z':  0.9380  ,'label':'     OH_O11'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08300  ,'y':   0.2500  ,'z':  0.5000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9170  ,'y':   0.2500  ,'z':   0.000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.5830  ,'y':   0.2500  ,'z':   0.000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.4170  ,'y':   0.2500  ,'z':  0.5000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.9170  ,'y':   0.7500  ,'z':  0.5000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.08300  ,'y':   0.7500  ,'z':   0.000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.4170   ,'y':  0.7500   ,'z':   0.000  ,'label':'     CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5830   ,'y':  0.7500   ,'z':  0.5000  ,'label':'    CW_O12'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.08300   ,'y':  0.4160   ,'z':  0.9167  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.9170   ,'y':  0.4160   ,'z':  0.5833  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5830   ,'y': 0.08400   ,'z':  0.5833  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.4170   ,'y': 0.08400   ,'z':  0.9167  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.9170   ,'y':  0.5840   ,'z': 0.08330  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x': 0.08300   ,'y':  0.5840   ,'z':  0.4167  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.4170   ,'y':  0.9160   ,'z':  0.4167  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5830   ,'y':  0.9160   ,'z': 0.08330  ,'label':'   ZW1_O13'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.000   ,'y':  0.6720   ,'z':  0.2500  ,'label':'  W2_O1(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5000   ,'y':  0.8280   ,'z':  0.2500  ,'label':'  W2_O1(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.000   ,'y':  0.3280   ,'z':  0.7500  ,'label':'  W2_O1(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5000   ,'y':  0.1720   ,'z':  0.7500  ,'label':'  W2_O1(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.000   ,'y':  0.4850   ,'z':  0.2500  ,'label':'  W3_O2(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':  0.5000   ,'y': 0.01500   ,'z':  0.2500  ,'label':'  W3_O2(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.000   ,'y':  0.5150   ,'z':  0.7500  ,'label':'  W3_O2(4)'},
        {'Zatom':8      ,'fraction':1.000  ,'x':   0.5000  ,'y':   0.9850  ,'z':   0.7500 ,'label':'   ZW3_O2(4)'} ]



    cryst['volume'] = cryst['a'] * cryst['b'] * cryst['c']

    return cryst

def structure_palygorskiteO():
    cryst = {} # cryst.copy()

    cryst['name']   = b"PalygorskiteO"
    cryst['a']      =  12.78
    cryst['b']      =  17.89
    cryst['c']      =  5.21
    cryst['alpha']  = 90.0
    cryst['beta']   = 90.0
    cryst['gamma']  = 90.0
    cryst['n_atom'] = 84
    cryst['volume'] = cryst['a'] * cryst['b'] * cryst['c']

    cryst['atom']   = [
        {'Zatom': 13, 'fraction': 1.000, 'x':   0.000  ,'y':  0.08333   ,'z':   0.5000  ,'label': '   Al  '},
        {'Zatom': 13, 'fraction': 1.000, 'x':  0.5000  ,'y':   0.4166   ,'z':   0.5000  ,'label': '   Al  '},
        {'Zatom': 13, 'fraction': 1.000, 'x':   0.000  ,'y':   0.9166   ,'z':   0.5000  ,'label': '   Al  '},
        {'Zatom': 13, 'fraction': 1.000, 'x':  0.5000  ,'y':   0.5833   ,'z':   0.5000  ,'label': '   Al  '},
        {'Zatom': 12, 'fraction': 1.000, 'x':   0.000  ,'y':   0.1666   ,'z':    0.000  ,'label': '   Mg  '},
        {'Zatom': 12, 'fraction': 1.000, 'x':  0.5000  ,'y':   0.3333   ,'z':    0.000  ,'label': '   Mg  '},
        {'Zatom': 12, 'fraction': 1.000, 'x':   0.000  ,'y':   0.8333   ,'z':    0.000  ,'label': '   Mg  '},
        {'Zatom': 12, 'fraction': 1.000, 'x':  0.5000  ,'y':   0.6666   ,'z':    0.000  ,'label': '   Mg  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2083  ,'y':  0.08333   ,'z':   0.8333  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2916  ,'y':   0.4166   ,'z':   0.8333  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7083  ,'y':   0.4166   ,'z':   0.1666  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7916  ,'y':  0.08333   ,'z':   0.1666  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7916  ,'y':   0.9166   ,'z':   0.1666  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7083  ,'y':   0.5833   ,'z':   0.1666  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2916  ,'y':   0.5833   ,'z':   0.8333  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2083  ,'y':   0.9166   ,'z':   0.8333  ,'label': '  Si1  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2083  ,'y':   0.1666   ,'z':   0.3333  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2916  ,'y':   0.3333   ,'z':   0.3333  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7083  ,'y':   0.3333   ,'z':   0.6666  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7916  ,'y':   0.1666   ,'z':   0.6666  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7916  ,'y':   0.8333   ,'z':   0.6666  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.7083  ,'y':   0.6666   ,'z':   0.6666  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2916  ,'y':   0.6666   ,'z':   0.3333  ,'label': '  Si2  '},
        {'Zatom': 14, 'fraction': 1.000, 'x':  0.2083  ,'y':   0.8333   ,'z':   0.3333  ,'label': '  Si2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':    0.000   ,'z':   0.3333  ,'label': '   OH  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.5000   ,'z':   0.3333  ,'label': '   OH  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.5000   ,'z':   0.6666  ,'label': '   OH  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':    0.000   ,'z':   0.6666  ,'label': '   OH  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':  0.08333   ,'z':   0.8333  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.4166   ,'z':   0.8333  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.4166   ,'z':   0.1666  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':  0.08333   ,'z':   0.1666  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':   0.9166   ,'z':   0.1666  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.5833   ,'z':   0.1666  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.5833   ,'z':   0.8333  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':   0.9166   ,'z':   0.8333  ,'label': '   O1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':   0.1666   ,'z':   0.3333  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.3333   ,'z':   0.3333  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.3333   ,'z':   0.6666  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':   0.1666   ,'z':   0.6666  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':   0.8333   ,'z':   0.6666  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.6666   ,'z':   0.6666  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.6666   ,'z':   0.3333  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':   0.8333   ,'z':   0.3333  ,'label': '   O2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':   0.2500   ,'z':   0.8333  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.2500   ,'z':   0.8333  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.2500   ,'z':   0.1666  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':   0.2500   ,'z':   0.1666  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.9166  ,'y':   0.7500   ,'z':   0.1666  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5833  ,'y':   0.7500   ,'z':   0.1666  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.4166  ,'y':   0.7500   ,'z':   0.8333  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x': 0.08333  ,'y':   0.7500   ,'z':   0.8333  ,'label': ' H2OB  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':    0.000   ,'z':   0.8333  ,'label': '   O3  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.5000   ,'z':   0.8333  ,'label': '   O3  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.5000   ,'z':   0.1666  ,'label': '   O3  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':    0.000   ,'z':   0.1666  ,'label': '   O3  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.2500   ,'z':   0.3333  ,'label': '   O4  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.2500   ,'z':   0.6666  ,'label': '   O4  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.7500   ,'z':   0.6666  ,'label': '   O4  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.7500   ,'z':   0.3333  ,'label': '   O4  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.1250   ,'z':   0.5833  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.3750   ,'z':   0.5833  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.3750   ,'z':   0.4166  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.1250   ,'z':   0.4166  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.8750   ,'z':   0.4166  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.6250   ,'z':   0.4166  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.6250   ,'z':   0.5833  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.8750   ,'z':   0.5833  ,'label': '   O5  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.1250   ,'z':  0.08333  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.3750   ,'z':  0.08333  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.3750   ,'z':   0.9166  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.1250   ,'z':   0.9166  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.8750   ,'z':   0.9166  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.7500  ,'y':   0.6250   ,'z':   0.9166  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.6250   ,'z':  0.08333  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.2500  ,'y':   0.8750   ,'z':  0.08333  ,'label': '   O6  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':   0.000  ,'y':   0.3333   ,'z':   0.5000  ,'label': '  ZW1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5000  ,'y':   0.1666   ,'z':   0.5000  ,'label': '  ZW1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':   0.000  ,'y':   0.6666   ,'z':   0.5000  ,'label': '  ZW1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5000  ,'y':   0.8333   ,'z':   0.5000  ,'label': '  ZW1  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':   0.000  ,'y':   0.4166   ,'z':    0.000  ,'label': '  ZW2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5000  ,'y':  0.08333   ,'z':    0.000  ,'label': '  ZW2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':   0.000  ,'y':   0.5833   ,'z':    0.000  ,'label': '  ZW2  '},
        {'Zatom': 8., 'fraction': 1.000, 'x':  0.5000  ,'y':   0.9166   ,'z':    0.000  ,'label': '  ZW2  '}  ]

    return cryst


def structure_group(cryst1,cryst2,axis='a'):
    cryst = {} # cryst.copy()

    cryst['name'] = cryst1['name']+b"+"+cryst2['name']
    if axis == 'a':
        cryst['a'] =  cryst1['a'] + cryst2['a']
        cryst['b'] =  cryst1['b']
        cryst['c'] =  cryst1['c']
        if cryst1['b'] != cryst2['b']:
            print("Warning: b axes are not the same!")
        if cryst1['c'] != cryst2['c']:
            print("Warning: c axes are not the same (taken the first one)!")
    elif axis == 'b':
        cryst['a'] =  cryst1['a']
        cryst['b'] =  cryst1['b'] + cryst2['b']
        cryst['c'] =  cryst1['c']
        if cryst1['a'] != cryst2['a']:
            print("Warning: a axes are not the same (taken the first one)!")
        if cryst1['c'] != cryst2['c']:
            print("Warning: c axes are not the same (taken the first one)!")
    elif axis == 'c':
        cryst['a'] =  cryst1['a']
        cryst['b'] =  cryst1['b']
        cryst['c'] =  cryst1['c'] + cryst2['c']
        if cryst1['b'] != cryst2['b']:
            print("Warning: b axes are not the same (taken the first one)!")
        if cryst1['a'] != cryst2['a']:
            print("Warning: a axes are not the same (taken the first one)!")
    else:
        raise Exception("Error: Bad grouping axis.")

    cryst['alpha'] = cryst1['alpha']
    cryst['beta'] =  cryst1['beta']
    cryst['gamma'] = cryst1['gamma']

    cryst['n_atom'] =  cryst1['n_atom'] + cryst2['n_atom']

    tmp = []
    for at1 in cryst1['atom']:
        at11 = at1.copy()
        if axis == 'a':
            scale = cryst1['a'] / (cryst1['a'] + cryst2['a'])
            at11['x'] *= scale
        if axis == 'b':
            scale = cryst1['b'] / (cryst1['b'] + cryst2['b'])
            at11['y'] *= scale
        if axis == 'c':
            scale = cryst1['c'] / (cryst1['c'] + cryst2['c'])
            at11['z'] *= scale
        tmp.append(at11)

    for at1 in cryst2['atom']:
        at11 = at1.copy()
        if axis == 'a':
            scale = cryst2['a'] / (cryst1['a'] + cryst2['a'])
            at11['x'] *= scale
            at11['x'] += cryst1['a'] / (cryst1['a'] + cryst2['a'])
        if axis == 'b':
            scale = cryst2['b'] / (cryst1['b'] + cryst2['b'])
            at11['y'] *= scale
            at11['y'] += cryst1['a'] / (cryst1['a'] + cryst2['a'])
        if axis == 'c':
            scale = cryst2['c'] / (cryst1['c'] + cryst2['c'])
            at11['z'] *= scale
            at11['z'] += cryst1['a'] / (cryst1['a'] + cryst2['a'])
        tmp.append(at11)

    cryst['atom'] = tmp

    cryst['volume'] = cryst['a'] * cryst['b'] * cryst['c']
    return cryst


def lorentz(theta_bragg_deg):
    tr = theta_bragg_deg * numpy.pi / 180.
    polarization_factor = 0.5 * (1.0 + (numpy.cos(2.0 * tr))**2)
    lorentz_factor = 1.0 / numpy.sin(2.0 * tr)
    geometrical_factor = 1.0 * numpy.cos(tr) / numpy.sin(2.0 * tr)

    return polarization_factor*lorentz_factor*geometrical_factor


def plot_lines(x1,y1,xtitle=r"$2\theta$",ytitle="Intensity",toptitle="",noblock=0):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = numpy.repeat(x1,3)
    y = numpy.zeros_like(x)
    idx = -1
    for i in range(x1.size):
        idx += 1
        y[idx] = 0.0
        idx += 1
        y[idx] = y1[i]
        idx += 1
        y[idx] = 0.0

    numBins = 50
    ax.plot(x,y,color='green')
    plt.title(toptitle)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)

    if noblock == 0:
        plt.show()

def calculate_reflections(cryst,wavelength_in_A=1.0,debyeWaller=1.0,rel_angle=1.0,twotheta_max=30.0,structure_factor_min=1e-3,file_out="",verbose=1):
    """
    Calculate crystal reflections
    :param cryst: crystal structure
    :param wavelength_in_A: photon wavelength in m (default=1A)
    :param debyeWaller: Debye-Waller term (default=1.0)
    :param rel_angle: for structure factors, incident angle/ Bragg angle (default=1.0)
    :param twotheta_max: Maximum 2theta for simulations in degrees (default=30 deg)
    :param structure_factor_min: minimum value for structure factor for considering the reflectio.
                 Set to a negative value to consider all reflections
    :return: a numpy array [8,nreflections] with first index:
             0 = miller index h
             1 = miller index k
             2 = miller index l
             3 = dspacing in A
             4 = |Real(Fh)} with Fh the structure factor
             5 = 2thete: Twice the Bragg angle
             6 = multiplicity of the reflection
             7 = intensity (arbitrary units)
             8 = intensity (% of highest reflection)

    """
    photon_energy_in_keV = ev2meter / (wavelength_in_A*1e-10)


    # get limits of indices
    dspacingmin = wavelength_in_A / 2 / numpy.sin(twotheta_max / 2 * numpy.pi / 180)
    print("dspacingmin: ",dspacingmin)
    hmax = int(cryst['a']/dspacingmin)
    kmax = int(cryst['b']/dspacingmin)
    lmax = int(cryst['c']/dspacingmin)


    # loop over all reflections
    nmiller = (2*hmax+1)*(2*kmax+1)*(2*lmax+1)-1
    out = numpy.zeros((9,nmiller))
    print("Total number of h k l permutations: %d"%nmiller)

    idx = -1
    for hh in range(-hmax,hmax+1):
        for kk in range(-kmax,kmax+1):
            for ll in range(-lmax,lmax+1):
                if hh == 0 and kk == 00 and ll == 00: continue
                dspacing = xraylib.Crystal_dSpacing(cryst,hh,kk,ll )
                fH = xraylib.Crystal_F_H_StructureFactor(cryst, photon_energy_in_keV, hh, kk, ll, debyeWaller, rel_angle)
                idx += 1
                # print("hkl: %3d %3d %3d, %5.3f A, F=%5.1f, idx:%4d"%(hh,kk,ll,dspacing, numpy.abs(numpy.real(fH)),idx))
                out[0,idx] = hh
                out[1,idx] = kk
                out[2,idx] = ll
                out[3,idx] = dspacing
                out[4,idx] = numpy.abs(numpy.real(fH))
                # out[5,idx] = xraylib.Bragg_angle(cryst,photon_energy_in_keV,hh,kk,ll ) * 2 * 180 / numpy.pi #2theta in deg
                out[5,idx] = numpy.arcsin(wavelength_in_A/2/dspacing) * 180.0 / numpy.pi * 2
                out[6,idx] = 1.0 # reserved for multiplicity
                # reserved for intensity out[7,idx]
                # reserved for normalized intensity out[8,idx]
    n = out.shape[1]

    #
    # remove forbidden (or low intensity) reflections
    #

    if structure_factor_min >= 0:
        igood = numpy.where( out[4,:] > structure_factor_min)
        igood = numpy.array(igood)
        igood.shape = -1
        print("igood (forbiden) shape: ",igood.shape)
        out = out[:,igood]
        n = out.shape[1]
        print("shape arter removing forbidden: ",out.shape)


    #
    # group by multiplicity
    #

    if 1:
        # define a flag that distinguishes different reflections
        out_flag = numpy.abs(out[0,:]) + numpy.abs(out[1,:]) * 2 + numpy.abs(out[2,:]) * 4
        tmp = out[5,:] * (1.0 + out_flag * 1e-5)
        shit, igood = numpy.unique(tmp, return_index=True)

        igood = numpy.array(igood)
        igood.shape = -1
        n = igood.shape[0]
        print("igood (multiplicity) shape: ",igood.shape)

        out = out[:,igood]
        tmp2 = tmp[igood]

        # set multiplicities
        for i in range(n):
            print(i, numpy.array(numpy.where(tmp == tmp2[i])).size )
            out[6,i] = numpy.array(numpy.where(tmp == tmp2[i])).size




    #
    # compute intensities
    #
    for i in range(n):
        # M * F**2 * lorent_etc
        intensity = out[6,i] * out[4,i]**2 * lorentz(0.5*out[5,i])
        print("hkl, M, F, L:",out[0,i],out[1,i],out[2,i],out[6,i],out[4,i],lorentz(0.5*out[5,i]))
        out[7,i] = intensity

    intensity_max =  out[7,:].max()
    print("intensity: ", out[7,:])
    print("intensity_max: ",intensity_max)

    for i in range(n):
        out[8,i] = 100 * out[7,i] / intensity_max

    #
    # remove reflections at theta >
    #
    igood = numpy.where( out[5,:] <= twotheta_max)
    igood = numpy.array(igood)
    igood.shape = -1
    out = out[:,igood]


    txt = ("%4s "*3+"%15s "*4+"%15s "+"%15s "+"\n")%('h','k','l','2*Theta','d-spc','|F|','M','IntAll','IntNorm')
    # ,format='(3A4,4A15,A15,2A15)')
    n = out.shape[1]
    # 0 = miller index h
    # 1 = miller index k
    # 2 = miller index l
    # 3 = dspacing in A
    # 4 = |Real(Fh)} with Fh the structure factor
    # 5 = 2thete: Twice the Bragg angle
    # 6 = multiplicity of the reflection
    # 7 = intensity (arbitrary units)
    # 8 = intensity (% of highest reflection)
    for i in range(n):
        txt += "%4d %4d %4d %15.5f %15.5f %15.5f %15d %15.5f %15.5f \n"%(
                out[0,i],out[1,i],out[2,i],
                out[5,i],out[3,i],out[4,i],out[6,i],out[7,i],out[8,i])

    if file_out != "":
        f = open(file_out,'w')
        f.write(txt)
        f.close()

    if verbose:
        print(txt)

    return out.copy()

def test_sepiolite_pattern():
    cryst =  structure_sepiolite()

    out = calculate_reflections(cryst, wavelength_in_A=1.0, twotheta_max=30.0, structure_factor_min=1e-3,file_out="",verbose=1)

    print("out shape",out.shape)
    plot_lines(out[5,:],out[8,:])

def test_group_si():
    si = structure_silicon()
    out = calculate_reflections(si, wavelength_in_A=1.0, twotheta_max=60.0, structure_factor_min=1e-3,file_out="",verbose=1)
    plot_lines(out[5,:],out[8,:],toptitle="Si",noblock=1)

    #
    #

    ss = structure_group(si,si,axis='a')
    ss_ss = structure_group(ss,ss,axis='b')
    ss_ss_ss = structure_group(ss_ss,ss_ss,axis='c')

    out = calculate_reflections(ss_ss_ss, wavelength_in_A=1.0, twotheta_max=60.0, structure_factor_min=1e-3,file_out="",verbose=1)
    plot_lines(out[5,:],out[8,:],toptitle="SiSi",noblock=0)



    print(structure_info(si))

    print(structure_info(ss_ss_ss))

def test_group_sepiolite():
    s = structure_sepiolite()
    out = calculate_reflections(s, wavelength_in_A=1.0, twotheta_max=15.0, structure_factor_min=1e-3,file_out="",verbose=1)
    plot_lines(out[5,:],out[8,:],toptitle="Sepiolite",noblock=1)

    #
    #

    ss = structure_group(s,s,axis='a')
    ss_ss = structure_group(ss,ss,axis='b')
    ss_ss_ss = structure_group(ss_ss,ss_ss,axis='c')
    #
    out = calculate_reflections(ss_ss_ss, wavelength_in_A=1.0, twotheta_max=15.0, structure_factor_min=1e-3,file_out="",verbose=1)
    plot_lines(out[5,:],out[8,:],toptitle="Supercell",noblock=0)



    print(structure_info(s))

    print(structure_info(ss_ss_ss))

def test_group_ab(a=structure_sepiolite(),b=structure_palygorskiteO()):

    out = calculate_reflections(a, wavelength_in_A=1.0, twotheta_max=15.0, structure_factor_min=1e-3,file_out="",verbose=1)
    plot_lines(out[5,:],out[8,:],toptitle=a['name'],noblock=1)

    #
    #
    #
    ab = structure_group(a,b,axis='a')
    ab_ab = structure_group(ab,ab,axis='b')
    ab_ab_ab = structure_group(ab_ab,ab_ab,axis='c')
    #
    out = calculate_reflections(ab_ab_ab, wavelength_in_A=1.0, twotheta_max=15.0, structure_factor_min=1e-3,file_out="",verbose=1)
    plot_lines(out[5,:],out[8,:],toptitle=ab_ab_ab['name'],noblock=0)


    print(structure_info(ab_ab_ab))

if __name__ == "__main__":

    # test_sepiolite_pattern()

    # test_group_si()

    # test_group_sepiolite()

    test_group_ab(a=structure_palygorskiteO(),b=structure_palygorskiteO())

