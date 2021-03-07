# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:18:46 2021

@author: mohit
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

loan = pd.read_csv(r'E:\UPgrade\Git\Probability\Inferential Statistics - Student Loan.csv')
loan = loan.iloc[:,0:4]
loan.info()
loan ['Recovery'] = loan['Recovery (%)'].apply(lambda x : float(x.replace('%','')))
loan['Probability of Default'].value_counts()

loan['Unrecover']=((loan['Exposure at Default (in lakh Rs.)']*(100-loan ['Recovery']))/100)*100000
loan['Overall_lost'] = loan['Unrecover']*loan['Probability of Default']
loan['Overall_lost'].sum()