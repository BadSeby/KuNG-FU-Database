#Library
import sys
import checks
from Bio import Entrez
from Bio import SeqIO
from Bio.SeqFeature import FeatureLocation


# Function to check if exist TCGA samples
def checktcga(fusione,tcga):
	fus=fusione.strip().split("-")
	gene_a=fus[0]
	gene_b=fus[1]
	lfus=[]
	for k in tcga:
		if tcga[k][1]==gene_a and tcga[k][2]==gene_b:
			lfus.append(tcga[k][0])
	return(lfus)


# Function to get greakpoint
def getbreakpoint(brk3,brk5,kin):
	if kin==3:
		if brk3!=0:
			return(brk3)
		else:
			return(brk5)
	else:
		return(brk5)


# FUnction to get NM Sequence
def getsequence(nm,exon,term):
	Entrez.email= "sebydibella@gmail.com"
	genomeAccessions = [str(nm)]
	handle = Entrez.efetch(db="nucleotide", id=genomeAccessions, rettype="gb")	#Parsing del Record
	records = SeqIO.parse(handle, "gb")
	str_exon=""
	cont_term=0
	breakpoint=0
	breakpoint1=0
	cds=0
	for i,record in enumerate(records):
		cont=1
		for feature in record.features:
			if feature.type== "exon":
				loc=feature.location
				if(cont==int(exon)):
					str_exon=feature.location.extract(record).seq
					if term=="5":
						exr=int(loc.end)+1
					if term=="3":
						breakpoint=int(loc.start)+1
				cont=cont+1
			if feature.type== "CDS":
				loc_cds=feature.location
				if term=="5":
					cds=int(loc_cds.start)+1
				if term=="3":
					cds=float(((loc_cds.end-loc_cds.start)-1)/3)
		if term=="5":
			cont_term=float((((exr+1)-(cds+1))-1)/3)
			breakpoint1=cont_term
		if term=="3":
			breakpoint1=float((breakpoint-(loc_cds.start+1))/3)
			cont_term=cds-breakpoint1
	return(str_exon,cont_term,breakpoint1)


# Function to choose NM
def getnm(nm1,nm2,nm3,li):
	retitem=""
	if((str(nm1)=="") and (str(nm2)=="") and (str(nm3)=="")):
		print(">>>[4] NMs are all blank, it is impossibile complete the sequences")
		sys.exit()
	else:
		if(str(nm1)!=""):
			retitem=nm1
		else:
			if(str(nm2)!=""):
				retitem=nm2
			else:
				retitem=nm3
	return(retitem)


#Function to get chromosome gene
def gchr(gid,hgnc,hhgnc):
	id_field=hhgnc.index("Chromosome")
	return(hgnc[gid][id_field])


# Function to get uniprot kinase domain
def getuniprot(uniprot,huniprot,iduni):
	id_uniprot=huniprot.index("Uniprot_ID")
	id_desc_anno=huniprot.index("Desc_Anno")
	retitem=""
	domain_entry={}
	ldomain=[]
	list_domain=["Protein kinase","Protein kinase 1","Protein kinase 2","PI3K/PI4K","Bromo","Bromo 1","Bromo 2","Histidine kinase"]
	cont=0
	for uni in uniprot.keys():
		if(str(uniprot[uni][id_uniprot])==str(iduni)):
			info=uniprot[uni][id_desc_anno].strip().split("; ")
			if(info[1] in list_domain):
				domain_entry[cont]=info[0]+"_"+info[1]
				ldomain.append(info[0])
				ldomain.append(info[1])
				cont=cont+1
			else:
				retitem=""
		else:
			retitem=""
	if cont>1:
		print("### ===> ### ===> 8.5.1: More entry are found for kinase domain >>> "+iduni+" <<< ")
		if("Protein kinase 1" in ldomain):
			if("Protein kinase 2" in ldomain):
					retitem1=ldomain[0].split("_")
					retitem2=ldomain[1].split("_")
					retitem=ldomain[0]+"_"+ldomain[2]
					return(retitem)
		else:
			if("Bromo 1" in ldomain):
				if("Bromo 2" in ldomain):
						retitem1=ldomain[0].split("_")
						retitem2=ldomain[1].split("_")
						retitem=ldomain[0]+"_"+ldomain[2]
						return(retitem)
			else:
				for e in domain_entry.keys():
					print("\n["+str(e)+"]=> "+str(domain_entry[e]))
				idx = int(input("### ===> ### 8.5.2: Insert domain of riferiment: "))
				retitem=domain_entry[idx].split("_")
				retitem=retitem[0]
				return(retitem)
	if cont==1:
		print("### ===> ### 8.5.3: Domain found is unique ###")
		#retitem=info[0]
		retitem=domain_entry[0].split("_")
		retitem=retitem[0]
		return(retitem)
	if retitem=="":
		print(">>>[6] Uniprot ID is not found in Uniprot or kinase domain is not indicated for "+iduni+" <<< ")
		sys.exit()


# Function to chhose betwee two fields nm
def chooser_nm(in1,in2,field,li):
	cont=0
	retitem=""
	if(in1=="" and in2==""):
		print(">>>[8] Both fields for \""+field+"\" are blank! <<<")
	else:
		if(in1=="" or in2==""):
			if(in1==""):
				retitem=in2
			else:
				retitem=in1
		else:
			if ", " in in1:
				in3=in1.split(", ")
				if in2 in in3:
					in3.remove(in2)
					hinput={0:in3[0],1:in2}
				else:#Nel caso in cui in2 non sia in3
					in1=in3[0]
					in1a=in3[1]
					hinput={0:in1,1:in2,2:in1a}
			else:
				hinput={0:in1,1:in2}
			if(in1!=in2):
				print("###===> Step 8.5: Select what \""+field+"\" choose! <<< ")
				for h in hinput.keys():
					print("["+str(h)+"]=> "+str(hinput[h]))
				cont=h+1
				print("["+str(cont)+"]=> Insert your NM")
				idx = str(input("###===> Step 8.6: Insert chosed ID for \""+field+"\": "))
				if(str(idx).startswith("NM_")):
					retitem=str(idx)
				else:
					retitem=hinput[int(idx)]
			else:	#Se sono uguali
				retitem=in1
	return(retitem)


# Function to chhose betwee two fields 
def chooser(in1,in2,field,li):
	retitem=""
	if(in1=="" and in2==""):
		print(">>>[8] Both fields for \""+field+"\" are blank! <<<")
	else:
		if(in1=="" or in2==""):
			if(in1==""):
				retitem=in2
			else:
				retitem=in1
		else:
			hinput={0:in1,1:in2}
			if(in1!=in2):
				print("###===> Step 6: Select what \""+field+"\" choose! <<< ")
				for h in hinput.keys():
					print("["+str(h)+"]=> "+str(hinput[h]))
				idx = int(input("###===> Step 6A: Insert ID choose for \""+field+"\": "))
				retitem=hinput[idx]
			else:	#Se sono uguali
				retitem=in1
	return(retitem)


#GET info HGNC
def gethgnc(hgnc,hhgnc,gid,field):
	id_field=hhgnc.index(field)
	return(hgnc[gid][id_field])


# GET ingo Kinase
def getgroup(kinase,dkin):
	gkin=dkin[kinase]
	if(gkin==""):
		print(">>>[7] Kinase is missed, try using HGNC kinase name in column \"Kinase\" or re-check ==> "+str(kinase))
		sys.exit()
	return(gkin)


# Function to get Approved Name
def getgene(hgnc,hhgnc,ckgene,field):
	idxfield=hhgnc.index(field)
	return(hgnc[ckgene][idxfield])


# Function to get Meta Info Cell Line
def getcline(cline,hcline,cklinea,field):
	idxfield=hcline.index(field)
	return(cline[cklinea][idxfield])


# Function to fill missed field in cell line section
def filled(li,lhead,cline,hcline,hgnc,hhgnc,dkin,uniprot,huniprot,tcga):
	print("### ===> Step 7: Start filling Entry in  section Cell Line! ###")
	wdict=[]
	llinea=li.strip().split("\t")

	######################################################################
	id_cellline=lhead.index("Cell_line")	#Cell line
	id_gene5=lhead.index("Gene_5")	#Gene 5'
	id_gene3=lhead.index("Gene_3")	#Gene 3'
	id_kinase=lhead.index("Kinase")	#Kinase
	id_nmkinasepaper=lhead.index("NM_of_kinase_(paper)") #NM kinase (paper)
	id_nmkinasekim=lhead.index("NM_of_kinase_(KIM)")	#NM kinase (KIM)
	id_nmkinasetrex=lhead.index("NM_of_kinase_(TReX)") #NM kinase (TReX)
	id_kinasedomain=lhead.index("Kinase_domain")	#Kinase domain
	id_nmpartnerpaper=lhead.index("NM_of_partner_(paper)") #NM partner (paper)
	id_exon5=lhead.index("Exon_5") #Exon 5
	id_exon3=lhead.index("Exon_3") #Exon 3
	id_fustype=lhead.index("Fusion_Type") #Fusion Type
	id_knownfus=lhead.index("Known_Fusion") #Known Fusion
	id_tech=lhead.index("Technology")	#Tecnology
	id_pmid=lhead.index("Reference_PMID")	#PubMed ID
	######################################################################



	######################################################################
	#######################	Sez LINEA CELLULARE	##########################
	######################################################################
	print("### ===> ### 7.1: Check cell line in our dictionaru! ###")
	cklinea=checks.checkline(llinea[id_cellline],cline,li)	#Recupero le informazioni relative alla linea cellulare
	print("### ===> ### 7.3: Get Cell Line Canonical Name in our dictionary! ###")
	gcname=getcline(cline,hcline,cklinea,"Canonical Name")
	print("### ===> ### 7.4: Get Cell Line Synonym in our dictionary! ###")
	gsynonym=getcline(cline,hcline,cklinea,"Synonym Group")
	print("### ===> ### 7.5: Get Cell Line Tissue in our dictionary!! ###")
	gtissue=getcline(cline,hcline,cklinea,"Primary Tissue")

	print("### ===> ### 7.6: Check 5' gene in our HGNC dictionary! ###")
	ckgene5=checks.checkgene(llinea[id_gene5],hgnc,hhgnc,li)
	print("### ===> ### 7.8: Get gene 5' Canonical Name del Gene 5' in HGNC dictionary! ###")
	g5gene=getgene(hgnc,hhgnc,ckgene5,"Approved Symbol")

	print("### ===> ### 7.9: Check 3' gene in our HGNC dictionary! ###")
	ckgene3=checks.checkgene(llinea[id_gene3],hgnc,hhgnc,li)
	print("### ===> ### 7.10: Get gene 3' Canonical Name del Gene 5' in HGNC dictionary! ###")
	g3gene=getgene(hgnc,hhgnc,ckgene3,"Approved Symbol")
	######################################################################


	######################################################################
	############################	Sez KINASE	##########################
	######################################################################
	print("### ===> Step 8: Start filling step for kinase section! ###")
	print("### ===> ### 8.1: Get group of kinase ###")
	gkin=getgroup(llinea[id_kinase],dkin)
	if(llinea[id_kinase]==g3gene):
		gid=ckgene3
		partner=g5gene
		gidpartner=ckgene5
	else:
		gid=ckgene5
		partner=g3gene
		gidpartner=ckgene3

	print("### ===> ### 8.2: Get Entrez Gene ID of Kinase ###")
	gentrez=gethgnc(hgnc,hhgnc,gid,"Entrez Gene ID")
	gentrez_ncbi=gethgnc(hgnc,hhgnc,gid,"Entrez Gene ID(supplied by NCBI)")
	id_entrez=chooser(gentrez,gentrez_ncbi,"Entrez",li)

	guniprot_id=gethgnc(hgnc,hhgnc,gid,"UniProt ID(supplied by UniProt)")
	if(guniprot_id!=""):
		print("### ===> ### 8.3: Get Uniprot ID of Kinase ###")
	else:
		print(">>>[9] No Math is found for Uniprot ID, field MANDATORY!")
		sys.exit()

	print("### ===> ### 8.4: Get NM of kinase ###")
	if(llinea[id_nmkinasepaper]==""):
		gnmkinase=gethgnc(hgnc,hhgnc,gid,"RefSeq IDs")
		gnmkinase_ncbi=gethgnc(hgnc,hhgnc,gid,"RefSeq(supplied by NCBI)")
		id_nmkinase=chooser_nm(gnmkinase,gnmkinase_ncbi,"NM",li)
	else:
		id_nmkinase=llinea[id_nmkinasepaper]

	print("### ===> ### 8.5: Get Kinase Domain ###")
	gkindom=getuniprot(uniprot,huniprot,guniprot_id)
	######################################################################


	######################################################################
	############################	Sez PARTNER	##########################
	######################################################################
	print("### ===> Step 9: Start Filling step for section Partner! ###")
	print("### ===> ### 9.1: Recupero NM del partner ###")
	if(llinea[id_nmpartnerpaper]==""):
		gnmpartner=gethgnc(hgnc,hhgnc,gidpartner,"RefSeq IDs")
		gnmpartner_ncbi=gethgnc(hgnc,hhgnc,gidpartner,"RefSeq(supplied by NCBI)")
		id_nmpartner=chooser_nm(gnmpartner,gnmpartner_ncbi,"NM",li)
	else:
		id_nmpartner=llinea[id_nmpartnerpaper]
	######################################################################


	######################################################################
	############################	Sez FUSION	##########################
	######################################################################
	print("### ===> Step 10: Start fillinf step for section Fusion! ###")
	print("### ===> ### 10.1: Get Fusion ###")
	gfusion=str(g5gene)+"-"+str(g3gene)
	print("### ===> ### 10.2: Get gene 5' chromosome ###")
	gchr5loc=gchr(ckgene5,hgnc,hhgnc)
	print("### ===> ### 10.3: Get gene 3' chromosome ###")
	gchr3loc=gchr(ckgene3,hgnc,hhgnc)

	if(g5gene==llinea[id_kinase]):
		print("### ===> ### 10.4: Get sequence 5' ###: "+g5gene.strip())
		nmgene5=getnm(llinea[id_nmkinasepaper].strip(),id_nmkinase,llinea[id_nmkinasekim].strip(),li)
		gseq5,cont_seq5,break5=getsequence(nmgene5,llinea[id_exon5],"5")
		ex_kin=5
	else:
		print("### ===> ### 10.4: Get sequence 5' ###: "+g5gene.strip())
		nmgene5=getnm(llinea[id_nmpartnerpaper].strip(),id_nmpartner,"",li)
		gseq5,cont_seq5,break5=getsequence(nmgene5,llinea[id_exon5],"5")

	if(g3gene==llinea[id_kinase]):
		print("### ===> ### 10.5: Get sequence 3' ###: "+g3gene.strip())
		nmgene3=getnm(llinea[id_nmkinasepaper].strip(),id_nmkinase,llinea[id_nmkinasekim].strip(),li)
		gseq3,cont_seq3,break3=getsequence(nmgene3,llinea[id_exon3],"3")
		ex_kin=3
	else:
		print("### ===> ### 10.5: Get sequence 3' ###: "+g3gene.strip())
		nmgene3=getnm(llinea[id_nmpartnerpaper],id_nmpartner,"",li)
		gseq3,cont_seq3,break3=getsequence(nmgene3,llinea[id_exon3],"3")

	print("### ===> ### 10.6: Get breakpoint ### ")
	gbreak=getbreakpoint(int(break3),int(break5),ex_kin)

	print("### ===> ### 10.7: Get protein fusion length ### ")
	gfuslen=int(float(float(cont_seq5)+float(cont_seq3)))
	######################################################################


	######################################################################
	############################	Sez META	##########################
	######################################################################
	print("### ===> Step 11: Start Filling steo for section Meta! ###")
	print("### ===> ### 11.1: GET TCGA samples with fusions ### ")
	gfusion_tcga=checktcga(gfusion,tcga)
	if len(gfusion_tcga)>=1: #C'e' almeno una fusione
		tcga_bool="Y"
		sample=["TCGA-"+str(s) for s in gfusion_tcga]
		tcga_sample=", ".join(sample)
	else:
		tcga_bool="N"
		tcga_sample=""
	######################################################################


	######################################################################
	################################	WRITING	##########################
	######################################################################
	wdict.extend((llinea[id_cellline],gcname,gsynonym,gtissue,llinea[id_gene5],llinea[id_gene3],g5gene,g3gene,
		llinea[id_kinase],gkin,id_entrez,guniprot_id,llinea[id_nmkinasepaper],id_nmkinase,llinea[id_nmkinasekim],llinea[id_nmkinasetrex],gkindom,llinea[id_kinasedomain],
		llinea[id_nmpartnerpaper],id_nmpartner,
		gfusion,gchr5loc,gchr3loc,llinea[id_exon5],llinea[id_exon3],str(gbreak),str(gseq5),str(gseq3),str(gfuslen),llinea[id_fustype],llinea[id_knownfus],
		llinea[id_tech],tcga_bool,tcga_sample,llinea[id_pmid]))
	return(wdict)
	######################################################################
