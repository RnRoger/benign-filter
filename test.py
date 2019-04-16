from collections import Counter
with open("data/gnomad.exomes.r2.1.1.sites.21.vcf", "r") as exomes:
    count = 0
    value_list = []
    for line in exomes:
        count += 1
        if count > 900:
            pairs = line.split(";")
            for pair in pairs:
                if pair.startswith("aaf"): #n_alt_alleles
                    value = pair.split("=")[1]
                    value_list.append(value)

    print(Counter(value_list))