# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:01 2021

@author: floor
"""

import numpy as np
import pandas as pd
from ast import literal_eval

# Import pergene_insertions.txt 
df = pd.read_csv(r"C:\Users\floor\PycharmProjects\LaanLab-SATAY-DataAnalysis\satay_analysis_testdata\Output_Processing_WT1_KornmannLab\ERR1533147_trimmed.sorted.bam_pergene_insertions.txt", sep = "\t")
df.columns = ["gene","chromosome", "start bp", "stop bp", "insertions", "reads"]

# Convert entire column to a list
df.loc[:,'insertions'] = df.loc[:,'insertions'].apply(lambda x: literal_eval(x))
df.loc[:,'reads'] = df.loc[:,'reads'].apply(lambda x: literal_eval(x))

# Compute the average number of reads per insertion for each gene by adding up all the reads in 1 gene
# and dividing them by the number of insertions

y = [ ]
for index, row in df.iterrows():
    if row['insertions'] != []:
        x = [row['gene'], sum(row['reads'])/len(row['reads'])]
        y.append(x)
    else: 
        x = [row['gene'], 0 ]
        y.append(x)
                                         
gene_readsperins =  pd.DataFrame(y)
gene_readsperins.columns = ["gene", "reads per insertions"]

del (y, x, index, row)

# compute the average reads per insertions over all the data.
# so we can compare this number with all the genes
avrg_reads_per_ins = gene_readsperins["reads per insertions"].sum()/len(gene_readsperins)

# compare to general reads per insertion




     
