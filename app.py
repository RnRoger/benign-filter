#!/usr/bin/python3
"""Handle connections and send back results"""
import os
import json

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
    
    # Default file
    filename = "data/gnomad.exomes.r2.1.1.sites.21.vcf"
    # Load the file
    if 'filename' in data:
        filename = data['filename']
    CLASSIFIER.load_file(filename)
    
    # Classify
    classification = CLASSIFIER.classify()
    
    # return jsonify(classification)
    with open(f"data/{data['chr']}.json", "w") as outfile:
        json.dump(classification, outfile)
    return "ok"
    

class Classifier:
    def __init__(self):
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
        
        # List for benign hits
        benign = []
        count = 0
        # Use an enumerator to go through the records
        for record in vcf_reader:
            count += 1
            try:
                # For testing, only take the first x rows
                # Due to the Ensembl rule the program will take a long time to run otherwise.
                if count <10:
                # If count > 0: # Uncomment to use all rows
                    # Get information from the record
                    attributes = {
                        'ID' : count,
                        'CHROM' : record.CHROM,
                        'POS' : record.POS,
                        'REF' : record.REF,
                        'NAME': record.ID,
                        'Allele frequency': record.INFO["AF"][0]
                    }
                    # Store the allele if it is found in less than 1% of the population
                    if attributes.get('Allele frequency') < 0.01:
                        benign.append(attributes)
                else:
                    break
            except:
                pass
    
        return benign


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
