from Bio import Entrez
from Bio import SeqIO
from Bio import GenBank
import re
    
def download_pubmed (keyword):
    """
    El siguiente comando permite buscar articulos en pubmed mediante palabras claves
    """
     
    Entrez.email = 'jefferson.hernandez@est.ikiam.edu.ec'
    busq = Entrez.read(Entrez.esearch(db="pubmed", 
                            term=keyword,
                            usehistory="y"))
    webenv = busq["WebEnv"]
    query_key = busq["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                           rettype="medline", 
                           retmode="text", 
                           retstart=0,
                           retmax=543, webenv=webenv, query_key=query_key)
    data = handle.read()
    dataexp = re.sub(r'\n\s{6}','', data)
    return dataexp
    

def mapscience(archivo):
    """Este comando genera un mapa de ciencia de los paises de los autores"""
    contentsse = re.sub(r'\s+[Eceinlort]{10}\s+[aders]{7}.*','',archivo)
    contentssc = re.sub(r'\s[\w._%+-]+@[\w.-]+\.[a-zA-Z]{1,4}','',contentsse)
    contentsna = re.sub(r'\..\d.\,',',',contentssc)
    contentsnu = re.sub(r'\..\d.','',contentsna)
    x=contentsnu[1:].split('PMID-')
    AD1=[]
    for PMID in x:
        q=PMID.split('\n')
        for fila in q:
            w=fila.split(' ')
            if w[0] == 'AD':
                e=fila.split(',')
                AD1.append(e[-1])
    
    AD2=[]
    for dire in AD1:
        r=dire
        t=dire.split(' ')
        if t[0] == "AD":
            u=t[-1]
        AD2.append(u)
    
    b=0
    AD3 =[0]*len(AD2)
    for obj in AD2:
        bytes(obj,encoding="utf8")
        if obj != '':
            g=obj
            if g[0] == ' ':
                g = re.sub (r'^\s','',g)
            if g[-1] == '.':
                g = re.sub (r'\.$','',g)
            g = re.sub (r'\.$','',g)
            g = re.sub (r'\s$','',g)
        AD3[b]=g
        b=b+1
        
    return AD3
