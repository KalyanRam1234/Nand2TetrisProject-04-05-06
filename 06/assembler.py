from table1 import *
class Parser:
    def __init__(self, filename):
        self.filename=str(filename)
        self.comptable=comptable()
        self.desttable=desttable()
        self.jumptable=jumptable()
    def readfile(self):
        file1=open(self.filename, "r")
        file2=open("temp.asm", "w")
        for element in file1.readlines():
            x=""
            if element=="\n": continue
            else:
                for i in range(len(element)):
                    if(element[i]==" "): continue
                    elif element[i]=='/' and element[i+1]=='/': break
                    else: x+=element[i]
                if "\n" not in x :
                    x+="\n"
            file2.writelines(x)
        file1.close()
        file2.close()
    def removespace(self):
        file2=open("temp.asm", "r")
        file1=open("temp1.asm", "w")
        for element in file2.readlines():
            if element!="\n": file1.writelines(element)
        file2.close()
        file1.close()
    def PreDefinedTable(self):
        self.table={'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576}
        for i in range(0,16):
            s="R"+str(i)
            self.table[s]=i
    def AddLabel(self):
        file2=open("temp1.asm", "r")
        count=0
        for element in file2.readlines():
            if "(" in element:
                x=""
                for i in range(len(element)-1):
                    if element[i]=="(" or element[i]==')' : continue
                    x+=element[i]
                self.table[x]=count
            else:    
                count+=1
        file2.close()
    def PrintTable(self): #for testing
        for element in self.table:
            print(element, self.table[element])
    def ReadInstructions(self):
        file1=open("temp1.asm", "r")
        name=self.filename.split(".")
        final=name[0]+".hack"
        file2=open(final,"w")
        n=16
        for element in file1.readlines():
            if '@' in element:
                x=""
                check=True
                for i in range(1,len(element)-1): 
                    x+=element[i]
                    if(ord(element[i])<48 or ord(element[i])>57): check=False
                if x not in self.table and check==False :
                    self.table[x]=n
                    n+=1
                elif check==True:
                    self.table[x]=int(x)
                p=format(self.table[x], "b")
                x=""
                for i in range(0,16-len(p)):
                    x+="0"
                x=x+p+"\n"
                file2.writelines(x)
            elif "=" in element:
                x="111"
                inst=element.split("=")
                k=inst[1].split("\n")
                x+=self.comptable[k[0]]
                x+=self.desttable[inst[0]]
                x+="000\n"
                file2.writelines(x)
            elif ";" in element:
                x="111"
                inst=element.split(";")
                k=inst[1].split("\n")
                x+=self.comptable[inst[0]]
                x+="000"
                x+=self.jumptable[k[0]]+"\n"
                file2.writelines(x)
        file1.close()
        file2.close()
file=str(input())
omg=Parser(file)
omg.readfile()
omg.removespace()
omg.PreDefinedTable()
omg.AddLabel()
omg.ReadInstructions()
#omg.PrintTable()