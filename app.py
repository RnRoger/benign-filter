import vcf
import pandas as pdb
csf_reader = vcf.Reader(open("data/gnomad.exomes.r2.1.1.sites.21.vcf"))

exomes = []
for count, record in enumerate(csf_reader):
    if count <25:
        attr = {
            'Character Name' : record.CHROM,
            'ID': record.ID,
            'Allele Frequency': record.INFO["AF"][0]
        }
        print(attr)
        if attr.get('Allele Frequency') < 0.01:
            exomes.append(attr)
    else:
        break

print("Exomes found:")
print(exomes)