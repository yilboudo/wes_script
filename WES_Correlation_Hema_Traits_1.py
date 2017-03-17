
#python WES_Correlation_Hema_Traits_1.py Table_All_Variants Table_All_Variants.clean 

#python WES_Correlation_Hema_Traits_1.py Table_All_Variants Table_All_Variants.clean 



import sys, os

#file1: input Snp Table Already made
#file2:  output Snp Table Already made uncollapsed
#file3: input file2
#file4: input Hematolofical Traits Infos
#file5: output variants with Hematological Traits Merged
#Option6 : Input Hematological Trait Name
#file7: input Variants and Hematological Trait Name Merged
#File8: FINAL Output for Drawing

#Change final snps carriers file to have the list of all of them
input = open(sys.argv[1],'r')
output = open(sys.argv[2],'w')
header = next(input)
output.write(header)

last_column = (header.strip('\n').split('\t')).index('INDIVIDUAL_GENOTYPES') 
after_last_column = last_column + 1 

for line in input:
    col = line.strip('\n').split('\t')
    if len(col[0::]) > after_last_column:
    	output.write('\t'.join((col[0:after_last_column]))+'\n')
        for i in range(len(col[after_last_column::])):
             output.write('\t'.join((col[0:last_column]+[col[after_last_column+i]]))+'\n')
    else:
        output.write('\t'.join((col[0::])) + '\n')


output.close()

#Merge columns individuals with Hemato_traits
input_file = open(sys.argv[3],'r')

header_input_file = next(input_file);

import re

master_table = []

#Read in genotypes files
for line in input_file:
    line_new=re.sub(r':[A-Z]/[A-Z]','', line)
    col = line_new.strip('\n\r').split('\t')
    master_table.append(col[0::])


d = {}

#Read hematological data
f1 = open(sys.argv[4],'rU')
f2 = open(sys.argv[5],'w')

#Choose hematological trait
header_f1 = next(f1)
hematological_trait_name = sys.argv[6]


values_to_fill_in = (header_f1.strip('\n').split(',')).index(hematological_trait_name) 



f2.write(header_input_file.replace('INDIVIDUAL_GENOTYPES',hematological_trait_name))


#create dictionary
for line in f1:
    col = line.strip('\r\n').split(',')
    d[(col[0])] = (col[values_to_fill_in])


fresh_table = []
#Create a table for replacing values in dictionary    
for row in master_table:
    row = [str(x) for x in row]
    fresh_table.append('\t'.join(row) + '\n')



for line in fresh_table:
	col = line.strip('\n').split('\t')
	if col[-1] in d:
		vals = d[(col[-1])]
		f2.write('\t'.join((col[0:6] +[vals])) + '\n')
	else:
		f2.write('\t'.join((col[0:6] + ['NA'] ))+ '\n')

f2.close()






