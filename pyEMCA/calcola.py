import sys
import calcoli

def main(argv=None):
    prza=460000
    przb=315000
    przc=350000
    supa=130
    supb=110
    supc=118
    supseca=(8, 10)
    supsecb=(4, 0)
    supsecc=(8, 8)
    indmerca=(0.33, 0.5)
    indmercb=(0.33, 0.5)
    indmercc=(0.33, 0.5)
    pmededia=(100)
    pmededib=(100)
    pmededic=(100)
    supesta=(120)
    supestb=(0)
    supestc=(50)

    print "-------------------------"
    print "CALCOLO DATA"
    DATa=calcoli.Dat(prza, 0.02, 0, 6)
    DATb=calcoli.Dat(przb, 0.02, 0, 1)
    DATc=calcoli.Dat(przc, 0.02, 0, 1)
    print("DATa %s, DATb %s, DATc %s", DATa, DATb, DATc)

    print "-------------------------"
    print "CALCOLO SUPERFICIE"
    print "Digitare teorema di calcolo (1-4)"
    ans=input()
    if(ans==1):
       psupA=calcoli.pSupI(prza, supa, supseca, indmerca)
       psupB=calcoli.pSupI(przb, supb, supsecb, indmercb)
       psupC=calcoli.pSupI(przc, supc, supsecc, indmercc)
       psupmin = min(psupA, psupB, psupC)
       supA = calcoli.SupI(psupmin, 105, 130)
       supB = calcoli.SupI(psupmin, 105, 110)
       supC = calcoli.SupI(psupmin, 105, 118)
       print "Teorema I"
       print("supA, supB, supC", supA, supB, supC)
    elif(ans==4):
        psupA = calcoli.pSupIV(prza, pmededia, supesta, supa, supseca, indmerca)
        psupB = calcoli.pSupIV(przb, pmededib, supestb, supb, supsecb, indmercb)
        psupC = calcoli.pSupIV(przc, pmededic, supestc, supc, supsecc, indmercc)
        psupmin = min(psupA, psupB, psupC)
        supA = calcoli.SupIV(psupmin, 105, 130)
        supB = calcoli.SupIV(psupmin, 105, 110)
        supC = calcoli.SupIV(psupmin, 105, 118)
        print "Teorema IV"
        print("supA, supB, supC", supA, supB, supC)

    print "-------------------------"
    print "CALCOLO BAL"
    bala=calcoli.bal(psupmin, 0.33, 8, 8)
    balb=calcoli.bal(psupmin, 0.33, 8, 4)
    balc=calcoli.bal(psupmin, 0.33, 8, 8)
    print ("Bala, Balb, Balc", bala, balb, balc)

    print "-------------------------"
    print "CALCOLO LIV"
    liva=calcoli.liv(prza, 0.01, 3, 3)
    livb=calcoli.liv(przb, 0.01, 3, 2)
    livc=calcoli.liv(przc, 0.01, 3, 4)
    print ("lIVA, Livb, Livc", liva, livb, livc)

    print "-------------------------"
    print "CALCOLO SERVIZIO LINEARE"
    serA=calcoli.serLin(15000, 20, 30, 1, 2)
    serB=calcoli.serLin(15000, 20, 30, 1, 1)
    serC=calcoli.serLin(15000, 20, 30, 1, 2)
    print ("SerA, SerB, SerC", serA, serB, serC)


    print "-------------------------"
    print "CALCOLO SERVIZIO UEEC"
    serA = calcoli.serUEEC(15000, 20, 30, 1, 2)
    serB = calcoli.serUEEC(15000, 20, 30, 1, 1)
    serC = calcoli.serUEEC(15000, 20, 30, 1, 2)
    print ("SerA, SerB, SerC", serA, serB, serC)

    print "-------------------------"
    print "CALCOLO IMPIANTO"
    fova=calcoli.fov(10000, 0, 0)
    fovb=calcoli.fov(10000, 0, 1)
    fovc=calcoli.fov(10000, 0, 0)
    print("FOVA, FOVB, FOVC", fova, fovb, fovc)

    print "-------------------------"
    print "CALCOLO STATO MANUTENZIONE LINEARE"
    stma=calcoli.StmLin(50000,50, 2010, 2000)
    stmb=calcoli.StmLin(50000, 50, 2010, 2001)
    stmc=calcoli.StmLin(50000, 50, 2010, 2008)
    print ("StmA, Stmb, Stmc", stma, stmb, stmc)

    print "-------------------------"
    print "CALCOLO STATO MANUTENZIONE UEEC"
    #Da correggere i dati
    stma = calcoli.StmUEEC(50000, 50, 2010, 2000, 2000, 2010)
    stmb = calcoli.StmUEEC(50000, 50, 2010, 2001, 2000, 2010)
    stmc = calcoli.StmUEEC(50000, 50, 2010, 2008, 2000, 2010)
    print ("StmA, Stmb, Stmc", stma, stmb, stmc)

    # fine main
    return 50


if __name__ == "__main__":
    sys.exit(main())