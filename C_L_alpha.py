import math
import matplotlib.pyplot as plt
import numpy as np

#graph settings
x_min = -10 # deg
x_max = 22 # deg
y_min = -0.2
y_max = 3

alpha = np.arange(math.radians(-10),math.radians(22),math.radians(0.25)) #quarter degree range
#print(alpha)
b = 28.08 #m
S = 93.5 #m^2
A = pow(b,2)/S #aspect ratio
alpha_zero_lift = math.radians(-1.8)
alpha_zero_lift_flapped = math.radians(-7.2) - alpha_zero_lift
alpha_stall = math.radians(12.4)
alpha_stall_flapped = math.radians(9.1)
#chords
c_r = 5.39
c_t = 1.27
lambda_LE = math.radians(21.2)

beta = 1

V_approach = 65.84889 #m/s

M_cruise = V_approach/math.sqrt(1.4*287*288.15)

eta = 0.95 #airfoil eff. factor

c_L_max = 0.96
c_L_max_flapped = 2.36

#xy origin at the leading edge of the root chord (x span-dir, y chord-dir)
y_pos_half_c_root = c_r/2
y_pos_half_c_tip = math.tan(lambda_LE) * 0.5 * b + c_t/2
y_pos_half_c_diff = abs(y_pos_half_c_tip - y_pos_half_c_root)

lambda_half_c = math.atan(y_pos_half_c_diff/(b/2))

c_L_alpha = (2 * math.pi * A)/(2+math.sqrt(4+pow(A*beta/eta,2)*(1+(pow(math.tan(lambda_half_c),2)/pow(beta,2)))))
c_L_alpha_flapped = c_L_alpha * 1.85
print(c_L_alpha_flapped)

c_L = np.array(c_L_alpha * (alpha - alpha_zero_lift))
c_L_flapped = np.array(c_L_alpha_flapped * (alpha - alpha_zero_lift_flapped))

plt.plot(np.rad2deg(alpha), c_L, label='C_L_alpha', color = '#51BBFE')
plt.plot(np.rad2deg(alpha), c_L_flapped, label='C_L_alpha with flaps', color = '#8FF7A7')
plt.axhline(c_L_max, x_min, x_max, color='r', label='Maximum C_L without flaps', c = '#51BBFE', linestyle = 'dotted')
plt.axhline(c_L_max_flapped, x_min, x_max, color='y', label='Maximum C_L with flaps', c = '#8FF7A7', linestyle = 'dotted')
plt.axvline(math.degrees(alpha_stall), y_min, y_max, c='#51BBFE', label='Alpha_stall without flaps', linestyle = 'dotted')
plt.axvline(math.degrees(alpha_stall_flapped), y_min, y_max, c='#8FF7A7', label='Alpha_stall with flaps', linestyle = 'dotted')

plt.axhline(0, x_min, x_max, color='black')
plt.axvline(0, y_min, y_max, color = 'black')
plt.text(x_max - 2, y_min, 'C_L = 0')
plt.text(0 + 0.5, y_max - 0.25, 'Alpha = 0')

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(x_min,x_max,1))
plt.yticks(np.arange(y_min,y_max,0.2))
plt.ylabel('C_L')
plt.xlabel('Alpha')
plt.legend()
plt.show()