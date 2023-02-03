# here is code for magahit ,assembly
rule all:
    input:        
        directory("megahit_result"),

rule fastp:
    input:
        "original_fastq/FastqExamples/RV417026_S15_L001_R1_001.fastq",
        "original_fastq/FastqExamples/RV417026_S15_L001_R2_001.fastq"
    output:
        "filrered_result/RV417026_S15_L001_R1_001.cleaned.fastq",
        "filrered_result/RV417026_S15_L001_R2_001.cleaned.fastq"
    conda:
        "envs/mapping.yaml"
    shell:
        "fastp -i {input[0]} -o {output[0]} -I {input[1]} -O {output[1]} -q 20 -c -y -l 50 -g -p -f 10 -n 5 --adapter_sequence GCGAATTTCGACGATCGTTGCATTAACTCGCGAA --adapter_sequence_r2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"


rule megahit:
    input:
        "filrered_result/RV417026_S15_L001_R1_001.cleaned.fastq",
        "filrered_result/RV417026_S15_L001_R2_001.cleaned.fastq"
    output:
        directory("megahit_result")
    conda:
        "envs/mapping.yaml"
    shell:
        "megahit -1 {input[0]} -2 {input[1]}  -o {output}"

# rule ragtag_correct:
#     input:
#         "workflow/ref.fasta",
#         "megahit_result/final.contigs.fa"   
#     output:
#         directory("ragtag")
#     conda:
#         "envs/mapping.yaml"
#     shell:
#         "ragtag.py correct {input[0]} {input[1]} -o {output} -t 8"

