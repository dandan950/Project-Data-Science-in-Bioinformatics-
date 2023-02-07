#!/bin/bash


echo "befor the install, assume the computer have Miniconda";
source ~/mambaforge/etc/profile.d/conda.sh;
source ~/miniconda3/etc/profile.d/conda.sh;
conda install -n base -c conda-forge mamba -y;
source ~/mambaforge/etc/profile.d/conda.sh;
git clone https://github.com/cov-lineages/pangolin.git;
cd pangolin; 
conda env create -f environment.yml; 
conda activate pangolin;
pip install .;
mamba install -c conda-forge -c bioconda snakemake -y;
mamba install -c conda-forge -c bioconda bwa -y;
