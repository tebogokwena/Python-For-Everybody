# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:03:04 2022

@author: Tebogo Moloto
"""


cnt=0
big=0
sml=0
while True:
    number = (input('>'))          #get number input but store as string
    if number.lower()=='done':     #if condition to handle if the user is done with inputs (make a habit of checking this at the beginning of loops right after the input)
        print('Results: max: ',big,'min: ',sml) #print results if user is done
        break #end loop once results are printed
    else:                          #if user is not done
        try:                       #try change the input into integer type and compute results
            number=(int(number))  
            #print(type(number))              #type check
            if number>big:
                big=number
            elif number<sml:
                sml=number
            cnt+=1                            #increasing the count
        except:                    #if exception is thrown trying to change input to integer type then print error message and continue
            print('Invalid Input')
            continue
    
#the correct way to do this is actually to append a list with the values and then compute because assigning big and sml will always leave inaccuracy also ho
#do i get 