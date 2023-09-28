import os
import shutil, zipfile, re


def unarchive():
    shutil.make_archive("zipped", "zip","C:\\Workspace\\Python course\\unzip_me_for_instructions")
    shutil.unpack_archive("zipped.zip", "", "zip")
    
def readfiles(path):
    result= []
    for folder , sub_folders , files in os.walk(path):
        for f in files:
            
            if f != "Instructions.txt":
                content = open(os.path.join(os.getcwd(), folder, f))
                result.append(searchpattern(content.read()))
                
    return result

def get_phoneContainedFile(path):
    
    for folder , sub_folders , files in os.walk(path):
        for f in files:
            
            if f != "Instructions.txt":
                content = open(os.path.join(os.getcwd(), folder, f))
                if searchpattern(content.read()):
                    return os.path.join(os.getcwd(), folder, f)
                
                
                       
def searchpattern(text):
    number= re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    if number.search(text):
        return number.search(text)
    else:
        return ''
    
def display_result(file_name):
    result_list = readfiles(file_name)
    for match in result_list:
        if match != '':
            print("The phone number" , match.group() ,  " is found at the position ",  match.span(), "in the file ", get_phoneContainedFile(file_name))

    
    
              
file_name = "C:\Workspace\Python course\extracted_content"  
display_result(file_name)   

