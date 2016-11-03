import pickle
class Reservation:
   def __init__(self,passenger_id,passenger_fname,passenger_lname):
      self.passenger_id = passenger_id
      self.passenger_fname = passenger_fname
      self.passenger_lname = passenger_lname
      self.cost = 0
      self.reservation_id = []
      self.passenger_record = {'p_name'  : self.passenger_fname + self.passenger_lname,
                             'p_id'    : self.passenger_id,
                             'p_wallet': self.cost,
                             'p_reservation_id': self.reservation_id,
                            }
      self.airline_seats = { 'Business Class' : 50,
                           'First Class'    : 50,
                           'Premium Economy': 100,
                           'Regular Economy': 150 }
      self.airline_price = { 'Business Class' : 2500,
                           'First Class'    : 2000,
                           'Premium Economy': 1800,
                           'Regular Economy': 1500 }
      self.hotel_room = {'Penthouse'             : 10,
                       'King Deluxe Bedroom'    : 20,
                       'Queen Deluxe Bedroom'   : 20,
                       'Kind Standard Bedroom' : 30,
                       'Queen Standard Bedroom': 50 }
      self.hotel_price = {'Penthouse'            : 1000,
                        'King Deluxe Bedroom'    : 700,
                        'Queen Deluxe Bedroom'   : 600,
                        'Kind Standard Bedroom' : 450,
                        'Queen Standard Bedroom': 350 }
   def currentStatus(self,option):
       if option == "Airline":
           for key, value in self.airline_seats.items():
              print key, value
       elif option == "Hotel":
           for key,value in self.hotel_room.items():
              print key, value

   def Total(self):
       print self.passenger_record['p_wallet']

class Airline(Reservation):
   def __init__(self,passenger_id,passenger_fname,passenger_lname,airline_seat_section,
         airline_departure_date):
       Reservation.__init__(self,passenger_id,passenger_fname,passenger_lname)
       self.airline_seat_section = airline_seat_section
       self.airline_departure_date = airline_departure_date

   def CheckAvailability(self,h1):
       print " test"
       print self.airline_seats[self.airline_seat_section] 
       if self.airline_seats[self.airline_seat_section] >= h1:
            self.airline_seats[self.airline_seat_section] -= h1
            self.passenger_record['p_wallet'] +=        self.airline_price[self.airline_seat_section]*h1
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
        if (self.hotel_room.get(self.hotel_room_selection) != 0):
            self.hotel_room[self.hotel_room_selection] -= 1
            self.passenger_record['p_wallet'] += self.hotel_price[self.hotel_room_selection]
            print "\n\nReserved Hotel Room\n\n"
r="T"
while r=="T":
    print " MENU"
    print " 1. Airline booking"
    print " 2. hotel booking "
    ch=raw_input("choose 1 or 2")
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
        file1= open("reservation.txt"."a")
        pickle.dump(
        #g=d.airline_seats[e]
        d.CheckAvailability(h)
        print" current status of available seats"
        d.currentStatus("Airline")
    
    elif ch == "2":
        print" Hotel reservation menu:"
        q= raw_input("passenger_fname:")
        r=raw_input("passenger_lname:")
        p=raw_input("passenger_id:")
        s=int(raw_input("hotel_room_selection:"))
        t=raw_input("hotel_check_in_date:") 
        u=raw_input("hotel_check_out_date:")
        w= Hotel(p,q,r,s,t,u)
        w.CheckAvailability()
        w.currentStatus("Hotel")
    else:
        print " wrong choice"
    r=raw_input("enter T to continue")

