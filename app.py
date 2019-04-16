import vcf # pip install PyVCF
import pandas as pdb

def main():
    # Create a reader
    csf_reader = vcf.Reader(open("data/gnomad.exomes.r2.1.1.sites.21.vcf"))
    # List for benign alleles
    exomes = []
    # Use an enumerator to go through the records
    for count, record in enumerate(csf_reader):
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


if __name__ == "__main__":
    main()