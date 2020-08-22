# KuNG-FU-Database: a database of KiNase Gene FUsions in cancer cell lines

<p align="center">
  <img src="http://www.kungfudb.org/img/kungfu_logo.png" width="350" title="hover text" alt="KuNG-FU-Database">
</p>

<p align="justify">
KuNG FU (KiNase Gene FUsion) is a novel homogeneous user-friendly on line database collecting the largest manually curated catalogue of annotated, potentially active and experimentally validated kinase gene fusions identified in cancer cell lines. Only in-frame kinase gene fusions retaining an intact catalytic domain were included, to offer a druggable set of kinase gene fusion targets characterized in cancer cell line models. The KuNG FU database was developed and made available online to support the strong interest in kinase gene fusion research models in drug development and diagnostic tool design, often hampered by a lack of exhaustive and convenient specific databases.
</p>

# Workflow

<p align="center">
  <img src="http://www.kungfudb.org/img/schema_kungfu.png" title="hover text" alt="KuNG-FU-Database schema">
</p>

<p align="justify">
  <ul>
    <li>
  MySQL database containing kinase gene fusions (retaining in-frame and intact kinase domain) in cell lines with detailed molecular description, derived from automated searches and extensive manual curation from over a million scientific papers, dated starting from 2013 and integrated with public datasets and previous literature
    </li>
Intuitive web interface supporting free-text searches, as well as filtering based on keywords (kinase gene name, kinase group name, cell line name, primary tissue or chromosomal rearrangement event generating the gene fusion)
Queries allowed among a wide panel of human cancer cell lines, both from the CCLE (The Cancer Cell Line Encyclopedia, Barretina, J. et al. 2012) and other databases, as well as reported in sparse publications (about 50% of the database content)
Query output containing all the data types collected for each kinase gene fusion, organized in sub-sections, such as ‘Cell Line’, ‘AGFusion Plot’, ‘Fusion’, ‘Kinase’ and ‘Supporting Literature’ annotation fields
Sub-sections providing detailed kinase gene fusion molecular information, such as breakpoints, respective specific transcripts and introns/exons involved in the fusion event, along with a graphical representation of the gene fusion construct and protein domains for visual inspection through AGFusion plots (Murphy, C. et al., 2016)
Published experimental methods used for gene fusion validation with respective supporting literature PMID references, and links to the Tumor Fusion Gene Data Portal database (Hu, X. et al., 2018) for corresponding gene fusion events detected in patient-derived tumor samples
Graphical summaries of the KuNG FU database content
Satabase content open to regular updates and exportable in txt format; also open to contributions from users who are encouraged to submit their own experimentally validated kinase gene fusion data through the web based submission form, available in the KuNG FU Upload Page
    </ul>
</p>
