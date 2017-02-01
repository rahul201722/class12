import pickle
import os
class Reservation:
   airline_seats = { 'Business Class' : 50,
                           'First Class'    : 50,
                           'Premium Economy': 100,
                           'Regular Economy': 150 }
   hotel_room = {'Penthouse': 10,
                       'King Deluxe Bedroom'    : 20,
                       'Queen Deluxe Bedroom'   : 20,
                       'Kind Standard Bedroom' : 30,
                       'Queen Standard Bedroom': 50 }
   def __init__(self,passenger_id,passenger_fname,passenger_lname):
      self.passenger_id = passenger_id
      self.passenger_fname = passenger_fname
      self.passenger_lname = passenger_lname
      self.cost = 0
      self.reservation_id = []
      self.seats=0
      self.passenger_record = {'p_name'  : self.passenger_fname + self.passenger_lname,
                             'p_id'    : self.passenger_id,
                             'p_wallet': self.cost,
                             'p_reservation_id': self.reservation_id,
                             'p_seats':  self.seats
                              
                            }
     
      self.airline_price = { 'Business Class' : 2500,
                           'First Class'    : 2000,
                           'Premium Economy': 1800,
                           'Regular Economy': 1500 }
     
      self.hotel_price = {'Penthouse'            : 1000,
                        'King Deluxe Bedroom'    : 700,
                        'Queen Deluxe Bedroom'   : 600,
                        'Kind Standard Bedroom' : 450,
                        'Queen Standard Bedroom': 350 }
   
 
   def Total(self):
       print self.passenger_record['p_wallet']
class Airline(Reservation):
   def __init__(self,passenger_id,passenger_fname,passenger_lname,airline_seat_section,
         airline_departure_date):
       Reservation.__init__(self,passenger_id,passenger_fname,passenger_lname)
       self.airline_seat_section = airline_seat_section
       self.airline_departure_date = airline_departure_date
   def CheckAvailability(self,h1):
        print " Total seats were :" ,self.airline_seats[self.airline_seat_section]
        print " price of ", self.airline_seat_section , "is:", self.airline_price[self.airline_seat_section]
        if self.airline_seats.get(self.airline_seat_section) >= h1:
            self.airline_seats[self.airline_seat_section] -= h1
            self.passenger_record['p_wallet'] += self.airline_price[self.airline_seat_section]*h1
            self.passenger_record['p_seats']=h1
            print " amount to be paid",self.passenger_record['p_wallet']
            print "\n\nReserved Airline Ticket\n\n"
class Hotel(Reservation):
    def __init__(self,passenger_id,passenger_fname,passenger_lname,hotel_room_selection,
             hotel_check_in_date,hotel_check_out_date):
        Reservation.__init__(self,passenger_id,passenger_fname,passenger_lname)
        self.hotel_room_selection = hotel_room_selection
        self.hotel_check_in_date = hotel_check_in_date
        self.hotel_check_out_date = hotel_check_out_date
    def CheckAvailability(self):
        print " total selected room before: " , self.hotel_room[self.hotel_room_selection]
        print " price of " , self.hotel_room_selection , " is" , self.hotel_price[self.hotel_room_selection]
        if (self.hotel_room.get(self.hotel_room_selection) != 0):
            self.hotel_room[self.hotel_room_selection] -= 1
            self.passenger_record['p_wallet'] += self.hotel_price[self.hotel_room_selection]
           
            print "\n\nReserved Hotel Room\n\n"
def CurrentStatus(option):#this feature is not working as current status is not shown
   
       if option == "Airline" :
          try:
             print "entered"
             while True:
                print "entered2while loop"
                file1= open("reservation.txt","r+")
                lst2=pickle.load(file1)
                Reservation.airline_seats = lst2[0]
                
 
          except EOFError:
             file1.close()
             
             
          for key, value in Reservation.airline_seats.items():
             print key, value
          
       elif option == "Hotel":
          try:
             print "entered"
             while True:
                print "entered2while loop"
                file2= open("reservation2.txt","r+")
                lst2=pickle.load(file2)
                Reservation.hotel_room = lst2[0]
 
 
          except EOFError :
             file2.close()
             
          for key,value in Reservation.hotel_room.items():
              print key, value
 
 
print"WELCOME"
 
print " Current Status "
currentstatus = int(raw_input("Enter 1 for Airline Status ,Enter 2 for Hotel status :"))
   
if currentstatus == 1 :
   print "Current status of airline reservations"
   CurrentStatus("Airline")
else :
   print"Current status of Hotel Booking"
   CurrentStatus("Hotel")
 
ch="T"
while ch!="5":
    print " MENU"
    print " 1. Airline booking"
    print " 2. Hotel booking "
    print " 3. Cancellation of airline "
    print " 4. Cancellation of Hotel"
    print"5.exit"
    lst1=[]
    ch=raw_input("choose 1 or 2 or 3 or 4")
    if ch == "1":
            
        print" Airline menu:"
        a= raw_input("passenger_fname:")
        b=raw_input("passenger_lname:")
        c=raw_input("passenger_id:")
        print " choose from following"
        print"1. Business Class"
        print"2. First Class"
        print'3. Premium Economy'
        print'4. Regular Economy'
        e1=int(raw_input(" type airline_seat_section:"))
        if e1==1:
            e= "Business Class"
        if e1==2:
            e= "First Class"
        if e1==3:
            e= "Premium Economy"
        if e1==4:
            e= "Regular Economy"   
        f=raw_input("airline_departure_date:")
        h=int(raw_input("no. of seats required:"))
        d= Airline(c,a,b,e,f)
       
        
        #g=d.airline_seats[e]
        d.CheckAvailability(h)
        print" current status of available seats"
        currentStatus("Airline")
        
        
        file1= open("reservation.txt","a+")
        lst1.append(d.airline_seats)
        lst1.append(d.passenger_record)
        pickle.dump(lst1,file1)
        file1.flush()
        file1.close()
           
    elif ch == "2":
        print" Hotel reservation menu:"
        q= raw_input("passenger_fname:")
        r=raw_input("passenger_lname:")
        p=raw_input("passenger_id:")
        print " choose from following"
        print"1.'Penthouse'   "
        print"2.'King Deluxe Bedroom'"
        print"3.'Queen Deluxe Bedroom' "
        print"4. ' King Standard Bedroom '"
        print"5. 'Queen standard Bedroom' "
        s1=int(raw_input("hotel_room_selection:"))
        if s1==1:
            s= 'Penthouse'
        if s1==2:
            s= 'King Deluxe Bedroom'
        if s1==3:
            s= 'Queen Deluxe Bedroom'
        if s1==4:
            s= ' King Standard Bedroom '
        if s1==5:
            s= 'Queen Deluxe Bedroom'   
        
        t=raw_input("hotel_check_in_date:")
        u=raw_input("hotel_check_out_date:")
        w= Hotel(p,q,r,s,t,u)
 
        w.CheckAvailability()
        print" current status of available rooms"
        currentStatus("Hotel")
        lst2=[]
        file2= open("reservation2.txt","a+")
        lst2.append(w.hotel_room)
        lst2.append(w.passenger_record)
        pickle.dump(lst2,file2)
        file2.flush()
        file2.close()
       
                  
    elif ch == "3" :
       
           try:
              filein=open("reservation.txt", "r")
              fileout=open("cancelreservation.txt", "a")
              fileout1=open("temp.txt", "w")
              name = raw_input("Enter the name+lastname of passenger to delete ticket")
              while True:
                 o=pickle.load(filein)
                 print 'entered'
                 diction=o[1]
                 if (diction['p_name'] == name) :
                    print"record found"
                    pickle.dump(o,fileout)
                    print ''''choose and ENTER YOUR SEAT TYPE:
                              1. Business Class
                              2. First Class
                              3. Premium Economy
                              4. Regular Economy'''
                    s1=int(raw_input("Enter from the above choices 1 , 2 , 3 , 4 "))
                    if s1==1:
                       s= 'Business Class'
                    if s1==2:
                       s= 'First Class'
                    if s1==3:
                       s= 'King Standard Bedroom'
                    if s1==4:
                       s= 'Regular Economy '
                      
                    
                    print"no of current available seats",Reservation.airline_seats[s]
                    Reservation.airline_seats[s] += diction['p_seats']
                    print"no of available seats increased",diction['p_seats']
                    print"no of new available seats",Reservation.airline_seats[s]
                    fileout.flush()
                 else:
                    pickle.dump(o,fileout1) 
                    fileout1.flush()    
           except EOFError:
              filein.close()
              
           filein.close()   
           fileout.close()
           fileout1.close()
           os.remove("reservation.txt")
           os.rename("temp.txt","reservation.txt")
    elif ch == "4":
       try:
          filein=open("reservation2.txt", "r")
          fileout=open("cancelreservation.txt", "a")
          fileout1=open("temp2.txt", "w")
          name = raw_input("Enter the name+lastname of passenger to delete ticket")
          while True:
             print "entered"
             o=pickle.load(filein)
             diction=o[1]
             if (diction['p_name'] == name) :
                print"record found"
                pickle.dump(o,fileout)
                print ''''choose and ENTER YOUR SEAT TYPE:
                              1. Penthouse
                              2. King Deluxe Bedroom
                              3. Queen Deluxe Bedroom
                              4. Regular Economy
                              5. Queen Deluxe Bedroom'''
                s1=int(raw_input("Enter from the above choices 1 , 2 , 3 , 4 , 5 "))
                if s1==1:
                   s= 'Penthouse'
                if s1==2:
                   s= 'King Deluxe Bedroom'
                if s1==3:
                   s= 'Queen Deluxe Bedroom'
                if s1==4:
                   s= 'King Standard Bedroom'
                if s1== 5:
                   s= 'Queen Deluxe Bedroom'
                      
                    
                print"no of available rooms",Reservation.hotel_room[s]
                Reservation.hotel_room[s] += 1
                print"no of available rooms increased", Reservation.hotel_room[s]
                print"no of new available rooms",Reservation.hotel_room[s]
                fileout.flush()
          else:
             pickle.dump(o,fileout1) 
             fileout1.flush()    
       except EOFError:
              filein.close()
             
       filein.close()       
       fileout.close()
       fileout1.close()
       os.remove("reservation2.txt")
           
       os.rename("temp2.txt","reservation2.txt")
           
 
         
    elif ch == "5":
       exit
