#Practical 7 - stop codon usage
#Read yeast cDNA FASTA, identify genes with in-frame stop codons, output to stop_genes.fa
#1. Define stop codons
stop_codons_dna = ['TAA', 'TAG', 'TGA']
start_codon_dna = 'ATG'
#2.Initialize variables for FASTA file
current_header = ''
current_seq = ''
output_genes = []  # Store (gene_name, stop_codons_present, full_seq) for valid genes
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
with open(input_file, 'r') as f:
    for line in f:
        line = line.strip() #Remove whitespace
        if not line:
            continue #skip empty lines
            #Check if line is a header
        if line.startswith('>'):
            #Process previous gene if it exists
            if current_header and current_seq:
                #extract gene name
                gene_name = current_header.split()[0][1:]
                #find start codon (ATG) to define in-frame
                start_pos = current_seq.find(start_codon_dna)
                stop_codons_present = set()
                if start_pos != -1:  # Only process genes with start codon
                    # Iterate in triplets from start codon (in-frame)
                    for pos in range(start_pos + 3, len(current_seq) - 2, 3):
                        codon = current_seq[pos:pos+3]
                        if codon in stop_codons_dna:
                            stop_codons_present.add(codon)
                            # No break: find all unique stop codons in the gene
                # Keep gene if at least one stop codon is present
                if stop_codons_present:
                    output_genes.append((gene_name, sorted(stop_codons_present), current_seq))
            # Reset for new gene
            current_header = line
            current_seq = ''
        else:
            # Merge sequence lines (sequence runs onto several lines)
            current_seq += line
    # Process the last gene in the file
    if current_header and current_seq:
        gene_name = current_header.split()[0][1:]
        start_pos = current_seq.find(start_codon_dna)
        stop_codons_present = set()
        if start_pos != -1:
            for pos in range(start_pos + 3, len(current_seq) - 2, 3):
                codon = current_seq[pos:pos+3]
                if codon in stop_codons_dna:
                    stop_codons_present.add(codon)
        if stop_codons_present:
            output_genes.append((gene_name, sorted(stop_codons_present), current_seq))

# 4. Write results to new FASTA file: stop_genes.fa (required by assignment)
output_file = 'stop_genes.fa'
with open(output_file, 'w') as f:
    for gene_name, stop_codons, seq in output_genes:
        # Header: only gene name + stop codons (comma-separated)
        header = f">{gene_name} {','.join(stop_codons)}"
        # Write header and sequence (split seq into 80 chars per line for standard FASTA)
        f.write(header + '\n')
        for i in range(0, len(seq), 80):
            f.write(seq[i:i+80] + '\n')

# 5. Print completion message (for verification)
print(f"Processing complete! Results saved to {output_file}")
print(f"Number of genes with in-frame stop codons: {len(output_genes)}")
