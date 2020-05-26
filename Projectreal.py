from os import system, name
x=""
def exitt():#นอก
    clear()
def eerror():#นอก
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("\t\t\t\t     !!!!!Error Please Check!!!!!\t\t\t\t\t ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
def clear():#นอก
        if name == 'nt': 
            _ = system('cls')  
        else: 
            _ = system('clear')
def eng():#นอก
    item = ['Football ball 1','Football ball 2','Football ball 3','Volleyball ball 1','Volleyball ball 2','Basketball ball 1','Basketball ball 2','Petanque ball']
    lend = []
    exit = 0
    menu = ""
    def cantdeleted():
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("\t\t\t\t  You do not borrow this device.\t\t\t\t   ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def deleted():
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("\t\t\t\tReturned selected sport equipment.\t\t\t ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def eerror():
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("\t\t\t\t     !!!!!Error Please Check!!!!!\t\t\t\t\t ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def borrowed():
        clear()
        print("\n")
        print("{0:=^100}".format(""))
        print("") 
        print("\t\t\t\t You have already borrowed this device\t\t\t\t")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
        addmenu()
    def balance():
        clear()
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("{0:^}{1:^98}{2:^}".format("","Equipment you can borrow",""))
        print("")
        print("{0:=^100}".format(""))
        print("")
        for x in item:
            print("{0:^}{1:^98}{2:^}".format("",x,""))
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def show():
        clear()
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("{0:^}{1:^98}{2:^}".format("","Equipment you borrow",""))
        print("")
        print("{0:=^100}".format(""))
        print("")
        for x in lend:
            print("{0:^}{1:^98}{2:^}".format("",x,""))
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def clear():
        if name == 'nt': 
            _ = system('cls')  
        else: 
            _ = system('clear')      
    def Menu(x): ####################################################หน้าเมนู################################################################
        while(x=="" or x==False):        
            print("{0:=^100}".format(""))
            print("|\t\t\t\t\t\t\t\t\t\t \t \t   |")
            print("|\t\t\t\tSchool sports equipment borrowing system\t\t\t   |")
            print("|\t\t\t\t\t\t\t\t\t\t \t  \t   |")
            print("{0:=^100}".format(""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:^}{1:^98}{2:^}".format("","[ Menu ]"," "))
            print("\t\t\t\t\t(1) Borrow equipment\t\t\t\t\t\t")
            print("\t\t\t\t\t(2) Return equipment\t\t\t\t\t\t")
            print("\t\t\t\t\t(3) Show borrowed equipment\t\t\t\t\t\t")
            print("\t\t\t\t\t(4) Show equipment you can borrow\t\t\t\t\t\t")
            print("\t\t\t\t\t(5) Back to choose language\t\t\t\t\t    ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:=^100}".format(""))
            x = str(input("select:"))
            if(x=="1" or x=="2" or x=="3" or x=="4" or x=="5"):
                clear()
                continue
            else:
                clear()
                eerror()
                x=False
        return x
    def addmenu(): ###########################################เลือกเมนู#############################################
        while True:
            print("\n")
            print("{0:=^100}".format(""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:^}{1:^98}{2:^}".format("","  Borrow Equipment  ",""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t ")
            print("{0:=^100}".format(""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t ")
            print("{0:^}{1:^98}{2:^}".format("","[ Menu ]",""))
            print("\t\t\t\t\t(1) Equipment\t\t\t\t\t   ")
            print("\t\t\t\t\t(2) Back to Main Menu\t\t\t\t\t   ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:=^100}".format(""))
            choose = str(input("Select: "))
            clear()
            if choose == "1":
                print("{0:=^100}".format(""))
                print("")
                print("{0:^}{1:^98}{2:^}".format("","   Sports equipment list ","")) 
                x = 0 
                n = 0 
                for i in item:
                    print("\t\t\t\t\t",x+1,") ",i)
                    x=x+1
                    n=n+1    
                print("{0:^}{1:^102}{2:^8}".format("","(0) Back to Main Menu",""))
                print("")
                print("{0:=^100}".format(""))
                selected = str(input("Select : "))
                clear()
                if selected == "1":
                    if "Football ball 1" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Football ball 1" not in lend:
                        clear()
                        lend.insert(0,'Football ball 1')
                        item.remove('Football ball 1')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Football ball 1 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "2":
                    if "Football ball 2" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Football ball 2" not in lend:
                        clear()
                        lend.insert(1,'Football ball 2')
                        item.remove('Football ball 2')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Football ball 2 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "3":
                    if "Football ball 3" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Football ball 3" not in lend:
                        clear()
                        lend.insert(2,'Football ball 3')
                        item.remove('Football ball 3')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Football ball 3 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "4":
                    if "Volleyball ball 1" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Volleyball ball 1" not in lend:
                        clear()
                        lend.insert(3,'Volleyball ball 1')
                        item.remove('Volleyball ball 1')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Volleyball ball 1 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "5":
                    if "Volleyball ball 2" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Volleyball ball 2" not in lend:
                        clear()
                        lend.insert(4,'Volleyball ball 2')
                        item.remove('Volleyball ball 2')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Volleyball ball 2 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "6":
                    if "Basketball ball 1" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Basketball ball 1" not in lend:
                        clear()
                        lend.insert(5,'Basketball ball 1')
                        item.remove('Basketball ball 1')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Basketball ball 1 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "7":
                    if "Basketball ball 2" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Basketball ball 2" not in lend:
                        clear()
                        lend.insert(6,'Basketball ball 2')
                        item.remove('Basketball ball 2')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Basketball ball 2 has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "8":
                    if "Petanque ball" in lend:
                        clear()
                        borrowed()
                        break
                    elif "Petanque ball" not in lend:
                        clear()
                        lend.insert(7,'Petanque ball')
                        item.remove('Petanque ball')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t  Petanque ball has been borrowed.\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "0":
                    clear()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif choose == "2":
                clear()
                break
            else:
                clear()
                eerror()
                continue    
    def deletemenu():
        while True:
            print("{0:=^100}".format(""))
            print("")
            print("{0:^}{1:^98}{2:^}".format("","Choose the device that you want to return.",""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t ")
            print("{0:=^100}".format(""))
            print("")
            print("\t\t\t\t\t(1) Football ball 1  \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(2) Football ball 2 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(3) Football ball 3 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(4) Volleyball ball 1 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(5) Volleyball ball 2\t\t\t\t\t   ")
            print("\t\t\t\t\t(6) Basketball ball 1 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(7) Basketball ball 2\t\t\t\t\t   ")
            print("\t\t\t\t\t(8) Petanque ball \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(9) Return all equipment \t\t\t\t\t\t   ")
            print("{0:^}{1:^102}{2:^8}".format("","(0) Back to Main Menu",""))
            print(" ")
            print("{0:=^100}".format(""))
            print("")
            print("{0:^}{1:^98}{2:^}".format("","Equipment that you have borrowed",""))
            print("")
            print("{0:=^100}".format(""))
            print("")
            for x in lend:
                print("{0:^}{1:^98}{2:^}".format("",x,""))
            print("")
            print("{0:=^100}".format(""))
            selected = str(input("Select : "))
            clear()
            if selected == "1":
                if "Football ball 1" in lend:
                    clear()
                    lend.remove("Football ball 1")
                    item.insert(0,'Football ball 1')
                    deleted()
                    deletemenu() 
                    break
                elif "Football ball 1" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "2":
                if "Football ball 2" in lend:
                    clear()
                    lend.remove("Football ball 2")
                    item.insert(1,'Football ball 2')
                    deleted()
                    deletemenu()
                    break
                elif "Football ball 2" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "3":
                if "Football ball 3" in lend:
                    clear()
                    lend.remove("Football ball 3")
                    item.insert(2,'Football ball 3')
                    deleted()
                    deletemenu()
                    break
                elif "Football ball 3" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "4":
                if "Volleyball ball 1" in lend:
                    clear()
                    lend.remove("Volleyball ball 1")
                    item.insert(3,'Volleyball ball 1')
                    deleted()
                    deletemenu()
                    break
                elif "Volleyball ball 1" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "5":
                if "Volleyball ball 2" in lend:
                    clear()
                    lend.remove("Volleyball ball 2")
                    item.insert(4,'Volleyball ball 2')
                    deleted()
                    deletemenu()
                    break
                elif "Volleyball ball 2" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "6":
                if "Basketball ball 1" in lend:
                    clear()
                    lend.remove("Basketball ball 1")
                    item.insert(5,'Basketball ball 1')
                    deleted()
                    deletemenu()
                    break
                elif "Basketball ball 1" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "7":
                if "Basketball ball 2" in lend:
                    clear()
                    lend.remove("Basketball ball 2")
                    item.insert(6,'Basketball ball 2')
                    deleted()
                    deletemenu()
                    break
                elif "Basketball ball 2" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "8":
                if "Petanque ball" in lend:
                    clear()
                    lend.remove("Petanque ball")
                    item.insert(7,'Petanque ball')
                    deleted()
                    deletemenu()
                    break
                elif "Petanque ball" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "9":
                lend.clear()
                item.clear()
                item.insert(0,'Football ball 1')
                item.insert(1,'Football ball 2')
                item.insert(2,'Football ball 3')
                item.insert(3,'Volleyball ball 1')
                item.insert(4,'Volleyball ball 2')
                item.insert(5,'Basketball ball 1')
                item.insert(6,'Basketball ball 2')
                item.insert(7,'Petanque ball')
                print("\n")
                print("{0:=^100}".format(""))
                print("")
                print("{0:^}{1:^98}{2:^}".format("","You have returned all equipment.",""))
                print("")
                print("{0:=^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif selected == "0":
                clear()
                break
            else:
                clear()
                eerror()
                continue
    while(exit==0): ###########################################ฟังชั่นเลือกเมนู#############################################
        menu = ""
        menu = str(Menu(menu))
        if(menu=="1"):
            clear()
            addmenu()
        elif(menu=="2"):
            clear()
            deletemenu()
        elif(menu=="3"):
            clear()
            show()
        elif(menu=="4"):
            clear()
            balance()
        elif(menu=="5"):
            clear()
            break
        else :
            eerror()
    #print("\n")
    #print("{0:=^100}".format(""))
    #print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
    #print("\t\t\t  . . . . . . . . . . Thank You. . . . . . . . . . \t\t\t\t   ")
    #print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
    #print("{0:=^100}".format(""))
    #print("\n")
##############################################################################################################################
def thai():#นอก
    item = ['ลูกฟุตบอล 1','ลูกฟุตบอล 2','ลูกฟุตบอล 3','ลูกวอลเลย์บอล 1','ลูกวอลเลย์บอล 2','ลูกบาสเกตบอล 1','ลูกบาสเกตบอล 2','ลูกเปตอง']
    lend = []
    exit = 0
    menu = ""
    def cantdeleted():
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("\t\t\t\t\tคุณไม่ได้ยืมอุปกรณ์นี้.\t\t\t\t   ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def deleted():
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("  \t\t\t\tคืนอุปกรณ์ กีฬาที่เลือกแล้ว.\t\t\t ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def eerror():
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("\t\t\t\t!!!!!มีข้อผิดพลาด กรุณาตรวจสอบความถูกต้อง\t\t\t\t\t ")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def borrowed():
        clear()
        print("\n")
        print("{0:=^100}".format(""))
        print("") 
        print("  \t\t\t\t\tคุณได้ยืมอุปกรณ์ นี้แล้ว\t\t\t\t")
        print("")
        print("{0:=^100}".format(""))
        print("\n")
        addmenu()
    def balance():
        clear()
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("{0:^}{1:^98}{2:^}".format("","อุปกรณ์ ที่คุณสามารถยืมได้",""))
        print("")
        print("{0:=^100}".format(""))
        print("")
        for x in item:
            print("{0:^}{1:^98}{2:^}".format("",x,""))
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def show():
        clear()
        print("\n")
        print("{0:=^100}".format(""))
        print("")
        print("{0:^}{1:^98}{2:^}".format("","อุปกรณ์ ที่คุณยืม",""))
        print("")
        print("{0:=^100}".format(""))
        print("")
        for x in lend:
            print("{0:^}{1:^98}{2:^}".format("",x,""))
        print("")
        print("{0:=^100}".format(""))
        print("\n")
    def clear():
        if name == 'nt': 
            _ = system('cls')  
        else: 
            _ = system('clear') 
    def Menu(x): ####################################################หน้าเมนู################################################################
        while(x=="" or x==False):        
            print("{0:=^100}".format(""))
            print("|\t\t\t\t\t\t\t\t\t\t \t \t   |")
            print("|\t\t\t\t\tระบบยืมอุปกรณ์ กีฬาภายในโรงเรียน\t\t\t\t|")
            print("|\t\t\t\t\t\t\t\t\t\t \t  \t   |")
            print("{0:=^100}".format(""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:^}{1:^98}{2:^}".format("","[ เมนู ]"," "))
            print("\t\t\t\t\t(1) เมนูยืมอุปกรณ์\t\t\t\t\t\t")
            print("\t\t\t\t\t(2) เมนูคืนอุปกรณ์\t\t\t\t\t\t")
            print("\t\t\t\t\t(3) แสดงอุปกรณ์ ที่ยืม\t\t\t\t\t\t")
            print("\t\t\t\t\t(4) แสดงอุปกรณ์คงเหลือ\t\t\t\t\t\t")
            print("\t\t\t\t\t(5) กลับไปหน้าเลือกภาษา\t\t\t\t\t    ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:=^100}".format(""))
            x = str(input("เลือกเมนู:"))
            if(x=="1" or x=="2" or x=="3" or x=="4" or x=="5"):
                clear()
                continue
            else:
                clear()
                eerror()
                x=False
        return x
    def addmenu(): ###########################################เลือกเมนู#############################################
        while True:
            print("\n")
            print("{0:=^100}".format(""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:^}{1:^98}{2:^}".format("","  เมนูยืมอุปกรณ์  ",""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t ")
            print("{0:=^100}".format(""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t ")
            print("{0:^}{1:^98}{2:^}".format("","[ ตัวเลือก ]",""))
            print("\t\t\t\t\t(1) เลือกอุปกรณ์\t\t\t\t\t   ")
            print("\t\t\t\t\t(2) กลับหน้าเมนูหลัก\t\t\t\t\t   ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
            print("{0:=^100}".format(""))
            choose = str(input("เลือกฟังชั่น: "))
            clear()
            if choose == "1":
                print("{0:=^100}".format(""))
                print("")
                print("{0:^}{1:^98}{2:^}".format("","   รายการอุปกรณ์ กีฬา ","")) 
                x = 0 
                n = 0 
                for i in item:
                    print("\t\t\t\t\t",x+1,") ",i)
                    x=x+1
                    n=n+1
                print("{0:^}{1:^102}{2:^8}".format("","(0) กลับไปที่เมนูหลัก",""))
                print("")
                print("{0:=^100}".format(""))
                selected = str(input("เลือกอุปกรณ์ ที่ต้องการยืม : "))
                clear()
                if selected == "1":
                    if "ลูกฟุตบอล 1" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกฟุตบอล 1" not in lend:
                        clear()
                        lend.insert(0,'ลูกฟุตบอล 1')
                        item.remove('ลูกฟุตบอล 1')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกฟุตบอล 1 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "2":
                    if "ลูกฟุตบอล 2" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกฟุตบอล 2" not in lend:
                        clear()
                        lend.insert(1,'ลูกฟุตบอล 2')
                        item.remove('ลูกฟุตบอล 2')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกฟุตบอล 2 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "3":
                    if "ลูกฟุตบอล 3" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกฟุตบอล 3" not in lend:
                        clear()
                        lend.insert(2,'ลูกฟุตบอล 3')
                        item.remove('ลูกฟุตบอล 3')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกฟุตบอล 3 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "4":
                    if "ลูกวอลเลย์บอล 1" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกวอลเลย์บอล 1" not in lend:
                        clear()
                        lend.insert(3,'ลูกวอลเลย์บอล 1')
                        item.remove('ลูกวอลเลย์บอล 1')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกฟุตบอล 1 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "5":
                    if "ลูกวอลเลย์บอล 2" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกวอลเลย์บอล 2" not in lend:
                        clear()
                        lend.insert(4,'ลูกวอลเลย์บอล 2')
                        item.remove('ลูกวอลเลย์บอล 2')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกวอลเลย์บอล 2 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "6":
                    if "ลูกบาสเกตบอล 1" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกบาสเกตบอล 1" not in lend:
                        clear()
                        lend.insert(5,'ลูกบาสเกตบอล 1')
                        item.remove('ลูกบาสเกตบอล 1')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกบาสเกตบอล 1 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "7":
                    if "ลูกบาสเกตบอล 2" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกบาสเกตบอล 2" not in lend:
                        clear()
                        lend.insert(6,'ลูกบาสเกตบอล 2')
                        item.remove('ลูกบาสเกตบอล 2')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกบาสเกตบอล 2 เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "8":
                    if "ลูกเปตอง" in lend:
                        clear()
                        borrowed()
                        break
                    elif "ลูกเปตอง" not in lend:
                        clear()
                        lend.insert(7,'ลูกเปตอง')
                        item.remove('ลูกเปตอง')
                        print("\n")
                        print("{0:=^100}".format(""))
                        print("")
                        print("\t\t\t\t\tยืมลูกเปตอง เรียบร้อย .\t\t\t\t\t   ")
                        print("")
                        print("{0:=^100}".format(""))
                        print("\n")
                        addmenu()
                        break
                    else:
                        clear()
                        eerror()
                        continue
                elif selected == "0":
                    clear()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif choose == "2":
                clear()
                break
            else:
                clear()
                eerror()
                continue    
    def deletemenu():
        while True:
            print("{0:=^100}".format(""))
            print("")
            print("{0:^}{1:^98}{2:^}".format("","เลือกอุปกรณ์ ที่ต้องการคืน",""))
            print("\t\t\t\t\t\t\t\t\t\t\t\t ")
            print("{0:=^100}".format(""))
            print("")
            print("\t\t\t\t\t(1) ลูกฟุตบอล 1 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(2) ลูกฟุตบอล 2 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(3) ลูกฟุตบอล 3 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(4) ลูกวอลเลย์บอล 1 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(5) ลูกวอลเลย์บอล 2\t\t\t\t\t   ")
            print("\t\t\t\t\t(6) ลูกบาสเกตบอล 1 \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(7) ลูกบาสเกตบอล 2\t\t\t\t\t   ")
            print("\t\t\t\t\t(8) ลูกเปตอง \t\t\t\t\t\t   ")
            print("\t\t\t\t\t(9) คืนอุปกรณ์ ทั้งหมด\t\t\t\t  ")
            print("{0:^}{1:^95}{2:^8}".format("","(0) กลับเมนูหลัก",""))
            print(" ")
            print("{0:=^100}".format(""))
            print("")
            print("{0:^}{1:^98}{2:^}".format("","อุปกรณ์ ที่คุณยืม",""))
            print("")
            print("{0:=^100}".format(""))
            print("")
            for x in lend:
                print("{0:^}{1:^98}{2:^}".format("",x,""))
            print("")
            print("{0:=^100}".format(""))
            selected = str(input("เลือกอุปกรณ์ ที่ต้องการคืน : "))
            clear()
            if selected == "1":
                if "ลูกฟุตบอล 1" in lend:
                    clear()
                    lend.remove("ลูกฟุตบอล 1")
                    item.insert(0,'ลูกฟุตบอล 1')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกฟุตบอล 1" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "2":
                if "ลูกฟุตบอล 2" in lend:
                    clear()
                    lend.remove("ลูกฟุตบอล 2")
                    item.insert(1,'ลูกฟุตบอล 2')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกฟุตบอล 2" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "3":
                if "ลูกฟุตบอล 3" in lend:
                    clear()
                    lend.remove("ลูกฟุตบอล 3")
                    item.insert(2,'ลูกฟุตบอล 3')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกฟุตบอล 3" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "4":
                if "ลูกวอลเลย์บอล 1" in lend:
                    clear()
                    lend.remove("ลูกวอลเลย์บอล 1")
                    item.insert(3,'ลูกวอลเลย์บอล 1')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกวอลเลย์บอล 1" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "5":
                if "ลูกวอลเลย์บอล 2" in lend:
                    clear()
                    lend.remove("ลูกวอลเลย์บอล 2")
                    item.insert(4,'ลูกวอลเลย์บอล 2')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกวอลเลย์บอล 2" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "6":
                if "ลูกบาสเกตบอล 1" in lend:
                    clear()
                    lend.remove("ลูกบาสเกตบอล 1")
                    item.insert(5,'ลูกบาสเกตบอล 1')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกบาสเกตบอล 1" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "7":
                if "ลูกบาสเกตบอล 2" in lend:
                    clear()
                    lend.remove("ลูกบาสเกตบอล 2")
                    item.insert(6,'ลูกบาสเกตบอล 2')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกบาสเกตบอล 2" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "8":
                if "ลูกเปตอง" in lend:
                    clear()
                    lend.remove("ลูกเปตอง")
                    item.insert(7,'ลูกเปตอง')
                    deleted()
                    deletemenu()
                    break
                elif "ลูกเปตอง" not in lend:
                    clear()
                    cantdeleted()
                    deletemenu()
                    break
                else:
                    clear()
                    eerror()
                    continue
            elif selected == "9":
                lend.clear()
                item.clear()
                item.insert(0,'ลูกฟุตบอล 1')
                item.insert(1,'ลูกฟุตบอล 2')
                item.insert(2,'ลูกฟุตบอล 3')
                item.insert(3,'ลูกวอลเลย์บอล 1')
                item.insert(4,'ลูกวอลเลย์บอล 2')
                item.insert(5,'ลูกบาสเกตบอล 1')
                item.insert(6,'ลูกบาสเกตบอล 2')
                item.insert(7,'ลูกเปตอง')
                print("\n")
                print("{0:=^100}".format(""))
                print("")
                print("{0:^}{1:^98}{2:^}".format("","คุณได้คืนอุปกรณ์ทั้งหมด",""))
                print("")
                print("{0:=^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif selected == "0":
                clear()
                break
            else:
                clear()
                eerror()
                continue
    while(exit==0): ###########################################ฟังชั่นเลือกเมนู#############################################
        menu = ""
        menu = str(Menu(menu))
        if(menu=="1"):
            clear()
            addmenu()
        elif(menu=="2"):
            clear()
            deletemenu()
        elif(menu=="3"):
            clear()
            show()
        elif(menu=="4"):
            clear()
            balance()
        elif(menu=="5"):
            clear()
            break
        else :
            eerror()
    #print("\n")
    #print("{0:=^100}".format(""))
    #print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
    #print("\t\t\t  . . . . . . . . . . ขอบคุณครับ . . . . . . . . . . \t\t\t\t   ")
    #print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
    #print("{0:=^100}".format(""))
    #print("\n")
##############################################################################################################################    
while(x=="" or x==False):#นอก        
    print("{0:=^100}".format(""))
    print("|\t\t\t\t\t\t\t\t\t\t \t \t   |")
    print("|\t\t\t\t\tPlease select a language.\t\t\t\t   |")
    print("|\t\t\t\t\t\t\t\t\t\t \t  \t   |")
    print("{0:=^100}".format(""))
    print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
    print("{0:^}{1:^98}{2:^}".format("",""," "))
    print("\t\t\t\t\t   (1) English\t\t\t\t\t\t")
    print("\t\t\t\t\t   (2) ภาษาไทย\t\t\t\t\t\t")
    print("\t\t\t\t\t   (0) Exit/ออกจากโปรแกรม\t\t\t\t\t\t")
    print("\t\t\t\t\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t\t\t\t\t    ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
    print("{0:=^100}".format(""))
    l = str(input("select :"))
    if(l=="1"):
        clear()
        eng()
        continue
    elif(l=="2"):
        clear()
        thai()
        continue
    elif(l=="0"):
        clear()
        break
    else :
        clear()
        eerror()
        continue
print("\n")
print("{0:=^100}".format(""))
print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
print("""         **************   ******       ******   *******           ********
         **************   ******       ******     ******         ****** 
             *****        ******       ******      ******        ******
             *****        *******************           **********
             *****        *******************           **********
             *****        *******************        ******    ******
             *****        ******       ******      ******        ******
             *****        ******       ******    ******           *******
             *****        ******       ******   *******            *******
            """)
#print("\t\t\t  . . . . . . . . . . Thank You/ขอบคุณครับ . . . . . . . . . . \t\t\t\t   ")
print("\t\t\t\t\t\t\t\t\t\t\t\t   ")
print("{0:=^100}".format(""))
print("\n")            