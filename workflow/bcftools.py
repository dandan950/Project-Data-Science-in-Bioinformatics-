#here is bcftools code

rule sam_sort:
    input:
        "mapped/RV417026_S15_L001_1.bam"
    output:
        "sorted/RV417026_S15_L001.bam"
    conda:
        "envs/mapping.yaml"
    shell:
        "samtools sort {input} -o {output}"

rule sam_index:
    input:
        "sorted/RV417026_S15_L001.bam"
    output:
        "sorted/RV417026_S15_L001.bam.bai"
    conda:
        "envs/mapping.yaml"
    shell:
        "samtools sort {input} -o {output}"

rule mpileup:
    input:
        "sorted/RV417026_S15_L001.bam",
        "workflow/ref.fasta",
    output:
        "sorted/RV417026_S15_L001.bcf",
    conda: 
        "envs/mapping.yaml"
    shell:
        "bcftools mpileup -Ob -o {output} -f {input[1]} {input[0]}"


rule call_variant:
    input:
        "sorted/RV417026_S15_L001.bcf",
    output:
        "result/RV417026_S15_L001.vcf",
    conda:
        "envs/mapping.yaml"
    shell:
        "bcftools call -m -v -Ov -o {output} {input}" 

rule filter_vcf:
    input:
        "result/RV417026_S15_L001.vcf",
    output:
        "result/RV417026_S15_L001_final.vcf",
    conda:
        "envs/mapping.yaml"
    shell:
        "vcfutils.pl varFilter {input} > {output}"

rule vcf_bgzip:
    input:
        "result/RV417026_S15_L001_final.vcf",
    output:
        "result/RV417026_S15_L001_final.vcf.gz",
    conda:
        "envs/mapping.yaml"
    shell:
        "bcftools view {input} -Oz -o {output}"      

# rule vcf_index:
#     input:
#         "result/RV417026_S15_L001_final.vcf.gz",
#     output:
#         "result/RV417026_S15_L001_final.vcf.gz.tbi",
#     conda:
#         "envs/mapping.yaml"
#     shell:
#         "tabix {input} > {output}"
