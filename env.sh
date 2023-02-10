#!/bin/bash


echo "befor the install, assume the computer have Mambaforege in the path: ~/mambaforge";
source ~/mambaforge/etc/profile.d/conda.sh;
# automatically install mamba
conda install -n base -c conda-forge mamba -y;
source ~/mambaforge/etc/profile.d/conda.sh;
# automatically install pangolin from github and activate pangolin
git clone https://github.com/cov-lineages/pangolin.git;
cd pangolin; 
conda env create -f environment.yml; 
conda activate pangolin;
# install pangolin
pip install .;
# automatically install snakemake
mamba install -c conda-forge -c bioconda snakemake -y;
# automatically install bwa
mamba install -c conda-forge -c bioconda bwa -y;
