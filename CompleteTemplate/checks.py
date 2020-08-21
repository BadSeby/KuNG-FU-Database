######################################################################################
######################################################################################
######################################################################################
####### Function to check fields
######################################################################################
######################################################################################
######################################################################################

#Library
import sys

# Function to check gene name in HGNC
def checkgene(gene,hgnc,hhgnc,li):
	dentry={}
	cont=0
	id_hgnc=hhgnc.index("HGNC ID")
	id_approved=hhgnc.index("Approved Symbol")
	id_prev_symb=hhgnc.index("Previous Symbols")
	id_synonyms=hhgnc.index("Synonyms")
	for k in hgnc.keys():
		lhgnc=hgnc[k][id_approved].split(", ")+hgnc[k][id_prev_symb].split(", ")+hgnc[k][id_synonyms].split(", ")
		if gene in lhgnc:
			dentry[cont]=hgnc[k]
			cont=cont+1
	if cont==0:
		sys.exit(">>>[6] Gene is not in our dictionary, check gene ==> "+gene)
	if cont>1:
		print("### ===> ### ===> 7.6.1: More matches are found in our dictionary >>> "+gene.upper()+" <<< ")
		for e in dentry.keys():
			print("\n["+str(e)+"]=> "+str(dentry[e]))
		idx = int(input("### ===> ### 7.7: Insert ID gene: "))
		retitem=dentry[idx][0]
	if cont==1:
		print("### ===> ### 7.7: Gene is found unique ###")
		retitem=dentry[0][0]
	return(retitem)


# Function to check if line is in pur dictionary
def checkline(cellline,cline,li):
	dentry={}
	cont=0
	for k in cline.keys():
		lkey=k.strip().split("_")
		if cellline in lkey:
			dentry[cont]=k
			cont=cont+1
	if cont==0:
		sys.exit(">>>[5] Line is not in pur dictionary, complete the file with data for line ==> "+cellline)
	if cont>1:
		print("### ===> ### ===> 7.1.1: More matches are found in our dictionary >>> "+cellline.upper()+" <<<")
		for e in dentry.keys():
			print("["+str(e)+"]=> "+str(cline[dentry[e]]))
		idx = int(input("### ===> ### 7.2: Insert ID for line: "))
		retitem=dentry[idx]
	if cont==1:
		print("### ===> ### 7.2: The line is found unique ###")
		retitem=dentry[0]
	return(retitem)


######################################################################################
######################################################################################
######################################################################################
####### Function to check USER fields
######################################################################################
######################################################################################
######################################################################################

#Check USER fields are filled Kinase section
def ckkinase(lhead,llinea):
	id_nmkinasepaper=lhead.index("NM_of_kinase_(paper)") #NM kinase (paper)
	id_nmkinasekim=lhead.index("NM_of_kinase_(KIM)")	#NM kinase (KIM)
	id_nmkinasetrex=lhead.index("NM_of_kinase_(TReX)") #NM kinase (TReX)
	id_kinasedomain=lhead.index("Kinase_domain")	#Kinase domain

	str_miss=""
	cont=0
	if(llinea[id_nmkinasepaper]==""):
		cont=cont+1
		str_miss=str_miss+" *** NM_of_kinase_(paper)"
	if(llinea[id_nmkinasekim]==""):
		cont=cont+1
		str_miss=str_miss+" *** NM_of_kinase_(KIM)"
	if(llinea[id_nmkinasetrex]==""):
		cont=cont+1
		str_miss=str_miss+" *** NM_of_kinase_(TReX)"
	if(llinea[id_kinasedomain]==""):
		cont=cont+1
		str_miss=str_miss+" *** Kinase_domain"
	print("### ===> ### 6.1: Field USER in Kinase section not defined are  "+str(cont)+"/4, see: >>> "+str(str_miss)+" <<< ")


#Check USER field in section PARTNER
def ckpartner(lhead,llinea):
	id_nmpartnerpaper=lhead.index("NM_of_partner_(paper)") #NM partner (paper)
	str_miss=""
	cont=0
	if(llinea[id_nmpartnerpaper]==""):
		cont=cont+1
		str_miss=str_miss+" *** NM_of_partner_(paper)"
	print("### ===> ### 6.2: Field USER in Partner section not defined are "+str(cont)+"/1, see: >>> "+str(str_miss)+" <<< ")


# Check USER field in Fusion section
def ckfusion(lhead,llinea):
	id_exon5=lhead.index("Exon_5") #Exon5
	id_exon3=lhead.index("Exon_3") #Exon3
	id_fustype=lhead.index("Fusion_Type") #Fusion Type
	id_knownfus=lhead.index("Known_Fusion") #Known Fusion
	str_miss=""
	cont=0
	if(llinea[id_exon5]==""):
		cont=cont+1
		str_miss=str_miss+" *** Exon5"
		sys.exit(">>>[4] Exon 5' missed, I can not found sequence, breakpoint and fusion protein")
	if(llinea[id_exon3]==""):
		cont=cont+1
		str_miss=str_miss+" *** Exon3"
		sys.exit(">>>[4] Exon 3' missed, I can not found sequence, breakpoint and fusion protein")
	if(llinea[id_fustype]==""):
		cont=cont+1
		str_miss=str_miss+" *** FusionType"
	if(llinea[id_knownfus]==""):
		cont=cont+1
		str_miss=str_miss+" *** KnownFusion"
	#Messaggio campi user
	print("### ===> ### 6.3: Field USER in Fusion section not defined are "+str(cont)+"/4, see: >>> "+str(str_miss)+" <<< ")


# CHeck USER Fiels in Meta Section
def ckmeta(lhead,llinea):
	id_tech=lhead.index("Technology") #Technology
	str_miss=""
	cont=0
	if(llinea[id_tech]==""):
		cont=cont+1
		str_miss=str_miss+" *** Technology"
	print("### ===> ### 6.4: Field USER in Meta section not defined are  "+str(cont)+"/1, see: >>> "+str(str_miss)+" <<< ")
