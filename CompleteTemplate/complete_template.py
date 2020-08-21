##########################################################################
# This script take in input txt fusion template 
# and fill semi-automatically data
##########################################################################

# Library
import sys
import dicts # Import dictionary
import checks # Import check function
import fills # Importa fill function


# Function to write output file
def dwriter(wdict,lhead,fin):
	# Mgs Positive
	print("### Step 12: Write new file filling columns in cell line section! ###")
	# Input file
	fname=fin.replace("input","output")
	# Split name file for txt
	fname1=fname.split(".txt")
	# Output
	fout=open(fname1[0]+"_res.txt","a")
	string_fill="\t".join(wdict)
	fout.write(string_fill+"\n")
	#Chiudo il file
	fout.close()


# Function to start filling step
def fill(fin,li,lhead,cline,hcline,hgnc,hhgnc,dkin,uniprot,huniprot,tcga):
	# Cell line Section
	li=fills.filled(li,lhead,cline,hcline,hgnc,hhgnc,dkin,uniprot,huniprot,tcga)

	# Write Row
	dwriter(li,lhead,fin)


# Check Files fill by USER
def checkuser(lhead,llinea):
	# Section kinase
	checks.ckkinase(lhead,llinea)
	# Section partner
	checks.ckpartner(lhead,llinea)
	# Section fusion
	checks.ckfusion(lhead,llinea)
	# Section meta
	checks.ckmeta(lhead,llinea)


# Function to check that mandatory filed are present
def checkobb(fin):
	# Open reading file
	filein=open(fin,"r")
	# Reading all lines
	linein=filein.readlines()
	# Header
	header=0
	# Cycle lines
	for li in linein:
		# Header
		if header==0:
			# Split header for tab
			lhead=li.strip().split("\t")
			# Identify IDs for mandatory field
			id_cellline=lhead.index("Cell_line")	#Cell line
			id_gene5=lhead.index("Gene_5")	#Gene 5'
			id_gene3=lhead.index("Gene_3")	#Gene 3'
			id_kinase=lhead.index("Kinase")	#Kinase
			id_pmid=lhead.index("Reference_PMID")	#Reference PMID
			#Salto Header
			header=1
		else:
			# Split line for tab
			llinea=li.split("\t")
			# If some mandatory field is empty
			if(((((llinea[id_cellline]=="") or (llinea[id_gene5]=="")) or (llinea[id_gene3]=="")) or (llinea[id_kinase]=="")) or (llinea[id_pmid].strip()=="")):
				# Msg Error
				sys.exit(">>>[1] Mandatory fields are NOT complete, see: \n"+li)
	# Close file
	filein.close()
	# Msg positive
	print("### ===> ###: Mandatory filed are present in all entries! ###")


# Main
def main():
	######################################################################
	##############################	INPUT	##############################
	######################################################################
	# File input
	finput="input/test.txt"
	
	# Dict cell line (Yu)
	file_cell_line="table/cell_lines.txt"
	# Dict HGNC
	file_hgnc="table/hgnc.txt"
	# Dict kinase group
	groupkin="table/kinases.txt"
	# Dict Uniprot
	uniprot="table/uniprot_domain.bed"
	# Dict TCGA Data Fusion Portal
	file_tcga="table/tcga_fusion.txt"
	######################################################################

	# Msg positive
	print("### Step 1: Start step to fill template! ###")

	# Msg positive
	print("### Step 2: CHeck if mandatory fields are present in all entries! ###")
	checkobb(finput)

	######################################################################
	##############################	DICTs	##############################
	######################################################################
	#Msg positive
	print("### Step 3: Start steo to create dictionaries! ###")

	#Dict Yu cell line
	dict_cellline,h_celline=dicts.mkdict_cell(file_cell_line)
	
	#Dict HGNC
	dict_hgnc,h_hgnc=dicts.mkdict_hgnc(file_hgnc)
	
	#Dict Kinase Group
	kingroup=dicts.mkdict_kin(groupkin)
	
	#Dict Uniprot
	dict_uni,h_uni=dicts.mkdict_uni(uniprot)
	
	#Dict TCGA
	dict_tcga,h_tcga=dicts.mkdict_tcga(file_tcga)
	######################################################################

	######################################################################
	##############################	FILE	##############################
	######################################################################
	#Msg positive
	print("### Step 4: Start input file ananlysis! ###")
	#Open reading file
	filein=open(finput,"r")
	linein=filein.readlines()
	header=0
	entry=1
	for li in linein:
		#Header
		if header==0:
			#Split header fo tab
			lhead=li.strip().split("\t")
			#Jump Header
			header=1
		else:
			#Split line for tab
			llinea=li.split("\t")
			#Msg positive
			print("\n\n### Step 5:  Analisi Entry ["+str(entry)+"]: ###")
			print(llinea)
			#Msg positive
			print("### Step 6: Start check USER's fields! ###")
			checkuser(lhead,llinea)

			#Msg positive
			print("### Step 7: Start filling! ###")

			#Filling
			fill(finput,li,lhead,dict_cellline,h_celline,dict_hgnc,h_hgnc,kingroup,dict_uni,h_uni,dict_tcga)

			entry=entry+1
	######################################################################


# Main
main()
