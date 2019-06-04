gnomad files = ["data/gnomad.exomes.r2.1.1.sites.21.vcf"]
rule all:
    input:
        "data/gnomad.exomes.r2.1.1.sites.21.vcf"

rule FlaskApp:
    shell:
        "python app.py &" 

rule SendRequest:
    shell:
        """curl -H "Content-Type: application/json" -d "{\"filename\":\"data/gnomad.exomes.r2.1.1.sites.21.vcf\"}" http://localhost:8080"""