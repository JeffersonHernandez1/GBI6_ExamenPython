def download_pubmed (keyword):
    """
    La palabra "keyword" es clave para nuestra búsqueda.
    """
    from Bio import Entrez
    from Bio import SeqIO
    from Bio import GenBank 
    Entrez.email = 'jefferson.hernandez@est.ikiam.edu.ec'
    handle = Entrez.esearch(db='pubmed',
                        sort='relevance',
                        retmax='200',
                        retmode='xml',
                        term=keyword)
    results = Entrez.read(handle)
    id_list = results["IdList"]
    ids = ','.join(id_list)
    Entrez.email = 'A.N.Other@example.com'
    handle = Entrez.efetch(db='pubmed',
                       retmode='text',
                       id=ids)
    lista_id = ids.split(",")
    return (lista_id)

def mining_pubs(tipo):
    """Docstring mining_pubs"""
    if tipo == "AD":
        
    
    return 
