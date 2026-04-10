# Task 1: Protein Mass Calculator
# Create a dictionary to store amino acid masses (key: symbol, value: mass in amu)
aa_mass = {
    'G': 57.02,
    'A': 71.04,
    'S': 87.03,
    'P': 97.05,
    'V': 99.07,
    'T': 101.05,
    'C': 103.01,
    'I': 113.08,
    'L': 113.08,
    'N': 114.04,
    'D': 115.03,
    'Q': 128.06,
    'K': 128.09,
    'E': 129.04,
    'M': 131.04,
    'H': 137.06,
    'F': 147.07,
    'R': 156.10,
    'Y': 163.06,
    'W': 186.08
}

# Function to calculate total protein mass
# Input: amino acid sequence (string)
# Output: total mass (float) or error message (string)
def calculate_protein_mass(sequence):
    # Initialize total mass to 0
    total_mass = 0

    # Iterate over each amino acid in the input sequence
    for aa in sequence:
        # Check if the amino acid is valid (exists in the dictionary)
        if aa not in aa_mass:
            return f"Error: Invalid amino acid detected -> {aa}"
        
        # Add the mass of current amino acid to total
        total_mass += aa_mass[aa]

    # Return the final total mass
    return total_mass

# ------------------------------
# Example function calls
# ------------------------------
print("=== Task 1 Example Output ===")
# Test with valid sequence
print("Mass of GASPV:", calculate_protein_mass("GASPV"))
# Test with invalid amino acid
print(calculate_protein_mass("GAZ"))
print()