#VIT ENTRANCE EXAM PROCESS
print("....VIT COLLEDGE ADMISSION CRITERIA....")
a=input("IF YOU WANT TO TAKE ADMISSION IN VIT , PRESS Y/N ")
if a=="Y" or a=="y":
    print("WELCOME")
else:
    print("OK")
    exit()
 #CRITERIAS FOR ELIGIBILITY
if a=="Y" or a=="y":
    print("CONDITIONS MUST BE FOLLOWED TO GET ADMISSION UG ENGINEERING THROUGH VITEEE.")
b=input("ENTER YOUR 12TH BRANCH....PCM/PCB/PCMB :")
if b=="PCM" or b=="PCB" or b=="PCMB":
    print("ELIGIBLE")
else:
    print("SORRY")
c=int(input("ENTER YOUR 12TH PERCENTAGE:"))
if c>=60:
    print("VALID PERCENT")
else:
    print("SORRY")
d=int(input("ENTER BIRTH YEAR:"))
if d>=2003 and d<=2009:
    print("ELIGIBLE")
else:
    print("SORRY")
    
print("NOW YOU ARE ELIGIBLE TO FILL THE VITEEE APPLICATION FORM")
#BRANCES ONE CAN OPT AFTER THE RESULT DECLARATION
r=int(input("ENTER YOUR VITEEE RANK:"))
if r<=100000:
    print("....VELLORE/CHENNAI/AMRAVATI/BHOPAL IS CALLING YOU....")
else:
    print("....VELLORE/CHENNAI NOT POSSIBLE....")
    print("....ONLY BHOPAL AND AMRAVATI IA CALLING....")
    
