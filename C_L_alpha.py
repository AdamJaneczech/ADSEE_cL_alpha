import math
import matplotlib.pyplot as plt
import numpy as np

#graph settings
x_min = -20 # deg
x_max = 22 # deg
y_min = -1.5
y_max = 2

alpha = np.arange(math.radians(-20),math.radians(20),math.radians(0.25)) #quarter degree range
#print(alpha)
b = 28.08 #m
S = 93.5 #m^2
A = pow(b,2)/S #aspect ratio
alpha_zero_lift = math.radians(-1.8)
#chords
c_r = 5.39
c_t = 1.27
lambda_LE = math.radians(21.2)

beta = 1

V_approach = 65.84889 #m/s

M_cruise = V_approach/math.sqrt(1.4*287*288.15)

eta = 0.95 #airfoil eff. factor

c_L_max = 1.5 #DUMMY VALUE!!!

#xy origin at the leading edge of the root chord (x span-dir, y chord-dir)
y_pos_half_c_root = c_r/2
y_pos_half_c_tip = math.tan(lambda_LE) * 0.5 * b + c_t/2
y_pos_half_c_diff = abs(y_pos_half_c_tip - y_pos_half_c_root)

lambda_half_c = math.atan(y_pos_half_c_diff/(b/2))

c_L_alpha = (2 * math.pi * A)/(2+math.sqrt(4+pow(A*beta/eta,2)*(1+(pow(math.tan(lambda_half_c),2)/pow(beta,2)))))

c_L = np.array(c_L_alpha * (alpha - alpha_zero_lift))

plt.plot(np.rad2deg(alpha), c_L, label='C_L_alpha')
plt.axhline(c_L_max, x_min, x_max, color='r', label='maximum c_L')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(x_min,x_max,1))
plt.yticks(np.arange(y_min,y_max,0.1))
plt.ylabel('C_L')
plt.xlabel('alpha')
plt.legend()
plt.show()