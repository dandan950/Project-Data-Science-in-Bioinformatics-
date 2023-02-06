import os
import sys
def pangolinexec(inputfile="", outputfile=""):
    execstr=""
    if inputfile!="":
        execstr = execstr+"pangolin " + inputfile
        if outputfile!="":
            execstr=execstr + " --outfile " + outputfile
    return execstr+"; "
SAMPLES = ["RV417026_S15_L001", "RV417027_S18_L001", "RV417028_S20_L001","RV417029_S19_L001"]

def bwa_index():
    pass
    makefile_str="mkdir midresult;cd midresult;touch ref.amb ref.ann ref.bwt ref.pac ref.sa; cd ..;"
    bwa_str="bwa index -p midresult/ref workflow/ref.fasta;"
    return makefile_str+bwa_str


def run_snakemake():
    envstr="source ~/mambaforge/etc/profile.d/conda.sh;conda activate pangolin;"
    snakemakestr=" snakemake -c10  --use-conda;"
    bwa=bwa_index()
    pangolinstr=""
    for i in SAMPLES:
        pangolinstr+=pangolinexec("result/{0}_consensus.fa".format(i),"result/{0}.csv".format(i))
    condastr="bash -c \" {0} {1} {2} {3}\"".format(envstr,bwa,snakemakestr,pangolinstr)
    print(condastr)
    os.system(condastr)

if __name__ == "__main__":
    run_snakemake()
