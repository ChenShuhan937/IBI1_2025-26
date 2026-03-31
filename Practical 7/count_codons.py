# Practical 7 - Task 3: Codon frequency
# Count in-frame codons upstream of specified stop codon, generate pie chart
import matplotlib.pyplot as plt
from collections import defaultdict

# 1. Define valid stop codons and start codon (DNA version)
valid_stop_codons = ['TAA', 'TAG', 'TGA']
start_codon = 'ATG'
# Set plot style (ensure clear labels)
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (12, 8)

# 2. Get and validate user input (only one of the three stop codons)
while True:
    user_stop = input("Please enter a stop codon (TAA/TAG/TGA): ").strip().upper()
    if user_stop in valid_stop_codons:
        break
    else:
        print(f"Invalid input! Please enter only one of: {', '.join(valid_stop_codons)}")

# 3. Initialize variables for FASTA parsing and codon counting
codon_count = defaultdict(int)  # Key: codon, Value: count
input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

# 4. Read FASTA file and process each gene
with open(input_file, 'r') as f:
    current_header = ''
    current_seq = ''
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            # Process previous gene
            if current_header and current_seq:
                start_pos = current_seq.find(start_codon)
                if start_pos != -1:
                    # Find ALL positions of the user-specified stop codon (in-frame)
                    stop_positions = []
                    for pos in range(start_pos + 3, len(current_seq) - 2, 3):
                        codon = current_seq[pos:pos+3]
                        if codon == user_stop:
                            stop_positions.append(pos)
                    # Use the LAST stop codon (longest ORF) if exists
                    if stop_positions:
                        final_stop_pos = stop_positions[-1]
                        # Count all in-frame codons from start to final stop (excluding stop)
                        for pos in range(start_pos, final_stop_pos, 3):
                            codon = current_seq[pos:pos+3]
                            codon_count[codon] += 1
            # Reset for new gene
            current_header = line
            current_seq = ''
        else:
            current_seq += line
    # Process the last gene
    if current_header and current_seq:
        start_pos = current_seq.find(start_codon)
        if start_pos != -1:
            stop_positions = []
            for pos in range(start_pos + 3, len(current_seq) - 2, 3):
                codon = current_seq[pos:pos+3]
                if codon == user_stop:
                    stop_positions.append(pos)
            if stop_positions:
                final_stop_pos = stop_positions[-1]
                for pos in range(start_pos, final_stop_pos, 3):
                    codon = current_seq[pos:pos+3]
                    codon_count[codon] += 1

# 5. Print codon count results 
print(f"\nCodon counts upstream of {user_stop} (longest ORF only):")
for codon, count in sorted(codon_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{codon}: {count}")

# 6. Generate well-labelled pie chart
# Prepare data (filter low-count codons for readability, group as 'Other')
threshold = max(codon_count.values()) * 0.01  # 1% threshold to reduce slice number
main_codons = {k: v for k, v in codon_count.items() if v >= threshold}
other_count = sum(v for k, v in codon_count.items() if v < threshold)
if other_count > 0:
    main_codons['Other'] = other_count

# Plot pie chart
labels = list(main_codons.keys())
sizes = list(main_codons.values())
colors = plt.cm.Set3(range(len(labels)))  # Color palette for distinct slices

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                   startangle=90, labeldistance=1.05)
# Customize text for readability
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(8)

# Add title and labels (well-labelled as required)
ax.set_title(f"Codon Frequency Upstream of {user_stop} (Longest ORF)", fontsize=14, pad=20)
# Save pie chart to file 
piechart_file = f"codon_frequency_{user_stop}.png"
plt.tight_layout()
plt.savefig(piechart_file, dpi=300, bbox_inches='tight')
plt.close()  # Close plot to avoid screen display

# 7. Print completion message
print(f"\nPie chart saved to {piechart_file}")