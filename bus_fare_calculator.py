# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# Task: Design and implementation of a graphical userinterface
# Bahareh Darvishmohammadi the Material Coder, studentnr:256276

'''
This program is bus fare calculator which calculates the
total fee for the bus passengers. the types of passenger could be adult, youth
and children and the types of the ticket can be single, one day or night ticket.
first the user enters the number of adults, youth and/or children and then choose
the type of the ticket. when the user press the calculate button it shows the result of
calculation. Moreover, the clear button can be used for removeing the user entries and
options.
'''

from tkinter import *

class Bus_fare_cal_ui:
   '''
   This class include attributes and methods for bus fare
   graphical user interface and also the calculation
   '''

   def __init__(self, bus_fare):

      '''
      Constructor, creates a new object of bus fare.
      attribure that has defined for this constructor including __bus_fare,
      and the attributes for user interface. the __bus_fare attribute holds
      the info of the fares.
      :param bus_fare: bus_fare info
      '''

      self.__bus_fare = bus_fare

      self.__window = Tk()
      self.__window.option_add("*Font", "Verdana 16")

      self.__label_adult = Label(self.__window, text = 'Adult')
      self.__adult_nr = Entry(self.__window)
      self.__label_youth = Label(self.__window, text = 'Youth')
      self.__youth_nr = Entry(self.__window)
      self.__label_child = Label(self.__window, text = 'Children')
      self.__child_nr = Entry(self.__window)

      self.__radio_var = IntVar()
      self.__radio_var.set(1)
      self.__rb_single = Radiobutton(self.__window, text='Single Ticket',
                                    variable=self.__radio_var, value=1)

      self.__rb_day = Radiobutton(self.__window,text='One Day Ticket',
                                    variable=self.__radio_var, value=2)

      self.__rb_night = Radiobutton(self.__window, text='Night Ticket',
                                    variable=self.__radio_var, value=3)

      self.__cal_button = Button(self.__window, text="Calculate",
                                    command=self.calculate_total_fare)
      self.__calculate_result = Label(self.__window, text="")

      self.__clear_button = Button(self.__window, text="Clear",
                                  command=self.clear)

      self.__quit_button = Button(self.__window, text="Quit",
                                 command=self.quit)

      self.__label_adult.grid(row=0, column=0, sticky ="W")
      self.__label_youth.grid(row=1, column=0, sticky ="W")
      self.__label_child.grid(row=2, column=0, sticky ="W")
      self.__adult_nr.grid(row=0, column=1, sticky ="W")
      self.__youth_nr.grid(row=1, column=1, sticky ="W")
      self.__child_nr.grid(row=2, column=1, sticky ="W")
      self.__rb_single.grid(row=3, column=0)
      self.__rb_day.grid(row=3, column=1)
      self.__rb_night.grid(row=3, column=2)
      self.__cal_button.grid(row=4, column=0)
      self.__calculate_result.grid(row=4, column=1)
      self.__clear_button.grid(row=5, column=0)
      self.__quit_button.grid(row=5, column=1)

   def isvalidnumber(self, text):
      '''
      This method checks if the entry content is a valid number.
      :param text: the entry content(str)
      :return: flag: True if the entry is a number
                     otherwise, False.
      '''
      flag = True
      for char in text:
         if char not in '0123456789':
            flag = False

      return flag


   def start(self):
      self.__window.mainloop()

   def clear(self):
      '''
      This method removes the text in the entry widget, the radiobutton option
      and the label for showing calculation result.
      '''
      self.__adult_nr.delete(0, 'end')
      self.__youth_nr.delete(0, 'end')
      self.__child_nr.delete(0, 'end')
      self.__rb_single.select()
      self.__calculate_result["text"] = ""

   def calculate_fare(self,ticket):
      '''
      This method is for calculating the fee for each type of passenger.
      (adult, youth or children )
      :param ticket: the type of ticket which can be a single, oneday or night ticket.
      :return: adult_fare: the fee for adult passengers
               youth_fare: the fee for youth passengers
               child_fare: the fee for children passengers
               error: True: if the user entry is not a valid number
                      False: if the user entry is not a valid number
               empty: True: if all the user entry are empty.
                      False: if all the user entry are not emtry.
      '''
      adult_fare = 0
      youth_fare = 0
      child_fare = 0
      error = False
      empty = False
      if self.__adult_nr.get() != "" and self.__youth_nr.get() != "" and self.__child_nr.get() != "" \
            and self.isvalidnumber(self.__adult_nr.get()) and self.isvalidnumber(self.__youth_nr.get()) \
                      and self.isvalidnumber(self.__child_nr.get()):

         adult_fare = int(self.__adult_nr.get()) * int(self.__bus_fare["adults"][ticket])
         youth_fare = int(self.__youth_nr.get()) * int(self.__bus_fare["youth"][ticket])
         child_fare = int(self.__child_nr.get()) * float(self.__bus_fare["children"][ticket])

      elif self.__child_nr.get() == "" and self.__youth_nr.get() == "" and self.__adult_nr.get() == "":

         empty = True

      elif self.__adult_nr.get() == "" and self.__youth_nr.get() == ""\
              and self.isvalidnumber(self.__child_nr.get()) :

         adult_fare = 0
         youth_fare = 0
         child_fare = int(self.__child_nr.get()) * float(self.__bus_fare["children"][ticket])

      elif self.__adult_nr.get() == "" and self.__child_nr.get() == "" \
              and self.isvalidnumber(self.__youth_nr.get()):

         adult_fare = 0
         youth_fare = int(self.__youth_nr.get()) * int(self.__bus_fare["youth"][ticket])
         child_fare = 0

      elif self.__child_nr.get() == "" and self.__youth_nr.get() == "" \
              and self.isvalidnumber(self.__adult_nr.get()):

         adult_fare = int(self.__adult_nr.get()) * int(self.__bus_fare["adults"][ticket])
         youth_fare = 0
         child_fare = 0

      elif self.__adult_nr.get() == "" and self.isvalidnumber(self.__youth_nr.get()) \
                      and self.isvalidnumber(self.__child_nr.get()):

         adult_fare = 0
         youth_fare = int(self.__youth_nr.get()) * int(self.__bus_fare["youth"][ticket])
         child_fare = int(self.__child_nr.get()) * float(self.__bus_fare["children"][ticket])

      elif self.__youth_nr.get() == "" and self.isvalidnumber(self.__adult_nr.get()) \
                      and self.isvalidnumber(self.__child_nr.get()):

         adult_fare = int(self.__adult_nr.get()) * int(self.__bus_fare["adults"][ticket])
         youth_fare = 0
         child_fare = int(self.__child_nr.get()) * float(self.__bus_fare["children"][ticket])

      elif self.__child_nr.get() == "" and self.isvalidnumber(self.__youth_nr.get()) \
                      and self.isvalidnumber(self.__adult_nr.get()):

         adult_fare = int(self.__adult_nr.get()) * int(self.__bus_fare["adults"][ticket])
         youth_fare = int(self.__youth_nr.get()) * int(self.__bus_fare["youth"][ticket])
         child_fare = 0

      elif self.isvalidnumber(self.__adult_nr.get())== False or self.isvalidnumber(self.__youth_nr.get())== False \
                      or self.isvalidnumber(self.__child_nr.get())== False:

         error = True

      return adult_fare, youth_fare, child_fare, error, empty


   def calculate_total_fare(self):
      '''
      This method is for calculating the total fee for all types of passengers.
      '''

      adult_fare = 0
      youth_fare = 0
      child_fare = 0
      error = False
      empty = False
      if self.__radio_var.get() == 1:
         adult_fare, youth_fare, child_fare, error, empty = self.calculate_fare("single")
      elif self.__radio_var.get() == 2:
         adult_fare, youth_fare, child_fare, error, empty = self.calculate_fare("day")
      elif self.__radio_var.get() == 3:
         adult_fare, youth_fare, child_fare, error, empty = self.calculate_fare("night")

      fare = adult_fare + youth_fare + child_fare
      if empty == True:
         self.__calculate_result["text"] = "Please enter a number."
      elif error == False:
         self.__calculate_result["text"] = fare
      elif error == True:
         self.__calculate_result["text"] = "Please enter a valid number."


   def quit(self):
      '''
      when the user press the quit button, the execution of the program will end.
      :return:
      '''
      self.__window.destroy()



def main():
   '''
   This main method includes the definition of data structure for holding the info
   related to the fare for each type of passenger and for types of ticket. It also
   make a new object of bus_fare_cal_ui class and use the star method of the object.
   '''

   bus_fare = { "adults": {"single":3, "day":8, "night":3} , "youth": {"single":3, "day":6, "night":3},
                "children": {"single":1.5, "day":4, "night":3}}

   ui = Bus_fare_cal_ui(bus_fare)
   ui.start()

main()
