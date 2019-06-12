#!/usr/bin/python3
"""Handle connections and send back results"""
import os
<<<<<<< HEAD
import json
=======
>>>>>>> 42c20fe88e9628c9a6b4b6420913355a3ff2f478

import vcf # pip install PyVCF
import pandas as pdb
import numpy
from werkzeug.exceptions import BadRequest # For custom error messages

# 3rd party imports 
from flask import Flask, request, jsonify
from flask.json import JSONEncoder


APP = Flask(__name__)


@APP.route('/', methods=['POST'])
def index():
    """Read and process client input"""
    # Retrieve data from request
    data = request.get_json()
    
    filename = "data/gnomad.exomes.r2.1.1.sites.21.vcf"
    # Load the file
    if 'filename' in data:
        filename = data['filename']
    CLASSIFIER.load_file(filename)
    
    # Classify
    classification = CLASSIFIER.classify()
    
<<<<<<< HEAD
    # return jsonify(classification)
    with open(f"data/{data['chr']}.json", "w") as outfile:
        json.dump(classification, outfile)
    return "ok"
    

=======
    return jsonify(classification)
    

    """
    model = 'general-10e-300v.bin'
    if 'model' in data:
        model = data['model']
    CLASSIFIER.load(model)

    if 'tokens' in data:
        classification = CLASSIFIER.tokens(data['tokens'])
        return jsonify(classification)
    elif 'text' in data:
        classification = CLASSIFIER.text(data['text'])
        return jsonify(classification)

    return jsonify({})
    """

>>>>>>> 42c20fe88e9628c9a6b4b6420913355a3ff2f478
class Classifier:
    def __init__(self):
        # self.sumthin = ?
        pass
    
    def load_file(self, filename):
        # Create a reader
        try:
            self.vcf_reader = vcf.Reader(open(filename))
        except FileNotFoundError:
            raise BadRequest('The file could not be opened, please check the filename.')
        
        
    def classify(self):
        # Load reader
        vcf_reader= self.vcf_reader
        
        # List for benign alleles
        exomes = []
        count=0
        # Use an enumerator to go through the records
        for record in vcf_reader:
            count+=1
            try:
<<<<<<< HEAD
                if count <10: # For testing, only take the first x rows
                #if count > 0: # Use all rows
                    # Get information from the record
                    attr = {
                        'ID' : count,
                        'CHROM' : record.CHROM,
                        'POS' : record.POS,
                        'REF' : record.REF,
                        'NAME': record.ID,
=======
                if count <25: # For testing, only take the first x rows
                #if count > 0: # Use all rows
                    # Get information from the record
                    attr = {
                        'Name' : record.CHROM,
                        'ID': record.ID,
>>>>>>> 42c20fe88e9628c9a6b4b6420913355a3ff2f478
                        'Allele frequency': record.INFO["AF"][0]
                    }
                    # Store the allele if it is found in less than 1% of the population
                    if attr.get('Allele frequency') < 0.01:
<<<<<<< HEAD
                        exomes.append(attr)
=======
                        exomes.append(attr['ID'])
>>>>>>> 42c20fe88e9628c9a6b4b6420913355a3ff2f478
                else:
                    break
            except:
                pass
    
<<<<<<< HEAD
=======
        print("Exomes found:")
        print(exomes)
>>>>>>> 42c20fe88e9628c9a6b4b6420913355a3ff2f478
        return exomes


class Float32Encoder(JSONEncoder):
    """Encode numpy floats for json"""
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(Float32Encoder, self).default(obj)


def main():
    """Start the script"""
    global CLASSIFIER
    CLASSIFIER = Classifier()

    APP.json_encoder = Float32Encoder

    APP.run(host="0.0.0.0", port=80)


if __name__ == '__main__':
    main()
