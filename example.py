# Labaratorijas darbs Nr.1.4 "Inerces momenta noteikšana, izmantojot Maksvela svārstu".
# Aprēķini izmantojot Python programmēšanas valodu.
# Skriptu izstrādātāja:

# Maksims Koļcovss
# Karolīna Bucenka

import sympy
from math import sqrt
from sympy import symbols, diff

# Stjūdentu koeficenti:

Stjudents_Bezgaliba = 1.96
Stjudents_5 = 2.78
Stjudents_10 = 2.96

# Aprēķini bez gredzena (nenoslogota svārsta inerces moments I)
# I = mr^2 (gt^2 / 2h - 1)

g = 9.81  # Brīvās krišanas paātrinājums (m/s^2)
r = 0.005  # radiuss (m)
h = 0.4  # augstums (m)
tvid_1 = 1.36  # laiks vidējais (s)
m = 0.159  # masa (kg)

# Laika rezultāti pie m
t_1 = 1.324  # (s)
t_2 = 1.353  # (s)
t_3 = 1.281  # (s)
t_4 = 1.437  # (s)
t_5 = 1.368  # (s)
t_6 = 1.341  # (s)
t_7 = 1.374  # (s)
t_8 = 1.368  # (s)
t_9 = 1.41  # (s)
t_10 = 1.312  # (s)

# Laika rezultāti pie m_2
t2_1 = 2.052  # (s)
t2_2 = 2.061  # (s)
t2_3 = 2.034  # (s)
t2_4 = 2.074  # (s)
t2_5 = 2.067  # (s)

# Laika rezultāti pie m_3
t3_1 = 2.159  # (s)
t3_2 = 2.135  # (s)
t3_3 = 2.181  # (s)
t3_4 = 2.146  # (s)
t3_5 = 2.126  # (s)

# Inerces moments I1 (bez gredzena)

I1 = m * (r * r) * (g * (tvid_1 * tvid_1) / (2 * h) - 1)

# Aprēķini ar gredzenu (Noslogotais svārsts)
# I = mr^2 (gt^2 / 2h - 1)

m_2 = 0.41816  # masa (kg)
tvid_2 = 2.06  # laiks vidējais (s)

# I kopa ar gredzenu (0.41816 kg)

I_kopa_1 = m_2 * (r * r) * (g * (tvid_2 * tvid_2) / (2 * h) - 1)

# Aprēķini ar gredzenu (Noslogotais svārsts)
# I = mr^2 (gt^2 / 2h - 1)

m_3 = 0.5545  # masa (kg)
tvid_3 = 2.15  # laiks vidējais (s)

# I kopa ar gredzenu (0.5545 kg)

I_kopa_2 = m_3 * (r * r) * (g * (tvid_3 * tvid_3) / (2 * h) - 1)

# Teorētiskā inerces momenta gredzena aprēķins (0.41816 kg)
# Ig teoretiskais = Mg / 8 (D1^2-D2^2)

D1 = 0.085  # Diametrs (metros) - gredzena iekšējais diametrs
D2 = 0.105  # Diametrs (metros) - ārējais diametrs

gredzens_1 = 0.25916  # gredzena svars (kg)
gredzens_2 = 0.3955  # gredzena svars (kg)

Ig1_teoretiski = (gredzens_1 / 8) * ((D1 * D1) * (D2 * D2))

# Teorētiskā inerces momenta gredzena aprēķins (0.5545 kg)
# Ig teoretiskais = Mg / 8 (D1^2-D2^2)

Ig2_teoretiski = (gredzens_2 / 8) * ((D1 * D1) * (D2 * D2))

# Inerces moments Ig
# Ig= Ikop - I

Ig1 = I_kopa_1 - I1
Ig2 = I_kopa_2 - I1


# Enerģijas nezudamības likums

# Kīnetiskā enerģija sākumā pie standartmasas,m_2,m_3
Wk0 = 0  # (J)
# Potenciāla enerģija sākumā pie standartmasas
# Wp0=mgh
Wp0_pie_m = m * g * h  # (J)
# Potenciāla enerģija sākuma pie m_2
# Wp0=mgh
Wp0_pie_m2 = m_2 * g * h  # (J)
# Potenciāla enerģija sākumā pie m_3
# Wp0=mgh
Wp0_pie_m3 = m_3 * g * h  # (J)

#Kīnetiskā enerģija beigās pie standartmasas
Wkb_pie_m = (m + I1 / (r * r)) * 2 * (h * h) / (tvid_1 * tvid_1)  # (J)
#Kīnetiskā enerģija beigās pie m_2
Wkb_pie_m2 = (m_2 + I_kopa_1 /
              (r * r)) * 2 * (h * h) / (tvid_2 * tvid_2)  # (J)
#Kīnetiskā enerģija beigās pie m_3
Wkb_pie_m3 = (m_3 + I_kopa_2 /
              (r * r)) * 2 * (h * h) / (tvid_3 * tvid_3)  # (J)

# Potenciālā enerģija beigās pie standartmasas,m_2,m_3
Wpb = 0  # (J)




# Kļūdas aprēķiņi laikam

# Kļūdas aprēķiņi laikam t pie standartmasas
# Vidēja kvadratiskā kļūda

Videja_kvadratiska_kluda_m = sqrt(
    ((t_1 - tvid_1) * (t_1 - tvid_1) + (t_2 - tvid_1) * (t_2 - tvid_1) +
     (t_3 - tvid_1) * (t_3 - tvid_1) + (t_4 - tvid_1) * (t_4 - tvid_1) +
     (t_5 - tvid_1) * (t_5 - tvid_1) + (t_6 - tvid_1) * (t_6 - tvid_1) +
     (t_7 - tvid_1) * (t_7 - tvid_1) + (t_8 - tvid_1) * (t_8 - tvid_1) +
     (t_9 - tvid_1) * (t_9 - tvid_1) + (t_10 - tvid_1) * (t_10 - tvid_1)) /
    (10 * (10 - 1)))  # (s)

# Gadījumā kļūda
Gadijuma_kluda_m = Videja_kvadratiska_kluda_m * Stjudents_10  #(s)

# Sistemātiskā kļūda
# mazāka iedaļas vertība =0.001
mv = 0.001
Sistematiska_kluda_m = mv / 3 * Stjudents_Bezgaliba  #(s)

# Absolūta kļūda

if Gadijuma_kluda_m <= Sistematiska_kluda_m:
  Absoluta_kluda_m = Sistematiska_kluda_m  #(s)

elif Gadijuma_kluda_m > Sistematiska_kluda_m:
  Absoluta_kluda_m = Gadijuma_kluda_m  #(s)

# Relatīvā kļūda

Relativa_kluda_m = Absoluta_kluda_m / tvid_1 * 100  #(s)

# Kļūdas aprēķiņi laikam t pie m_2
# Vidēja kvadratiskā kļūda

Videja_kvadratiska_kluda_m2 = sqrt(
    ((t2_1 - tvid_2) * (t2_1 - tvid_2) + (t2_2 - tvid_2) * (t2_2 - tvid_2) +
     (t2_3 - tvid_2) * (t2_3 - tvid_2) + (t2_4 - tvid_2) * (t2_4 - tvid_2) +
     (t2_5 - tvid_2) * (t2_5 - tvid_2)) / (5 * (5 - 1)))  # (s)

# Gadījumā kļūda
Gadijuma_kluda_m2 = Videja_kvadratiska_kluda_m2 * Stjudents_5  #(s)

# Sistemātiskā kļūda
# mazāka iedaļas vertība =0.001
mv2 = 0.001
Sistematiska_kluda_m2 = mv2 / 3 * Stjudents_Bezgaliba  #(s)

# Absolūta kļūda

if Gadijuma_kluda_m2 <= Sistematiska_kluda_m2:
  Absoluta_kluda_m2 = Sistematiska_kluda_m2  #(s)

elif Gadijuma_kluda_m2 > Sistematiska_kluda_m2:
  Absoluta_kluda_m2 = Gadijuma_kluda_m2  #(s)

# Relatīvā kļūda

Relativa_kluda_m2 = Absoluta_kluda_m2 / tvid_2 * 100  #(s)

# Kļūdas aprēķiņi laikam t pie m_3
# Vidēja kvadratiskā kļūda

Videja_kvadratiska_kluda_m3 = sqrt(
    ((t3_1 - tvid_3) * (t3_1 - tvid_3) + (t3_2 - tvid_3) * (t3_2 - tvid_3) +
     (t3_3 - tvid_3) * (t3_3 - tvid_3) + (t3_4 - tvid_3) * (t3_4 - tvid_3) +
     (t3_5 - tvid_3) * (t3_5 - tvid_3)) / (5 * (5 - 1)))  # (s)

# Gadījumā kļūda
Gadijuma_kluda_m3 = Videja_kvadratiska_kluda_m3 * Stjudents_5  #(s)

# Sistemātiskā kļūda
# mazāka iedaļas vertība =0.001
mv3 = 0.001
Sistematiska_kluda_m3 = mv / 3 * Stjudents_Bezgaliba  #(s)

# Absolūta kļūda

if Gadijuma_kluda_m3 <= Sistematiska_kluda_m3:
  Absoluta_kluda_m3 = Sistematiska_kluda_m3  #(s)

elif Gadijuma_kluda_m3 > Sistematiska_kluda_m3:
  Absoluta_kluda_m3 = Gadijuma_kluda_m3  #(s)

# Relatīvā kļūda

Relativa_kluda_m3 = Absoluta_kluda_m3 / tvid_3 * 100  #(s)

# Kļūdas h,D1,D2,r,m

# Sistemātiskas kļūdas
m, m_2, m_3, r, g, tvid_1,tvid_2,tvid_3, h = symbols('m m_2 m_3 r g tvid_1 tvid_2 tvid_3 h')

# mazākā iedāļas vertība h = 0.001 m

sistematiska_kluda_h = 0.001 / 3 * Stjudents_Bezgaliba

# mazākā iedāļas vertība r,d1,d2=0.00005 m

sistematiska_kluda_d1 = 0.00005 / 3 * Stjudents_Bezgaliba
sistematiska_kluda_d2 = sistematiska_kluda_d1
sistematiska_kluda_r = sistematiska_kluda_d1

# mazākā iedāļas vertība m=0.00001 kg

sistematiska_kluda_m = 0.00001 / 3 * Stjudents_Bezgaliba

# Relatīvas kļūdas

relativa_kluda_h = sistematiska_kluda_h/h*100
relativa_kluda_d1 = sistematiska_kluda_d1/D1*100
relativa_kluda_d2 = sistematiska_kluda_d2/D2*100
relativa_kluda_r = sistematiska_kluda_r/r*100
relativa_kluda_m = sistematiska_kluda_m/m*100

# I pie m
I_m = m * (r * r) * (g * (tvid_1 * tvid_1) / (2 * h) - 1)

dI_dm = diff(I_m, m)
dI_dr = diff(I_m, r)
dI_dh = diff(I_m, h)
dI_dt = diff(I_m, tvid_1)


values = {
    m: 0.159,
    m_2: 0.41816,
    m_3: 0.5545,
    r: 0.005,
    g: 9.81,
    tvid_1: 1.36,
    tvid_2: 2.06,
    tvid_3: 2.15,
    h: 0.4
}

dI_dm_value = dI_dm.subs(values)
dI_dr_value = dI_dr.subs(values)
dI_dh_value = dI_dh.subs(values)
dI_dt_value = dI_dt.subs(values)


Si = sqrt(((dI_dm_value) * sistematiska_kluda_m) * ((dI_dm_value) * sistematiska_kluda_m) + ((dI_dr_value) * sistematiska_kluda_r) * ((dI_dr_value) * sistematiska_kluda_r) + ((dI_dt_value) * Absoluta_kluda_m) * ((dI_dt_value) * Absoluta_kluda_m) + ((dI_dh_value) * sistematiska_kluda_h) * ((dI_dh_value) * sistematiska_kluda_h))

Relativa_kluda_I=Si/I1*100

# I pie m2

I_m2 = m_2 * (r * r) * (g * (tvid_2 * tvid_2) / (2 * h) - 1)

dI_dm2 = diff(I_m2, m_2)
dI_dt2 = diff(I_m2, tvid_2)
dI_dr1 = diff(I_m2, r)
dI_dh1 = diff(I_m2, h)
dI_dm2_value = dI_dm2.subs(values)
dI_dt2_value = dI_dt2.subs(values)
dI_dr_value1 = dI_dr1.subs(values)
dI_dh_value1 = dI_dh1.subs(values)

Si2 = sqrt(((dI_dm2_value) * sistematiska_kluda_m) * ((dI_dm2_value) * sistematiska_kluda_m) + ((dI_dr_value1) * sistematiska_kluda_r) * ((dI_dr_value1) * sistematiska_kluda_r) + ((dI_dt2_value) * Absoluta_kluda_m2) * ((dI_dt2_value) * Absoluta_kluda_m2) + ((dI_dh_value1) * sistematiska_kluda_h) * ((dI_dh_value1) * sistematiska_kluda_h))

Relativa_kluda_Ikop1=Si2/I_kopa_1*100

# I pie m3

I_m3 = m_3 * (r * r) * (g * (tvid_3 * tvid_3) / (2 * h) - 1)

dI_dm3 = diff(I_m3, m_3)
dI_dt3 = diff(I_m3, tvid_3)
dI_dr2 = diff(I_m3, r)
dI_dh2 = diff(I_m3, h)
dI_dm3_value = dI_dm3.subs(values)
dI_dt3_value = dI_dt3.subs(values)
dI_dr_value2 = dI_dr2.subs(values)
dI_dh_value2 = dI_dh2.subs(values)


Si3 = sqrt(((dI_dm3_value) * sistematiska_kluda_m) * ((dI_dm3_value) * sistematiska_kluda_m) + ((dI_dr_value2) * sistematiska_kluda_r) * ((dI_dr_value2) * sistematiska_kluda_r) + ((dI_dt3_value) * Absoluta_kluda_m3) * ((dI_dt3_value) * Absoluta_kluda_m3) + ((dI_dh_value2) * sistematiska_kluda_h) * ((dI_dh_value2) * sistematiska_kluda_h))
Relativa_kluda_Ikop2=Si3/I_kopa_2*100





# Inerces moments 1 gredzenam (teorētiski) ∆Ig1

# Ig = sqrt((D1 * m / 4 * ∆D1)^2 * (D2 * m / 4 * ∆D2)^2 + (D1^2+D2^2 / 8 * ∆m)^2

term = ((D1 * gredzens_1 / 4) * sistematiska_kluda_d1) * ((D1 * gredzens_1 / 4) * sistematiska_kluda_d1)
term2 = ((D2 * gredzens_1 / 4) * sistematiska_kluda_d2) * ((D2 * gredzens_1 / 4) * sistematiska_kluda_d2)
term3 = (((D1**2 + D2**2) / 8) * sistematiska_kluda_m) * (((D1**2 + D2**2) / 8) * sistematiska_kluda_m)

Ig_kluda_Si = sympy.sqrt(term + term2 + term3)


# Inerces moments 2 gredzenam (teorētiski) ∆Ig2

term4 = ((D1 * gredzens_2 / 4) * sistematiska_kluda_d1) * ((D1 * gredzens_2 / 4) * sistematiska_kluda_d1)
term5 = ((D2 * gredzens_2 / 4) * sistematiska_kluda_d2) * ((D2 * gredzens_2 / 4) * sistematiska_kluda_d2)
term6 = (((D1**2 + D2**2) / 8) * sistematiska_kluda_m) * (((D1**2 + D2**2) / 8) * sistematiska_kluda_m)

Ig_kluda_2_Si = sympy.sqrt(term + term2 + term3)


# Relatīvās kļūdas

relativa_kluda_ig_Teoretiski = (Ig_kluda_Si / Ig1)*100
relativa_kluda_ig2_Teoretiski = (Ig_kluda_2_Si / Ig2)*100


# Inerces moments 1. gredzenam (eksperimentāli) ∆Ig
# Ig1=Ikop1-I0
# Ikop1= m_2*(r*r)*(g*(tvid_2*tvid_2)/(2*h)-1)

#r= 0.005
#g= 9.81
#tvid_2 = 2.06
#h = 0.4
#sistematiska_kluda_m = 0.000653
#m_2 = 0.41816 
#m_3 = 0.5545 
#t_vid_3 = 2.12
#Absoluta_kluda_m2 = 0.01951
#sistematiska_kluda_h = 0.000653
#sistematiska_kluda_r =  3.266666666666667e-05


#term_eks_pec_m2 = ((r*r)*(g*(tvid_2 * tvid_2)/(2*h)-1) * sistematiska_kluda_m) * ((r*r)*(g*(tvid_2*tvid_2)/(2*h)-1) * sistematiska_kluda_m)

#term_eks_pec_r2 = ((2*m_2*r)*(g*(tvid_2*tvid_2)/(2*h)-1) * sistematiska_kluda_r) * ((2*m_2*r)*(g*(tvid_2*tvid_2)/(2*h)-1) * sistematiska_kluda_r)

#term_eks_pec_t2 = (m_2*(r*r)*(g*tvid_2/h-1) * Absoluta_kluda_m2) * (m_2*(r*r)*(g*tvid_2/h-1) * Absoluta_kluda_m2)

#term_eks_pec_h2= (m_2*(r*r)*(g*tvid_2/(-2*h*h)-1) * sistematiska_kluda_h) * (m_2*(r*r)*(g*tvid_2/(-2*h*h)-1) * sistematiska_kluda_h)

#Ig_kluda_eks_Si = term_eks_pec_m2 + term_eks_pec_r2 + term_eks_pec_t2 + term_eks_pec_h2
#Ig_kluda_eks_Si_kvadratsakne = sympy.sqrt(Ig_kluda_eks_Si)
#print (Ig_kluda_eks_Si_kvadratsakne)

#print(term_eks_pec_m2)
#print(term_eks_pec_r2)
#print(term_eks_pec_t2)
#print(term_eks_pec_h2)
#print(Ig_kluda_eks_Si)

#Ig11=I_kopa_1-I1

#print(Ig11)

#abs_kl_Ig1_eks = sympy.sqrt((Ig_kluda_eks_Si * Ig_kluda_eks_Si)+(Absoluta_kluda_m * Absoluta_kluda_m))

#print(abs_kl_Ig1_eks)

#relativa_kluda_Ig1_eks=abs_kl_Ig1_eks/Ig11*100

#print (relativa_kluda_Ig1_eks)
# Inerces moments 2. gredzenam (eksperimentāli) ∆Ig
# Ig1=Ikop2-I0
# Ikop2= m_3*(r*r)*(g*(tvid_3*tvid_3)/(2*h)-1)





#term_eks_pec_m3 = ((r*r)*(g*(tvid_3*tvid_3)/(2*h)-1) * sistematiska_kluda_m) * ((r*r)*(g*(tvid_3*tvid_3)/(2*h)-1) * sistematiska_kluda_m)

#term_eks_pec_r3 = ((2*m_3*r)*(g*(tvid_3*tvid_3)/(2*h)-1) * sistematiska_kluda_r) * ((2*m_3*r)*(g*(tvid_3*tvid_3)/(2*h)-1) * sistematiska_kluda_r)

#term_eks_pec_t3 = (m_3*(r*r)*(g*tvid_3/h-1) * Absoluta_kluda_m3) * (m_3*(r*r)*(g*tvid_3/h-1) * Absoluta_kluda_m3)

#term_eks_pec_h3 = (m_3*(r*r)*(g*tvid_3/(-2*h*h)-1) * sistematiska_kluda_h) * (m_3*(r*r)*(g*tvid_3/(-2*h*h)-1) * sistematiska_kluda_h)

#Ig2_kluda_eks_Si = sympy.sqrt(term_eks_pec_m3+term_eks_pec_r3+term_eks_pec_t3+term_eks_pec_h3)

#Ig22=I_kopa_2-I1

#abs_kl_Ig2_eks = sympy.sqrt((Ig2_kluda_eks_Si*Ig2_kluda_eks_Si)+(Absoluta_kluda_m3*Absoluta_kluda_m3))

#relativa_kluda_Ig2_eks = abs_kl_Ig2_eks/Ig22*100



# Saglabāšana teksta datnē ar mērvienībām

with open('rezultati.txt', 'w', encoding='utf-8') as f:
  f.write(f"Inerces moments I1 (bez gredzena): {I1} kg*m^2\n")
  f.write(
      f"Inerces moments I kopa ar gredzenu (0.41816 kg): {I_kopa_1} kg*m^2\n")
  f.write(
      f"Inerces moments I kopa ar gredzenu (0.5545 kg): {I_kopa_2} kg*m^2\n")
  f.write(
      f"Teorētiskā inerces momenta gredzena aprēķins (0.259 kg): {Ig1_teoretiski} kg*m^2\n"
  )
  f.write(
      f"Teorētiskā inerces momenta gredzena aprēķins (0.396 kg): {Ig2_teoretiski} kg*m^2\n"
  )
  f.write(f"Inerces moments Ig (0.41816 kg): {Ig1} kg*m^2\n")
  f.write(f"Inerces moments Ig (0.5545 kg): {Ig2} kg*m^2\n")
  f.write(
      f"Potenciāla enerģija pie standartmasas (Wp0_m=6.2392E-01): {Wp0_pie_m} J\n"
  )
  f.write(f"Potenciāla enerģija pie m_2 (Wp0_m2=1.6409E+00): {Wp0_pie_m2} J\n")
  f.write(f"Potenciāla enerģija pie m_3 (Wp0_m3=2.1759E+00): {Wp0_pie_m3} J\n")
  f.write(
      f"Kīnetiskā enerģija pie standartmasas (Wkb_m=6.2392E-01): {Wkb_pie_m} J\n"
  )
  f.write(f"Kīnetiskā enerģija pie m_2 (Wkb_m2=1.6409E+00): {Wkb_pie_m2} J\n")
  f.write(f"Kīnetiskā enerģija pie m_3 (Wkb_m3=2.1759E+00): {Wkb_pie_m3} J\n")
  f.write(
      f"Enerģijas nezudamības likums pie m (Wk0 + Wp0 = Wkb + Wpb): {Wp0_pie_m} + {Wk0} = {Wkb_pie_m} + {Wpb} \n"
  )
  f.write(
      f"Enerģijas nezudamības likums pie m_2 (Wk0 + Wp0 = Wkb + Wpb): {Wp0_pie_m2} + {Wk0} = {Wkb_pie_m2} + {Wpb} \n"
  )
  f.write(
      f"Enerģijas nezudamības likums pie m_3 (Wk0 + Wp0 = Wkb + Wpb): {Wp0_pie_m3} + {Wk0} = {Wkb_pie_m3} + {Wpb} \n"
  )

  f.write(
      f"Vidējā kvadratiskā kļūda pie m (0.01449): {Videja_kvadratiska_kluda_m} s\n"
  )
  f.write(f"Gadījumā kļūda m (0.04290): {Gadijuma_kluda_m} s\n")
  f.write(
      f"Sistematiskā kļūda pie m (0.000653333): {Sistematiska_kluda_m} s\n")
  f.write(f"Absolūta kļūda pie m (0.04290): {Absoluta_kluda_m} s\n")
  f.write(f"Relatīva kļūda pie m (3.161851415): {Relativa_kluda_m} s\n")

  f.write(
      f"Vidējā kvadratiskā kļūda pie m_2 (0.00692): {Videja_kvadratiska_kluda_m2} s\n"
  )
  f.write(f"Gadījumā kļūda m_2 (0.01923): {Gadijuma_kluda_m2} s\n")
  f.write(
      f"Sistematiskā kļūda pie m_2 (0.000653333): {Sistematiska_kluda_m2} s\n")
  f.write(f"Absolūta kļūda m2 (0.01923): {Absoluta_kluda_m2} s\n")
  f.write(f"Relatīva kļūda pie m_2 (0.934583981): {Relativa_kluda_m2} s\n")

  f.write(
      f"Vidējā kvadratiskā kļūda pie m_3 (0.00964): {Videja_kvadratiska_kluda_m3} s\n"
  )
  f.write(f"Gadījumā kļūda m_3 (0.02679): {Gadijuma_kluda_m3} s\n")
  f.write(
      f"Sistematiskā kļūda pie m_3 (0.000653333): {Sistematiska_kluda_m3} s\n")
  f.write(f"Absolūta kļūda m3 (0.02679): {Absoluta_kluda_m3} s\n")
  f.write(f"Relatīva kļūda pie m_3 (1.246394343): {Relativa_kluda_m3} s\n")


  f.write(f"Masas m relatīvā kļūda: {Relativa_kluda_m}%\n")
  f.write(f"Augstuma h relatīvā kļūda: {relativa_kluda_h}%\n")
  f.write(f"Diametra D1 relatīvā kļūda: {relativa_kluda_d1}%\n")
  f.write(f"Diametra D2 relatīvā kļūda: {relativa_kluda_d2}%\n")



  f.write(f"Sistematiskā kļūda masai : {sistematiska_kluda_m} kg\n")
  f.write(f"Relatīva kļūda masai : {relativa_kluda_m} %\n")
  f.write(f"Sistematiskā kļūda augstumam : {sistematiska_kluda_h} m\n")
  f.write(f"Relatīva kļūda augstumam : {relativa_kluda_h} %\n")
  f.write(f"Sistematiskā kļūda iekšējam diametram : {sistematiska_kluda_d1} m\n")
  f.write(f"Relatīva kļūda iekšējam diametram : {relativa_kluda_d1} %\n")
  f.write(f"Sistematiskā kļūda pie ārējam diametram : {sistematiska_kluda_d2} m\n")
  f.write(f"Relatīva kļūda pie ārējam diametram : {relativa_kluda_d2} %\n")
  f.write(f"Sistematiskā kļūda radiusam : {sistematiska_kluda_r} m\n")
  f.write(f"Relatīva kļūda radiusam : {relativa_kluda_r} %\n")
  f.write(f"Absolūta kļūda pie I : {Si} kg*m^2\n")
  f.write(f"Relatīva kļūda pie I : {Relativa_kluda_I} %\n")
  f.write(f"Absolūta kļūda pie Ikop1 : {Si2} kg*m^2\n")
  f.write(f"Relatīva kļūda pie Ikop1 : {Relativa_kluda_Ikop1} %\n")
  f.write(f"Absolūta kļūda pie Ikop2 : {Si3} kg*m^2\n")
  f.write(f"Relatīva kļūda pie Ikop2 : {Relativa_kluda_Ikop2} %\n")

  f.write(f"Absolūta kļūda pie Ig1 Teoretiski: {Ig_kluda_Si} kg*m^2\n")
  f.write(f"Absolūta kļūda pie Ig2 Teoretiski: {Ig_kluda_2_Si} kg*m^2\n")
  f.write(f"Relatīva kļūda pie Ig1 Teoretiski: {relativa_kluda_ig_Teoretiski} %\n")
  f.write(f"Relatīva kļūda pie Ig2 Teoretiski : {relativa_kluda_ig2_Teoretiski} %\n")

  #f.write(f"Absolūta kļūda pie eks Ig1 : {abs_kl_Ig1_eks} kg*m^2\n")  
  #f.write(f"Absolūta kļūda pie eks Ig2 : {abs_kl_Ig2_eks} kg*m^2\n")
  #f.write(f"Relatīva kļūda pie eks Ig1 : {relativa_kluda_Ig1_eks} %\n")  
  #f.write(f"Relatīva kļūda pie eks Ig2 : {relativa_kluda_Ig2_eks} %\n")