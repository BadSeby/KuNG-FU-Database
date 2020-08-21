# Script Python to separate entry pubmed complete from incomplete entry (title and/or abstract)
#
# 2_divide.py
# This file separate entry complete o incomplete in Title and/or Abstract
#

# Library
from itertools import *

# Main
def main():
	# Input file
	fin = "paper_download_pmid_to_keep.txt"

	# Output File complete
	fcomplete="2_entry_complete.txt"
	# Output file incomplete
	fpartial="2_entry_partial.txt"
	# Number lines of block entry pubmed
	nlines=12
	# Open file output complete
	fcomp=open(fcomplete,"w")
	# Open file output incomplete
	fpart=open(fpartial,"w")
	# Read file input
	with open(fin,"r") as f:
		while True:
			# Read 12 lines
			next_lines=list(islice(f,nlines))
			if not next_lines:
				break
			# If Title and/or Abstract are ? (empty)
			if(next_lines[1].strip()=="Title: ?" or next_lines[2].strip()=="Abstract: ?"):
				# Write in incomplete output file
				for start in range(0,len(next_lines),1):
					fpart.write(next_lines[start])
			else:
				# Write in complete output file
				for start in range(0,len(next_lines),1):
					fcomp.write(next_lines[start])

	# Close output file complete and incomplete
	fcomp.close()
	fpart.close()

# Main
main()
