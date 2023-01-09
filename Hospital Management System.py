

print("<<<<<----- RADIX HEALTHCARE LIMITED ----->>>>>")
print("<<-- Welcome to the Login Page -->>")
from datetime import date
today=date.today()
print(today)
import time
print (time.strftime("%H:%M:%S"))
w="m"
while w=="m":
    print("1- If you are Owner \n2- If you are Doctor/Nurse/Worker \n3- If you are patient \n ")
    specify=int(input("Specify Yourself: "))
    if specify==1: #Owner Portal
        print("<<<<<<<<<<<----------- Welcome to the Owner portal ---------->>>>>>>>>>")
        recO=["9iq1t5","faraz@99"] # first is password and then username
        recT=["8uw2t6","Aneeq@990"]
        nameown=input("Enter UserName: ")
        passown=input("Enter Owner Password: ")
        if [passown,nameown]==recO or [passown,nameown]==recT:
            add=input("Press \n1- To Add/Remove Employee \n2- To View Employee Record \n3-To Search an Employee \n4-Owner's Patient Management Portal \n5-To Calculate Expenditure \n").lower()
            if add=="1":
                adrem=input("What do you want?? r-to remove and a- to add ")
                if adrem=="a":
                    print("You're making changes to the database:")
                    designation=input("Enter designation: Doctor/worker/nurse: >>")
                    ward=input("Enter Ward: >>")
                    Name=input("Enter name: >>")
                    usname=input("Enter username you wanna assign to the employee: >>")
                    password=input("Input password: >>")
                    address=input("Enter the address: ")
                    email=input("Enter email: >>")
                    qualification=input("Enter the qualification : ")
                    montsal=int(input("Enter the monthly salary: >>"))
                    experience=input("Enter the experience in years: ")
                    f=open("1.txt","a")
                    f.write(f"\n{designation},{ward},{Name},{usname},{password},{address},{email},{qualification},{montsal},{experience}")
                    f.close()
                if adrem=="r":
                    un=input("Enter Username of the employee you want to delete : ")
                    pw=input("Enter Password of employee you want to delete : ")
                    f=True
                    with open ("1.txt","r") as file:
                        lines=file.readlines()
                        with open ("1.txt","w") as b:
                            for line in lines:
                                a=line.split(",")
                                if a[3]!=un and a[4]!=pw:
                                    f=True
                                    b.write(line)
                            print("   Employee Deleted!!   ")
            if add=="2":
                import pandas as pd
                pd.set_option('display.expand_frame_repr', False)
                df=pd.read_csv("1.txt")
                print(df)
            if add=="3":
                search="s"
                while search=="s":
                    found=True
                    name=input("Enter The Name of the employee you want to search: ")
                    import pandas as hey
                    hey.set_option('display.expand_frame_repr', False)
                    found=True
                    ca=hey.read_csv("1.txt")
                    prin=ca.loc[ca['NAME']==name]
                    if len(prin)!=0:
                        print(prin)
                    if len(prin)==0:
                        print("User Not Found!")
                    search=input("Press s to search again: ").lower()
            if add=="4":
                patient="y"
                while patient=="y":
                    print("               <<<<<-----   WELCOME TO THE OWNER'S PATIENT MANAGEMENT PORTAL   ----->>>>>")
                    command=input("Press: \n1-To to view current patients \n2-To view Discharged patients \n3-To Add a Patient \n4-To Delete a Patient")
                    if command=="1":
                        import pandas as pd
                        pd.set_option('display.expand_frame_repr', False)
                        df=pd.read_csv("currentpatient.txt")
                        print(df)
                    if command=="2":
                        import pandas as fd
                        fd.set_option('display.expand_frame_repr', False)
                        ff=fd.read_csv("dischargedpatient.txt")
                        print(ff)
                    if command=="3":
                        patnam=input("Enter Patient Name: ")
                        patnum=input("Enter Patient Number: ")
                        patadd=input("Enter Address of Patient: ")
                        patcont=input("Enter Contact Number of Patient or Any Relative: ")
                        patward=input("Enter Patient Ward: ")
                        prevdig=input("Any Previous Disease history: ")
                        smoke=input("Smoking/drinking status: ")
                        diag=input("Current Diagnosis: ")
                        with open ("currentpatient.txt","a") as file:
                            file.write(f"\n{patnam},{patnum},{patadd},{patcont},{patward},{prevdig},{smoke},{diag}")
                    if command=="4":
                        pat=input("Enter Patient Number : ")
                        with open ("currentpatient.txt","r") as file:
                            lines=file.readlines()
                            with open("dischargedpatient.txt","a") as dis:
                                for line in lines:
                                    a=line.split(",")
                                    if a[1]==pat:
                                        dis.writelines(line)
                        f=True
                        with open ("currentpatient.txt","r") as file:
                            lines=file.readlines()
                            with open ("currentpatient.txt","w") as rem:
                                for line in lines:
                                    b=line.split(",")
                                    if b[1]!=pat:
                                        f=True
                                        rem.write(line)
                    patient=input("Do you want to go to OWNER's Patient Portal again?? y/n ")
            if add=="5":
                pf="y"
                while pf=="y":
                    print("                                              <------Hospital Management System----->                       ")
                    print("                                                           Welcome                                           ")
                    print("                                                WELCOME TO PROFIT/LOSS PORTAL                      ")
                    print("                                           These are the Expenditures of our Hospital                        ")
                    print(" Bills\n Doctor Salary\n Maintenance\n Patient's Food\n ")
                    print("Hospital Expenditures")
                                                       #Expenditure
                    #Bills
                    elec_bill=200000
                    gas_bill=120000
                    print(elec_bill)
                    print(gas_bill)
                    total_bill=(gas_bill+elec_bill)
                    print("The Total Bill Of Electricity And Gas is : ",total_bill)
                    #Doctor's Payment
                    print("Our Hospital Have 4 Wards : Oncology ,Surgical, Dengue,  Orthopedic")
                    #Ocology
                    print("In our Ocology Ward,We Have A Doctor and His Secretery")
                    print("In Our Hospital,We have A Best Cancer Specialist Doctor")
                    doctor_salary_o=150000
                    secretery_salary_o=100000
                    print(doctor_salary_o)
                    print(secretery_salary_o)
                    totalsalaryofdoctor_o=(doctor_salary_o+secretery_salary_o)
                    print("Total salary Of Doctor is : ",totalsalaryofdoctor_o)
                    #Surgical
                    print("In our Surgical Ward,We Have A Doctor and His Secretery")
                    print("As,In Most Hospital Doctor Show some kind of carelssness.But Our Doctors Are Well Trained")
                    doctor_salary_s=1000000
                    secretery_salary_s=150000
                    print(doctor_salary_s)
                    print(secretery_salary_s)
                    totalsalaryofdoctor_s=(doctor_salary_s+secretery_salary_s)
                    print("Here the total salary of doctor is :",totalsalaryofdoctor_s)
                    #Dengue
                    print("In our Dengue Ward,We Have A Doctor and His Secretery")
                    print("You get to feel at Home")
                    doctor_salary_d=500000
                    secretery_salary_d=130000
                    print(doctor_salary_d)
                    print(secretery_salary_d)
                    totalsalaryofdoctor_d=(secretery_salary_d+doctor_salary_d)
                    print("It is a little a bit expensive ,So we get income from this ward a little bit more :",totalsalaryofdoctor_d)
                    #Orthopedic
                    print("In our Chrona Ward,We Have A Doctor and His Secretery")
                    print("This disease spread from one patient to other person,but in our hospital we have a trained staff")
                    doctor_salary_or=1000000
                    secretery_salary_or=60000
                    print(doctor_salary_or)
                    print(secretery_salary_or)
                    totalsalaryofdoctor_or=(doctor_salary_or+secretery_salary_or)
                    print("Total Bill is :",totalsalaryofdoctor_or)
                    #Maintenance
                    maintenance=int(input("How Much Money Spend on maintanace per month : "))
                    maintenance_month=maintenance
                    print(maintenance_month)
                    #Patient Food
                    print("Our Hospital System system gives a food to the patient")
                    patientfood=int(input("How Much money Spend On Patient Food : "))
                    patientfoodpermonth=patientfood
                    print(patientfoodpermonth)
                    Total_expenditure=(totalsalaryofdoctor_o+totalsalaryofdoctor_d+totalsalaryofdoctor_s+totalsalaryofdoctor_or+maintenance_month+patientfoodpermonth)
                    print("Our total expenditure is : ", Total_expenditure)
                                                          #Income
                                                        #Denguepatient
                    print("Our Hospital Doctors wll behaved with patient")
                    patientindengueward_d=int(input("How many patient are come in Dengue Ward : "))
                    doctor_fee_d=12000
                    patientbill_d=patientindengueward_d*doctor_fee_d
                    print("The Patient Bill Is About : ",patientbill_d)
                                                             #Ocologypatient
                    print("Our Hospital Doctors wll behaved with patient")
                    patientinocologyward_o=int(input("How many patient are come in Ocology Ward : "))
                    doctor_fee_o=16500
                    patientbill_o=patientinocologyward_o*doctor_fee_o
                    print("The Patient Bill Is About : ",patientbill_o)
                                                            #Surgicalpatient
                    print("Our Hospital Doctors wll behaved with patient")
                    patientinsurgicalward_s=int(input("How many patient are come in surgical Ward : "))
                    doctor_fee_s=20000
                    patientbill_s=patientinsurgicalward_s*doctor_fee_s
                    print("The Patient Bill Is About : ",patientbill_s)
                                                                #Orthopedicpatient
                    print("Our Hospital Doctors wll behaved with patient")
                    patientinorthopedicward_or=int(input("How many patient are come in orthopedic Ward : "))
                    doctor_fee_or=19000
                    patientbill_or=patientinorthopedicward_or*doctor_fee_or
                    print("The Patient Bill Is About : ",patientbill_or)
                    Total_Income=(patientbill_d+patientbill_o+patientbill_s+patientbill_or)
                    print("OK,Now My Total Income Is :", Total_Income)
                    if(Total_Income>Total_expenditure):
                        print("Hurra! My System Is in Profit")
                    elif(Total_Income<Total_expenditure):
                        print("System Is in Loss")
                        print("Take Loan to meet expenses")
                        loanly=input("Sir,Do you want to take loan (y/n) ")
                        if loanly=="n":
                            print("Ok,Sir")
                            print("Now,You Find Difficulty without gettting this")
                        if loanly=="y":
                            Minimum_loan=(Total_expenditure-Total_Income)
                            print("You Should Took a loan of This Amount To Run Your Hospital : ",Minimum_loan)
                            How_Much=int(input("Sir,How much Amount do you want : "))
                            print(How_Much)
                            totalincome=(How_Much+Total_Income)
                            print(totalincome)
                            New_balance=(Total_expenditure-totalincome)
                            print("Sir,Your New Bank Balance Is : ",New_balance)
                            print("Sir,You should return Your Loan withi a amonth",-How_Much)
                            if (totalincome>Total_expenditure):
                                print("TOTAL INCOME IS LESS THAN TOTAL EXPENSES")
                            if (totalincome<Total_expenditure):
                                print("NET INCOME CAN COVER THE EXPENDITURE")
                    elif(Total_Income==Total_expenditure):
                        print("what fine! My System Is not in Profit nor loss")
                    pf=input("Do you again want to go to PROFIT-LOSS page?? y/n")

        else:
            print("Unauthorized Access! ")
            break
        w=input("press 'm' to go to mainpage or q to quit ")
        
    if specify==2: #Employee portal
        print("<<<<<<<<<<---------- WELCOME TO THE EMPLOYEE PORTAL ---------->>>>>>>>>>")
        username=input("Enter Username: ")
        password=input("Enter Password: ")
        import pandas as hy
        hy.set_option('display.expand_frame_repr', False)
        reed=hy.read_csv("1.txt")
        prin=reed.loc[(reed['USERNAME']==username) & (reed['PASSWORD']==password)]
        if len(prin)!=0:
            print(prin)
        if len(prin)==0:
            print("User Not Found!")
        w=input("press 'm' to go to mainpage or q to quit ")
    if specify==3:#Patient portal
        print("<<<<<<<<<<---------- WELCOME TO THE PATIENT PORTAL ---------->>>>>>>>>>")
        patport="y"
        while patport=="y":
            sp=input("Press \nF-To Go to Financial Assistance Form \nP-To get to the Pharmacy Portal \nD-To Go to Dues Calculator ").lower()
            if sp=="f":
                print("<<<<<<<<--------     Welcome To Financial Aid Segment     -------->>>>>>>>                                            ")
                print("                     Fill out the following form in order to get the facility for free treatment                               ")
                print("Following are the conditions to get financial aid:- ")
                print("\n")
                print("1.This aid is only for those who are unable to afford the expenditures for the treatment.\n2.Your monthly income should be less than 50000.")
                print("\n")
                print("If you are suitable for this aid hit YES in following and then form will appear in front of you and  you have to fill out this form.")
                quest=input("Do you want this aid for treatment  yes/no:")
                if quest=="yes":
                    import webbrowser
                    webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSdTXzpXcrbZk6GrbgAXgiQmFQkAhyjyhXK_MLSRCPgthGJXzw/viewform?usp=sf_link")
                if quest=="no":
                    print("Thanks!")
                    
            if sp=="p":
                print("                  ++++++++++++++++ Welcome To Pharmacy +++++++++++++++")
                w="b"
                while w=="b":
                    print("\n\n                 Here are the General prescriptions")
                    emgmed=str(input("\n\n1-Painkiller\n2-Paracitamol\n3-Morphone\n4-Lorazepam\n5-Hydralazine\n6-Fentanyl\n7-Nloxone\n8-Sodium bicarbonate\n9-Vecuronium\n10-Volume Expanders\n11-Monoclonel Antibodies\n12-Cancer Growth Blockers\n13-Anti-Angiogenics\n14-PARP Inhibitors\n15-Dolo650\n16-Surgical Gauze\n17-Alcohal Pads\n18-Surgical Toolkit\n19-Pyodine\n20-Chlorofom\n21-Cotton Rolls\n\nSpecify and Press Enter :"))
                    if emgmed=="1" or emgmed=='painkiller' or emgmed=='Painkiller':
                        painquan=int(input("\n                        Specify the quantity of Painkillers!\n\nSpecify and Press Enter: "))
                        painprc=painquan*25
                        print("                                     \nTotal price for %d Painkillers is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="2" or emgmed=='paracitamol' or emgmed=='Paracitamol':
                        painquan=int(input("\n                        Specify the quantity of Paracitamol!\n\nSpecify and Press Enter: "))
                        painprc=painquan*10
                        print("                                     \nTotal price for %d Paracitamols is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="3" or emgmed=='Morphine' or emgmed=='morphone':
                        painquan=int(input("\n                        Specify the quantity of Morphine!\n\nSpecify and Press Enter: "))
                        painprc=painquan*230
                        print("                                     \nTotal price for %d Morphines is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="4" or emgmed=='lorazepam' or emgmed=='Lorazepam':
                        painquan=int(input("\n                        Specify the quantity of Lorazepam!\n\nSpecify and Press Enter: "))
                        painprc=painquan*300
                        print("                                     \nTotal price for %d Lorazepams is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="5" or emgmed=='hydralazine' or emgmed=='Hydralazine':
                        painquan=int(input("\n                        Specify the quantity of Hydralazine!\n\nSpecify and Press Enter: "))
                        painprc=painquan*190
                        print("                                     \nTotal price for %d Hydralazines is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="6" or emgmed=='Fentanyl' or emgmed=='fentanyl':
                        painquan=int(input("\n                        Specify the quantity of Fentanyl!\n\nSpecify and Press Enter: "))
                        painprc=painquan*200
                        print("                                     \nTotal price for %d Fentanyls is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="7" or emgmed=='nloxone' or emgmed=='Nloxone':
                        painquan=int(input("\n                        Specify the quantity of Nloxone!\n\nSpecify and Press Enter: "))
                        painprc=painquan*215
                        print("                                     \nTotal price for %d Nloxones is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="Sodium bicarbonate" or emgmed=='8' or emgmed=='sodium bicarbonate':
                        painquan=int(input("\n                        Specify the quantity of Sodium Bicarbonate !\n\nSpecify and Press Enter: "))
                        painprc=painquan*70
                        print("                                     \nTotal price for %d Sodium Bicarbonate is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="9" or emgmed=='Vecuronium' or emgmed=='vecuronium':
                        painquan=int(input("\n                        Specify the quantity of Vecuronium!\n\nSpecify and Press Enter: "))
                        painprc=painquan*400
                        print("                                     \nTotal price for %d Vecuroniums is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="10" or emgmed=='volume expanders' or emgmed=='Volume expanders':
                        painquan=int(input("\n                        Specify the quantity of Volume Expanders !\n\nSpecify and Press Enter: "))
                        painprc=painquan*1300
                        print("                                     \nTotal price for %d Volume Expanders is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="11" or emgmed=='monoclonel antibodies' or emgmed=='Monoclonel Antibodies':
                        painquan=int(input("\n                        Specify the quantity of Monoclonel Antibodies!\n\nSpecify and Press Enter: "))
                        painprc=painquan*25000
                        print("                                     \nTotal price for %d Monoclonel Antibodies is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="12" or emgmed=='Cancer Growth Blockers' or emgmed=='cancer growth blockers':
                        painquan=int(input("\n                        Specify the quantity of Cancer Growth Blockers!\n\nSpecify and Press Enter: "))
                        painprc=painquan*40000
                        print("                                     \nTotal price for %d Cancer Growth Blockers is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="13" or emgmed=='Anti-Angiogenics' or emgmed=='anti-angiogenics' or emgmed=='Anti Angiogenics' or emgmed=='anti angiogenics':
                        painquan=int(input("\n                        Specify the quantity of Anti-Angiogenics !\n\nSpecify and Press Enter: "))
                        painprc=painquan*100000
                        print("                                     \nTotal price for %d Anti-Angiogenics is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="14" or emgmed=='PARP Inhibitors' or emgmed=='parp inhibitors':
                        painquan=int(input("\n                        Specify the quantity of PARP Inhibitors !\n\nSpecify and Press Enter: "))
                        painprc=painquan*80000
                        print("                                     \nTotal price for %d PARP Inhibitors is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="15" or emgmed=='Dolo650' or emgmed=='dolo650':
                        painquan=int(input("\n                        Specify the quantity of Dolo 650!\n\nSpecify and Press Enter: "))
                        painprc=painquan*900
                        print("                                     \nTotal price for %d Dolo 650 is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="16" or emgmed=='Surgical Gauze' or emgmed=='surgical gauze':
                        painquan=int(input("\n                        Specify the quantity of surgical gauze!\n\nSpecify and Press Enter: "))
                        painprc=painquan*20
                        print("                                     \nTotal price for %d surgical gauze is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="17" or emgmed=='Alcohal Pads' or emgmed=='alcohol pads':
                        painquan=int(input("\n                        Specify the quantity of Alcohol Pads!\n\nSpecify and Press Enter: "))
                        painprc=painquan*20
                        print("                                     \nTotal price for %d Alcohol Pads is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="18" or emgmed=='Surgical Toolkit' or emgmed=='surgical toolkit':
                        painquan=int(input("\n                        Specify the quantity of Surgical Toolkit!\n\nSpecify and Press Enter: "))
                        painprc=painquan*4000
                        print("                                     \nTotal price for %d Surgical Toolkit is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="19" or emgmed=='Pyodine' or emgmed=='pyodine':
                        painquan=int(input("\n                        Specify the quantity of Pyodine !\n\nSpecify and Press Enter: "))
                        painprc=painquan*100
                        print("                                     \nTotal price for %d Pyodine is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="20" or emgmed=='Chlorofom' or emgmed=='chlorofom':
                        painquan=int(input("\n                        Specify the quantity of Chlorofom !\n\nSpecify and Press Enter: "))
                        painprc=painquan*2500
                        print("                                     \nTotal price for %d Chlorofom is Rs.%d/-"%(painquan,painprc))
                    if emgmed=="21" or emgmed=='Cotton roll' or emgmed=='cotton roll':
                        painquan=int(input("\n                        Specify the quantity of Cotton rolls !\n\nSpecify and Press Enter: "))
                        painprc=painquan*150
                        print("                                     \nTotal price for %d Cotton Rolls is Rs.%d/-"%(painquan,painprc))
                    w=input("press 'm' to go to mainpage or q to quit or b to go to the general precription page: ").lower()
            if sp=="d":
                print("                                         WELCOME TO PATIENT WARD DUES CALCULATION PANEL                                                        ")
                posres='yes'
                negres='no'
                entrui=str(input("DO YOU WANT PRIVATE ROOM (yes/no):\n"))
                if(entrui==negres):
                    print("                                                               WARDS ARE :                                                      ")
                    print("1.DENGUEE")
                    print("2.ONCOLOGY")
                    print("3.SURGICAL")
                    print("4.ORTHOPEDIC")
                    nwards=str(input("FROM WHICH WARD YOUR PATIENT HAVE CONCERN: "))
                    if(nwards=="1")or (nwards=="DENGUEE") or (nwards=="denguee"):
                        print("                ONE NIGHT STAY PER HEAD IN DENGUEE WARD IS 12000                      ")
                        priceofwrd=12000
                        nytes=int(input("HOW MANY NIGHT STAY YOUR DR HAS TOLD YOU?\n"))
                        sumedval=nytes*priceofwrd
                        print("your total bill is",sumedval)
                        print("     THANK YOU FOR CONSULTING PLZ PAY RPS",sumedval)
                    if(nwards=="2")or (nwards=="ONCOLOGY") or (nwards=="oncology"):
                        print("               ONE NIGHT STAY PER HEAD IN ONCOLOGY WARD IS 16500                     ")
                        priceofwrd=15600
                        nytes=int(input("HOW MANY NIGHT STAY YOUR DR HAS TOLD YOU?\n"))
                        sumedval=nytes*priceofwrd
                        print("your total bill is",sumedval)
                        print("     THANK YOU FOR CONSULTING PLZ PAY RPS",sumedval)
                    if(nwards=="3")or (nwards=="SURGICAL") or (nwards=="surgical"):
                        print("               ONE NIGHT STAY PER HEAD IN SURGICAL WARD IS 20000                     ")
                        priceofwrd=20000
                        nytes=int(input("HOW MANY NIGHT STAY YOUR DR HAS TOLD YOU?\n"))
                        sumedval=nytes*priceofwrd
                        print("your total bill is",sumedval)
                        print("     THANK YOU FOR CONSULTING PLZ PAY RPS",sumedval)
                    if(nwards=="4")or (nwards=="ORTHOPEDIC") or (nwards=="orthopedic"):
                        print("               ONE NIGHT STAY PER HEAD IN ORTHOPEDIC WARD IS 19000                   ")
                        priceofwrd=19000
                        nytes=int(input("HOW MANY NIGHT STAY YOUR DR HAS TOLD YOU?\n"))
                        sumedval=nytes*priceofwrd
                        print("your total bill is",sumedval)
                        print("     THANK YOU FOR CONSULTING PLZ PAY RPS",sumedval)

                if(entrui==posres):
                    print("                   ONE NIGHT STAY PER HEAD AT PRIVATE ROOM IS 35000                      ")
                    priceofwrd=35000
                    nytes=int(input("HOW MANY NIGHT STAY YOUR DR HAS TOLD YOU?\n"))
                    hmkk=priceofwrd*nytes
                    print("your total bill is",hmkk)
                    print("                                          THANK YOU FOR CONSULTING PLZ PAY RPS",hmkk                      )
            w=input("Press 'm' To Get to the Main Page and 'p' to Get Back To the Patient Portal")
                                               
            
w="q"
while w=="q":
    print("Greetings!!!")
    print("___Radix Healthcare system____")
    break
            
            

            
        
            
                    


            
    

                
        
    

           
    
        
        
            
        






    
   
        
        
    
    
    
    
