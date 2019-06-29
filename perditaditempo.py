#orologio


n0= " -------  "
n01="|       | "
n02="|       | "
n03="|       | "
n04="|       | "
n05=" -------  "


n1= "  /|    "
n11=" / |    "
n12="/  |    "
n13="   |    "
n14="   |    "
n15="___|___ "

n2= " ------  "
n21="|     /  "
n22="     /   "
n23="    /    "
n24="   /   | "
n25=" ------- "

n3= " ------  "
n31="       | "
n32="       | "
n33="   ----| "
n34="       | "
n35=" ------ "

n4= "    /   "
n41="   /    "
n42="  /     "
n43=" /  |   "
n44="----|-- " 
n45="    |   "

n5= " ------- "
n51="|        "
n52="|______  "
n53="       | "
n54="       | "
n55="-------  "

n6= " ------  "
n61="|        "
n62="|______  " 
n63="|      | "
n64="|      | "
n65="|______| "

n7= " ------- "
n71="      /  "
n72="     /   "
n73="    /    "
n74="   /     "
n75="  /      "

n8= " ------  "
n81="|      | "
n82="|______| "
n83="|      | "
n84="|      | "
n85=" ------  "

n9= " ------  "
n91="|      | "
n92="|______| "
n93="       | "
n94="       | "
n95=" ______| "

np= "  "
np1="  "
np2="| "
np3="  "
np4="| "
np5="  "

riga01=""
riga02=""
riga03=""
riga04=""
riga05=""
riga06=""

decimi=0
timer="00.00"
print(n0+n0+np+n0+n0+"\n"+n01+n01+np1+n01+n01+"\n"+n02+n02+np2+n02+n02+"\n"+n03+n03+np3+n03+n03+"\n"+n04+n04+np4+n04+n04+"\n"+n05+n05+np5+n05+n05+"\n")
while timer!="00:01":
    decimi=decimi+1
    if decimi==10000000:
        decimi=0
        if timer[3:]=="59":
            timer1=int(timer[:2])+1
            timer2=0
            timer=str(timer1)+":"+str(timer2)
        else:
            timer1=timer[:2]
            timer2=(int(timer[3:])+1)
            timer=str(timer1)+":"+str(timer2)
        if len(timer)<5:
            if len(timer[:2])==1:
                timer="0"+timer
            if len(timer[3:])==1:
                timer=timer[:3]+"0"+timer[-1]
        print(timer)   
        
'''
        
        if timer[0]=="0":
            riga01=n0
            riga02=n01
            riga03=n02
            riga04=n03
            riga05=n04
            riga06=n05
        elif timer[0]=="1":
            riga01=n1
            riga02=n11
            riga03=n12
            riga04=n13
            riga05=n14
            riga06=n15
        elif timer[0]=="2":
            riga01=n2
            riga02=n21
            riga03=n22
            riga04=n23
            riga05=n24
            riga06=n25
        elif timer[0]=="3":
            riga01=n3
            riga02=n31
            riga03=n32
            riga04=n33
            riga05=n34
            riga06=n35
        elif timer[0]=="4":
            riga01=n4
            riga02=n41
            riga03=n42
            riga04=n43
            riga05=n44
            riga06=n45
        elif timer[0]=="5":
            riga01=n5
            riga02=n51
            riga03=n52
            riga04=n53
            riga05=n54
            riga06=n55
        elif timer[0]=="6":
            riga01=n6
            riga02=n61
            riga03=n62
            riga04=n63
            riga05=n64
            riga06=n65
        elif timer[0]=="7":
            riga01=n7
            riga02=n71
            riga03=n72
            riga04=n73
            riga05=n74
            riga06=n75
        elif timer[0]=="8":
            riga01=n8
            riga02=n81
            riga03=n82
            riga04=n83
            riga05=n84
            riga06=n85
        elif timer[0]=="9":
            riga01=n9
            riga02=n91
            riga03=n92
            riga04=n93
            riga05=n94
            riga06=n95


        if timer[1]=="0":
            riga01=riga01+n0
            riga02=riga02+n01
            riga03=riga03+n02
            riga04=riga04+n03
            riga05=riga05+n04
            riga06=riga06+n05
        elif timer[1]=="1":
            riga01=riga01+n1
            riga02=riga02+n11
            riga03=riga03+n12
            riga04=riga04+n13
            riga05=riga05+n14
            riga06=riga06+n15
        elif timer[1]=="2":
            riga01=riga01+n2
            riga02=riga02+n21
            riga03=riga03+n22
            riga04=riga04+n23
            riga05=riga05+n24
            riga06=riga06+n25
        elif timer[1]=="3":
            riga01=riga01+n3
            riga02=riga02+n31
            riga03=riga03+n32
            riga04=riga04+n33
            riga05=riga05+n34
            riga06=riga06+n35
        elif timer[1]=="4":
            riga01=riga01+n4
            riga02=riga02+n41
            riga03=riga03+n42
            riga04=riga04+n43
            riga05=riga05+n44
            riga06=riga06+n45
        elif timer[1]=="5":
            riga01=riga01+n5
            riga02=riga02+n51
            riga03=riga03+n52
            riga04=riga04+n53
            riga05=riga05+n54
            riga06=riga06+n55
        elif timer[1]=="6":
            riga01=riga01+n6
            riga02=riga02+n61
            riga03=riga03+n62
            riga04=riga04+n63
            riga05=riga05+n64
            riga06=riga06+n65
        elif timer[1]=="7":
            riga01=riga01+n7
            riga02=riga02+n71
            riga03=riga03+n72
            riga04=riga04+n73
            riga05=riga05+n74
            riga06=riga06+n75
        elif timer[1]=="8":
            riga01=riga01+n8
            riga02=riga02+n81
            riga03=riga03+n82
            riga04=riga04+n83
            riga05=riga05+n84
            riga06=riga06+n85
        elif timer[1]=="9":
            riga01=riga01+n9
            riga02=riga02+n91
            riga03=riga03+n92
            riga04=riga04+n93
            riga05=riga05+n94
            riga06=riga06+n95

        riga01=riga01+np
        riga02=riga02+np1
        riga03=riga03+np2
        riga04=riga04+np3
        riga05=riga05+np4
        riga06=riga06+np5
        
        if timer[3]=="0":
            riga01=riga01+n0
            riga02=riga02+n01
            riga03=riga03+n02
            riga04=riga04+n03
            riga05=riga05+n04
            riga06=riga06+n05
        elif timer[3]=="1":
            riga01=riga01+n1
            riga02=riga02+n11
            riga03=riga03+n12
            riga04=riga04+n13
            riga05=riga05+n14
            riga06=riga06+n15
        elif timer[3]=="2":
            riga01=riga01+n2
            riga02=riga02+n21
            riga03=riga03+n22
            riga04=riga04+n23
            riga05=riga05+n24
            riga06=riga06+n25
        elif timer[3]=="3":
            riga01=riga01+n3
            riga02=riga02+n31
            riga03=riga03+n32
            riga04=riga04+n33
            riga05=riga05+n34
            riga06=riga06+n35
        elif timer[3]=="4":
            riga01=riga01+n4
            riga02=riga02+n41
            riga03=riga03+n42
            riga04=riga04+n43
            riga05=riga05+n44
            riga06=riga06+n45
        elif timer[3]=="5":
            riga01=riga01+n5
            riga02=riga02+n51
            riga03=riga03+n52
            riga04=riga04+n53
            riga05=riga05+n54
            riga06=riga06+n55
        elif timer[3]=="6":
            riga01=riga01+n6
            riga02=riga02+n61
            riga03=riga03+n62
            riga04=riga04+n63
            riga05=riga05+n64
            riga06=riga06+n65
        elif timer[3]=="7":
            riga01=riga01+n7
            riga02=riga02+n71
            riga03=riga03+n72
            riga04=riga04+n73
            riga05=riga05+n74
            riga06=riga06+n75
        elif timer[3]=="8":
            riga01=riga01+n8
            riga02=riga02+n81
            riga03=riga03+n82
            riga04=riga04+n83
            riga05=riga05+n84
            riga06=riga06+n85
        elif timer[3]=="9":
            riga01=riga01+n9
            riga02=riga02+n91
            riga03=riga03+n92
            riga04=riga04+n93
            riga05=riga05+n94
            riga06=riga06+n95

        if timer[4]=="0":
            riga01=riga01+n0
            riga02=riga02+n01
            riga03=riga03+n02
            riga04=riga04+n03
            riga05=riga05+n04
            riga06=riga06+n05
        elif timer[4]=="1":
            riga01=riga01+n1
            riga02=riga02+n11
            riga03=riga03+n12
            riga04=riga04+n13
            riga05=riga05+n14
            riga06=riga06+n15
        elif timer[4]=="2":
            riga01=riga01+n2
            riga02=riga02+n21
            riga03=riga03+n22
            riga04=riga04+n23
            riga05=riga05+n24
            riga06=riga06+n25
        elif timer[4]=="3":
            riga01=riga01+n3
            riga02=riga02+n31
            riga03=riga03+n32
            riga04=riga04+n33
            riga05=riga05+n34
            riga06=riga06+n35
        elif timer[4]=="4":
            riga01=riga01+n4
            riga02=riga02+n41
            riga03=riga03+n42
            riga04=riga04+n43
            riga05=riga05+n44
            riga06=riga06+n45
        elif timer[4]=="5":
            riga01=riga01+n5
            riga02=riga02+n51
            riga03=riga03+n52
            riga04=riga04+n53
            riga05=riga05+n54
            riga06=riga06+n55
        elif timer[4]=="6":
            riga01=riga01+n6
            riga02=riga02+n61
            riga03=riga03+n62
            riga04=riga04+n63
            riga05=riga05+n64
            riga06=riga06+n65
        elif timer[4]=="7":
            riga01=riga01+n7
            riga02=riga02+n71
            riga03=riga03+n72
            riga04=riga04+n73
            riga05=riga05+n74
            riga06=riga06+n75
        elif timer[4]=="8":
            riga01=riga01+n8
            riga02=riga02+n81
            riga03=riga03+n82
            riga04=riga04+n83
            riga05=riga05+n84
            riga06=riga06+n85
        elif timer[4]=="9":
            riga01=riga01+n9
            riga02=riga02+n91
            riga03=riga03+n92
            riga04=riga04+n93
            riga05=riga05+n94
            riga06=riga06+n95
    print(riga01+"\n"+riga02+"\n"+riga03+"\n"+riga04+"\n"+riga05+"\n"+riga06+"\n") 
'''
