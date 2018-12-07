'''
Created on 07-Nov-2018

@author: sankar.biswas
'''
import os
import re

def picking():
    
    file_path = "/Users/sankar.biswas/Desktop/Tasks/Test Files"
    files = []
    file_names = dict()
    file_names_version = dict()
    final_jar = ''
    for i in os.listdir(file_path):
        if os.path.isfile(os.path.join(file_path,i)) and 'spark_app' in i and '.jar' in i:
            file_names[i] = i[7:14]
            file_names_version[i] = re.sub('\W+','',file_names[i])
    final_jar = max(file_names_version, key = file_names_version.get)
    print(final_jar)
        
    
picking()
