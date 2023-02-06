# Project-Data-Science-in-Bioinformatics 

|  Member       | 
|  ----         |
| Ruidan LIU    | 
| Yifei YAO     | 
| Hong YANG     | 
| Chengcheng LI | 


### Two Pipelines

we use `snakemake` to help us to simpllify the progress and use `vscode` to connect the server `c44` .

And we design two pipelines, the following:

- QC and filter low quality read data --> read align-->read sort-->variant calling-->create consensus sequence -->lineage detection

- [x] QC and filter low quality read data
- [x] read align
- [x] read sort
- [x] variant calling
- [x] create consensus sequence 
- [x] lineage detection

- QC and filter low quality read data -->de novo assembly(Fragments -> Contigs -> Scaffolds) -->lineage detection

- [x] QC and filter low quality read data
- [x] de novo assembly(Fragments -> Contigs -> Scaffolds)
- [x] lineage detection


# Pipeline Implement and Explanation

### Tools

conda</br>
snakemake</br>
- fastqc >=0.11.9
- fastp >=0.22.0
- bcftools >=1.9
- samtools >=1.9
- bwa =0.7.17
- picard
- megahit=1.2.9
- ragtag
- quast


### Pipeline Workflow Explanation
Before you use our pipeline, you should create original data folder firstly.

##### Create Original Data Folder

* `Project-Data-Science-in-Bioinformatics-/original_fastq`: original read data(.fastq/.fastq.gz). </br>
But `original_fastq` is ignored, which you could see in `.gitignore`, that means `original_fastq` will be not uploaded to github. As read(.fastq) is too big that it can't be uploaded into github.</br>
The original read files are in `local/work` in server


1.You need to self create `Project-Data-Science-in-Bioinformatics-/original_fastq` folder. And put data to the folder.</br>
```
tar -zxvf FastqExamples.tar.gz -C /homes/hong.yang/Project-Data-Science-in-Bioinformatics-/original_fastq/
```
2.You need to decompress `fastq.gz` to `fastq`, using `gzip -d RV417002*` command in`original_fastq/FastqExamples` folder.</br>
After decompressing, `.fastq` file is in `Project-Data-Science-in-Bioinformatics-/original_fastq/FastqExample` folder.</br>

```
gzip -d RV41702*
```

##### Somes Files Explanation
* `Project-Data-Science-in-Bioinformatics-/workflow` folder: source code folder </br>
  * `workflow/snakefile`: this is code of pipeline, using snakemake to manage.</br>
  * `workflow/envs/mapping.yaml`: is the environment
* `main.py`: connect snakefile, pangolin and display. 
* `env.sh` : configuration environment automatically.
  
# How to Run

You should use the following steps:
```
bash env.sh
```

```
conda activate pangolin
```

```
python3 main.py
```
