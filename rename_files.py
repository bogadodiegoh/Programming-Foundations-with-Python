import os
def rename_files():
    file_list = os.listdir(r"carpeta_de_imagenes")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Workin Directory is " + saved_path)
    os.chdir(r"carpeta_de_imagenes")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(str.maketrans('','','0123456789')))
    os.chdir(saved_path)
    
rename_files()    
