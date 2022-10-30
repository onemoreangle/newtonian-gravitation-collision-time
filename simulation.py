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

dt = Decimal(0.001)
t = Decimal(0)
v = Decimal(0)
r = Decimal(r_i)

while r > r_f:
    r += v * dt
    a = - Decimal(gravitational_constant * (m_1 + m_2)) / Decimal(pow(r, 2))
    v += a * dt
    t += dt

print('With a dt of ' + str(dt) + ' our simulation time in seconds is')
print(t)

print('According to our full final equation, the following should be the time in seconds:')
print(- math.sqrt(r_i / (2*gravitational_constant*(m_1 + m_2))) * (r_i * (math.atan(math.sqrt(r_f / delta_s)) - 0.5 * math.pi) - math.sqrt(r_f * delta_s)))

print("And according to the Kepler equation, we get:")
print(math.pi * math.sqrt(pow(r_i, 3) / (8 * gravitational_constant * (m_1 + m_2))))