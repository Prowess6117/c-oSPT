#!/usr/bin/env python3
"""Pruebas DOCUMENTALES, no motor de cálculo ni aptitud de diseño real.
IEEE 80-2013/Cor1-2015: §11.3.1 ec.(46), B.1 (B.3), §16.5 ecs.(85)-(99),
H.3.1/H.3.2 Figs. H.3/H.4, Tablas H.5/H.6.
Ejecutar: python3 docs/estudios/diagnostico_inconsistencias_ieee80.py
Solo biblioteca estándar, sin datos de proyectos ni archivos protegidos.
"""
from math import sqrt, log, pi


def seccion_termica_kcmil(I_kA):
    # Datos expresos B.1: tc=0.5s; 30% cobre-acero; Tm=700C, Ta=40C
    return I_kA*197.4/sqrt(
        (3.85/(0.5*0.00378*5.862))*log((245+700)/(245+40))
    )


def malla(IG_A, con_varillas=False):
    # Malla cuadrada 70x70m; 6 conductores por dirección; suelo uniforme.
    lado, h, D, d, rho, Lc = 70., 0.5, 14., 0.0105, 140., 840.
    n=2*Lc/(4*lado)
    assert n==6
    kii=1 if con_varillas else 1/(2*n)**(2/n)
    kh=sqrt(1+h/1.)
    km=(
        log(D**2/(16*h*d)+(D+2*h)**2/(8*D*d)-h/(4*d))
        + kii/kh*log(8/(pi*(2*n-1)))
    )/(2*pi)
    ks=(1/(2*h)+1/(D+h)+(1/D)*(1-0.5**(n-2)))/pi
    ki=.644+.148*n
    LR=20*7.5 if con_varillas else 0.0
    Lm=Lc+(1.55+1.22*7.5/sqrt(2*lado*lado))*LR if con_varillas else Lc
    Ls=.75*Lc+.85*LR
    return rho*km*ki*IG_A/Lm, rho*ks*ki*IG_A/Ls


def check(v, ref, tolerance=1e-6):
    assert abs(v-ref)<=tolerance, (v,ref,tolerance)


def main():
    a814=seccion_termica_kcmil(6.814)
    a184=seccion_termica_kcmil(6.184)
    i_retro=59.81/seccion_termica_kcmil(1)
    check(a814,65.904981079462,1e-8)
    check(a184,59.811623568446,1e-8)
    check(i_retro,6.184,0.001)
    area_mm2=a814*0.506707479098
    d_min=sqrt(4*area_mm2/pi)
    check(d_min,6.5207,0.002)

    # Entrada de H.3 = 744.8A, diferente de la corriente inferida de tablas.
    grid1_real=malla(744.8,False)
    grid2_real=malla(744.8,True)
    grid1_impl=malla(780,False)
    grid2_impl=malla(780,True)
    for got,ref in zip(grid1_real,(221.1692590225,91.6827309042)):
        check(got,ref,1e-8)
    for got,ref in zip(grid2_real,(155.2658933035,76.2509841184)):
        check(got,ref,1e-8)
    assert round(grid1_impl[0])==232
    assert round(grid1_impl[1],1)==96.0
    assert round(grid2_impl[0])==163
    assert round(grid2_impl[1])==80

    # Control independiente: resistencias / GPR tabulados sí usan 744.8A.
    rg1=140*(1/840+1/sqrt(20*4900)*(1+1/(1+0.5*sqrt(20/4900))))
    check(rg1*744.8,780.0,.1)
    check(1.022*744.8,761.,.3)

    # Intersección de intervalos de redondeo de las cuatro tensiones:
    # 232, 96.0, 163, 80 corresponden a corriente común ~780 A.
    limites=[]
    for rods,ref_em,ref_es,precision_paso in [
        (False,232.,96.,.1),(True,163.,80.,1.)
    ]:
        em1,es1=malla(1.,rods)
        limites.append(((ref_em-.5)/em1,(ref_em+.5)/em1))
        limites.append(((ref_es-precision_paso/2)/es1,
                        (ref_es+precision_paso/2)/es1))
    inferior=max(a for a,b in limites)
    superior=min(b for a,b in limites)
    assert inferior <= 780 <= superior

    print(f'B.1: I=6.814 kA -> {a814:.6f} kcmil, {area_mm2:.4f} mm2, d={d_min:.4f} mm')
    print(f'B.1: I=6.184 kA -> {a184:.6f} kcmil; 59.81 implica I={i_retro:.6f} kA')
    print(f'H.5 con 744.8 A -> Em={grid1_real[0]:.6f} V; Es={grid1_real[1]:.6f} V')
    print(f'H.5 con 780 A -> Em={grid1_impl[0]:.6f} V; Es={grid1_impl[1]:.6f} V (232, 96.0 publicados)')
    print(f'H.6 con 744.8 A -> Em={grid2_real[0]:.6f} V; Es={grid2_real[1]:.6f} V')
    print(f'H.6 con 780 A -> Em={grid2_impl[0]:.6f} V; Es={grid2_impl[1]:.6f} V (163, 80 publicados)')
    print(f'Intervalo comun compatible con redondeos: [{inferior:.3f}, {superior:.3f}] A')
    print('PRUEBAS MATEMÁTICAS SUPERADAS. Origen editorial histórico no verificado.')


if __name__=='__main__':
    main()
