# Project-Data-Science-in-Bioinformatics 

|  Member       | 
|  ----         |
| Ruidan LIU    | 
| Yifei YAO     | 
| Hong YANG     | 
| Chengcheng LI | 


Our project will show in 2 parts: pipeline and GUI

### Pipeline

we use `snakemake` to help us to simpllify the progress and use `vscode` to connect the server `c44` .

And Our pipeline design is the following:

- QC and filter low quality read data --> read align-->read sort-->assemble-->variant detection

Now the schedule is the following:

- [x] QC and filter low quality read data
- [x] read align
- [x] read sort
- [ ] assemble
- [ ] variant detection

### GUI

we plan to use a web to show our result

### Contribution

|  Member       | Contribution|
|  ----------   |-------------|
| Ruidan LIU    | read sort (samtools)   |
| Yifei YAO     | read align (bwa)|
| Hong YANG     | QC and filter low quality read data (fastq)|
| Chengcheng LI | assemble |

## Pipeline Implement and Explanation

### Tools

We design to use some biotools to help us to implement the pipeline.

conda</br>
snakemake</br>
- fastqc >=0.11.9
- fastp >=0.22.0
- bcftools >=1.9
- samtools >=1.9
- bwa =0.7.17

### Pipeline Workflow Explanation

##### Read Data Explanation

* `Project-Data-Science-in-Bioinformatics-/original_fastq/FastqExamples`: original read data(.fastq/.fastq.gz). </br>
*But `original_fastq` is ignored, which you could see in `.gitignore`, that means `original_fastq` will be not uploaded to github. As read(.fastq) is too big that it can't be uploaded into github.*</br>
***1.You need to self create `Project-Data-Science-in-Bioinformatics-/original_fastq/FastqExamples` folder.</br>
2.You need to decompress `fastq.gz` to `fastq`, using `gzip -d RV417002*` command in`original_fastq/FastqExamples` folder.</br>
After decompressing, `.fastq` file is in `Project-Data-Science-in-Bioinformatics-/original_fastq/FastqExample` folder.</br>***
```
gzip -d RV417002*
```

* `Project-Data-Science-in-Bioinformatics-/workflow/ref.fasta`:  reference read data, used to align

##### Source Code Explanation
* `Project-Data-Science-in-Bioinformatics-/workflow` folder: source code folder </br>
  * `workflow/snakefile`: this is code of pipeline, using snakemake to manage.</br>
  * `workflow/envs/mapping.yaml`: is the environment

### Some Commands

```
fastqc -o ../../cleaned_fastqc_result/ -t 16 RV417026_S15_L001_R1_001.cleaned.fasq.gz RV417026_S15_L001_R2_001.cleaned.fastq.gz
```

```
fastp -i RV417026_S15_L001_R1_001.fastq.gz -o RV417026_S15_L001_R1_001.cleaned.fasq.gz -I RV417026_S15_L001_R2_001.fastq.gz -O RV417026_S15_L001_R2_001.cleaned.fastq.gz -q 20 -c -y -l 50 -g -p -f 10 -n 5 --adapter_sequence GCGAATTTCGACGATCGTTGCATTAACTCGCGAA --adapter_sequence_r2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
```


## GUI Implement Explanation

# How to Run

use command `snakemake --cores 50 -p -F --use-conda` in `Project-Data-Science-in-Bioinformatics-` folder, not in `Project-Data-Science-in-Bioinformatics-/workflow` folder.

```
snakemake --cores 50 -p -F --use-conda
```

