sequenceString = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

def  searchGen(string):
    genlist = string.split('ATG')
    replaceList =[]
    for gen in genlist:

        if 'TAG' in gen:
            replaceList.append(gen.split("TAG"))

        if 'TAA' in gen:
            replaceList.append(gen.split("TAA"))

        if 'TGA' in gen:
            replaceList.append(gen.split("TGA"))

        if len(genlist) / 3 != float:
         return genlist




print(searchGen(sequenceString))
