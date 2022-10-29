from decimal import *
import math

gravitational_constant = 6.6743E-11
radius_sun = 6.9634E8
radius_earth = 6.3781E6
m_1 = mass_sun = 1.989E30
m_2 = mass_earth = 5.972E24

r_i = 148.6E9
r_f = radius_sun + radius_earth
delta_s = r_i - r_f

dt = Decimal(0.005)
t = Decimal(0)
v = Decimal(0)
r = Decimal(r_i)
r_prev = Decimal(r_i)

while r > r_f:
    a = - Decimal(gravitational_constant * (m_1 + m_2)) / pow(r + (r - r_prev) * Decimal(0.5), 2)
    v += a * Decimal(0.5) * dt
    r_prev = r
    r += v * dt 
    v += a * Decimal(0.5) * dt
    t += dt

print('According to our full final equation, the following should be the time in seconds:')
print(- math.sqrt(r_i / (2*gravitational_constant*(m_1 + m_2))) * (r_i * (math.atan(math.sqrt(r_f / delta_s)) - 0.5 * math.pi) - math.sqrt(r_f * delta_s)))

print("And according to the Kepler equation, we get:")
print(math.pi * math.sqrt(pow(r_i, 3) / (8 * gravitational_constant * (m_1 + m_2))))