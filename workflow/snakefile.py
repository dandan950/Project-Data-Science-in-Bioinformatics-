SAMPLES = ["RV417026_S15_L001_R1_001","RV417026_S15_L001_R2_001"]

rule fastp:
    input:
        "../original_fastq/FastqExamples/RV417026_S15_L001_R1_001.fastq.gz",
        "../original_fastq/FastqExamples/RV417026_S15_L001_R2_001.fastq.gz"
    output:
        "filrered_result/RV417026_S15_L001_R1_001.cleaned.fastq.gz",
        "filrered_result/RV417026_S15_L001_R2_001.cleaned.fastq.gz"
    conda:
        "envs/mapping.yaml"
    shell:
        "fastp -i {input[0]} -o {output[0]} -I {input[1]} -O {output[1]} -q 20 -c -y -l 50 -g -p -f 10 -n 5 --adapter_sequence GCGAATTTCGACGATCGTTGCATTAACTCGCGAA --adapter_sequence_r2 AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"
