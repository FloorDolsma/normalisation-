# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:01 2021

@author: floor
"""

import numpy as np
import pandas as pd

from genomicfeatures_dataframe_with_normalization import dna_features
   
dna_df2 = dna_features(region = 3,#['xiii', 0, 14790],
                 wig_file = r"C:\Users\floor\OneDrive\Documenten\MASTER\MEP\D18524C717111_BDDP200001534-1A_HJVN5DSXY_L1_sample1interleavedsorted_singleend_trimmed.sorted.bam.wig",
                 pergene_insertions_file = r"C:\Users\floor\OneDrive\Documenten\MASTER\MEP\D18524C717111_BDDP200001534-1A_HJVN5DSXY_L1_sample1interleavedsorted_singleend_trimmed.sorted.bam_pergene_insertions.txt",
                 variable="reads",
                 normalization_window_size=20000,
                 normalize=True,
                 plotting=True,
                 savefigure=False,
                 verbose=True)

y = []
for index, row in dna_df2.iterrows():
    if row['Feature_type'] != None and 'Gene' in row['Feature_type']:
     x= [row['Feature_name'], row['Nreadsperinsrt']]
     y.append(x)
     
readsperins=pd.DataFrame(y,columns=['Gene_name','Reads_per_ins'])

     