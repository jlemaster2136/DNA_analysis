def dna_alignment(strand_a, strand_b):
    locations = []
    percentage = []
    bond_alignment = []
    if len(strand_a) >= len(strand_b):
        for n in range(len(strand_a)):
            if len(strand_a[n:]) >= len(strand_b):
                shared = 0
                bonds = ''
                for i in range(len(strand_b)):
                    if strand_a[(n+i)] == strand_b[i]:
                        shared += 1
                        bonds += '|'
                    else:
                        bonds += ' '
                        continue
                locations.append(n)
                percentage.append(shared/len(strand_b))
                bond_alignment.append(bonds)
            else:
                continue
        percent = float((max(percentage) * 100))
        best = f'Best alignment: {percent:.2f}% similarity (bp {locations[percentage.index(max(percentage))+1]}-{locations[percentage.index(max(percentage))+1]+len(strand_b)} on strand A)'
        strand_a_comp = strand_a[locations[percentage.index(max(percentage))]:(locations[percentage.index(max(percentage))] + len(strand_b))]
        complimentary_strand = ''
        for thing in strand_a_comp:
            if thing == 'A':
                complimentary_strand += 'T'
            elif thing == 'T':
                complimentary_strand += 'A'
            elif thing == 'C':
                complimentary_strand += 'G'
            elif thing == 'G':
                complimentary_strand += 'C'
            else:
                complimentary_strand += 'X'
        sequences = [f"5' - {strand_b} - 3'", f"     {bond_alignment[locations[percentage.index(max(percentage))]]}     ", f"3' - {complimentary_strand} - 5'"]
        return best + '\n' + "\n".join(sequences)
    if len(strand_a) < len(strand_b):
        for n in range(len(strand_b)):
            if len(strand_b[n:]) >= len(strand_a):
                shared = 0
                bonds = ''
                for i in range(len(strand_a)):
                    if strand_b[(n + i)] == strand_a[i]:
                        shared += 1
                        bonds += '|'
                    else:
                        bonds += ' '
                        continue
                locations.append(n)
                percentage.append(shared / len(strand_a))
                bond_alignment.append(bonds)
            else:
                continue
        percent = float((max(percentage)*100))
        best = f'Best alignment: {percent:.2f}% similarity (bp {locations[percentage.index(max(percentage))+1]}-{locations[percentage.index(max(percentage))+1]+len(strand_a)} on strand B)'
        strand_b_comp = strand_b[locations[percentage.index(max(percentage))]:(
                    locations[percentage.index(max(percentage))] + len(strand_a))]
        complimentary_strand = ''
        for thing in strand_b_comp:
            if thing == 'A':
                complimentary_strand += 'T'
            elif thing == 'T':
                complimentary_strand += 'A'
            elif thing == 'C':
                complimentary_strand += 'G'
            elif thing == 'G':
                complimentary_strand += 'C'
            else:
                complimentary_strand += 'X'
        sequences = [f"5' - {strand_a} - 3'", f"     {bond_alignment[locations[percentage.index(max(percentage))]]}     ", f"3' - {complimentary_strand} - 5'"]
        return best + '\n' + "\n".join(sequences)

a = 'ATGTCGAAAGCTACATATAAGGAACGTGCTGCTACTCATCCTAGTCCTGTTGCTGCCAAGCTATTTAATATCATGCACGAAAAGCAAACAAACTTGTGTGCTTCATTGGATGTTCGTACCACCAAGGAATTACTGGAGTTAGTTGAAGCATTAGGTCCCAAAATTTGTTTACTAAAAACACATGTGGATATCTTGACTGATTTTTCCATGGAGGGCACAGTTAAGCCGCTAAAGGCATTATCCGCCAAGTACAATTTTTTACTCTTCGAAGACAGAAAATTTGCTGACATTGGTAATACAGTCAAATTGCAGTACTCTGCGGGTGTATACAGAATAGCAGAATGGGCAGACATTACGAATGCACACGGTGTGGTGGGCCCAGGTATTGTTAGCGGTTTGAAGCAGGCGGCGGAAGAAGTAACAAAGGAACCTAGAGGCCTTTTGATGTTAGCAGAATTGTCATGCAAGGGCTCCCTAGCTACTGGAGAATATACTAAGGGTACTGTTGACATTGCGAAGAGCGACAAAGATTTTGTTATCGGCTTTATTGCTCAAAGAGACATGGGTGGAAGAGATGAAGGTTACGATTGGTTGATTATGACACCCGGTGTGGGTTTAGATGACAAGGGAGACGCATTGGGTCAACAGTATAGAACCGTGGATGATGTGGTCTCTACAGGATCTGACATTATTATTGTTGGAAGAGGACTATTTGCAAAGGGAAGGGATGCTAAGGTAGAGGGTGAACGTTACAGAAAAGCAGGCTGGGAAGCATATTTGAGAAGATGCGGCCAGCAAAACTAA'
b = 'CTGATGCTGCCAAGCTATTCAATATCATGCACCATAAGCAAACAAACTTGTGTGCTTCATTGGATGTTGGTACCACCAAGGAATTACTGGAGTAAGTTGAAGCATTAGGTCCCAAAATTTGTTTACTTATAACACATGTGGATATCTTGACTGAATTATCCATGGAGGGCACAGTAAAGCCGCTAAAGGCATTATCCGCCAAGTACAATTTTTTACTCTTCGAAGACAGAAAATTTGCTGACATTGGTAATACAGTCAAATTGCAGTACTCTGCGGGTGTATACAGAATAGCAGAATGGGCAGACATTACGAATGCACACGGTGTGGTGGGCCCAGGTATTGTTAGCGGTTTGAAGCAGGCGGCGGAAGAAGTAACAAAGGAACCTAGAGGCCTTTTGATGTTAGCAGAATTGTCATGCAAGGGCTCCCTAGCTACTGGAGAATATACTAAGGGTACTGTTGACATTGCGAAGAGCGACAAAGATTTTGTTATCGGCTTTATTGCTCAAAGAGACATGGGTGGAAGAGATGAAGGTTACGATTGGTTGATTATGACTCCCGGTGTGGGTTTACATGACAAGGGAGACGCGTTGGGTCAACAGTATAGAACCGTGGATGATGTGGTCTCTACAGGATCTGACATTATTATTGTTGGAAGAGGACTGTTTGCAAAGGGAAGGGATGCTAA'



print(dna_alignment(a, b))