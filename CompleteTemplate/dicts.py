# Library
import sys

# Function to create TCGA DIct
def mkdict_tcga(tcga):
	filein=open(tcga,"r")
	linein=filein.readlines()
	header=0
	dictn={}
	
	cont=0
	for li in linein:
		if header==0:
			lheader=li.split("\t")
			header=1
		else:
			
			llinea=li.split("\t")
			
			dictn[cont]=[]
			dictn[cont].extend((str(llinea[1].strip()),str(llinea[2].strip()),str(llinea[3].strip())))
		
		cont=cont+1
	
	print("### ===> ### 3.5: TCGA dict is created! ###")
	#Return dict
	return(dictn,lheader)


# FUnction to create Uniprot dict
def mkdict_uni(uniprot):
	dict_uni={}
	filein=open(uniprot,"r")
	linein=filein.readlines()
	header=0
	cont=0
	for li in linein:
		if header==0:
			lhead=li.strip().split("\t")
			header=1
		else:
			llinea=li.strip().split("\t")
			dict_uni[cont]=[]
			dict_uni[cont].extend((llinea))
			cont=cont+1
	filein.close()
	print("### ===> ### 3.4: Uniprot dict is created! ###")
	return(dict_uni,lhead)


# Function to create Kinase Grooup Dictionary
def mkdict_kin(fin):
	dictk={}
	filein=open(fin,"r")
	linein=filein.readlines()
	header=0
	for li in linein:
		if header==0:
			header=1
		else:
			llinea=li.strip().split("\t")
			dictk[llinea[1]]=llinea[2]
	filein.close()
	print("### ===> ### 3.3: Kinase Group dict is created! ###")
	return(dictk)


# Function to create HGNC dict
def mkdict_hgnc(hgnc):
	filein=open(hgnc,"r")
	linein=filein.readlines()
	header=0
	dictn={}
	for li in linein:
		if header==0:	#Salto header
			header=1
			lheader=li.split("\t")
		else:
			llinea=li.split("\t")
			chiave=llinea[0].strip()
			if chiave in dictn.keys():
				sys.exit(">>>[3] key is already present in hgnc dict, check ==> "+chiave)
			else:	#Chiave assente
				dictn[chiave]=[]
				dictn[chiave].extend(llinea[0:])
	filein.close()
	print("### ===> ### 3.2: HGNC dict is created! ###")
	return(dictn,lheader)


# Functino to create Yu cell line dict
def mkdict_cell(cline):
	filein=open(cline,"r")
	linein=filein.readlines()
	header=0
	dictn={}
	for li in linein:
		if header==0:	#Salto header
			header=1
			lheader=li.split("\t")
		else:
			llinea=li.split("\t")
			if not(llinea[14].strip()=="--"):
				arr_syn=llinea[14].strip().replace("\"","").split(", ")
				string_syn="_".join(arr_syn)
				chiave=llinea[0].strip()+"_"+llinea[1].strip()+"_"+llinea[2].strip()+"_"+string_syn
			else:
				chiave=llinea[0].strip()+"_"+llinea[1].strip()+"_"+llinea[2].strip()
			if chiave in dictn.keys(): #Chiave presente
				print(">>>[2] key is already present in cell line dict, check ==> "+chiave)
				sys.exit()
			else:	#Chiave assente
				dictn[chiave]=[]
				dictn[chiave].extend(llinea[0:])
	filein.close()
	print("### ===> ### 3.1: Cell Line dict is created! ###")
	return(dictn,lheader)
