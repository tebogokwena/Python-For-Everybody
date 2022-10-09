# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:32:51 2022

@author: Tebogo Moloto
"""



cnt=0
total=0
avg=0
while True:
    number = (input('>'))          #get number input but store as string
    if number.lower()=='done':     #if condition to handle if the user is done with inputs (make a habit of checking this at the beginning of loops right after the input)
        print('Results: ',total,cnt,avg) #print results if user is done
        break #end loop once results are printed
    else:                          #if user is not done
        try:                       #try change the input into integer type and compute results
            number=(int(number))   
            #print(type(number))              #type check
            total=total+number                #adding up inputs
            cnt+=1                            #increasing the count
            avg=total/cnt                     #average is total divided by total count
        except:                    #if exception is thrown trying to change input to integer type then print error message and continue
            print('Invalid Input')
            continue
        