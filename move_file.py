import os 
import shutil

from_dir = '/Users/DC/Downloads'
to_dir = '/Users/DC/Downloads/Project 102/documents'
list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    
    name, extension = os.path.splitext(file_name)
    
   
    if extension == "":
        continue  
    

    if extension in ['.txt', '.doc', '.docx', '.pdf']:

        path1 = os.path.join(from_dir, file_name)
     
        path2 = os.path.join(to_dir, "Document_Files")

        path3 = os.path.join(path2, file_name)
        
       
        if not os.path.exists(path2):

            os.makedirs(path2)
            print(f"Creating directory and moving {file_name}")
        else:
            print(f"Moving {file_name}")
        
     
        shutil.move(path1, path3)
