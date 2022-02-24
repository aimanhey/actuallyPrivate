import os
import pandas as pd
import numpy as np
import datetime


num = input ("Isikan sesuatu :")
print('Sebentar')
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith('.pdf')]

print(files)

current_dir =os.getcwd()
jsonl_dir_path=os.path.join(current_dir, 'jsonl')
os.mkdir(jsonl_dir_path)

template = '{"document": {"input_config": {"gcs_source": {"input_uris": [ "%s" ]}}}}'

# helper function to get the file name without the .pdf part and the folder path
def getName(filepath):
    index = filepath.rfind('/')
    return filepath[index:-4]
    
index = 0


files_modified=['gs://supplier_invoice/pdfFolder/'+s  for s in files]

print(files_modified)

mylist=files_modified

for filepath in mylist:
    todump = template % filepath
    # this will put all your JSONL files in a folder "JSONL" and the file names will be 
    with open("jsonl" +getName(filepath) + '.jsonl', 'w', encoding='utf-8') as f:
        f.write(todump + '\n')
    index += 1
print(("wrote {} JSONL documents!").format(index))


files_jsonl = [f for f in os.listdir('./jsonl') ]


files_modified_1=['gs://supplier_invoice/jsonl/'+s  for s in files_jsonl]

series_1=[]
i=0
while i < len(files_modified_1):
    series_1.append(np.nan)
    i+=1



print(files_modified_1)
print(series_1)

kek=pd.DataFrame(files_modified_1,series_1)
print(kek)
x = datetime.datetime.now()
print(x.strftime("%d-%B-%Y %I:%M %p"))
y=x.strftime("%d-%B-%Y")
kek.to_csv('{}.csv'.format(str(y)),header=False)


