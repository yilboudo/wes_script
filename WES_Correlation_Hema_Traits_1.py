
#python WES_Correlation_Hema_Traits_1.py Table_All_Variants Table_All_Variants.clean 

#python WES_Correlation_Hema_Traits_1.py Table_All_Variants Table_All_Variants.clean 

import sys, os

#file1: input Snp Table Already made
#file2:  output Snp Table Already made uncollapsed
#file3: input file2

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


