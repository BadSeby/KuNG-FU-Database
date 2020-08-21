# Script Python to Search in Pubmed
#
# 0b_donwload_id.py
# This file search and write 
# PubMed ID of papers of query
#

#Library
from Bio import Entrez
from Bio import Medline
import time
#Try-Except
try:
    from urllib.error import HTTPError  # for Python 3
except ImportError:
    from urllib2 import HTTPError  # for Python 2

#Email Insert your email
Entrez.email="sebydibella@gmail.com"
#String to search
query="((cell line) AND English[Language])"

#Inizitialize List
lista_id=[]
#Cont
starting=0
# Use cicle to obtain results,
# limit 100.000 entry any time
# the value 1100273 is returned by 0a_download_id_date.py
#Get all results
for start in range(0,1100273,100000):
	#Select db to interrogate
	handle = Entrez.esearch(db="pubmed",term=query,usehistory="y",retstart=starting,retmax=100000)
	#All records
	record = Entrez.read(handle)
	#Count results
	count = int(record["Count"])
	#PMID for each entry
	ids = record["IdList"]
	#Count+100000
	starting=starting+100000
	#Insert PMID in list
	lista_id.append(ids)

#Unflutten list
flattened_list = [y for x in lista_id for y in x]
print("Records found in Pubmed:"+str(count)+"\n")
#Output file with PMID
file_out=open("All_Papers.txt","w")
file_out.write("Records found in Pubmed:"+str(count)+"\n")
#Each MID
for start in range(0,1061638,1):
	#Write Output file
	file_out.write(str(flattened_list[start])+"\n")

#Close Output file
file_out.close()
