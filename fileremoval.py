import os
def remove():
    filepath=f"static"
    x=os.listdir(filepath)
    for i in x:
        if ".jpg" in i:
            try:
                os.remove(f"static\{i}") 
            except:
                print("error in removing the files")