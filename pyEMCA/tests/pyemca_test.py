#!/usr/bin/env python

"""
Tests for the pyEMCA function.
"""

import unittest
import numpy as np
from ..pyemca import Dat, pSupI, SupI, pSupIV, SupIV, bal, liv, \
serLin, serUEEC, StmLin, StmUEEC, Impianto, qualitative_correction, estimation

class TestEMCA(unittest.TestCase):
    """
    Test.
    """
    supseca={'3':8, '23':10}
    supsecb={'3':4, '23':0}
    supsecc={'3':8, '23':8}
    pDatPrz=0.02
    pLivPrz=0.01
    pMed=100
    indmerc={'3':0.33, '23':0.5}
    supesta=[120]
    supestb=[0]
    supestc=[50]
    subject = {'date': 0, 'surface': 105, 'floor': 3, 'year_works': 2010}
    records = [{'price': 460000, 'date': 6, 'surface': 130, 'surface_sec': supseca, 'surface_sec_index': indmerc, 'floor': 3, 'year_works': 2000}, \
    {'price': 315000, 'date': 1, 'surface': 110, 'surface_sec': supsecb, 'surface_sec_index': indmerc, 'floor': 2, 'year_works': 2001}, \
    {'price': 350000, 'date':1, 'surface': 118, 'surface_sec': supsecc, 'surface_sec_index': indmerc, 'floor': 4, 'year_works': 2008}]
        
    def test_dat(self):
        """
        Test a simple, valid example.
        """
        DATa=Dat(self.records[0]['price'], self.pDatPrz, self.subject['date'], self.records[0]['date'])
        DATb=Dat(self.records[1]['price'], self.pDatPrz, self.subject['date'], self.records[1]['date'])
        DATc=Dat(self.records[2]['price'], self.pDatPrz, self.subject['date'], self.records[2]['date'])
        self.assertEquals(DATa, 4600.0)
        self.assertEquals(DATb, 525.0)
        self.assertEquals(DATc, 583.3333333333334)

    def test_psup1(self):
        """
        Test a simple, valid example.
        """
        psupA=pSupI(self.records[0]['price'], self.records[0]['surface'], self.records[0]['surface_sec'], self.indmerc)
        psupB=pSupI(self.records[1]['price'], self.records[1]['surface'], self.supsecb, self.indmerc)
        psupC=pSupI(self.records[2]['price'], self.records[2]['surface'], self.supsecc, self.indmerc)
        psupmin = min(psupA, psupB, psupC)
        supA = SupI(psupmin, self.subject['surface'], self.records[0]['surface'])
        supB = SupI(psupmin, self.subject['surface'], self.records[1]['surface'])
        supC = SupI(psupmin, self.subject['surface'], self.records[2]['surface'])
        self.assertEquals(supA, -70202.18228498075)
        self.assertEquals(supB, -14040.436456996149)
        self.assertEquals(supC, -36505.134788189986)        
        
    def test_psup4(self):
        """
        Test a simple, valid example.
        """        
        psupA = pSupIV(self.records[0]['price'], self.pMed, self.supesta, self.records[0]['surface'], self.supseca, self.indmerc)
        psupB = pSupIV(self.records[1]['price'], self.pMed, self.supestb, self.records[1]['surface'], self.supsecb, self.indmerc)
        psupC = pSupIV(self.records[2]['price'], self.pMed, self.supestc, self.records[2]['surface'], self.supsecc, self.indmerc)
        psupmin = min(psupA, psupB, psupC)
        supA = SupIV(psupmin, self.subject['surface'], self.records[0]['surface'])
        supB = SupIV(psupmin, self.subject['surface'], self.records[1]['surface'])
        supC = SupIV(psupmin, self.subject['surface'], self.records[2]['surface'])        
        self.assertEquals(supA, -70172.09563543004)
        self.assertEquals(supB, -14034.419127086006)
        self.assertEquals(supC, -36489.48973042362)  
        
    def test_bal1(self):
        """
        Test a simple, valid example.
        """   
        psupA=pSupI(self.records[0]['price'], self.records[0]['surface'], self.supseca, self.indmerc)
        psupB=pSupI(self.records[1]['price'], self.records[1]['surface'], self.supsecb, self.indmerc)
        psupC=pSupI(self.records[2]['price'], self.records[2]['surface'], self.supsecc, self.indmerc)
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
        psupA = pSupIV(self.records[0]['price'], self.pMed, self.supesta, self.records[0]['surface'], self.supseca, self.indmerc)
        psupB = pSupIV(self.records[1]['price'], self.pMed, self.supestb, self.records[1]['surface'], self.supsecb, self.indmerc)
        psupC = pSupIV(self.records[2]['price'], self.pMed, self.supestc, self.records[2]['surface'], self.supsecc, self.indmerc)
        psupmin = min(psupA, psupB, psupC)
        bala=bal(psupmin, 0.33, 8, 8)
        balb=bal(psupmin, 0.33, 8, 4)
        balc=bal(psupmin, 0.33, 8, 8)
        self.assertEquals(bala, 0.0)
        self.assertEquals(balb, 3705.086649550706)
        self.assertEquals(balc, 0.0) 

    def test_liv(self):
        """
        Test a simple, valid example.
        """   
        liva=liv(self.records[0]['price'], self.pLivPrz, self.subject['floor'], self.records[0]['floor'])
        livb=liv(self.records[1]['price'], self.pLivPrz, self.subject['floor'], self.records[1]['floor'])
        livc=liv(self.records[2]['price'], self.pLivPrz, self.subject['floor'], self.records[2]['floor'])
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

    def test_serueec(self):
        """
        Test a s
        """
        serA = serUEEC(15000, 20, 30, 1, 2)
        serB = serUEEC(15000, 20, 30, 1, 1)
        serC = serUEEC(15000, 20, 30, 1, 2)
        self.assertEquals(serA, -7618.619047619047)
        self.assertEquals(serB, 0.0)
        self.assertEquals(serC, -7618.619047619047)      
        
    def test_impianto(self):
        """
        Test a s
        """ 
        fova=Impianto(0, 0, 10000)
        fovb=Impianto(0, 1, 10000)
        fovc=Impianto(0, 0, 10000)   
        self.assertEquals(fova, 0)
        self.assertEquals(fovb, -10000)
        self.assertEquals(fovc, 0)
        
    def test_stmlin(self):
        """
        Test a s
        """ 
        stma=StmLin(50000, 50, self.subject['year_works'], self.records[0]['year_works'])
        stmb=StmLin(50000, 50, self.subject['year_works'], self.records[1]['year_works'])
        stmc=StmLin(50000, 50, self.subject['year_works'], self.records[2]['year_works'])       
        self.assertEquals(stma, 10000.0)
        self.assertEquals(stmb, 9000.0)
        self.assertEquals(stmc, 2000.0)
        
    def test_stmueec(self):
        """
        Test a s
        """        
        stma = StmUEEC(50000, 50, 2010, 2000, 2000, 2010)
        stmb = StmUEEC(50000, 50, 2010, 2001, 2000, 2010)
        stmc = StmUEEC(50000, 50, 2010, 2008, 2000, 2010)
        self.assertEquals(stma, 6035.602000000001)
        self.assertEquals(stmb, 5432.041800000001)
        self.assertEquals(stmc, 1207.1204000000002) 
        
    def test_last_step(self):
        """
        Test a s
        """        
        corrected_prices = [432205.91, 344189.76, 363229.03]
        base_matrix = [[1, 0],[0, 1],[0, 0]]
        last_step = qualitative_correction(base_matrix, corrected_prices)
        benchmark = np.array([363229.03, 68976.88, -19039.27])
        self.assertTrue(np.allclose(last_step, benchmark, rtol=1e-03, atol=1e-08, equal_nan=False))
        
    def test_estimation(self):
        estimation(subject=self.subject, records=self.records, pDatPrz=self.pDatPrz, pMed=self.pMed, surface_sec_indexes=self.indmerc, theorem=1, impianti=1, costo_impianti=1, qualitative=1, costo_qualitative=1)
        self.assertTrue(1)
       
if __name__ == '__main__':
    unittest.main()