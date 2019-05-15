'''
Created on Jan 27, 2019

@author: Lisa Wang 

Program implements assignment problem from Week 1 
Computes the class details of a gym 

INPUT - 
length of class in minutes (in hours and in minutes),
length of after-class break(in minutes), 
the name of class 

PROGRAM DATA :
o the class time is between 10:30 a.m. and 8:30 p.m.
o there is a short break after each class, including the last one.
o the base price of class is $3. 
o 20 cents are added to the base price for each full 15 minutes of class time.

OUTPUT - 
class price, class frequency in one day's schedule, 
time that gym have to stay open for one more class, 
how long is the stay-open time.  
'''
#get input 
print('This program computes how many gym classes can be offered in one day.')

classname = input('Please enter the name of class:')

classhr = eval(input('Please enter the length (in hours and in minutes) of class, hours:'))

classmi = eval(input('minutes:'))

break_time = eval(input('Now enter the length of the after-class break in minutes:'))

#data parameters
FEE = 3 #$
COST_INCREMENT = 0.2 #$
TIME_INCREMENT = 15 #minutes 
START_TIME = 630 # in minutes since the start of the day 
END_TIME = 1230 # in minutes since the start of the day 
OPENING_PERIOD = 600 #in minutes

#print class name 
print(classname)

#compute class price 
price = FEE + COST_INCREMENT*(classhr*60)/TIME_INCREMENT + COST_INCREMENT*(classmi//TIME_INCREMENT)
print('Price:$',price)

#compute class length  
length = classhr*60 + classmi
print('Length:',length,'min +',break_time,'min break')

#compute class frequency 
frequency = OPENING_PERIOD//(length+break_time)
print('Can be offered',frequency,'times a day')

#compute the opening time for one more class
additional_class = (length+break_time)*(frequency+1)
last_timehr = (START_TIME + additional_class)//60 # in hour
last_timemi = str((START_TIME + additional_class)%60) # in minute
print('To offer one more class,stay open until',last_timehr,':',last_timemi.zfill(2),',')

#compute the passing time for regular closing time 
passing_time = (START_TIME+additional_class)-END_TIME
print("That's",passing_time,'minutes past the regular closing time.')