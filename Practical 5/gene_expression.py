#Practical 5 gene expression analysis
#Import matplotlib for bar chart
import matplotlib.pyplot as plt
#create dictionary with initial 5 genes and expression values
gene_exp={
    "TP53":12.4,
    "EGFR":15.1,
    "BRCA1":8.2,
    "PTEN":5.3,
    "ESR1":10.7
}
#print the initial dictionary
print("Initial gene expression dictionary:")
print(gene_exp)
#Add gene "MYC" to the dictionary
gene_exp["MYC"]=11.6
#Print updated dictionary with MYC
print("\nUpdated dictionary with MYC:")
print(gene_exp)
#create well-labelled bar chart for all 6 genes
#Extract genes(x-axis) and expression values (y-axis)
genes=list(gene_exp.keys())
expressions=list(gene_exp.values())
#set up bar chart
plt.figure(figsize=(10,6)) #chart size
plt.bar(genes,expressions,color="steelblue") #bar chart with color
#Add labels and title
plt.xlabel('Gene Name')
plt.ylabel('Expression Level')
plt.title('Gene Expression Levels in Biological Sample')
plt.xticks(rotation=0) #Keep gene names horizontal for readability
plt.grid(axis='y', linestyle='--', alpha=0.7) #Add horizontal grid
#Save chart
plt.savefig('gene_expression_bar_chart.png')
plt.close() #Close plot to avoid display issues
print("\nBar chart saved as'gene_expression_bar_chart.png'")
#gene of interest query
#modify the below variable 'gene_interest' to check different genes
gene_interest="EGFR"
#check if gene exists,print value or error message
if gene_interest in gene_exp:
    print(f"\nExpression level of {gene_interest}:{gene_exp[gene_interest]}")
else:
    print(f"\nError: Gene'{gene_interest}'is not present in the dataset.")
#Calculate and print average gene expression level
total_exp=sum(expressions)
num_genes=len(expressions)
average_exp= total_exp / num_genes
print(f"\nAverage gene expression level across all {num_genes} genes:{average_exp:.2f}")


