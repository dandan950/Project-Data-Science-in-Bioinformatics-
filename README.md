# User Manual

|  Member       | 
|  ----         |
| Ruidan LIU    | 
| Yifei YAO     | 
| Hong YANG     | 
| Chengcheng LI | 


### Pipelines Introduction

we use `snakemake` to help us to simpllify the progress and use `vscode` to connect the server `c44` .

And we design two pipelines, the following:

- `reference-guided assembly pipeline` QC and filter low quality read data --> read align-->read sort-->variant calling-->create consensus sequence -->lineage detection</br>
in `workflow`

- `de novo assembly pipeline` QC and filter low quality read data -->de novo assembly(Fragments -> Contigs -> Scaffolds) --> quast evaluation-->lineage detection</br>
in`workflow2`



##### Tools

miniconda</br>
snakemake</br>
python3</br>
- fastqc >=0.11.9
- fastp >=0.22.0
- bcftools >=1.9
- samtools >=1.9
- bwa =0.7.17
- picard
- megahit=1.2.9
- ragtag
- quast


# Before You Use

Before you use our pipeline, you should create original data folder in our project folder firstly. And put original data into the folder, then decompress gz files(.fastq.gz -> .fastq). The following is more details:

##### Create Original Data Folder and Put Original Read Data

*  You need to create `original_fastq` folder in our project folder `Project-Data-Science-in-Bioinformatics-/`, it use to put original read data(.fastq/.fastq.gz). Please make sure the folder name is same. </br>
`original_fastq` is ignored, which you could see in `.gitignore`</br>


* After creating `/original_fastq` folder. You need to put data to the folder. </br>
The original read files are in `local/work` in server. </br>
The following command is let `FastqExamples.tar.gz` in `local/work` folder decompress into `original_fastq` folder</br>
```
tar -zxvf FastqExamples.tar.gz -C /homes/hong.yang/Project-Data-Science-in-Bioinformatics-/original_fastq/
```
##### Decompression
You need to decompress `fastq.gz` to `fastq`, using `gzip -d RV417002*` command in`original_fastq/FastqExamples` folder.</br>
After decompressing, `.fastq` file is in `Project-Data-Science-in-Bioinformatics-/original_fastq/FastqExample` folder.</br>
The following command is to decompress all `fastq.gz` files in `original_fastq/FastqExamples`.

```
gzip -d RV41702*
```

  
# How to Run

You should use the following steps in`Project-Data-Science-in-Bioinformatics-` folder:
```
bash env.sh
```

```
conda activate pangolin
```

```
python3 main.py
```
Note: `main.py` will generate `midresult`, which is used in pipeline 1. Before you test pipeline 1,  please make sure run main.py firstly.
# Somes Files Explanation
* `/workflow` folder: source code of pipeline 1  (reference-guided assembly pipeline) folder </br>
  * `workflow/snakefile`: this is code of pipeline (reference-guided assembly pipeline), using snakemake to manage.</br>
  * `workflow/envs/mapping.yaml`: is the environment
* `/workflow2` folder: source code of pipeline 2 (de novo assembly pipeline) folder </br>
  * `workflow2/snakefile`: this is code of pipeline (de novo assembly pipeline), using snakemake to manage.</br>
  * `workflow2/envs/mapping.yaml`: is the environment
* `main.py`: link the pipeline 1 and pipeline2, connect snakefile, pangolin，generate midresult and display results. 
* `env.sh` : configuration environment automatically.

# Report
After using, you could see report of `quast`, `pangolin`, `fastqc`
