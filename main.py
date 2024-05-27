# Izstrādātāji:

# Stanislava Shulzhenko
# Kristina Poltaracka

# Labaratorijas darbs Nr.1.6.1 "Lodītes kustības noteikšana ar ballistisko svārstu".

import sympy
from math import sqrt
from sympy import symbols, sqrt, diff

# Konstantes

g=9.81 # Brīvās krišanas paātrinājums (m/s^2)
ml=0.01397 # Lodītes masa (kg)
mr=0.1372 # Rāmīša masa (kg)
l=0.749 # Diegas garums (m)
r=0.0075 # Lodītes radiuss (m)
st_5=2.78 # Stjūdenta koeficients pie n=5
st_bezg=1.96 # Stjūdenta koeficients pie n=bezgalība
h_1=0.705 # Augstums 1. (m)
h_2=0.605 # Augstums 2. (m)
h_3=0.505 # Augstums 5. (m)
h_4=0.305 # Augstums 4. (m)
h_5=0.105 # Augstums 3. (m)

mv_l=0.001 # Mazāka vertība garumam (m)
mv_s=0.001 # Mazāka vertība novirzei (m)
mv_h=0.001 # Mazāka vertība augstumam (m)

# Mērījumi 
# Rāmīša novirze (m)

s1_1, s1_2, s1_3, s1_4, s1_5 = 0.066, 0.065, 0.064, 0.064, 0.064  # pie h_1
s2_1, s2_2, s2_3, s2_4, s2_5 = 0.06, 0.06, 0.06, 0.061, 0.062  # pie h_2
s3_1, s3_2, s3_3, s3_4, s3_5 = 0.055, 0.053, 0.057, 0.059, 0.056  # pie h_3
s4_1, s4_2, s4_3, s4_4, s4_5 = 0.043, 0.042, 0.042, 0.041, 0.04  # pie h_4
s5_1, s5_2, s5_3, s5_4, s5_5 = 0.021, 0.022, 0.023, 0.022, 0.023  # pie h_5

# Lodītes ātrums (digitāli) (m/s)

v1_1d, v1_2d, v1_3d, v1_4d, v1_5d = 2.963, 2.996, 2.96, 2.989, 3.002  # pie h_1
v4_1d, v4_2d, v4_3d, v4_4d, v4_5d = 1.759, 1.765, 1.826, 1.77, 1.763  # pie h_4
v5_1d, v5_2d, v5_3d, v5_4d, v5_5d = 1.011, 1.013, 1.014, 0.988, 0.987  # pie h_5

# Sistemātiskas kļūdas

sist_kluda_h=mv_h/3*st_bezg # Augstumam
sist_kluda_l=mv_l/3*st_bezg # Garumam


# ------------------------------------------------------------------------------------------------------------------------------
# Tiešie mērījumi
# Aprēķini pie h_1

s1_vid=(s1_1+s1_2+s1_3+s1_4+s1_5)/5
s1_kv=sqrt(((s1_1-s1_vid)**2+(s1_2-s1_vid)**2+(s1_3-s1_vid)**2+(s1_4-s1_vid)**2+(s1_5-s1_vid)**2)/(5*4))
gad_kluda_s1=s1_kv*st_5
sist_kluda_s1=mv_s/3*st_bezg

if gad_kluda_s1 <= sist_kluda_s1:
  abs_kluda_s1 = sist_kluda_s1 
elif gad_kluda_s1 > sist_kluda_s1:
  abs_kluda_s1 = gad_kluda_s1  

rel_kluda_s1=abs_kluda_s1/s1_vid * 100

# Aprēķini pie h_2

s2_vid=(s2_1+s2_2+s2_3+s2_4+s2_5)/5
s2_kv=sqrt(((s2_1-s2_vid)**2+(s2_2-s2_vid)**2+(s2_3-s2_vid)**2+(s2_4-s2_vid)**2+(s2_5-s2_vid)**2)/(5*4))
gad_kluda_s2=s2_kv*st_5
sist_kluda_s2=mv_s/3*st_bezg

if gad_kluda_s2 <= sist_kluda_s2:
  abs_kluda_s2 = sist_kluda_s2 
elif gad_kluda_s2 > sist_kluda_s2:
  abs_kluda_s2 = gad_kluda_s2  

rel_kluda_s2=abs_kluda_s2/s2_vid * 100

# Aprēķini pie h_3

s3_vid=(s3_1+s3_2+s3_3+s3_4+s3_5)/5 
s3_kv=sqrt(((s3_1-s3_vid)**2+(s3_2-s3_vid)**2+(s3_3-s3_vid)**2+(s3_4-s3_vid)**2+(s3_5-s3_vid)**2)/(5*4))
gad_kluda_s3=s3_kv*st_5
sist_kluda_s3=mv_s/3*st_bezg

if gad_kluda_s3 <= sist_kluda_s3:
  abs_kluda_s3 = sist_kluda_s3 
elif gad_kluda_s3 > sist_kluda_s3:
  abs_kluda_s3 = gad_kluda_s3  

rel_kluda_s3=abs_kluda_s3/s3_vid * 100

# Aprēķini pie h_4

s4_vid=(s4_1+s4_2+s4_3+s4_4+s4_5)/5
s4_kv=sqrt(((s4_1-s4_vid)**2+(s4_2-s4_vid)**2+(s4_3-s4_vid)**2+(s4_4-s4_vid)**2+(s4_5-s4_vid)**2)/(5*4))
gad_kluda_s4=s4_kv*st_5
sist_kluda_s4=mv_s/3*st_bezg

if gad_kluda_s4 <= sist_kluda_s4:
  abs_kluda_s4 = sist_kluda_s4 
elif gad_kluda_s4 > sist_kluda_s4:
  abs_kluda_s4 = gad_kluda_s4  

rel_kluda_s4=abs_kluda_s4/s4_vid * 100

# Aprēķini pie h_5

s5_vid=(s5_1+s5_2+s5_3+s5_4+s5_5)/5
s5_kv=sqrt(((s5_1-s5_vid)**2+(s5_2-s5_vid)**2+(s5_3-s5_vid)**2+(s5_4-s5_vid)**2+(s5_5-s5_vid)**2)/(5*4))
gad_kluda_s5=s5_kv*st_5
sist_kluda_s5=mv_s/3*st_bezg

if gad_kluda_s5 <= sist_kluda_s5:
  abs_kluda_s5 = sist_kluda_s5 
elif gad_kluda_s5 > sist_kluda_s5:
  abs_kluda_s5 = gad_kluda_s5  

rel_kluda_s5=abs_kluda_s5/s5_vid * 100


# ------------------------------------------------------------------------------------------------------------------------------
# Netiešie mērījumi

mr_sym, ml_sym, l_sym, g_sym, s1_vid_sym, s2_vid_sym, s3_vid_sym, s4_vid_sym, s5_vid_sym, h_1_sym, h_2_sym, h_3_sym, h_4_sym, h_5_sym = symbols('mr_sym ml_sym l_sym g_sym s1_vid_sym s2_vid_sym s3_vid_sym s4_vid_sym s5_vid_sym h_1_sym h_2_sym h_3_sym h_4_sym h_5_sym')

values = {
    mr_sym: 0.1372,
    ml_sym: 0.01397,
    l_sym: 0.749,
    g_sym: 9.81,
    s1_vid_sym: 0.065,
    s2_vid_sym: 0.061,
    s3_vid_sym: 0.056,
    s4_vid_sym: 0.042,
    s5_vid_sym: 0.022,
    h_1_sym: 0.705,
    h_2_sym: 0.605,
    h_3_sym: 0.505,
    h_4_sym: 0.305,
    h_5_sym: 0.105
}

# Lodītes ātrums pirms sadursmes (eksperimentāli)
# Ātrums pie h_1

v1_pirms=(1+(mr_sym/ml_sym))*s1_vid_sym*sqrt(g_sym/l_sym)
v1_pirms_val = v1_pirms.subs(values)

dV_ds_1=diff(v1_pirms, s1_vid_sym)
dV_dl_1=diff(v1_pirms, l_sym)

dV_ds_val_1=dV_ds_1.subs(values)
dV_dl_val_1=dV_dl_1.subs(values)

v1_pirms_kluda=sqrt((dV_ds_val_1*abs_kluda_s1)**2+(dV_dl_val_1*sist_kluda_l)**2)
v1_pirms_rel=v1_pirms_kluda/v1_pirms_val*100

# Ātrums pie h_2

v2_pirms=(1+(mr_sym/ml_sym))*s2_vid_sym*sqrt(g_sym/l_sym)
v2_pirms_val = v2_pirms.subs(values)

dV_ds_2=diff(v2_pirms, s2_vid_sym)
dV_dl_2=diff(v2_pirms, l_sym)

dV_ds_val_2=dV_ds_2.subs(values)
dV_dl_val_2=dV_dl_2.subs(values)

v2_pirms_kluda=sqrt((dV_ds_val_2*abs_kluda_s2)**2+(dV_dl_val_2*sist_kluda_l)**2)
v2_pirms_rel=v2_pirms_kluda/v2_pirms_val*100

# Ātrums pie h_3

v3_pirms=(1+(mr_sym/ml_sym))*s3_vid_sym*sqrt(g_sym/l_sym)
v3_pirms_val = v3_pirms.subs(values)

dV_ds_3=diff(v3_pirms, s3_vid_sym)
dV_dl_3=diff(v3_pirms, l_sym)

dV_ds_val_3=dV_ds_3.subs(values)
dV_dl_val_3=dV_dl_3.subs(values)

v3_pirms_kluda=sqrt((dV_ds_val_3*abs_kluda_s3)**2+(dV_dl_val_3*sist_kluda_l)**2)
v3_pirms_rel=v3_pirms_kluda/v3_pirms_val*100

# Ātrums pie h_4

v4_pirms=(1+(mr_sym/ml_sym))*s4_vid_sym*sqrt(g_sym/l_sym)
v4_pirms_val = v4_pirms.subs(values)

dV_ds_4=diff(v4_pirms, s4_vid_sym)
dV_dl_4=diff(v4_pirms, l_sym)

dV_ds_val_4=dV_ds_4.subs(values)
dV_dl_val_4=dV_dl_4.subs(values)

v4_pirms_kluda=sqrt((dV_ds_val_4*abs_kluda_s4)**2+(dV_dl_val_4*sist_kluda_l)**2)
v4_pirms_rel=v4_pirms_kluda/v4_pirms_val*100

# Ātrums pie h_5

v5_pirms=(1+(mr_sym/ml_sym))*s5_vid_sym*sqrt(g_sym/l_sym)
v5_pirms_val = v5_pirms.subs(values)

dV_ds_5=diff(v5_pirms, s5_vid_sym)
dV_dl_5=diff(v5_pirms, l_sym)

dV_ds_val_5=dV_ds_5.subs(values)
dV_dl_val_5=dV_dl_5.subs(values)

v5_pirms_kluda=sqrt((dV_ds_val_5*abs_kluda_s5)**2+(dV_dl_val_5*sist_kluda_l)**2)
v5_pirms_rel=v5_pirms_kluda/v5_pirms_val*100


# Teorētiski aprēķinātais ātrums ievērojot rotāciju
# Ātrums pie h_1

v1_iev=sqrt((10/7)*g_sym*h_1_sym)
v1_iev_val = v1_iev.subs(values)

dV_dH_1=diff(v1_iev, h_1_sym)
dV_dH_val_1=dV_dH_1.subs(values)

v1_iev_kl= dV_dH_val_1*sist_kluda_h
v1_iev_rel_kl=(v1_iev_kl/v1_iev_val)*100

# Ātrums pie h_2

v2_iev=sqrt((10/7)*g_sym*h_2_sym)
v2_iev_val = v2_iev.subs(values)

dV_dH_2=diff(v2_iev, h_2_sym)
dV_dH_val_2=dV_dH_2.subs(values)

v2_iev_kl= dV_dH_val_2*sist_kluda_h
v2_iev_rel_kl=(v2_iev_kl/v2_iev_val)*100

# Ātrums pie h_3

v3_iev=sqrt((10/7)*g_sym*h_3_sym)
v3_iev_val = v3_iev.subs(values)

dV_dH_3=diff(v3_iev, h_3_sym)
dV_dH_val_3=dV_dH_3.subs(values)

v3_iev_kl= dV_dH_val_3*sist_kluda_h
v3_iev_rel_kl=(v3_iev_kl/v3_iev_val)*100

# Ātrums pie h_4

v4_iev=sqrt((10/7)*g_sym*h_4_sym)
v4_iev_val = v4_iev.subs(values)

dV_dH_4=diff(v4_iev, h_4_sym)
dV_dH_val_4=dV_dH_4.subs(values)

v4_iev_kl= dV_dH_val_4*sist_kluda_h
v4_iev_rel_kl=(v4_iev_kl/v4_iev_val)*100

# Ātrums pie h_5

v5_iev=sqrt((10/7)*g_sym*h_5_sym)
v5_iev_val = v5_iev.subs(values)

dV_dH_5=diff(v5_iev, h_5_sym)
dV_dH_val_5=dV_dH_5.subs(values)

v5_iev_kl= dV_dH_val_5*sist_kluda_h
v5_iev_rel_kl=(v5_iev_kl/v5_iev_val)*100


# Teorētiski aprēķinātais ātrums neievērojot rotāciju
# Ātrums pie h_1

v1_neiev=(2*g_sym*h_1_sym)**0.5
v1_neiev_val = v1_neiev.subs(values)

dV_dH_2_1=diff(v1_neiev, h_1_sym)
dV_dH_val_2_1=dV_dH_2_1.subs(values)

v1_neiev_kl= dV_dH_val_2_1*sist_kluda_h
v1_neiev_rel_kl=(v1_neiev_kl/v1_neiev_val)*100

# Ātrums pie h_2

v2_neiev=(2*g_sym*h_2_sym)**0.5
v2_neiev_val = v2_neiev.subs(values)

dV_dH_2_2=diff(v2_neiev, h_2_sym)
dV_dH_val_2_2=dV_dH_2_2.subs(values)

v2_neiev_kl= dV_dH_val_2_2*sist_kluda_h
v2_neiev_rel_kl=(v2_neiev_kl/v2_neiev_val)*100

# Ātrums pie h_3

v3_neiev=(2*g_sym*h_3_sym)**0.5
v3_neiev_val = v3_neiev.subs(values)

dV_dH_2_3=diff(v3_neiev, h_3_sym)
dV_dH_val_2_3=dV_dH_2_3.subs(values)

v3_neiev_kl= dV_dH_val_2_3*sist_kluda_h
v3_neiev_rel_kl=(v3_neiev_kl/v3_neiev_val)*100

# Ātrums pie h_4

v4_neiev=(2*g_sym*h_4_sym)**0.5
v4_neiev_val = v4_neiev.subs(values)

dV_dH_2_4=diff(v4_neiev, h_4_sym)
dV_dH_val_2_4=dV_dH_2_4.subs(values)

v4_neiev_kl= dV_dH_val_2_4*sist_kluda_h
v4_neiev_rel_kl=(v4_neiev_kl/v4_neiev_val)*100

# Ātrums pie h_5

v5_neiev=(2*g_sym*h_5_sym)**0.5
v5_neiev_val = v5_neiev.subs(values)

dV_dH_2_5=diff(v5_neiev, h_5_sym)
dV_dH_val_2_5=dV_dH_2_5.subs(values)

v5_neiev_kl= dV_dH_val_2_5*sist_kluda_h
v5_neiev_rel_kl=(v5_neiev_kl/v5_neiev_val)*100


# Enerģijas zudumi renē 

I=(2/5)*ml*r**2

# V ir izmērīts diģitāli
# Zudumi pie h_1

v1_dig_vid=(v1_1d+v1_2d+v1_3d+v1_4d+v1_5d)/5
w1_dig=v1_dig_vid/r

Ep_1=ml*g*h_1
Ek_1_dig=(ml*v1_dig_vid**2)/2+(I*w1_dig**2)/2
Ez_1_dig=Ep_1-Ek_1_dig
zud_1_dig=Ez_1_dig/Ep_1*100

# Zudumi pie h_4

v4_dig_vid=(v4_1d+v4_2d+v4_3d+v4_4d+v4_5d)/5
w4_dig=v4_dig_vid/r

Ep_4=ml*g*h_4
Ek_4_dig=(ml*v4_dig_vid**2)/2+(I*w4_dig**2)/2
Ez_4_dig=Ep_4-Ek_4_dig
zud_4_dig=Ez_4_dig/Ep_4*100

# Zudumi pie h_5

v5_dig_vid=(v5_1d+v5_2d+v5_3d+v5_4d+v5_5d)/5
w5_dig=v5_dig_vid/r

Ep_5=ml*g*h_5
Ek_5_dig=(ml*v5_dig_vid**2)/2+(I*w5_dig**2)/2
Ez_5_dig=Ep_5-Ek_5_dig
zud_5_dig=Ez_5_dig/Ep_5*100


# V ir aprēķināts eksperimentāli
# Zudumi pie h_1

w1_eks=v1_pirms_val/r

Ek_1_eks=(ml*v1_pirms_val**2)/2+(I*w1_eks**2)/2
Ez_1_eks=Ep_1-Ek_1_eks
zud_1_eks=Ez_1_eks/Ep_1*100

# Zudumi pie h_4

w4_eks=v4_pirms_val/r

Ek_4_eks=(ml*v4_pirms_val**2)/2+(I*w4_eks**2)/2
Ez_4_eks=Ep_4-Ek_4_eks
zud_4_eks=Ez_4_eks/Ep_4*100

# Zudumi pie h_5

w5_eks=v5_pirms_val/r

Ek_5_eks=(ml*v5_pirms_val**2)/2+(I*w5_eks**2)/2
Ez_5_eks=Ep_5-Ek_5_eks
zud_5_eks=Ez_5_eks/Ep_5*100

lines = [
  f"-----------------------------------------1-----------------------------------------\n"
  f"\n"
  f"Lodītes ātrums pirms sadursmes (eksperimentāli) pie h=0,705 m: {v1_pirms_val} m/s\n"
  f"Absolūta kļūda: {v1_pirms_kluda} m/s\n"
  f"Relatīva kļūda: {v1_pirms_rel}%\n"
  f"\n"
  f"Lodītes ātrums pirms sadursmes (eksperimentāli) pie h=0,605 m: {v2_pirms_val} m/s\n"
  f"Absolūta kļūda: {v2_pirms_kluda} m/s\n"
  f"Relatīva kļūda: {v2_pirms_rel}%\n"
  f"\n"
  f"Lodītes ātrums pirms sadursmes (eksperimentāli) pie h=0,505 m: {v3_pirms_val} m/s\n"
  f"Absolūta kļūda: {v3_pirms_kluda} m/s\n"
  f"Relatīva kļūda: {v3_pirms_rel}%\n"
  f"\n"
  f"Lodītes ātrums pirms sadursmes (eksperimentāli) pie h=0,305 m: {v4_pirms_val} m/s\n"
  f"Absolūta kļūda: {v4_pirms_kluda} m/s\n"
  f"Relatīva kļūda: {v4_pirms_rel}%\n"
  f"\n"
  f"Lodītes ātrums pirms sadursmes (eksperimentāli) pie h=0,105 m: {v5_pirms_val} m/s\n"
  f"Absolūta kļūda: {v5_pirms_kluda} m/s\n"
  f"Relatīva kļūda: {v5_pirms_rel}%\n"
  f"\n"
  f"-----------------------------------------2-----------------------------------------\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums ievērojot rotāciju pie h=0,705 m: {v1_iev_val} m/s\n"
  f"Absolūta kļūda: {v1_iev_kl} m/s\n"
  f"Relatīva kļūda: {v1_iev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums ievērojot rotāciju pie h=0,605 m: {v2_iev_val} m/s\n"
  f"Absolūta kļūda: {v2_iev_kl} m/s\n"
  f"Relatīva kļūda: {v2_iev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums ievērojot rotāciju pie h=0,505 m: {v3_iev_val} m/s\n"
  f"Absolūta kļūda: {v3_iev_kl} m/s\n"
  f"Relatīva kļūda: {v3_iev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums ievērojot rotāciju pie h=0,305 m: {v4_iev_val} m/s\n"
  f"Absolūta kļūda: {v4_iev_kl} m/s\n"
  f"Relatīva kļūda: {v4_iev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums ievērojot rotāciju pie h=0,105 m: {v5_iev_val} m/s\n"
  f"Absolūta kļūda: {v5_iev_kl} m/s\n"
  f"Relatīva kļūda: {v5_iev_rel_kl}%\n"
  f"\n"
  f"-----------------------------------------3-----------------------------------------\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums neievērojot rotāciju pie h=0,705 m: {v1_neiev_val} m/s\n"
  f"Absolūta kļūda: {v1_neiev_kl} m/s\n"
  f"Relatīva kļūda: {v1_neiev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums neievērojot rotāciju pie h=0,605 m: {v2_neiev_val} m/s\n"
  f"Absolūta kļūda: {v2_neiev_kl} m/s\n"
  f"Relatīva kļūda: {v2_neiev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums neievērojot rotāciju pie h=0,505 m: {v3_neiev_val} m/s\n"
  f"Absolūta kļūda: {v3_neiev_kl} m/s\n"
  f"Relatīva kļūda: {v3_neiev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums neievērojot rotāciju pie h=0,305 m: {v4_neiev_val} m/s\n"
  f"Absolūta kļūda: {v4_neiev_kl} m/s\n"
  f"Relatīva kļūda: {v4_neiev_rel_kl}%\n"
  f"\n"
  f"Teorētiski aprēķinātais ātrums neievērojot rotāciju pie h=0,105 m: {v5_neiev_val} m/s\n"
  f"Absolūta kļūda: {v5_neiev_kl} m/s\n"
  f"Relatīva kļūda: {v5_neiev_rel_kl}%\n"
  f"\n"
  f"-----------------------------------------4-----------------------------------------\n"
  f"\n"
  f"Enerģijas zudumi renē (V ir izmērīts diģitāli) pie h=0,705 m: {zud_1_dig}%\n"
  f"Enerģijas zudumi renē (V ir aprēķināts eksperimentāli) pie h=0,705 m: {zud_1_eks}%\n"
  f"\n"
  f"Enerģijas zudumi renē (V ir izmērīts diģitāli) pie h=0,305 m: {zud_4_dig}%\n"
  f"Enerģijas zudumi renē (V ir aprēķināts eksperimentāli) pie h=0,305 m: {zud_4_eks}%\n"
  f"\n"
  f"Enerģijas zudumi renē (V ir izmērīts diģitāli) pie h=0,105 m: {zud_5_dig}%\n"
  f"Enerģijas zudumi renē (V ir aprēķināts eksperimentāli) pie h=0,105 m: {zud_5_eks}%\n"
]
with open('results.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
