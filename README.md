# Benign Filter Project
By Luuk van Damme & Rogier Stegeman

## Usage
### Run the program
Start the API, database and Kibana:
>`docker-compose up`<br>
This will start 3 containers. The required packages are either shipped with the official images or installed using `requirements.txt`. Add the `--build` flag to the command to rebuild the images with the changes.


Run Snakemake:
>`snakemake --latency-wait 30 --snakefile Snekfile`

Run pipeline again:
>Remove all files you want to run generate again and call Snakemake again

Easily remove all old files if you want Snakemake to run from scratch:
>`python clean_workspace.py`

### Inspect results
View HTML report:
>Open the html files in your browser

Explore Elasticsearch with Kibana:
>Go to http://localhost:5601

## Ports
|Service|Port|
|:-:|:-:|
|API|80|
|Elasticsearch|9200|
|Kibana|5601|

## TO-DO
* Use alpine version(s)

## Disclaimer
Snakemake is an amazing and powerful workflow management system but it doesn't shine in this project. Snakemake's real power can be seen in straightforward and linear data editing workflows of which RNAseq is a sublime example.
