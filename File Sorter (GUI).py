import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Sorter:
    #=====Interface=====#
    def __init__(self, root):
        self.root = root
        self.root.title("Files Sorter")
        self.root.geometry("1350x705+8+0")
        self.root.resizable(False, False)
        self.root.config(background="white")
        PIcon = PhotoImage(file="Assets/Anonymous.png")
        self.root.iconphoto(False, PIcon)

        self.Logo_Icon = PhotoImage(file="Assets/Logo.png")
        Title = Label(self.root, text="Files Sorting Application", image=self.Logo_Icon, compound=LEFT, font=("times new roman", 45, "bold"), bg="#023548", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1)

        #====Extensions & Variables ====#
        Style = ttk.Style()
        Style.map("TCombobox", selectbackground=[("readonly", "")])
        Style.map("TCombobox", selectforeground=[("readonly", "black")])
        Style.map("TCombobox", fieldbackgorund=[("readonly", "blue")])
       
        self.Image_Extensions = ["Image Extensions", ".png", ".jpg", "jpeg"]
        self.Audio_Extensions = ["Audio Extensions", ".mp3"]
        self.Video_Extensions = ["Video Extensions", ".mp4", ".mpeg4", ".3gp", ".avi", ".mkv"]
        self.Document_Extensions = ["Document Extensions", ".docx", ".doc", ".xlsx", ".pptx", ".ppsx", ".pptm", ".ppsm", ".pdf", ".rar", ".zip", ".csv", ".txt", ".py"]

        self.Folders = {
            "Images" : self.Image_Extensions,
            "Audios" : self.Audio_Extensions,
            "Videos" : self.Video_Extensions,
            "Documents" : self.Document_Extensions
        }
    
        self.Images_Icon = PhotoImage(file="Assets/Images.png")
        self.Audios_Icon = PhotoImage(file="Assets/Audios.png")
        self.Videos_Icon = PhotoImage(file="Assets/Videos.png")
        self.Docs_Icon = PhotoImage(file="Assets/Documents.png")
        self.OtherDocs_Icon = PhotoImage(file="Assets/Other Files.png")

        self.Var_FolderName = StringVar()

        #====Section 1====#
        Lbl_Select_Folder = Label(self.root, text="Select Folder : ", font=("times new roman", 25, "bold"), bg="white", fg="black").place(x=50, y=120)
        Txt_Select_Folder = Entry(self.root, textvariable=self.Var_FolderName, font=("times new roman", 15), bg="white", state="readonly", fg="black").place(x=270, y=120, width=860, height=45)
        Btn_Browse = Button(self.root, text="Browse", font=("times new roman", 15, "bold"), bg="#262626", fg="white", cursor="hand2", command=self.Browse_DIR).place(x=1150, y=120, height=45, width=150)
        HR = Label(self.root, bg="lightgray").place(x=50, y=190, height=2,width=1250)

        #====Section 2====#
        Lbl_Support_Ext = Label(self.root, text="Various Supported Extensions", font=("times new roman", 25), bg="white", fg="black").place(x=50, y=200)
        self.Img_Box = ttk.Combobox(self.root, font=("times new roman", 15), values=self.Image_Extensions, state="readonly", justify="center")
        self.Img_Box.place(x=50, y=260, width=270, height=30)
        self.Img_Box.current(0)
        
        self.Audio_Box = ttk.Combobox(self.root, font=("times new roman", 15), values=self.Audio_Extensions, state="readonly", justify="center")
        self.Audio_Box.place(x=377, y=260, width=270, height=30)
        self.Audio_Box.current(0)

        self.Video_Box = ttk.Combobox(self.root, font=("times new roman", 15), values=self.Video_Extensions, state="readonly", justify="center")
        self.Video_Box.place(x=702, y=260, width=270, height=30)
        self.Video_Box.current(0)
        
        self.Document_Box = ttk.Combobox(self.root, font=("times new roman", 15), values=self.Document_Extensions, state="readonly", justify="center")
        self.Document_Box.place(x=1029, y=260, width=270, height=30)
        self.Document_Box.current(0)        

        #====Section 3====#
        Frame1 = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Frame1.place(x=50, y=310, width=1250, height=280)
        self.Lbl_Total_Files = Label(Frame1, text="Total Files : ", font=("times new roman", 20), bg="white", fg="black")
        self.Lbl_Total_Files.place(x=10, y=10)

        self.Lbl_Total_Images = Label(Frame1, image=self.Images_Icon, compound=TOP, font=("times new roman", 18, "bold"), bg="#0875B7", fg="white", relief=RIDGE, bd=5)
        self.Lbl_Total_Images.place(x=10, y=50, width=200, height=200)

        self.Lbl_Total_Audios = Label(Frame1, image=self.Audios_Icon, compound=TOP, font=("times new roman", 18, "bold"), bg="#008EA4", fg="white", relief=RIDGE, bd=5)
        self.Lbl_Total_Audios.place(x=266, y=50, width=200, height=200)

        self.Lbl_Total_Videos = Label(Frame1, image=self.Videos_Icon, compound=TOP, font=("times new roman", 18, "bold"), bg="#DF002A", fg="white", relief=RIDGE, bd=5)
        self.Lbl_Total_Videos.place(x=522, y=50, width=200, height=200)

        self.Lbl_Total_Docs = Label(Frame1, image=self.Docs_Icon, compound=TOP, font=("times new roman", 18, "bold"), bg="#008EA4", fg="white", relief=RIDGE, bd=5)
        self.Lbl_Total_Docs.place(x=778, y=50, width=200, height=200)

        self.Lbl_Other_Docs = Label(Frame1, image=self.OtherDocs_Icon, compound=TOP, font=("times new roman", 18, "bold"), bg="Gray", fg="white", relief=RIDGE, bd=5)
        self.Lbl_Other_Docs.place(x=1034, y=50, width=200, height=200)

        #====Section 4====#
        self.Lbl_Status = Label(self.root, text="", font=("times new roman", 20), bg="white", fg="black")
        self.Lbl_Status.place(x=50, y=620)
        self.Lbl_Total = Label(self.root, text="", font=("times new roman", 20), bg="white", fg="black")
        self.Lbl_Total.place(x=310, y=620)
        self.Lbl_Moved = Label(self.root, text="", font=("times new roman", 20), bg="white", fg="black")
        self.Lbl_Moved.place(x=500, y=620)
        self.Lbl_Left = Label(self.root, text="", font=("times new roman", 20), bg="white", fg="black")
        self.Lbl_Left.place(x=700, y=620)

        self.Btn_Start = Button(self.root, text="Start", font=("times new roman", 15), bg="#FF5722", fg="white", activebackground="#FF5722", activeforeground="white", cursor="hand2", state=DISABLED, command=self.Start_Function)
        self.Btn_Start.place(x=880, y=614, height=45, width=200)
        self.Btn_Clear = Button(self.root, text="Clear", font=("times new roman", 15), bg="#607D8B", fg="white", activebackground="#607D8B", activeforeground="white", cursor="hand2", command=self.Clear)
        self.Btn_Clear.place(x=1100, y=614, height=45, width=200)

    #=====Backend=====#

    def Total_Counts(self):
        Images = 0
        Audios  = 0
        Videos = 0
        Documents = 0
        Others = 0
        self.Count = 0
        Combine_List = []

        for i in self.All_Files:
            if os.path.isfile(os.path.join(self.Directory,i))==True:
                self.Count+=1
                Ext = "."+i.split(".")[-1]
                for Folder_Name in self.Folders.items():
                    for x in Folder_Name[1]:
                        Combine_List.append(x)
                    if Ext.lower() in Folder_Name[1] and Folder_Name[0]=="Images":
                        Images+=1
                    if Ext.lower() in Folder_Name[1] and Folder_Name[0]=="Audios":
                        Audios+=1
                    if Ext.lower() in Folder_Name[1] and Folder_Name[0]=="Videos":
                        Videos+=1
                    if Ext.lower() in Folder_Name[1] and Folder_Name[0]=="Documents":
                        Documents+=1

        for i in self.All_Files:
            if os.path.isfile(os.path.join(self.Directory,i))==True:
                Ext = "."+i.split(".")[-1]
                if Ext.lower() not in Combine_List:
                    Others+=1

        self.Lbl_Total_Images.config(text="Total Images\n"+str(Images))
        self.Lbl_Total_Audios.config(text="Total Audios\n"+str(Audios))
        self.Lbl_Total_Videos.config(text="Total Videos\n"+str(Videos))
        self.Lbl_Total_Docs.config(text="Total Documents\n"+str(Documents))
        self.Lbl_Other_Docs.config(text="Other Files\n"+str(Others))
        self.Lbl_Total_Files.config(text="Total Files : "+str(self.Count))

    def Browse_DIR(self):
        AskDIR = filedialog.askdirectory(title="Select Directory For Sorting")
        
        if AskDIR!=None:
            self.Var_FolderName.set(str(AskDIR))

            self.Directory = self.Var_FolderName.get()
            self.Other_Name = "Other Files"
            self.All_Files = os.listdir(self.Directory)
            Length = len(self.All_Files)
            Count = 1
            self.Total_Counts()
            self.Btn_Start.config(state=NORMAL)

    def Start_Function(self):
        if self.Var_FolderName.get()!="":
            self.Lbl_Status.config(text="Status")
            self.Btn_Clear.config(state=DISABLED)
            C=0
            for i in self.All_Files:
                    if os.path.isfile(os.path.join(self.Directory, i))==True:
                        C+=1
                        self.Create_Move(i.split(".")[-1], i)
                        self.Lbl_Total.config(text="Total : "+str(self.Count))
                        self.Lbl_Moved.config(text="Moved : "+str(C))
                        self.Lbl_Left.config(text="Left : "+str(self.Count-C))
                        self.Lbl_Total.update()
                        self.Lbl_Moved.update()
                        self.Lbl_Left.update()
            messagebox.showinfo("Success", "Your Files Sorted Successfully !")
            self.Btn_Start.config(state=DISABLED)
            self.Btn_Clear.config(state=NORMAL)
        else:
            messagebox.showerror("Error", "Please Select Directory Before Sorting Files !")

    def Create_Move(self, Ext, Filename):
        Find = False
        for Folder_Name in self.Folders:
            if "."+Ext in self.Folders[Folder_Name]:
                if Folder_Name not in os.listdir(self.Directory):
                    os.mkdir(os.path.join(self.Directory, Folder_Name))
                shutil.move(os.path.join(self.Directory, Filename), os.path.join(self.Directory, Folder_Name))
                Find = True
                break
        if Find!=True:
            if self.Other_Name not in os.listdir(self.Directory):
                os.mkdir(os.path.join(self.Directory, self.Other_Name))
            shutil.move(os.path.join(self.Directory, Filename), os.path.join(self.Directory, self.Other_Name))

    def Clear(self):
        self.Btn_Start.config(state=DISABLED)
        self.Var_FolderName.set("")
        self.Lbl_Total.config(text="")
        self.Lbl_Moved.config(text="")
        self.Lbl_Left.config(text="")
        self.Lbl_Total_Images.config(text="")
        self.Lbl_Total_Audios.config(text="")
        self.Lbl_Total_Videos.config(text="")
        self.Lbl_Total_Docs.config(text="")
        self.Lbl_Other_Docs.config(text="")
        self.Lbl_Total_Files.config(text="Total Files : ")
        self.Lbl_Status.config(text="")

root = Tk()
Window = Sorter(root)
root.mainloop()