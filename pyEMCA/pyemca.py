def Dat(prz, saggio, mesidastima, mesiatto):
    if saggio > 0:
        pdat = (prz * (-saggio)) / 12
    else:
        pdat = (prz * (saggio)) / 12

    dat = pdat * (mesidastima - mesiatto)
    return dat

#Primo teorema
#supsec e indici sono due liste
def pSupI(prz, supPrinc, supSec, indici):
    i = 0
    supSecInd = 0
    psup = 0

    if not (isinstance(supSec, (int, long))):
        for superficie in supSec:
            supSecInd += superficie * indici[i]
            print "Debug"
            print superficie, indici[i]
            i = i + 1
    else:
        supSecInd += supSec * indici

    psup = prz / (supPrinc + supSecInd)
    print psup
    return psup

def SupI(psupmin,supSubject, stimaComp):

    sup = psupmin * (supSubject - stimaComp)
    return sup

#Quarto teorema
#pMedEdi, supEstm, supSec, indici -> Liste
def pSupIV(prz, pMedEdi, supEstm, supPrinc, supSec, indici):
    i = 0
    pMedEst = 0
    supSecInd = 0
    psup=0

    if not(isinstance(pMedEdi, (int, long))):
        for pmed in pMedEdi:
           pMedEst = pmed + supEstm[i]
           i = i + 1
        i = 0

    else:
        pMedEst = pMedEdi + supEstm
    print pMedEst

    if not (isinstance(supSec, (int, long))):
        for superficie in supSec:
            supSecInd += superficie * indici[i]
            i = i + 1
        print supSecInd
    else:
        supSecInd += supSec * indici

    psup = (prz - pMedEst) / (supPrinc + supSecInd)
    print psup
    return psup

def SupIV(psupmin, supSubject, stimaComp):

    sup = psupmin*(supSubject - stimaComp)
    return sup

def bal(psup, indice, supsecstima, supseccomp):
    psupsec = 0
    psupsec = psup * indice

    supsec = psupsec * (supsecstima - supseccomp)
    return supsec

def por(): #fisso
    return 13

def liv(prz, saggiovarp, livellosogg, livellocomp): #Bisogna implementare il controllo del piano
    if (livellocomp > livellosogg):
        pliv=prz*(saggiovarp)/(1+saggiovarp)
    else:
        pliv=prz*saggiovarp

    liv=pliv*(livellosogg - livellocomp)
    return liv

def serLin(costoSer, vetusta, vitautile, numserv, servcomp):

    pser=costoSer*(1-vetusta/float(vitautile))

    ser = pser * (numserv - servcomp)
    return ser

def serUEEC(costoSer, vetusta, vitautile, numserv, servcomp):
    x = (10 * (vetusta/float(vitautile)) + 2)
    pser = costoSer * (pow(x, 2) - 4.004)/140
    ser = pser * (numserv - servcomp)
    return ser

def fov(costoIMP, presSoggStima, presComp):
    pimp = costoIMP
    imp = pimp * (presSoggStima - presComp)
    return imp

def dom(): #fisso

    return 17
def Amm(): #fisso
    return 18

def StmLin(costoNuovoSTM, vitautile, anzRistSoggStm, anzRistComp):
    pstm = costoNuovoSTM * (1/float(vitautile))
    stm = pstm * (anzRistSoggStm-anzRistComp)
    return stm

def StmUEEC(costoNuovoSTM, vitautile, anzRistSoggStm, anzRistComp, annoComp, annoSogg):
    year = 2016
    x1=(year-annoComp)
    x2=(x1/float(vitautile))+0.2
    p1=pow(x2, 2)
    y1=(year-annoSogg)
    y2=(y1/float(vitautile))+0.2
    p2=pow(y2, 2)

    pstm = (((costoNuovoSTM *100)/140) * p1 - p2)/(year-annoComp)
    print pstm
    stm = pstm * (anzRistSoggStm - anzRistComp)
    return stm