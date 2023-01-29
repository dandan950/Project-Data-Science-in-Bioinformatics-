# Project-Data-Science-in-Bioinformatics 

## Pipeline

we use snakemake to help us to simpllify the progress and use vscode to connect the server.

And Our pipeline design is the following:

QC and filter low quality read data --> read align-->read sort-->assemble-->variant detection

## Tools

We design to use some biotools to help us to implement the pipeline.

conda 

snakemake

- fastqc =0.11.9
- fastp =0.22.0
- bwa = 0.7.17
- samtools = 1.16.1

## some command

fastqc -o ../../cleaned_fastqc_result/ -t 16 RV417026_S15_L001_R1_001.cleaned.fasq.gz RV417026_S15_L001_R2_001.cleaned.fastq.gz

fastp -i RV417026_S15_L001_R1_001.fastq.gz -o RV417026_S15_L001_R1_001.cleaned.fasq.gz -I RV417026_S15_L001_R2_001.fastq.gz -O RV417026_S15_L001_R2_001.cleaned.fastq.gz -q 20 -c -y -l 50 -g -p -f 10 -n 5 --adapter_sequence GCGAATTTCGACGATCGTTGCATTAACTCGCGAA --adapter_sequence_r2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
