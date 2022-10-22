# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:19:24 2020

@author: marcu
"""

import pandas as pd
from fpdf import FPDF
import math
import os
import time
import psutil 

contactListPath = 'example_contact_list.csv'
data = pd.read_csv(contactListPath)

# data = data.replace(r'^\s*$', 5, regex = True)

cols = data.columns.tolist()
data = data.iloc[:len(data), :5]


def construct_labels():

    end = False
    pdf = FPDF(format =  (10 * 2.54 * 10, 4.3* 2.54 * 10))
    pdf.set_font('Arial', size = 12)
    
    for index, row in data.iterrows():


        #print(f'{row[0]} completed')
        
        if index == 0:
            continue 
        
        pdf.add_page()
        pdf.cell(0,0, txt = 'PLACEHOLDER COMPANY INC.', align = 'L')
        pdf.ln(5)
        pdf.cell(0,0, txt = '3000 WATERMELON DR', align = 'L')
        pdf.ln(5)
        pdf.cell(0,0, txt = 'MURRAY, UTAH 84107', align = 'L')
        pdf.ln(5)
        pdf.cell(0,0, txt = 'USA', align = 'L')
        
        pdf.ln(22)

        for item in row:



            if type(item) != str:

                item = 5

            if item != 5:

                # if u'\u2013' in item:
                #     print(item)
                #     item.replace(u'\u2013', '-')
                pdf.cell(87)
                
                pdf.cell(200, 10, txt = f'{item}', align = 'L')
                pdf.ln(5)

            if item == 'ZUPANC':
                end = True

            if end:
                pdf.output(f'{contactListPath}_ENVELOPES.pdf', 'F')
                break
            
    pdf.output(f'{contactListPath}_ENVELOPES.pdf', 'F')
construct_labels()

'''
pdf.add_page()
pdf.set_font('Times New Roman', size = 14)
pdf.cell(200, 10, )
'''