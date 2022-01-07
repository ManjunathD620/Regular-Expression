import random
from tkinter import *

def Validate(str):
    if(str.count("(") == str.count(")")):
        return True
    else:
        return False

def stringGenerator(str,n):
    temp = ""
    for i in range(n):
        temp +=str
    return temp

def shuffleStrings(result):
    res =""
    random.shuffle(result)
    for x in result:
        res +=x
    return res

def plusCheck(str):
    res =[]
    i =0
    old = 0
    str +="+"

    for x in str:
        if(x == "+"): #a+J+L+gg
            if(old==0):
                res.append(str[:i])
            else:
                res.append(str[old+1:i])
            old = i
        i+=1
    temp = []
    random.shuffle(res)
    for i in res:
        temp.append(i)
    # temp.append(shuffleStrings(res))
    return temp #{S,F,SF,FKFF}

def simplifyStrings(str2,n):
    index = 0  #Example :- a+b
    res =[]
    result =""
    str2 +="+" # a+b+
    rdm = random.randint(0,n)
    check = 0 
    if (n==0):
        return ""
    
    elif(str2.find("^*")== -1 and str2.find("(") == -1):
        for x in str2:
            if(x=="+" and str2[:index-1].find("+") == -1):
                if(str2.rfind("+") == -1):
                    result += str2[:index-1]
                result +=str2[:index]
                result += stringGenerator(str2[:index],rdm) #aaaa
                res.append(result)
                result = ""
                check = index
            elif(x == "+"):
                
                result += str2[check+1:index]
                result += stringGenerator(str2[check+1 :index],n-rdm) #bbb
                res.append(result)
                result = ""
                check = index
            
            index +=1

        # res contain -> ["aaaa","bbb"]
    return shuffleStrings(res) # return "aaaabbb" or "bbbaaaa"

def solveRE(re):
    result = []
    tem =0 
    j = 0
    indicate =0
    
    if(re.find(")^*") != -1):
        for i in re:
            if(i=="("):
                if (tem == 0):
                    openRef = j
                else:
                    pass
                tem+=1
            elif(i == ")" and re[j+2]=="*"):
                if(indicate>0):
                    f = re[:openRef].rfind("^*")
                    if(re[f+2] == "+"):
                        temp = re[f+3:openRef]
                    else:
                        temp = re[f+2:openRef]

                    for i in range(5):
                        temp +=simplifyStrings(re[openRef+1:j],i)
                        result[i] += temp
                        if(re[f+2] == "+"):
                            temp = re[f+3:openRef]
                        else:
                            temp = re[f+2:openRef]

                    tem = 0
                    temp = ""
                    
                else:
                    for i in range(5):
                        result.append(simplifyStrings(re[openRef+1:j],i))
                    tem = 0
                    if(re[:openRef] !=""):
                        for x in range(len(result)):
                            result[x] = re[:openRef]+result[x]
                    indicate +=1
            j+=1

        if(re[re.rfind("^*")+2:] != "" ):
            for i in range(len(result)):
                result[i] += re[re.rfind("^*")+2:]
            
        return result
        
    else:

        t = 0
        str = ""

        if(re.find("^*") ==-1 and re.find("+")==-1 and re.find(")")==-1):
            result.append(re)
            return result
        elif(re.find("+") != -1 and re[re.find("+")-1] !="*"):
                return plusCheck(re)

        for i in range(len(re)): # We are replacing * operation
                                # i.e,  1* with (1)^*
            if(re[i] == "*"):
                if (t==0): 
                    str += re[:i+1].replace(f"{re[i-1]}*",f"({re[i-1]})^*")
                    t = i
                elif(re[i+1:].find("*)") == -1):
                    str += re[t+1:i+1].replace(f"{re[i-1]}*",f"({re[i-1]})^*",1)
                    t = i

                else:
                    str += re[t+1:i+1].replace(f"{re[i-1]}*",f"({re[i-1]})^*",1)
                    t = i
            elif(re[i+1:].find("*")== -1):
                str += re[i:]
                break
        return solveRE(str[1:-1])

class Main:
    class Error(Exception):
        pass
    
    def __init__(self):

        win = Tk() #creating the window,Initiallizing the required variables
        win.title("String generator")
        strvar = StringVar(win)
        labelvar = StringVar(win)
        win.geometry("600x300")

        def buttonCall(): #after clicking the generate button this function will execute
            try:
                if(Validate(strvar.get()) == False):
                    raise self.Error
                else:
                    result = solveRE(strvar.get()) #we are passing the Regular expression to solveRe fucntion 
                    # This function will return generated String
                    labelvar.set("\n{"+str(result)[1:-1]+',....'+"}")
                    # here we are setting label value with generated string
            except self.Error:
                labelvar.set("Invalid Regular Expression")
                # here we are setting label value to "invalid" if the given regular expression is invalid 
        Entry(win, width=20, textvariable=strvar).pack(pady=20) # we are adding widgets into main window
        Button(win, text="Generate", command=buttonCall).pack(pady=10)
        Label(win, text="",textvariable=labelvar,font=('Georgia 13')).pack(pady=10)
        win.mainloop()


if __name__ == "__main__":
    Main()


# Example of Regular Expression



# (0*10*)
# (a+b+xw)^*
# (0*1SRT0*Kop*DFH)
# (anz)^*(b)^*
# z(a+b)^*d(p+t)^*--(0+9)^*
# (a+b)^*055(8+9)^*56
# (a+b)^*(7+0)^*
# (0*+10*)
# (G*+1I*)

# (a+b)^*