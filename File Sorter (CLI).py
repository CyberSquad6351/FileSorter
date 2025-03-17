import os
import shutil

Folders = {
    "Images" : [".png", ".jpg", "jpeg"],
    "Audios" : [".mp3"],
    "Videos" : [".mp4", ".mpeg4", ".3gp", ".avi", ".mkv"],
    "Documents" : [".docx", ".doc", ".xlsx", ".pptx", ".ppsx", ".pptm", ".ppsm", ".pdf", ".rar", ".zip", ".csv", ".txt", ".py"]
}

def Create_Move(Ext, Filename):
    Find = False
    for Folder_Name in Folders:
        if "."+Ext in Folders[Folder_Name]:
            if Folder_Name not in os.listdir(Directory):
                os.mkdir(os.path.join(Directory, Folder_Name))
            shutil.move(os.path.join(Directory, Filename), os.path.join(Directory, Folder_Name))
            Find = True
            break
    if Find!=True:
        if Other_Name not in os.listdir(Directory):
            os.mkdir(os.path.join(Directory, Other_Name))
        shutil.move(os.path.join(Directory, Filename), os.path.join(Directory, Other_Name))

Directory = input("Please Enter The Directory Path Here : ")
Other_Name = "Other Files"
All_Files = os.listdir(Directory)
Length = len(All_Files)
Count = 1

for i in All_Files:
    if os.path.isfile(os.path.join(Directory, i))==True:
        Create_Move(i.split(".")[-1], i)
    print(f"Total Files : {Length} | Moved Files  : {Count} | Left Files {Length-Count}")
    Count+=1