# Script Python to Search in Pubmed
#
# 0a_donwlonad_date.py
# This file return the number of papers for your query
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

#Email
Entrez.email="sebydibella@gmail.com"
#String to search
query="((cell line) AND English[Language])"

#Initialize list
lista_id=[]
#Cont
starting=0

#Handle query
handle = Entrez.esearch(db="pubmed",term=query,usehistory="y",retstart=starting)
#Insert in record
record = Entrez.read(handle)
#Count Result
count = int(record["Count"])
#Print count of query result
print("Records found in Pubmed:"+str(count)+"\n")
