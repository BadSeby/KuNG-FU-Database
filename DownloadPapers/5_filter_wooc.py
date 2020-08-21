# Script Python to remove pmid with occurrences word to procede key words
#
# 5_filter_wooc.py
# The dict_wooc.txt file is genreated using 4_stats_kws.txt generated by 4_stats_kws.py
# removing duplicated and number of entry.
#

# Library
from itertools import *
import re

# Function to check word in abstract
def exact_Match(phrase, word):
    b = r'(\s|^|$)'
    text=phrase.lower().replace(",","").replace(";","").replace(".","").replace("\'","").replace("\"","").replace("\'","").replace("\"","").replace("(","").replace(")","")
    res = re.search(b + word.lower() + b, text, flags=re.IGNORECASE)
    if(res==None):
    	res=False
    else:
    	res=True
    return bool(res)

# Main
def main():
	# File Input
	fin="3_entry_complete_kws.txt"
	# File Output
	ffusion="5_entry_complete_kws_clean.txt"
	# File Dictionary
	fdict="dict_wooc.txt"
	# Open File Dictionary
	dictopen=open(fdict,"r")
	# Dictionary Word Occurance
	search_words=dictopen.read().splitlines()
	# Read 12 lines
	nlines=12
	# Open Output File
	ffus=open(ffusion,"w")
	with open(fin,"r") as f:
		while True:
			var_test=False
			# Read 12 lines
			next_lines=list(islice(f,nlines))
			if not next_lines:
				break
			# For each word
			for sw in search_words:
				babstract=exact_Match(next_lines[2].strip(),sw)
				# Set variable support
				var_test=var_test or babstract
			if(not(var_test)):
				for start in range(0,len(next_lines),1):
					# Write Output File
					ffus.write(next_lines[start])
	# Close Output File
	ffus.close()

# Main
main()
