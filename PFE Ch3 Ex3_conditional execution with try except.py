# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:10:36 2022

@author: Tebogo Moloto
"""

def computegrade():
    try:                                                             #try and except statements to catch incorrect type inputs
        score = float(input('Enter a score between 0.0 and 1.0: '))  #prompt user to input score and store in variable 'score'as float
        if score>1.0 or score<0.0:                                     #if and else statements to handle score outputs
            print('Error: Please enter a number between 0.0 and 1.0')
        else: 
            if score>=0.9:
                print('A')
            elif score>=0.8:
                print('B')
            elif score>=0.7:
                print('C')
            elif score>=0.6:
                print('D')
            else:
                print('F')
    except:
        print('Bad Score')


computegrade()




        
        
        