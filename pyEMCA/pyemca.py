import numpy as np

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
    supSecInd = 0
    psup = 0

    if not (isinstance(supSec, (int, long))):
        for (k,v),(k2,v2) in zip(supSec.items(),indici.items()):
            supSecInd += v * v2
    else:
        supSecInd += supSec * indici

    psup = prz / (supPrinc + supSecInd)
    return psup

def SupI(psupmin,supSubject, stimaComp):

    sup = psupmin * (supSubject - stimaComp)
    return sup

#Quarto teorema
#pMedEdi, supEstm, supSec, indici -> Liste
def pSupIV(prz, pMed, supEstm, supPrinc, supSec, indici):
    pMedEst = 0
    supSecInd = 0
    psup=0

    if not(isinstance(supEstm, (int, long))):
        for sup in supEstm:
           pMedEst = pMed + sup
    else:
        pMedEst = pMed + supEstm

    if not (isinstance(supSec, (int, long))):
        for (k,v),(k2,v2) in zip(supSec.items(),indici.items()):
            supSecInd += v * v2
    else:
        supSecInd += supSec * indici

    psup = (prz - pMedEst) / (supPrinc + supSecInd)
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
    stm = pstm * (anzRistSoggStm - anzRistComp)
    return stm
    
def Impianto(val_subject, val_record, costo_impianto):
    result = (val_subject - val_record) * costo_impianto
    return result
    
def qualitative_correction(base_matrix, corrected_prices):
    matrix = np.insert(base_matrix, 0, values=1, axis=1) 
    moore_penrose = np.linalg.pinv(matrix, rcond=1e-15)
    result = np.dot(moore_penrose, corrected_prices)
    return result
    
def estimation(subject, records, impianti, pDatPrz, pMed, surface_sec_indexes, theorem, costo_impianti, qualitative, costo_qualitative):
    for record in records:
        record['dat'] = Dat(record['price'], pDatPrz, subject['date'], record['date'])
        if theorem==1: 
            record['psup'] = pSupI(record['price'], record['surface'], record['surface_sec'], surface_sec_indexes)
        elif theorem==4: 
            record['psup'] = pSupIV(record['price'], pMed, supesta, record['surface'], record['surface_sec'], surface_sec_indexes)
        else: break      
    psupmin = min([record['psup'] for record in records])
    for record in records:
        if theorem==1: 
            record['sup'] = SupI(psupmin, subject['surface'], record['surface'])
    return