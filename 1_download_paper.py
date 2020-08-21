# Script Python to Download Papers from Pubmed
#
# 1_download_paper.py:
# This script download Paper Meta-Information from pubMed
#

# Library
from Bio import Entrez
from Bio import Medline
import time
import socket
from requests.exceptions import ConnectionError
# Try-Except
try:
    from urllib.error import HTTPError , URLError  # for Python 3
except ImportError:
    from urllib2 import HTTPError  # for Python 2


# Function to get pubmed id in text file
def get_lista_id(input_file):
	# Initialitinz empyt list
	lista=[]
	# Open reading file
	file_in=open(input_file,"r")
	# Reading all lines
	line_in=file_in.readlines()
	# Heaader
	header=0
	# Cycles all rows
	for li in line_in:
		if header==0: #Header
			header=1
		else:
			# Insert PubMedID in list
			lista.append(li.strip())
	# Close file
	file_in.close()
	# Return the list
	return(lista)

# Main
def main():
	# Read all PMIDs
	lista_id=get_lista_id("All_Papers.txt")
	# Email
	Entrez.email = "sebydibella@gmail.com"

	# Suffix file out
	k = "pmid_1"
	# File Output for papers not downloaded
	file_out_not = open("paper_NOT_download_"+k+"_to_log.txt","w")
	# Cont
	cont = 1
	# For each item in li
	for li in lista_id:
		# Attempt
		attempt = 1
		while attempt <= 3:
			try:
				# EFetch meta info
				handle = Entrez.efetch(db="pubmed", id=li, rettype="medline", retmode="txt")
				rec=Medline.read(handle)
				# Close Efetch
				handle.close()
				# variable support
				status=""
				# Check PMID exists
				if(not(rec.get("PMID") is None)):
					attempt1 = 1
					while attempt1 <= 3:
						try:
							# EFetch citation number
							handle1 = Entrez.esummary(db="pubmed",rettype="count",id=int(rec.get("PMID")))
							record1 = Entrez.read(handle1)
							handle1.close()

							attempt2 = 1
							while attempt2 <= 3:
								try:
									# EFetch Reference
									handle2 = Entrez.efetch(db="pubmed",rettype="medline",retmode="xml",id="\""+str(rec.get("PMID"))+"\"")
									record2 = Entrez.read(handle2)
									handle2.close()
									lsource=[] # List pmid reference
									# Recover Reference
									try:
										if("PubmedArticle" in record2.keys()):
											if("MedlineCitation" in record2["PubmedArticle"][0].keys()):
												if("CommentsCorrectionsList" in record2["PubmedArticle"][0]["MedlineCitation"].keys()): # If field not exists no references
													source=record2["PubmedArticle"][0]["MedlineCitation"]["CommentsCorrectionsList"]	# Recover sources
													for s in source:	# Recover sources and pmid
														if("PMID" in s.keys()):
															pmid_s=s["PMID"]
															lsource.append(str(pmid_s))	# PMID insert in list
														else:
															lsource.append("")
												else:	# Default value for no references
													lsource="empty"
											else:
													lsource="empty"
										else:
											lsource="empty"
									except IndexError:
										lsource="empty"

									# File output Paper Pubmed Downloaded
									status="success"
									file_out=open("paper_download_"+k+"_to_keep.txt","a")
									file_out.write("PMID: "+str(rec.get("PMID","?"))+"\n")
									file_out.write("Title: "+str(rec.get("TI","?"))+"\n")
									file_out.write("Abstract: "+str(rec.get("AB","?"))+"\n")
									file_out.write("Mesh: "+str(rec.get("MH","?"))+"\n")
									file_out.write("Authors: "+str(rec.get("AU","?"))+"\n")
									file_out.write("Source: "+str(rec.get("SO","?"))+"\n")
									file_out.write("Date of pubblication: "+str(rec.get("DP","?"))+"\n")
									file_out.write("Doi: "+str(rec.get("AID","?"))+"\n")
									file_out.write("Journal: "+str(rec.get("JT","?"))+"\n")
									file_out.write("No Citation: "+str(record1[0]["PmcRefCount"])+"\n")
									file_out.write("PMID Reference: "+str(lsource)+"\n\n")
									file_out.close()
								except HTTPError as err:
									if(err.code==101) or (err.code==110):
										attempt2 += 1
										time.sleep(10)
										print("Try2:"+str(li)+"\n")
								except URLError as err:
									attempt2 += 1
									time.sleep(10)
									print("URL Error: "+str(err)+" Try2:"+str(li)+"\n")
								except ConnectionResetError as err:
									attempt2 += 1
									time.sleep(10)
									print("ConnectionReset Error: "+str(err)+" Try2:"+str(li)+"\n")
								except socket.timeout:
									attempt2 += 1
									time.sleep(10)
									print("TimeOut Try2:"+str(li)+"\n")
								else:
									attempt2=4
						except HTTPError as err:
							if(err.code==101) or (err.code==110) or (err.code==10060):
								attempt1 += 1
								time.sleep(10)
								print("Try1:"+str(li)+"\n")
						except URLError as err:
							attempt1 += 1
							time.sleep(10)
							print("URL Error: "+str(err)+" Try1:"+str(li)+"\n")
						except ConnectionResetError as err:
							attempt1 += 1
							time.sleep(10)
							print("ConnectionReset Error: "+str(err)+" Try1:"+str(li)+"\n")
						except socket.timeout:
							attempt1 += 1
							time.sleep(10)
							print("TimeOut Try1:"+str(li)+"\n")
						else:
							attempt1=4
				else:
					file_out_not.write("PMID: "+str(li)+"\n")
					status="failed"
				# File Log
				file_out_log=open("log_cell_line_"+k+".txt","a")
				file_out_log.write("Download paper: "+str(cont)+" con pubmed id:"+str(li)+" STATUS: "+status+"\n")
				file_out_log.close()
				cont=cont+1

			except HTTPError as err:
				if(500 <= err.code <= 599) or (err.code==101) or (err.code==110) or (err.code==-3) or (err.code==10060):
					attempt += 1
					time.sleep(10)
					print("Try:"+str(li)+"\n")
			except URLError as err:
				attempt += 1
				time.sleep(10)
				print("URL Error: "+str(err)+" Try:"+str(li)+"\n")
			except ConnectionResetError as err:
				attempt += 1
				time.sleep(10)
				print("ConnectionReset Error: "+str(err)+" Try:"+str(li)+"\n")
			except socket.timeout:
				attempt += 1
				time.sleep(10)
				print("TimeOut Try:"+str(li)+"\n")
			else:
				attempt=4

	# Close file
	file_out_not.close()

# Main
main()
