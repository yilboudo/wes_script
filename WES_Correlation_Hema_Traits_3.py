#python WES_Correlation_Hema_Traits_3.py Table_All_Variants.clean.mcv.collapsed MCV_Variants_Results.txt "MCV"

import sys, os

from math import *


f3  = open(sys.argv[1],'r')
f4 = open(sys.argv[2],'w')

trait_name = sys.argv[3]


header='SNP\tNumb_Carriers\t'+ trait_name +'_Avg_zScore\n'



f4.write(header)



for line in f3:
	if line.startswith('SNP'):
		pass
	else:
	    col = line.strip('\r\n').split('\t')
	    col_replace_na = [x for x in col[0::] if x != 'NA']
	    if len(col_replace_na[0::]) > 1:
	    	col_float_convert =[col_replace_na[0]] + [float(x) for x in col_replace_na[1::]]
	    	col_final_float = [col_float_convert[0]] + [len(col[1::])] + [sum(col_float_convert[1::])/len(col_float_convert[1::])]
	    	col_final_string = [str(x) for x in col_final_float]
	    	f4.write('\t'.join((col_final_string[0::]))+'\n')
	    else:
	    	col_na_remain = [col_replace_na[0]] + [str(len(col_replace_na[0::]))] + ['NA']
	    	f4.write('\t'.join((col_na_remain[0::] ))+'\n')
	    


f4.close()


#option to replace NA by 0
#col_replace_na = ['0' if x == "NA" else x for x in col[0::]]