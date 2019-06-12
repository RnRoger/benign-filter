import vcf

vcf_reader = vcf.Reader(open('./data/gnomad.exomes.r2.1.1.sites.21.vcf','r'))

#TODO fix count
# List for benign alleles
exomes = []
count=1
# Use an enumerator to go through the records
for record in vcf_reader:
    print(record)
    #if count <25: # For testing, only take the first x rows
    if count > 0: # Use all rows
        # Get information from the record
        attr = {
            'Name' : record.CHROM,
            'ID': record.ID,
            'Allele frequency': record.INFO["AF"][0]
        }
        # Store the allele if it is found in less than 1% of the population
        if attr.get('Allele frequency') < 0.01:
            exomes.append(attr)
    else:
        break

print("Exomes found:")
print(exomes)