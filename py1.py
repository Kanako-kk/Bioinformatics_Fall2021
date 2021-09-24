dna_list = ['GAGGAGTC', 'CGAATAGC', 'GTCAGCTA', 'CCCCAG', 'ATCGGTG','ATATTGC']
#make a list with a length of DNA 
length_list= list(map(lambda dna: len(dna),dna_list))
print(length_list)

#at_content returns at content 
at_content= list(map(lambda dna: round((dna.count('A')+ dna.count('T'))/len(dna),3), dna_list))
print(at_content)

#at_rich returns DNA fragement with more than 0.5 at content
def atrich(dna):
    return (dna.count('A')+dna.count('T'))/len(dna)> 0.5
at_rich = list(filter(atrich, dna_list))
print(at_rich)
