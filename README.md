# User Manual

|  Group1 Member       | 
|  ----         |
| Ruidan LIU    | 
| Yifei YAO     | 
| Hong YANG     | 
| Chengcheng LI | 


### Pipelines Introduction

we use `snakemake` to help us to simpllify the progress and use `SSH` to connect the server `c44` .

The following is the architecture of our project:

- `(pipeline1) Reference-guided assembly pipeline` QC and filter low quality read data --> read align-->read sort-->variant calling-->create consensus sequence -->lineage detection</br>
in `workflow`</br>
    - workflow/snakefile: this is code of pipeline (reference-guided assembly pipeline), using snakemake to manage.</br>
    - workflow/envs/mapping.yaml: is the environment
- `(pipeline2) De novo assembly pipeline` QC and filter low quality read data -->de novo assembly(Fragments -> Contigs -> Scaffolds) --> quast evaluation-->lineage detection</br>
in`workflow2`</br>
    - workflow2/snakefile: this is code of pipeline (de novo assembly pipeline), using snakemake to manage.</br>
    - workflow2/envs/mapping.yaml: is the environment
- `env.sh` : configuration environment automatically and install pangolin, bwa and snakemake automatically.  
- `main.py`: link the pipeline 1 and pipeline2, connect snakefile, pangolin，generate midresult ,which used in pipeline1, and display results. 

Note: branch `de-novo-assembly` is just backup of pipeline 2. 


The following is some tools that we used in the project

|Tools |
|-------|
|mambaforge|
|snakemake|
|python3|
|pip|
|git|
|fastqc >=0.11.9|
| fastp >=0.22.0|
|bcftools >=1.9|
|samtools >=1.9|
| bwa =0.7.17|
| picard|
| megahit=1.2.9|
| ragtag|
| quast|


# Before You Use

Before you use our pipeline, you should create original data folder in our project folder firstly. And put original data into the folder, then decompress gz files(.fastq.gz -> .fastq). The following is more details:

##### Input Data Folder

-  You need to create `/original_fastq/FastqExample` folder in our project, it use to put original read data( only `.fastq` format). Please make sure the folder name is same. </br>
`original_fastq` is ignored, which you could see in `.gitignore`</br>


##### Environments and Software Requirement

You need to install `mambaforge`,`git`,`python3` and `pip` in advance and finish `conda init`.  

Tools| Link|
----|-------|
Mambaforge| https://github.com/conda-forge/miniforge#mambaforge |
git| |
python3| |
pip| |

How to install Mambaforge?
1. download https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh 
2. bash Mambaforge-Linux-X86_64.sh
3. finish the step of `conda init`

Where is Mambaforge Installing path?</br>
  Mambaforge path should in `/homes/{username}/mambaforge/...` directory(`~/mambaforge`). Because we will following this path to call mambaforge in `env.sh`. env.sh will automatically install pangolin, bwa and snakemake. The following code is calling path in env.sh.

```
source ~/mambaforge/etc/profile.d/conda.sh;
```

##### Suggest System

We suggest that run in the `Ubuntu`, Version 16 or newer version.

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
Note: 
* `main.py` will generate `midresult`, which is used in pipeline 1. Before you test pipeline 1,  please make sure run main.py firstly.
* `conda activate pangolin` is not necessary, which is included already in main.py.


# Report
After using, you could see report of `quast`, `pangolin`, `fastqc`
