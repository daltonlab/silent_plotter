# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:23:02 2019
v0.91: implemented Scatter and Histogram
v0.92: implemented (partially) comand line arguments
v0.93: Color according to file (need more flexibility)
@author: fabio
"""
#import re
#import numpy as np 
import os
import argparse
import matplotlib.pyplot as plt 


# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')
# Required positional argument
parser.add_argument('-s', '--silent', nargs='+', type=str,required=True, help='silent file')

# Optional positional argument
parser.add_argument('-p', '--plot', type=str, nargs='?', help='Plot type', default='scatter')
parser.add_argument('-mx', '--metricx', type=str, nargs='?', help='Metric to be used in x axis in scatter/histogram plot', default='rms')
parser.add_argument('-my', '--metricy', type=str, nargs='?', help='Metric to be used in x axis in scatter plot', default='score')
#parser.add_argument('-', '--metricy', type=str, nargs='?', help='Metric to be used in x axis in scatter plot', default='score')
# Optional argument
#parser.add_argument('--opt_arg', type=int, help='An optional integer argument')
# Switch
#parser.add_argument('--switch', action='store_true',help='A boolean switch')

args = parser.parse_args()
print("Argument values:")
print(args.plot)
print(args.metricx)
print(args.metricy)
print(args.silent)





os.chdir("C:\\Users\\fgozz\\Desktop\\data")
scores=[]
filename_list=[] #list of silent filenames
filename_int=[] #code for filenames
first_line=True #to get the first headers only

# read silent file, get headers, then all values. Strip additional headers
for file in args.silent:
    filename=str(file)
    with open(filename, 'r') as s_file:
        lines = s_file.readlines()
              
        for line in lines:
            
            if line.startswith('SCORE:') and first_line:
                first_line=False
                a=line.split()
                scores.append(a)
                filename_list.append(os.path.splitext(file)[0])
            if line.startswith('SCORE:') :
                a=line.split()
                if a[1] != 'score' :
                   scores.append(a)
                   filename_list.append(os.path.splitext(file)[0])

num_lin=len(scores) # Number of models
num_col=len(scores[0]) # Number of columns in SCORE line
idx_score=scores[0].index(args.metricy) 
idx_rms=scores[0].index(args.metricx)


for l in filename_list:
    if l=='total':
        filename_int.append(0)
    else:
        filename_int.append(1)

filename_int.pop()
x_vec=[]
y_vec=[]

for x in range(1,num_lin):
    x_vec.append(float(scores[x] [idx_rms]))
    y_vec.append(float(scores[x] [idx_score]))

colors = ['red','green']
plt.scatter(x_vec,y_vec, c=filename_int, label=filename_list, alpha=0.5, edgecolor='k')
plt.xlabel(args.metricx)
plt.ylabel(args.metricy)
plt.title('Rosetta Scatter Plot')
plt.legend(args.silent)
plt.show()
# plt.savefig('foo.png', bbox_inches='tight', dpi=300)
#plt.hist(x_vec, bins=15, edgecolor='k')
#plt.title(args.metricx)
#plt.show()
#plt.hist(y_vec, bins=15, edgecolor='k')
#plt.title(args.metricy)
#plt.show()


