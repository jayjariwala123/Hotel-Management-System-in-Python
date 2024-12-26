import pandas as pd
def menu() :
    print()
    print('******************************')
    print("This is hotel management system project")
    print("1.About the project")
    print("2.Show all customers Details")
    print("3.Add new customer detail")
    print("4.Add new detail with input")
    print("5.Show Details of customer detail with new column name")
    print("6.Sort customer detail by name")
    print("7.Show type of rooms available")
    print("8.Ask customer Choice of room and calculate charges according")
    print("9.Rent increment")
    print("10.List the charges in table laundry")
    print("11.Add detail of items and charges in laundry")
    print("12.Show laundry bill")
    print("13.Delete column address")
    print("14.Show menu of hotel")
    print("15.Add details of food item available in Hotel")
    print("16.Hotel bill")
    print('*****************************************************************************************')
    ch=int(input("Enter a choice from menu"))
    if ch==1 :
        about()
    elif ch==2 :
        no_index()
    elif ch==3 :
        new_customer()
    elif ch==4 :
        new_cust()
    elif ch==5 :
        new_column()
    elif ch==6 :
        sort_customer()
    elif ch==7 :
        show_roomtype()
    elif ch==8 :
        roomrent()
    elif ch==9 :
        rent_int()
    elif ch==10 :
        laundry()
    elif ch==11 :
        add_laundry()
    elif ch==12 :
        lbill()
    elif ch==13 :
        delete_col()
    elif ch==14 :
        show_restaurant()
    elif ch==15 :
        add_resturant()    
    elif ch==16 :
        res_bill()
    else:
        print("invalid option")
                    
def about():
        print(" This project is Developed by Harshit Gahlot on HOTEL MANAGEMENT SYSTEM........it contain 17 option..In this project 4 csv files are used Customers,roomtype,laundry,restaurants")

def no_index():
        print("Display Customer details without index")
        print()
        
        df=pd.read_csv("E:\\customers.csv",index_col=0)
        print(df)
    
def new_customer():
        print("Adding New customer details in file ")
        df=pd.read_csv("E:\\customers.csv")
        df.at['11',:]=['sara','50,karol bagh','8860671794','18-06-2022','22-06-2022','4']
        print(df)
        
def new_cust():
        print("Adding new customer in file")
            
        df=pd.read_csv("E:\\customers.csv", index_col=0)
        print(df)
        
        a=input("Enter the name of the customer=")
        b=input("Enter address=")
        c=int(input("Enter mobile number="))
        d=input("Enter the date of check in=")
        e=input("Enter the date of check out=")
        f=int(input("Enter the duration of stay="))
        df.loc[a]=[b,c,d,e,f]
        print(df)
        
def new_column():
            print("previous column name")
            
            df=pd.read_csv("E:\\customers.csv")
            print(df)
            print()
            print("Display Details of customer with Names")
            
            df=pd.read_csv("E:\\customers.csv",skiprows=1,names=['customer name','Residence','Day of arrival','Day of departure','stay'])
            print(df)
            
def sort_customer():
            print("Sorting customer name and details in ascendeing order")
            df=pd.read_csv("E:\\customers.csv",index_col=0)
            df=df.sort_values("name")
            print(df)
            
def show_roomtype():
            print("show type of room available")
            df=pd.read_csv("E:\\roomtype.csv",index_col=0)
            print("without index")
            print(df)
            
def roomrent():
            print("Room includes:1 double bed,Television,1 double door cupboard,1 coffee table with 2 sofa,bedroom attached washroom with hot/cold water")
            print("************ we have the following room for you:")
            print("1.Single room Rupee 2000 per Night")
            print("2.double room rupee 3000 per Night")
            print("3.Triple room Rupee 4000 per Night")
            print("4.King room rupee 6000 per Night")
            
            x=int(input("Enter your choice Please="))
            n=int(input("For how many night did you stay="))
            if(x==1):
                print("You have chosen single room")
                s=2000*n
            elif x == 2:
                print("You have chosen double room")
                s=3000*n
            elif x == 3:
                print("You chosen triple room")
                s=4000*n
            elif x == 4:
                print("you have chosen king room")
                s=6000*n
            else:
                print("please chosen a room")
            print("Your roomrent is=",s,"\n Thank you visit again")
                                
def rent_int():
            print("previous rent of rooms")
            print()
            df=pd.read_csv("E:\\roomtype.csv",index_col=0)
            print(df)
            print("Increase rent by rs.500")
            print()
            print("current rent of rooms") 
            df['rent']=[2500,3500,4500,6500]
            print(df)
            print()
                            
def laundry():
            df=pd.read_csv("E:\\laundry.csv",index_col=0)
            print()
            print(df)
            
                                
def add_laundry():
            print("Adding new items to be washed in hotel laundry")
            print()
            df=pd.read_csv("E:\\laundry.csv",index_col=0)
            a=int(input("Enter Sno"))
            b=input("Enter the name of the item=")
            c=int(input("Enter rate="))
            df.loc[a]=[b,c]
            print(df)
          
                                
def lbill():
            print("we change the following rate for laundry")
            print("1.shirt Rupees 75 1 piece")
            print("2.Trouser rupee 100 1 piece")
            print("3.Ladies suits rupee 100 1 piece")
            print("4.saree rupee 200 1 piece")
            print("5.Other rupee 200 1 piece")                            
            x=int(input("Enter your choice of cloth please="))
            n=int(input(" How many pieces you want to get washes="))
            if(x==1):
                print("you want to get shirt washed")
                s=75*n
            elif(x==2):
                print("you want to get trouser washed")
                s=100*n
            elif(x==3):
                print("you want to get ladies suit washed")
            elif(x==4):
                print("you want to get saree washed")
                s=200*n
            elif(x==5):
                print("you want to get other cloth washed")
                s=200*n
            else:
                print("Please choose the piece of cloth")
            print("Your laundry charges are =",s,"\n")
                
def delete_col():
            print("Delete column address from customers")
            print()
                                       
            df=pd.read_csv("E:\\customers.csv")
            print(df)
            print()          
            del df['address']
            print(df)
                                    
def show_restaurant():
            
            print('MENU')
            df=pd.read_csv("E:\\Resturant.csv",index_col=0)
            print(df)
            
            
def add_resturant():
            
            print("New dishes are")
            df=pd.read_csv("E:\\Resturant.csv",index_col=0)
            a=int(input("Enter Sno"))
            b=input("Enter the name of the item=")
            c=int(input("Enter rate="))
            df.loc[a]=[b,c]
            print(df)            
                                    
def res_bill():
            
            print("All food item available")
            df=pd.read_csv("E:\\Resturant.csv",index_col=0)
            print(df)                                       
            c=int(input("order Your item no."))
            d=int(input("Enter the quantity"))
                                    
            if(c==1):
                s=int(20*d)
            elif(c==2):
                s=int(10*d)
            elif(c==3):
                s=int(250*d)
            elif(c==4):
                s=int(150*d)
            elif(c==5):
                s=int(75*d)
            elif(c==6):
                s=int(90*d)
            else:
                print("invalid option")
            print("Total Food Bill is Rs=",s,"\n")

                                                                    
            opt=""
            opt=str("Enter your choice=")
            if opt =="1":
                about()
            elif opt =="2":
                no_index()
            elif opt =="3":
                new_customer()
            elif opt =="4":
                new_cust()
            elif opt =="5":
                new_column()
            elif opt =="6":
                sort_customer()
            elif opt =="7":
                show_roomtype()
            elif opt =="8":
                roomrent()
            elif opt =="9":
                rent_int()
            elif opt =="10":
                laundry()
            elif opt =="11":
                add_laundry()
            elif opt =="12":
                lbill()
            elif opt =="13":
                delete_col()
            elif opt =="14":
                show_resturant()
            elif opt =="15":
                add_resturant()
            elif opt =="16":
                res_bill()
            
import winsound
winsound.Beep(1000,500)
ch= True
while (ch is  True):
    about()
    menu()
    ch=False
    
    
                                                                        
                                        
                                        
                            
                                            
                            
        