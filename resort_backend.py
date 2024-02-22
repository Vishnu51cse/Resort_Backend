import mysql.connector
from mysql.connector import Error
try:
    con =mysql.connector.connect(host='localhost',user='root',password='vishnu',database='residence')
    if con.is_connected():
        db_Info = con.get_server_info()
        cursor=con.cursor()
     print("Welcome to the Programmers residency")
     def confirm():
        print("Have you Already Booked your  room")
        wel=input("Enter Yes\  No:")
        wel1=wel.lower()
        if wel1== "yes":
            choice()
        else:   
            print("Please login ")
            login()
            choice()

#Entering login details
    def login():
        name=input("Enter name :")
        country=input("Enter country(in double quotes)  :")
        if  len(country)!=0:
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into info values ('"+str(name)+"',"+str(country)+");")
            cursor.execute(insert_values1)
            con.commit()
        else:
            print("Enter country properly!!")
            login()
#Entering room booking details
    def room():
        rent=0
        print("Have a nice day!")
        name=input("Enter name :")
        days=int(input("no of days:"))
        print("1-->single bed-non a/c=Rs500")
        print("2-->single bed-a/c=Rs1000")
        print("3-->double bed-non a/c=Rs600")
        print("4-->double bed-a/c=Rs1600")
        roomtype=int(input("enter room type:"))
        if roomtype==1:
            rent= rent+days*500
            print(rent)
            import random
            w=random.randrange(1,40,1)
            print("Your room number:",w)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into booking values('"+str(name)+"',"+str(roomtype)+","+str(rent)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",rent)
        elif roomtype==2:
            rent=rent+days*1000
            print(rent)
            import random
            w=random.randrange(1,40,1)
            print("Your room number:",w)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into booking values ('"+str(name)+"',"+str(roomtype)+","+str(rent)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",rent)
        elif roomtype==3:
            rent= rent+days*600
            print(rent)
            import random
            w=random.randrange(1,40,1)
            print("Your room number:",w)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into booking values ('"+str(name)+"',"+str(roomtype)+","+str(rent)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",rent)
        elif roomtype==4:
            rent=rent+days*1600
            print(rent)
            import random
            w=random.randrange(1,40,1)
            print("Your room number:",w)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into booking values ('"+str(name)+"',"+str(roomtype)+","+str(rent)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",rent)
        else:
            print("rent invalid")


#Entering details for laundry
    def laundry():
        name=input("Enter name :")
        g=int(input("Enter no of clothes:"))
        print("Discount  in laundry if more than 10 clothes are there:")
        if g==10:
            print("You have discount")
            p=g*10
            print("Price=",p)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into laundry values ('"+str(name)+"',"+ str(g)+","+str(p)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",p)
        elif g<10:
            print("Price=",g*14)
            p=g*14
            print("Price=",p)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into laundry values ('"+str(name)+"',"+ str(g)+","+str(p)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                 print("You have to pay rupees=",p)
        else:
            print("You have discount")
            
            p=g*10
            print("Price=",p)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into laundry values ('"+str(name)+"',"+ str(g)+","+str(p)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                 print("You have to pay rupees=",p)
#Entering details for food
    def food():
        print("Do you want to know about the food court")
        print("1-->water=Rs20")
        print("2-->tea=Rs30")
        print("3-->breakfast combo=Rs90")
        print("4-->lunch=Rs110")
        print("5-->dinner=Rs150")
        print("6-->Exit")
        name=input("Enter name :")
        c=int(input("Enter your choice:"))
        self=0
        if (c==1):
            d=int(input("Enter the quantity:"))
            cost=self+20*d
            print("The cost of water you have purchased:",cost)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into food values ('"+str(name)+"',"+str(d)+","+str(cost)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                 print("You have to pay rupees=",cost)
        elif (c==2):
            d=int(input("Enter the quantity:"))
            cost=self+10*d
            print("The cost of tea you have purchased:",cost)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into food values ('"+str(name)+"',"+str(d)+","+str(cost)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",cost)
        elif (c==3):
            d=int(input("Enter the quantity:"))
            cost=self+90*d
            print("The cost of food you have purchased:",cost)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into food values ('"+str(name)+"',"+str(d)+","+str(cost)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",cost)
        elif (c==4):
            d=int(input("Enter the quantity:"))
            cost=self+110*d
            print("The cost of food you have purchased:",cost)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into food values ('"+str(name)+"',"+str(d)+","+str(cost)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",cost)
        elif (c==5):
            d=int(input("Enter the quantity:"))
            cost=self+150*d
            print("The cost of food you have purchased:",cost)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into food values ('"+str(name)+"',"+str(d)+","+str(cost)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",cost)
        elif (c==6):
            exit
        else:
            print("Invalid option")

    def game():
        print ("******GAME MENU*******")
        print ("1-->Table tennis=Rs60")
        print("2-->Bowling=Rs80")
        print("3-->Snooker=Rs70")
        print("4-->Video games=Rs90")
        print("5-->Pool=Rs50")
        print("6-->Exit")
        g=int(input("Enter your choice:"))
        name=input("Enter name :")
        game=0
        if (g==1):
            h=int(input("No. of hours:"))
            game=game+60*h
            print("The cost for playing",game)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into game values ('"+str(name)+"',"+str(h)+","+str(game)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",game)
        elif (g==2):
            h=int(input("No. of hours:"))
            game=game+80*h
            print("The cost for playing",game)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into game values ('"+str(name)+"',"+str(h)+","+str(game)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",game)
        elif (g==3):
            h=int(input("No. of hours:"))
            game=game+70*h
            print("The cost for playing",game)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into game values ('"+str(name)+"',"+str(h)+","+str(game)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",game)
        elif (g==4):
            h=int(input("No. of hours:"))
            game=game+90*h
            print("The cost for playing",game)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into game values ('"+str(name)+"',"+str(h)+","+str(game)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",game)
        elif (g==5):
            h=int(input("No. of hours:"))
            game=game+50*h
            print("The cost for playing",game)
            command1=("use residence;")
            cursor.execute(command1)
            insert_values1=("insert into game values ('"+str(name)+"',"+str(h)+","+str(game)+");")
            cursor.execute(insert_values1)
            con.commit()
            cj=input("Enter yes or no to see other features:")
            cj1=cj.lower()
            if cj1=="yes":
                choice()
            else:
                print("You have to pay rupees=",game)
        elif (g==6):
            exit
        else:
            print ("Invalid option")
            
    def pool():
        name=input("Enter name :")
        charge=0
        print("SWIMMING POOL!!")
        age=int(input("Enter age:"))
        print("You can have fun in the pool upto one hour")
        nu=int(input("Enter number of people:"))
        c=charge+nu*100
        print("Charge for ",nu,"is",c)
        command1=("use residence;")
        cursor.execute(command1)
        insert_values1=("insert into pool values ('"+str(name)+"', "+str(age)+","+str(nu)+","+str(c)+");")
        cursor.execute(insert_values1)
        con.commit()
        cj=input("Enter yes or no to see other features:")
        cj1=cj.lower()
        if cj1=="yes":
            choice()
        else:
            print("You have to pay rupees=",c)
    def  choice():
                print("Enter the department you have to see")
                print("1-->login ")
                print("2-->booking ")
                print("3-->laundry ")
                print("4-->food ")
                print("5-->games ")
                print("6-->swimming pool")
                print("7-->exit")
                dep=int(input("Enter the valid department number"))
                if dep==1:
                    login()
                elif dep==2:
                    room()
                elif dep==3:
                    laundry()
                elif dep==4:
                    food()
                elif dep==5:
                    game()
                elif dep==6:
                    pool()
                else:
                    exit




   
except Error as e:
    print("Error while connecting to MySQL", e)
    cursor.close()
    con.close()
    
confirm()



