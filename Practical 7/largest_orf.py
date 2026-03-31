#Practical 7 - Open Reading Frames
#Identify the longest ORF in the given mRNA sequence
#1. Define the specific sequence variable
#2. Define start and stop codons
#3. Initialize variables to store longest ORF and its length
#4. Traverse the sequence to find all start codons (AUG)
#5. From the start codon, check triplets for stop codon 
#6. Print the results
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon = 'AUG'
stop_codons = ['UAA','UAG','UGA']
longest_orf = ''
max_length = 0
#Iterate over every position
for start_pos in range(len(seq) - len(start_codon) + 1):
#Check if current position is the start codon
    if seq[start_pos:start_pos+3] == start_codon:
    #Iterate in steps of 3
        for stop_pos in range(start_pos + 3,len(seq) - 2, 3):
            current_codon = seq[stop_pos:stop_pos+3]
            #If stop codon is found, extract ORF
            if current_codon in stop_codons:
                orf=seq[start_pos:stop_pos+3]
                orf_length = len(orf)
                #Update ORF if current is longer
                if orf_length > max_length:
                    max_length = orf_length
                    longest_orf = orf
                    #Stop after first stop codon
                break
print(f"The longest ORF in the sequence:{longest_orf}") 
print(f"Length of the longest ORF(nucleotides): {max_length}")               

