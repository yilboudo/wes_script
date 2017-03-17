#python WES_Correlation_Hema_Traits_2.py Master_Genmod_WES_Zselect_traits.csv Table_All_Variants.clean Table_All_Variants.clean.mcv "MCV"

import sys, os,re

d = {}

#Read hematological data
f1 = open(sys.argv[1],'rU')
f2 = open(sys.argv[2],'r')
f3 = open(sys.argv[3],'w')

#Choose hematological trait
header_f1 = next(f1)
header_f2 = next(f2)

hematological_trait_name = sys.argv[4]


values_to_fill_in = (header_f1.strip('\n').split(',')).index(hematological_trait_name) 



f3.write(header_f2.replace('INDIVIDUAL_GENOTYPES',hematological_trait_name))


#create dictionary
for line in f1:
    col = line.strip('\r\n').split(',')
    d[(col[0])] = (col[values_to_fill_in])


#fresh_table = []
#Create a table for replacing values in dictionary    
#for row in master_table:
#    row = [str(x) for x in row]
#    fresh_table.append('\t'.join(row) + '\n')



for line in f2:
	line_new=re.sub(r':[A-Z]/[A-Z]','', line)
	col = line_new.strip('\n').split('\t')
	if col[-1] in d:
		vals = d[(col[-1])]
		f3.write('\t'.join((col[0:5] +[vals])) + '\n')
	else:
		f3.write('\t'.join((col[0:5] + ['NA'] ))+ '\n')

f3.close()
