# Script Python to calculate occurrences word to procede key words
#
# 4_stats_kws.py
# Questo file calcola le occorrenze delle parole che precedono le key words
#

# Library
from itertools import *
import re

# Main
def main():
	# File Input
	fin="3_entry_complete_kws.txt"
	# File Output
	ffusion="4_stats_kws.txt"
	# Number lines of block entry pubmed
	nlines=12
	# Open file Output
	ffus=open(ffusion,"w")
	# Key Words
	search_words=["fusion","inversion","translocation","rearrangement","fusions","inversions","translocations","rearrangements"]
	# Dictionary Key word
	dwords={'fusion':{},'inversion':{},'translocation':{},'rearrangement':{}}
	# Open file Input
	with open(fin,"r") as f:
		while True:
			var_test=False
			# Read 12 lines
			next_lines=list(islice(f,nlines))
			if not next_lines:
				break
			# Split the abstract " "
			arr_phrase=next_lines[2].strip().split(" ")
			# Recover PMID
			pmid=next_lines[0].strip().split(": ")
			# For each key words
			for word in search_words:
				# Calculate all indexs for key words
				arr_indexs=[index for index, value in enumerate(arr_phrase) if value == word]
				# For each indexs
				for idxs in arr_indexs:
					# print(dwords)
					# Recover word that procede key words
					pre_word=arr_phrase[idxs-1].strip()
					# Select dictionary to insert word
					if(word=="fusion" or word=="fusions"):
						if pre_word.lower().replace(",","").replace("\'","").replace("\"","") in dwords["fusion"].keys():
							dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"])+int(1)
							dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
						else:
							dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]={}
							dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(1)
							dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"]=[]
							dwords["fusion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
					if(word=="inversion" or word=="inversions"):
						if pre_word.lower().replace(",","").replace("\'","").replace("\"","") in dwords["inversion"].keys():
							dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"])+int(1)
							dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
						else:
							dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]={}
							dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(1)
							dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"]=[]
							dwords["inversion"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
					if(word=="translocation" or word=="translocations"):
						if pre_word.lower().replace(",","").replace("\'","").replace("\"","") in dwords["translocation"].keys():
							dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"])+int(1)
							dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
						else:
							dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]={}
							dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(1)
							dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"]=[]
							dwords["translocation"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
					if(word=="rearrangement" or word=="rearrangements"):
						if pre_word.lower().replace(",","").replace("\'","").replace("\"","") in dwords["rearrangement"].keys():
							dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"])+int(1)
							dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))
						else:
							dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]={}
							dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["cont"]=int(1)
							dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"]=[]
							dwords["rearrangement"][pre_word.lower().replace(",","").replace("\'","").replace("\"","")]["Pubmed"].append(str(pmid[1]))

	# For each key in dictionary
	for k in dwords.keys():
		for kk in dwords[k].keys():
			# Write Output file
			ffus.write(k+"\t"+kk+"\t"+str(dwords[k][kk]["cont"])+"\t"+str(dwords[k][kk]["Pubmed"])+"\n")
	# Close file output
	ffus.close()

# Main
main()
