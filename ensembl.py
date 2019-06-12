import json
import sys
import requests, sys
 
server = "http://rest.ensembl.org"

def main():
    data = []
    docs = json.load(open(f'./{sys.argv[1]}'))
    
    for doc in docs:
        rsID = doc["NAME"]
        if rsID == "None":
            doc["most_severe_consequence"]= None
            doc["clinical_significance"]= None
            data.append(doc)
        else:
            try:
                ext = f"/variation/human/{rsID}?genotyping_chips=1"
                r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
                if not r.ok:
                    r.raise_for_status()
                    sys.exit()
                decoded = r.json()
                for w in ["most_severe_consequence", "clinical_significance"]:
                    try:
                        doc[w] = decoded[w]
                    except:
                        doc[w] = "N/A"
                data.append(doc)
            except IndexError:
                print("No hit found by Ensembl")
                pass
            except:
                pass

    with open(f"data/{sys.argv[2]}ensembl.json", "w") as out:
        #data = str(data).replace("\'","\"")
        data = json.dump(data, out)


if __name__ == "__main__":
    main()