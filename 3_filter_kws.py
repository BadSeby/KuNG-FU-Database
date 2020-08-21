# Script Python to filter entry pubmed with key words
#
# 3_filter_kws.py
# Questo file filtra le entry pubmed senza parole chiave in Title o Abstract
#

# Library
from itertools import *
import re

# Function to find keyword
def exact_Match(phrase, word):
    b = r'(\s|^|$)' 
    res = re.search(b + word + b, phrase, flags=re.IGNORECASE)
    return bool(res)

# Main
def main():
	# File input
	fin="2_entry_complete.txt"
	
	# File output
	ffusion="3_entry_complete_kws.txt"
	# Number lines of block entry pubmed
	nlines=12
	# Key Words
	search_words=["fusion","inversion","translocation","rearrangement","fusions","inversions","translocations","rearrangements"]
	# Open File Output
	ffus=open(ffusion,"w")
	# Read file input
	with open(fin,"r") as f:
		while True:
			# Variable support
			var_test=False
			# Read 12 lines
			next_lines=list(islice(f,nlines))
			if not next_lines:
				break
			# For each key-word
			for sw in search_words:
				# Check kwy word in title
				btitle=exact_Match(next_lines[1].strip(),sw)
				# Check kwy word in abstract
				babstract=exact_Match(next_lines[2].strip(),sw)
				# If key word is found the variable support is set to TRUE
				if(btitle or babstract):
					var_test=True
			if(var_test):
				for start in range(0,len(next_lines),1):
					# Write in file output
					ffus.write(next_lines[start])
	# Close file output
	ffus.close()

# Main
main()
