#!/usr/bin/env python3
"""c-oSPT: ensayos DOCUMENTALES de ecuaciones citadas. No es motor ni diseño.
Fuente: IEEE Std 80-2013 incl. Cor 1-2015; IEEE Std 81-2012.
Los datos sintéticos se distinguen de referencias numéricas impresas.
Solo math/cmath de biblioteca estándar; sin archivos privados ni red.
"""
import math
import cmath

RESULTADOS = []

def chequeo(nombre, observado, esperado, tolerancia, nota=''):
    diff=abs(observado-esperado)
    assert diff <= tolerancia, f'{nombre}: {observado} / {esperado}; diff {diff} excede {tolerancia}'
    RESULTADOS.append((nombre, observado, esperado, diff, nota))
    return observado

def valor_si_positivo(nombre,x):
    if not (math.isfinite(x) and x>0):
        raise ValueError(f'{nombre}: entrada no positiva o no finita')
    return x

def cs_aproximado(rho, rho_s, h_s):
    for n,x in [('rho',rho),('rho_s',rho_s),('h_s',h_s)]: valor_si_positivo(n,x)
    if rho_s < rho:
        raise ValueError('IEEE80 §7.4: expresión empírica Cs no aplicable a superficie menos resistiva')
    return 1-0.09*(1-rho/rho_s)/(2*h_s+0.09)

def tolerables(rho, rho_s, hs, ts, masa):
    valor_si_positivo('ts',ts)
    if masa not in [50,70]: raise ValueError('masa de referencia no admitida')
    cs=cs_aproximado(rho,rho_s,hs) if rho_s!=rho else 1.0
    k={50:0.116,70:0.157}[masa]
    return (1000+1.5*cs*rho_s)*k/math.sqrt(ts), (1000+6*cs*rho_s)*k/math.sqrt(ts)

def seccion_kcmil(i_ka,t,tcap,alpha,rhomicro,ko,tm,ta):
    for name,x in [('i_ka',i_ka),('t',t),('tcap',tcap),('alpha',alpha),('rhomicro',rhomicro)]:valor_si_positivo(name,x)
    ratio=(ko+tm)/(ko+ta)
    if ratio<=1: raise ValueError('temperatura final debe superar inicial')
    return i_ka*197.4/math.sqrt(tcap/(t*alpha*rhomicro)*math.log(ratio))

def decremento(x_r,t,f):
    for name,x in [('x_r',x_r),('t',t),('f',f)]: valor_si_positivo(name,x)
    ta=x_r/(2*math.pi*f)
    return math.sqrt(1+(ta/t)*(-math.expm1(-2*t/ta)))

def sverak(rho, area, longitud, prof):
    for name,x in [('rho',rho),('area',area),('longitud',longitud)]:valor_si_positivo(name,x)
    if prof<0:raise ValueError('profundidad negativa')
    return rho*(1/longitud+1/math.sqrt(20*area)*(1+1/(1+prof*math.sqrt(20/area))))

def wenner(a,b,r):
    for n,x in [('a',a),('r',r)]:valor_si_positivo(n,x)
    if b<0:raise ValueError('b negativa')
    return 4*math.pi*a*r/(1+2*a/math.sqrt(a*a+4*b*b)-a/math.sqrt(a*a+b*b))

def dos_capas_superficie(a,rho1,rho2,h):
    # IEEE81 Anexo A (A.1)-(A.2), electrodos puntuales superficiales, no profundidad real
    for n,x in [('a',a),('rho1',rho1),('rho2',rho2),('h',h)]:valor_si_positivo(n,x)
    k=(rho2-rho1)/(rho2+rho1)
    s=0.0
    for n in range(1,1000):
        v=k**n*(1/math.sqrt(1+(2*n*h/a)**2)-1/math.sqrt(4+(2*n*h/a)**2))
        s+=v
        if n>10 and abs(v)<1e-14: break
    else: raise ArithmeticError('serie no converge con 1000 términos')
    return rho1*(1+4*s)

def km(D,h,d,n,varillas):
    for key,v in [('D',D),('h',h),('d',d),('n',n)]:valor_si_positivo(key,v)
    kii=1 if varillas else (2*n)**(-2/n)
    kh=math.sqrt(1+h)
    v=D**2/(16*h*d)+(D+2*h)**2/(8*D*d)-h/(4*d)
    if v<=0:raise ValueError('logaritmo fuera de dominio')
    return (math.log(v)+kii/kh*math.log(8/(math.pi*(2*n-1))))/(2*math.pi)

def ks(D,h,n):
    return (1/(2*h)+1/(D+h)+(1/D)*(1-.5**(n-2)))/math.pi

def tensiones_cuadrada(IG, D, h, d, n, Lc, Lr_total=0, lr=0, Lx=70,Ly=70):
    rods=Lr_total>0
    lm=Lc+(1.55+1.22*lr/math.sqrt(Lx**2+Ly**2))*Lr_total if rods else Lc
    ls=.75*Lc+.85*Lr_total
    ki=.644+.148*n
    rho=140
    return (rho*IG*km(D,h,d,n,rods)*ki/lm,rho*IG*ks(D,h,n)*ki/ls)

def matriz_schwarz():
    rho,A,Lc,h,dc,N,Lr,dr,k1,k2=100,25,60,.5,.010,4,2,.016,1.15,4.78
    a,b=dc/2,dr/2
    ap=math.sqrt(2*a*h)
    r1=rho/(math.pi*Lc)*(math.log(2*Lc/ap)+k1*Lc/math.sqrt(A)-k2)
    r2=rho/(2*math.pi*N*Lr)*(math.log(4*Lr/b)-1+2*k1*Lr/math.sqrt(A)*(math.sqrt(N)-1)**2)
    rm=rho/(math.pi*Lc)*(math.log(2*Lc/Lr)+k1*Lc/math.sqrt(A)-k2+1)
    eq=(r1*r2-rm**2)/(r1+r2-2*rm)
    det=r1*r2-rm**2
    # Comprobación de circuitos por solución de sistema 2x2, tensión fija de 1 V
    i1=(r2-rm)/det; i2=(r1-rm)/det
    chequeo('Schwarz KVL grupo malla',r1*i1+rm*i2,1.0,1e-12,'sintético')
    chequeo('Schwarz KVL grupo varillas',rm*i1+r2*i2,1.0,1e-12,'sintético')
    chequeo('Schwarz equivalencia de conductancia',1/(i1+i2),eq,1e-12,'sintético')
    chequeo('Schwarz resultado reproducido',eq,8.520098,0.00001,'sintético, no patrón externo')

def ejecutar():
    # B.1 IEEE80 §8.4 y §11, 70kg: Cs redondeado editorial vs cálculo completo.
    cs=cs_aproximado(400,2500,.102)
    chequeo('Cs B1',cs,0.74,.005,'aprox. (27) vs valor redondeado')
    touch,step=tolerables(400,2500,.102,.5,70)
    chequeo('Etouch B1',touch,838.2,3.0,'publicado usa Cs redondeado .74')
    chequeo('Estep B1',step,2686.6,10.0,'publicado usa Cs redondeado .74')
    chequeo('50kg debajo 70kg',float(tolerables(400,2500,.102,.5,50)[0]<touch),1.0,0,'orden de criterios')
    chequeo('t_s doble reduce límite factor sqrt2',tolerables(400,2500,.102,1,70)[0]/touch,1/math.sqrt(2),1e-12,'metamórfica')
    chequeo('térmico cobre B1',6.814*7.06*math.sqrt(.5),34.02,.02,'IEEE80 B.1')
    acero=seccion_kcmil(6.814,.5,3.85,.00378,5.862,245,700,40)
    chequeo('térmico acero 6.814 kA',acero,65.904981,.00001,'B1 reconciliado')
    chequeo('térmico 6.184 explica B1 editorial',seccion_kcmil(6.184,.5,3.85,.00378,5.862,245,700,40),59.81,.01,'dato diferente, no corrección oficial')
    chequeo('térmica escala lineal',seccion_kcmil(2*6.814,.5,3.85,.00378,5.862,245,700,40)/acero,2.0,1e-12,'metamórfica')
    for tf,xr,target in [(.05,10,1.232),(.10,20,1.232),(.2,30,1.181),(.5,10,1.026),(.5,40,1.101)]:
        chequeo(f'Df tf={tf} xr={xr}',decremento(xr,tf,60),target,.0003,'IEEE80 Tabla 10, 60Hz')
    assert decremento(40,.5,60)>decremento(10,.5,60)
    assert decremento(10,5,60)<decremento(10,.5,60)
    # 2 ramas retorna la misma corriente por KCL, sin tautología "I + (Itotal-I)"
    za=4.22+1.04j;zb=1.88+.89j;rg=2.5;vsource=2297
    zret=1/(1/za+1/zb)
    vgrid=vsource/(1/rg+1/za+1/zb) # fuente total de corriente
    i_grid=vgrid/rg;ia=vgrid/za;ib=vgrid/zb
    chequeo('KCL reparto corriente',abs(i_grid+ia+ib-vsource),0.,1e-10,'verificación por 3 ramas')
    chequeo('S_f ejemplo 15.9',abs(i_grid/vsource),.37,.005,'módulo, 0.37 redondeado')
    matriz_schwarz()
    # Wenner 81 §7.2.3: límite sonda ideal; finite depth must be explicit.
    chequeo('Wenner b=0',wenner(1,0,10),2*math.pi*10,1e-12,'identidad')
    chequeo('Wenner H1 0.3048 m',2*math.pi*.3048*109.38,209.5,.1,'Tabla H1 usa aprox., b/a=0.492')
    assert abs(wenner(.3048,.15,109.38)/(2*math.pi*.3048*109.38)-1)>.3
    # IEEE81 Anexo A: modelo dos capas de electrodos ideales; NO inversión validada
    chequeo('A2 homogéneo',dos_capas_superficie(5,100,100,6.096),100,1e-10,'K=0')
    assert abs(dos_capas_superficie(.001,300,100,6.096)-300)<.001
    assert abs(dos_capas_superficie(10000,300,100,6.096)-100)<1.0
    for a in [1,3,6,12,24,50]:
        x=dos_capas_superficie(a,300,100,6.096)
        assert 100<x<300
    # Recuperar h manteniendo resistividades conocidas. No implica inversión general 3 parámetros.
    a=24.; target=dos_capas_superficie(a,300,100,6.096)
    lo,hi=.25,40.
    for _ in range(75):
        m=(lo+hi)/2
        if dos_capas_superficie(a,300,100,m)<target:lo=m
        else:hi=m
    chequeo('A2 recuperar espesor con resistividades conocidas',(lo+hi)/2,6.096,.001,'bisección validación del modelo ideal')
    # Sverak 57 / ejemplos B.1-B.4, resultado redondeado editorial
    for k,area,L in [('B1',4900,1540),('B2',4900,1690),('B3',5292,2039),('B4',4900,1755)]:
        target={'B1':2.78,'B2':2.75,'B3':2.62,'B4':2.74}[k]
        chequeo('Sverak '+k,sverak(400,area,L,.5),target,.01,'IEEE80 B.'+k[-1])
    chequeo('GPR B1',1908*sverak(400,4900,1540,.5),5304,30,'referencia de 5304 usa 2.78 redondeado')
    chequeo('Sverak R proporcional a rho',sverak(200,4900,1540,.5)/sverak(400,4900,1540,.5),.5,1e-12,'metamórfica')
    assert sverak(400,4900,1690,.5)<sverak(400,4900,1540,.5)
    # B.1–B.4 tensiones. Valores publicados redondean factores Km/Ki/Ks intermedios.
    casos = [
      ('B.1',11,1540,0,0,70,70,1002.1,None),
      ('B.2',11,1540,150,7.5,70,70,747.4,548.9),
      ('B.3',11.35,1659,380,10,63,84,595.8,None),
      ('B.4',12.2,1575,180,7.5,70,105,761.1,574.6),
    ]
    for name,n,lc,lr_tot,lr,lx,ly,ref_em,ref_es in casos:
        ki=.644+.148*n
        lm=lc+(1.55+1.22*lr/math.sqrt(lx**2+ly**2))*lr_tot if lr_tot else lc
        ls=.75*lc+.85*lr_tot
        em=400*1908*km(7,.5,.01,n,lr_tot>0)*ki/lm
        es=400*1908*ks(7,.5,n)*ki/ls
        chequeo(name+' E_m',em,ref_em,.015*ref_em,'IEEE80 anexo B, precisión de términos intermedios')
        if ref_es is not None:
            chequeo(name+' E_s',es,ref_es,.015*ref_es,'IEEE80 anexo B, precisión de términos intermedios')

    # IEEE H.3: discrepancia de corriente, 2 grids separados; repetir pruebas de referencia
    for rods in [False,True]:
        e1,e2=tensiones_cuadrada(744.8,14,.5,.0105,6,840,150 if rods else 0,7.5 if rods else 0)
        E1,E2=tensiones_cuadrada(780,14,.5,.0105,6,840,150 if rods else 0,7.5 if rods else 0)
        if rods:
            chequeo('Grid2 E_m 744.8A',e1,155.265893,.0001,'derivado, no cifra editorial')
            chequeo('Grid2 E_s 744.8A',e2,76.250984,.0001,'derivado, no cifra editorial')
            chequeo('Grid2 E_m impreso con 780A',E1,163,.5,'H.6 usa corriente implícita')
            chequeo('Grid2 E_s impreso con 780A',E2,80,.5,'H.6 usa corriente implícita')
        else:
            chequeo('Grid1 E_m 744.8A',e1,221.169259,.0001,'derivado, no cifra editorial')
            chequeo('Grid1 E_s 744.8A',e2,91.682731,.0001,'derivado, no cifra editorial')
            chequeo('Grid1 E_m impreso con 780A',E1,232,.5,'H.5 usa corriente implícita')
            chequeo('Grid1 E_s impreso con 780A',E2,96,.05,'H.5 usa corriente implícita')
    # Rechazo deliberado de datos fuera de dominio
    for fn,args in [(cs_aproximado,(400,100,.1)),(tolerables,(100,2500,.1,-.5,70)),(sverak,(100,0,10,.5)),(wenner,(0,0,2)),(decremento,(10,0,60))]:
        try:fn(*args)
        except ValueError:pass
        else:raise AssertionError('Falta bloqueo de entrada inválida')
    print('RESULTADO:',len(RESULTADOS),'comprobaciones superadas; ninguna equivale a validación del motor.')
    for name,obs,exp,diff,nota in RESULTADOS:
        print(f'{name} | calculado {obs:.9g} | ref {exp:.9g} | err abs {diff:.4g} | {nota}')

if __name__=='__main__': ejecutar()