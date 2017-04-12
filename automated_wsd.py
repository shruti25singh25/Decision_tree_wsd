# author: Shruti Singh, Banasthali University

import os
import re

pathOfSM = raw_input('Enter the path of the directory containing tab and rs file : ')
re_file = raw_input("Enter the name of rs file: ")
eng_file = raw_input("Enter the name of the english sentence file : ")
hin_file = raw_input("Enter the name of hindi translation file : ")
tab_file = raw_input("Enter the name of the tab file: ")

path_re_file = pathOfSM+re_file
path_eng_file = pathOfSM+eng_file
path_hin_file = pathOfSM+hin_file
          
f1 = open(re_file,'r')
f2 = open(eng_file,'r')
lines2 = f2.readlines()
f3 = open(hin_file,'r')
lines3 = f3.readlines()
word = raw_input("Enter the require word: ")
f = open('clips.out','a')
f5 = open(tab_file,'r')
lines5 = f5.readlines()[1:]

extractMR = []

for line in f1:
	if 'Meaning' and '<-' in line:
        	extractMR.append(re.split(r'[=,&<]+',line))
    
for i in extractMR:
	temp = []
        i[2] = i[2][1:]
        temp = i[-1].split()
        i[-1] = temp[0]
               
for i in extractMR:
        i.pop(0)

engsentence = []
for line2 in lines2:
	line2 = line2.strip()
	engsentence.append(line2)

hinsentence = []
for line3 in lines3:
	line3 = line3.strip()
	hinsentence.append(line3)

triples = []
for line5 in lines5:
	line5 = line5.split()
	triples.append(line5[1])

#f.write(triples)
    
count = 0
for i in extractMR: 
	f.write('\n\n; Name/Unique Id of WSD rule maker to be added here.')
	f.write('\n')
	count1 = -1
	for j in triples:
		count1 = count1 + 1
		if i[2] == j:
#			f.write('@@@')
			f.write(engsentence[count1])
			f.write('\n')
			f.write(hinsentence[count1])
			f.write('\n')
          
	f.write('\n(defrule '+word+str(count))
        f.write('\n(declare (salience 0))')
        f.write('\n(id-root ?id '+word+')')
        f.write('\n?mng <-(meaning_to_be_decided ?id)')
	f.write('\n (' +i[2]+  ' ?id ?id1 )')
#        print('\n(id-cat_coarse ?id '+pos+')')
        f.write('\n=>')
        f.write('\n(retract ?mng)')
        f.write('\n(assert (id-wsd_root_mng ?id '+i[0]+')')
        f.write('\n(if ?*debug_flag* then')
        f.write('\n(printout wsd_fp "(dir_name-file_name-rule_name-id-wsd_root_mng  " ?*prov_dir* "  '+word+'.clp   '+word+str(count)+'   "  ?id "  '+i[0]+')" crlf))')
        f.write('\n)')
	f.write('\n')
	f.write('\n')
	 
        count = count + 1    

