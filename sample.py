import os

def get_SAMPLES():
    file = os.popen("ls -l ./original_fastq/FastqExamples/*.fastq|awk -F' ' '{print $9}'").read()
    SAMPLES=[]

    for item in file.split('\n')[0:-1]:
        i=item.split('/')
        if len(i)>=3:
            file_name=i[3]
            index=file_name.index('_R')
            sample=file_name[:index]

            if sample not in SAMPLES:
                SAMPLES.append(sample)

    return SAMPLES
