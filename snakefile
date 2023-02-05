rule all:
    input:        
        directory("quast_report")
        
# rule fastp:
#     input:
#         "original_fastq/FastqExamples/RV417027_S18_L001_R1_001.fastq",
#         "original_fastq/FastqExamples/RV417027_S18_L001_R2_001.fastq"
#     output:
#         "filrered_result/RV417027_S18_L001_R1_001.cleaned.fastq",
#         "filrered_result/RV417027_S18_L001_R2_001.cleaned.fastq"
#     conda:
#         "envs/mapping.yaml"
#     shell:
#         "fastp -i {input[0]} -o {output[0]} -I {input[1]} -O {output[1]} -q 20 -c -y -l 50 -g -p -f 10 -n 5 --adapter_sequence GCGAATTTCGACGATCGTTGCATTAACTCGCGAA --adapter_sequence_r2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"


rule megahit:
    input:
        "filrered_result/RV417027_S18_L001_R1_001.cleaned.fastq",
        "filrered_result/RV417027_S18_L001_R2_001.cleaned.fastq"
    output:
        "megahit_result/final.contigs.fa"
    conda:
        "envs/mapping.yaml"
    shell:
        "megahit -1 {input[0]} -2 {input[1]} -f -o megahit_result"

rule ragtag_correct:
    input:
        "workflow/ref.fasta",
        "megahit_result/final.contigs.fa"   
    output:
         multiext("ragtag_output/ragtag.correct", ".agp", ".asm.paf", ".asm.paf.log", ".err", ".fasta")
    conda:
        "envs/mapping.yaml"
    shell:
        "ragtag.py correct {input[0]} {input[1]}  -t 8"

rule ragtag_scaffold:
    input:
        "workflow/ref.fasta",
        "ragtag_output/ragtag.correct.fasta"       
    output:
        multiext("ragtag_output/ragtag.scaffold", ".agp", ".asm.paf",".confidence.txt", ".asm.paf.log", ".err", ".fasta",".stats")       
    conda:
        "envs/mapping.yaml"
    shell:
        "ragtag.py scaffold {input[0]} {input[1]} -o ragtag_output "


rule quast:
    input:
        "megahit_result/final.contigs.fa",
        "workflow/ref.fasta",
        "original_fastq/FastqExamples/RV417026_S15_L001_R1_001.fastq",
        "original_fastq/FastqExamples/RV417026_S15_L001_R2_001.fastq"
    output:
        directory("quast_report")
    conda:
        "envs/mapping.yaml"
    shell:
        "quast.py -l megahit {input[0]}  -r {input[1]} -1 {input[2]} -2 {input[3]}  --rna-finding  -o {output} -t 4"