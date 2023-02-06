import os
import sys
import csv

def pangolinexec(inputfile="", outDirectory="",outputfile=""):
    execstr=""
    if inputfile!="":
        execstr = execstr+"pangolin " + inputfile
        if outputfile!="":
            execstr=execstr + " --outdir " + outDirectory
            if outputfile!="":
                execstr=execstr + " --outfile " + outputfile
    return execstr+"; "

SAMPLES = ["RV417026_S15_L001", "RV417027_S18_L001", "RV417028_S20_L001","RV417029_S19_L001"]

#display results
def final_display():
    #print(" Pangolin don't have B.1.545 from it's lineage list: https://cov-lineages.org/lineage_list.html ")
    print("The following is leneage detection results of using reference-guided assembly pipeline:")
    for i in SAMPLES:
        filename="pipeline_ref_pangolin_report/"+"pangolin_"+i+'.csv'

        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("From ",i,"the lineage is:",row['lineage'])
    print("The following is leneage detection results of using de novo assembly pipeline:")
    for i in SAMPLES:
        filename="pipeline_deNovo_pangolin_report/"+"pangolin_"+i+'.csv'

        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print("From ",i,"the lineage is:",row['lineage'])

#generate midresult
def bwa_index():
    pass
    makefile_str="mkdir midresult;cd midresult;touch ref.amb ref.ann ref.bwt ref.pac ref.sa; cd ..;"
    bwa_str="bwa index -p midresult/ref workflow/ref.fasta;"
    return makefile_str+bwa_str

#run snakemake of first pipeline(use reference-guide assembly)
def run_snakemake():
    envstr="source ~/mambaforge/etc/profile.d/conda.sh;conda activate pangolin;"
    snakemakestr=" snakemake -c10  --use-conda;"
    bwa=bwa_index()
    pangolinstr=""
    for i in SAMPLES:
        pangolinstr+=pangolinexec("pipeline_ref_result/{0}_consensus.fa".format(i),"pipeline_ref_pangolin_report/","pangolin_{0}.csv".format(i))
    condastr="bash -c \" {0} {1} {2} {3}\"".format(envstr,bwa,snakemakestr,pangolinstr)
    print(condastr)
    os.system(condastr)

#run snakemake of second pipeline(use de novo assembly)
def run_snakemake2():
    envstr="source ~/mambaforge/etc/profile.d/conda.sh;conda activate pangolin;"
    snakemakestr=" snakemake -s workflow2/snakefile -c10  --use-conda --jobs 2;"
    bwa=bwa_index()
    pangolinstr=""
    for i in SAMPLES:
        pangolinstr+=pangolinexec("pipeline_deNovo_ragtag_output/scaffold/{0}/ragtag.scaffold.fasta".format(i),"pipeline_deNovo_pangolin_report","pangolin_{0}.csv".format(i))
    condastr="bash -c \" {0} {1} {2} {3}\"".format(envstr,bwa,snakemakestr,pangolinstr)
    print(condastr)
    os.system(condastr)

if __name__ == "__main__":
    run_snakemake()
    run_snakemake2()
    final_display()
