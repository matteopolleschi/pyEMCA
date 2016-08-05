#!/usr/bin/env python

"""
Tests for the pyEMCA function.
"""

import unittest
from ..pyemca import Dat, pSupI, SupI, pSupIV, SupIV, bal, liv, serLin

class TestEMCA(unittest.TestCase):
    """
    Test.
    """
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
    
#    def __init__(self):
#        self.prza=2131
    
    def test_dat(self):
        """
        Test a simple, valid example.
        """
        DATa=Dat(self.prza, 0.02, 0, 6)
        DATb=Dat(self.przb, 0.02, 0, 1)
        DATc=Dat(self.przc, 0.02, 0, 1)
        self.assertEquals(DATa, 4600.0)
        self.assertEquals(DATb, 525.0)
        self.assertEquals(DATc, 583.3333333333334)

    def test_psup1(self):
        """
        Test a simple, valid example.
        """
        psupA=pSupI(self.prza, self.supa, self.supseca, self.indmerca)
        psupB=pSupI(self.przb, self.supb, self.supsecb, self.indmercb)
        psupC=pSupI(self.przc, self.supc, self.supsecc, self.indmercc)
        psupmin = min(psupA, psupB, psupC)
        supA = SupI(psupmin, 105, 130)
        supB = SupI(psupmin, 105, 110)
        supC = SupI(psupmin, 105, 118)
        self.assertEquals(supA, -70202.18228498075)
        self.assertEquals(supB, -14040.436456996149)
        self.assertEquals(supC, -36505.134788189986)        
        
    def test_psup4(self):
        """
        Test a simple, valid example.
        """        
        psupA = pSupIV(self.prza, self.pmededia, self.supesta, self.supa, self.supseca, self.indmerca)
        psupB = pSupIV(self.przb, self.pmededib, self.supestb, self.supb, self.supsecb, self.indmercb)
        psupC = pSupIV(self.przc, self.pmededic, self.supestc, self.supc, self.supsecc, self.indmercc)
        psupmin = min(psupA, psupB, psupC)
        supA = SupIV(psupmin, 105, 130)
        supB = SupIV(psupmin, 105, 110)
        supC = SupIV(psupmin, 105, 118)        
        self.assertEquals(supA, -70172.09563543004)
        self.assertEquals(supB, -14034.419127086006)
        self.assertEquals(supC, -36489.48973042362)  
        
    def test_bal1(self):
        """
        Test a simple, valid example.
        """   
        psupA=pSupI(self.prza, self.supa, self.supseca, self.indmerca)
        psupB=pSupI(self.przb, self.supb, self.supsecb, self.indmercb)
        psupC=pSupI(self.przc, self.supc, self.supsecc, self.indmercc)
        psupmin = min(psupA, psupB, psupC)
        bala=bal(psupmin, 0.33, 8, 8)
        balb=bal(psupmin, 0.33, 8, 4)
        balc=bal(psupmin, 0.33, 8, 8)
        self.assertEquals(bala, 0.0)
        self.assertEquals(balb, 3706.6752246469837)
        self.assertEquals(balc, 0.0)           

    def test_bal4(self):
        """
        Test a simple, valid example.
        """   

    def test_liv(self):
        """
        Test a simple, valid example.
        """   
        liva=liv(self.prza, 0.01, 3, 3)
        livb=liv(self.przb, 0.01, 3, 2)
        livc=liv(self.przc, 0.01, 3, 4)
        self.assertEquals(liva, 0.0)
        self.assertEquals(livb, 3150.0)
        self.assertEquals(livc, -3465.3465346534654)   
        
    def test_serlin(self):
        """
        Test a simple, valid example.
        """   
        serA=serLin(15000, 20, 30, 1, 2)
        serB=serLin(15000, 20, 30, 1, 1)
        serC=serLin(15000, 20, 30, 1, 2)  
        self.assertEquals(serA, -5000.000000000001)
        self.assertEquals(serB, 0.0)
        self.assertEquals(serC, -5000.000000000001)        
       
if __name__ == '__main__':
    unittest.main()