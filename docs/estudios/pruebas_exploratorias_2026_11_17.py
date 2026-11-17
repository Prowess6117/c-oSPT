# NOTA POSTERIOR: las diferencias B.1/H.3 fueron resueltas matemáticamente.
# Ver diagnostico_inconsistencias_ieee80.py y DIAGNOSTICO_RESUELTO_B1_H3_2026-11-17.md
# c-oSPT — PRUEBAS DOCUMENTALES, NO MOTOR, NO USO EN DISEÑO REAL
# IEEE Std 80-2013/Cor1-2015 §§11.3,14.2-14.3,15.9-15.10, anexos B/H;
# IEEE Std 81-2012 §7.2.3.
# Ejecución: python3 docs/estudios/pruebas_exploratorias_2026_11_17.py
# Sin dependencias de terceros ni lectura de PDF, sin datos reales.
from math import pi, sqrt, log, exp

def porcentaje(valor, referencia):
    return 100*abs(valor-referencia)/abs(referencia)

def decremento(xr, tf, f=60):
    ta=xr/(2*pi*f)
    return sqrt(1+ta/tf*(1-exp(-2*tf/ta)))

def conductor_kcmil(ikA, tc, tcap, alfa, rho, ko, tm, ta):
    return ikA*197.4/sqrt(tcap/(tc*alfa*rho)*log((ko+tm)/(ko+ta)))

def conductor_mm2(ikA, tc, tcap, alfa, rho, ko, tm, ta):
    return ikA/sqrt(tcap*1e-4/(tc*alfa*rho)*log((ko+tm)/(ko+ta)))

def resist_schwarz(rho,A,Lc,h,dc,N,Lr,dr,k1,k2):
    a,b=dc/2,dr/2
    ap=sqrt(2*a*h) if h>0 else a
    r1=rho/(pi*Lc)*(log(2*Lc/ap)+k1*Lc/sqrt(A)-k2)
    r2=rho/(2*pi*N*Lr)*(log(4*Lr/b)-1+2*k1*Lr/sqrt(A)*(sqrt(N)-1)**2)
    rm=rho/(pi*Lc)*(log(2*Lc/Lr)+k1*Lc/sqrt(A)-k2+1)
    return r1,r2,rm,(r1*r2-rm**2)/(r1+r2-2*rm)

def wenner(a,b,r):
    return 4*pi*a*r/(1+2*a/sqrt(a*a+4*b*b)-a/sqrt(a*a+b*b))

def rg_simple(rho,A,L,h):
    return rho*(1/L+1/sqrt(20*A)*(1+1/(1+h*sqrt(20/A))))

def km(n,D,h,d,varillas=False):
    kii=1 if varillas else 1/(2*n)**(2/n)
    kh=sqrt(1+h/1.0)
    return (log(D*D/(16*h*d)+(D+2*h)**2/(8*D*d)-h/(4*d))
            +kii/kh*log(8/(pi*(2*n-1))))/(2*pi)

def ks(n,D,h):
    return (1/(2*h)+1/(D+h)+(1/D)*(1-.5**(n-2)))/pi

def main():
    print("A. Termica, anexo B.1")
    ac=conductor_kcmil(6.814,.5,3.85,.00378,5.862,245,700,40)
    am=conductor_mm2(6.814,.5,3.85,.00378,5.862,245,700,40)
    print("  acero cobre 30%: %.6f kcmil / %.6f mm2; impreso: 59.81 kcmil" %(ac,am))
    assert abs(am-ac*.5067074791)<.02
    assert porcentaje(ac,59.81)>10 # El valor editorial 59.81 corresponde a I=6.184 kA, no 6.814 kA
    cu=6.814*7.06*sqrt(.5)
    assert abs(cu-34.02)<.01
    kf=conductor_kcmil(1,1,3.85,.00378,5.86,245,1084,40)
    assert abs(kf-12.06)<.02
    print("  cobre: %.6f vs 34.02; Kf 30%% a 1084 C: %.6f vs 12.06" %(cu,kf))

    print("B. Decremento, ecuacion 84, tabla 10 a 60 Hz")
    for tf,xr,ref in [(.05,10,1.232),(.10,20,1.232),(.20,30,1.181),(.50,10,1.026),(.50,40,1.101)]:
        got=decremento(xr,tf)
        print("  t=%.2f xr=%d: %.6f vs %.3f"%(tf,xr,got,ref))
        assert abs(got-ref)<.0003
    print("  sensibilidad 50 Hz, tf=.05, X/R=10: %.6f" % decremento(10,.05,50))

    print("C. Sf ejemplo de 15.9")
    za,zb,rg=4.22+1.04j,1.88+.89j,2.5
    z=za*zb/(za+zb)
    f=z/(z+rg)
    ig=f*2297
    assert abs(z-(1.31+.52j))<.01
    assert abs(abs(f)-.37)<.005
    assert abs(ig+(2297-ig)-2297)<1e-9
    print("  Zeq=",z,"|Sf|=%.6f, |Ig|=%.6f; .37*2297=%.2f"%(abs(f),abs(ig),.37*2297))

    print("D. Schwarz sintetico, Fig24 curva B")
    r1,r2,rm,total=resist_schwarz(100,25,60,.5,.01,4,2,.016,1.15,4.78)
    determinant=r1*r2-rm*rm
    r_matrix=1/((r2-rm)/determinant+(r1-rm)/determinant)
    assert r1*r2/(r1+r2)<total<min(r1,r2)
    assert abs(total-r_matrix)<1e-10
    assert abs(resist_schwarz(200,25,60,.5,.01,4,2,.016,1.15,4.78)[-1]-2*total)<1e-10
    print("  R1 %.6f R2 %.6f Rm %.6f Rg %.6f" %(r1,r2,rm,total))

    print("E. Wenner / tabla H1 (es necesario controlar b/a)")
    for a,R,ref in [(.3048,109.38,209.5),(1.524,30.40,291.1),(3.048,15.01,287.5)]:
        approx=2*pi*a*R
        corrected=wenner(a,.15,R)
        assert abs(approx-ref)<.1
        print("  a=%.4f, b/a=%.3f: aprox=%.4f, completa=%.4f" %(a,.15/a,approx,corrected))
    assert abs(wenner(2,0,10)-2*pi*2*10)<1e-10

    print("F. Benchmark H3 Grid1")
    rho,A,L,h,ig=140,4900,840,.5,744.8
    rg=rg_simple(rho,A,L,h)
    gpr=rg*ig
    assert abs(rg-1.05)<.005 and abs(gpr-780)<.1
    n,D,d=6,14,.0105
    ki=.644+.148*n
    em=rho*ig*km(n,D,h,d)*ki/L
    es=rho*ig*ks(n,D,h)*ki/(.75*L)
    print("  Rg %.6f vs 1.05, GPR %.6f vs 780" %(rg,gpr))
    print("  Em %.6f vs 232, Es %.6f vs 96: CIFRAS TABULADAS IMPLICAN 780 A, no 744.8 A" %(em,es))

if __name__ == "__main__":
    main()
