#!/usr/bin/python3
"""Handle connections and send back results"""
import os

import vcf # pip install PyVCF
import pandas as pdb
import numpy 


# 3rd party imports 
from flask import Flask, request, jsonify
from flask.json import JSONEncoder


APP = Flask(__name__)


@APP.route('/', methods=['POST'])
def index():
    """Read and process client input"""
    # Retrieve data from request
    data = request.get_json()
    
    # Load the file
    if 'filename' in data:
        filename = data['filename']
    filename = "data/gnomad.exomes.r2.1.1.sites.21.vcf"
    CLASSIFIER.load_file(filename)
    
    # Classify
    classification = CLASSIFIER.classify()
    
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

class Classifier:
    def __init__(self):
        # self.sumthin = ?
        pass
    
    def load_file(self, filename):
        # Create a reader
        self.csf_reader = vcf.Reader(open(filename))
        
        
    def classify(self):
        # Load reader
        csf_reader= self.csf_reader
        
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
