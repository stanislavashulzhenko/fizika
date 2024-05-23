import sympy
from math import sqrt
from sympy import symbols, diff

# Konstantes

g=9.81 # Brīvās krišanas paātrinājums (m/s^2)
ml=0.01397 # Lodītes masa (kg)
mr=0.1372 # Rāmīša masa (kg)
l=0.749 # Vītnes garums (m)
r=0.0075 # Lodītes radiuss (m)
st_5=2.78 # Stjūdenta koeficients pie n=5
st_bezg=1.96 # Stjūdenta koeficients pie n=bezgalība
h_1=0.705 # Augstums 1. (m)
h_2=0.605 # Augstums 2. (m)
h_3=0.505 # Augstums 5. (m)
h_4=0.305 # Augstums 4. (m)
h_5=0.105 # Augstums 3. (m)

mv_m=0.00001 # Mazāka vertība masai (kg)
mv_l=0.001 # Mazāka vertība garumam (m)
mv_r=0.0005 # Mazāka vertība radiusam (m)
mv_s=0.001 # Mazāka vertība novirzei (m)

# Mērījumi 
# Rāmīša novirze pie h_1 (m)

s1_1=0.066 
s1_2=0.065
s1_3=0.064
s1_4=0.064
s1_5=0.064

# Rāmīša novirze pie h_2 (m)

s2_1=0.06 
s2_2=0.06
s2_3=0.06
s2_4=0.061
s2_5=0.062

# Rāmīša novirze pie h_3 (m)

s3_1=0.055 
s3_2=0.053
s3_3=0.057
s3_4=0.059
s3_5=0.056

# Rāmīša novirze pie h_4 (m)

s4_1=0.043 
s4_2=0.042
s4_3=0.042
s4_4=0.041
s4_5=0.04

# Rāmīša novirze pie h_5 (m)

s5_1=0.021 
s5_2=0.022
s5_3=0.023
s5_4=0.022
s5_5=0.023

# Lodītes ātrums (digitāli) pie h_1 (m/s)

v1_1d=2.963
v1_2d=2.996
v1_3d=2.96
v1_4d=2.989
v1_5d=3.002

# Lodītes ātrums (digitāli) pie h_4 (m/s)

v2_1d=1.759
v2_2d=1.765
v2_3d=1.826
v2_4d=1.77
v2_5d=1.763

# Lodītes ātrums (digitāli) pie h_5 (m/s)

v3_1d=1.011
v3_2d=1.013
v3_3d=1.014
v3_4d=0.988
v3_5d=0.987

# ------------------------------------------------------------------------------------------------------------------------------
# Tiešie mērījumi
# Aprēķini pie h_1

s1_vid=round((s1_1+s1_2+s1_3+s1_4+s1_5)/5, 3) 
s1_kv=round(sqrt(((s1_1-s1_vid)**2+(s1_2-s1_vid)**2+(s1_3-s1_vid)**2+(s1_4-s1_vid)**2+(s1_5-s1_vid)**2)/(5*4)), 6)
gad_kluda_s1=round(s1_kv*st_5, 3)
sist_kluda_s1=round(mv_s/3*st_bezg, 5)

if gad_kluda_s1 <= sist_kluda_s1:
  abs_kluda_s1 = sist_kluda_s1 
elif gad_kluda_s1 > sist_kluda_s1:
  abs_kluda_s1 = gad_kluda_s1  

rel_kluda_s1=round(abs_kluda_s1/s1_vid * 100, 2)



# Aprēķini pie h_2

s2_vid=round((s2_1+s2_2+s2_3+s2_4+s2_5)/5, 3) 
s2_kv=round(sqrt(((s2_1-s2_vid)**2+(s2_2-s2_vid)**2+(s2_3-s2_vid)**2+(s2_4-s1_vid)**2+(s2_5-s1_vid)**2)/(5*4)), 6)
gad_kluda_s2=round(s2_kv*st_5, 3)
sist_kluda_s2=round(mv_s/3*st_bezg, 5)

if gad_kluda_s2 <= sist_kluda_s2:
  abs_kluda_s2 = sist_kluda_s2 
elif gad_kluda_s2 > sist_kluda_s2:
  abs_kluda_s2 = gad_kluda_s2  

rel_kluda_s2=round(abs_kluda_s2/s2_vid * 100, 2)




# Aprēķini pie h_3

s3_vid=round((s3_1+s3_2+s3_3+s3_4+s3_5)/5, 3) 
s3_kv=round(sqrt(((s3_1-s3_vid)**2+(s3_2-s3_vid)**2+(s3_3-s3_vid)**2+(s3_4-s3_vid)**2+(s3_5-s3_vid)**2)/(5*4)), 6)
gad_kluda_s3=round(s3_kv*st_5, 3)
sist_kluda_s3=round(mv_s/3*st_bezg, 5)

if gad_kluda_s3 <= sist_kluda_s3:
  abs_kluda_s3 = sist_kluda_s3 
elif gad_kluda_s3 > sist_kluda_s3:
  abs_kluda_s3 = gad_kluda_s3  

rel_kluda_s3=round(abs_kluda_s3/s3_vid * 100, 2)



# Aprēķini pie h_4

s4_vid=round((s4_1+s4_2+s4_3+s4_4+s4_5)/5, 3) 
s4_kv=round(sqrt(((s4_1-s4_vid)**2+(s4_2-s4_vid)**2+(s4_3-s4_vid)**2+(s4_4-s4_vid)**2+(s4_5-s4_vid)**2)/(5*4)), 6)
gad_kluda_s4=round(s4_kv*st_5, 3)
sist_kluda_s4=round(mv_s/3*st_bezg, 5)

if gad_kluda_s4 <= sist_kluda_s4:
  abs_kluda_s4 = sist_kluda_s4 
elif gad_kluda_s4 > sist_kluda_s4:
  abs_kluda_s4 = gad_kluda_s4  

rel_kluda_s4=round(abs_kluda_s4/s4_vid * 100, 2)



# Aprēķini pie h_5

s5_vid=round((s5_1+s5_2+s5_3+s5_4+s5_5)/5, 3) 
s5_kv=round(sqrt(((s5_1-s5_vid)**2+(s5_2-s5_vid)**2+(s5_3-s5_vid)**2+(s5_4-s5_vid)**2+(s5_5-s5_vid)**2)/(5*4)), 6)
gad_kluda_s5=round(s5_kv*st_5, 3)
sist_kluda_s5=round(mv_s/3*st_bezg, 5)

if gad_kluda_s5 <= sist_kluda_s5:
  abs_kluda_s5 = sist_kluda_s5 
elif gad_kluda_s5 > sist_kluda_s5:
  abs_kluda_s5 = gad_kluda_s5  

rel_kluda_s5=round(abs_kluda_s5/s5_vid * 100, 2)
