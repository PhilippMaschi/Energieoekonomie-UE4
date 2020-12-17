# -*- coding: utf-8 -*-


import numpy as np

pe = np.array([160, 120, 80, 40, 0])
E = 80 - 0.5*pe
# Preisänderung ist immer 40:
delta_pe = 40
# Nachfrageänderung ist immer 20:
delta_E = 20

alpha = (delta_E/E) / (delta_pe/pe)

print(alpha)


#%%



#%%%
pe0 = 160
delta_pe = 160 - pe

E0 = 80 - 0.5*0
delta_E = 80 - 0.5*delta_pe

# Preiselastizität alpha:
alpha = delta_E/E0 / delta_pe/pe0




