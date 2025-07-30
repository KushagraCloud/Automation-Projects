#file organiser from downloads folder 
import os
import shutil

#using decorator
def decorate(fx):
    def mfx():
        print("Script is Running")
        fx()
        print("Script completed")
    return mfx 
@decorate   

#main script

def script():
    realpath=input("Enter the folder name to sort [Use uppercase if any]:\n")
    
    if not realpath:
        print("Folder name not provided.\nTip: ENTER THE EXACT SAME NAME OF FOLDER THAT EXISTS in your Home directory.")
        return
    
    downloadpath=os.path.join(os.path.expanduser("~"), realpath)
    if not os.path.exists(downloadpath):
        print(f" The folder '{realpath}' does not exist in your home directory.")
        return
   
    try:    
        os.chdir(downloadpath)
        files = os.listdir()
        if not files:
            print("Downloads folder is already empty.")
            
        
        else :
            for file in files:
                if os.path.isdir(file):
                    continue
                
                name, ext=os.path.splitext(file)    
                if file.endswith((".tar.gz", ".tar.xz", ".tar.bz2", ".tgz")):
                    ext = ".tar.gz"
                        
                elif ext in (".pdf" ,  ".odt", ".xls",".docx",  ".txt"):
                    destination=os.path.join(os.path.expanduser("~"), "Documents")
                            
                elif ext in (".jpg", ".webp", ".png", ".jpeg") :
                    destination=os.path.join(os.path.expanduser("~"), "Pictures")
                    
                elif ext in (".tar", ".zip", ".exe", ".tar.gz", ".tgz", ".gz", ".xz", ".bz2"):
                    destination=os.path.join(os.path.expanduser("~"), "Archives")
                
                elif ext in (".mkv" , ".avi" , ".mov" , ".wmv" , ".flv" , ".webm" , ".mpeg" , ".mpg" , ".3gp"  ,".mts" , ".m2ts",  ".ogv" , ".ts") :
                     destination=os.path.join(os.path.expanduser("~"), "Videos")
                    
                else:
                    continue        
                os.makedirs(destination , exist_ok=True)
                print(f"Moving: {file} → {destination}")
                shutil.move(file, os.path.join(destination, file))   

    except Exception as e:
        print("Some error encountered:", e)

script()
