#created by Rakuzan
from tkinter import * 
from time import sleep 
from random import randint, choice 
from turtle import heading 
  
class Field: 
    def __init__(self, c, n, m, width, height, walls = 0): 
        ''' 
       c - canvas instance 
       n - number of rows 
       m - number of columns 
       width - width of game field in pixels 
       height - width of game field in pixels 
       walls - if True matrix should have 0's surrounded by 1's (walls) 
       example 
       1 1 1 1 
       1 0 0 1 
       1 1 1 1 
       ''' 
        self.c = c 
        self.a = [] 
        self.a3 = [] 
        self.n = n + 2 
        self.m = m + 2 
        self.width = width 
        self.height = height 
        self.count = 0 
        for i in range(self.n): 
            self.a.append([]) 
            self.a3.append ([]) 
            for j in range(self.m): 
                # self.a[i].append(choice([0, 1])) 
                self.a[i].append(0) 
                self.a3[i].append(0) 
                if (randint(1,20) == 1) and self.a[i][j] == 0:  
                    self.a[i][j] = 1  
                elif (randint(1,7) == 1) and self.a[i][j] == 0:  
                    self.a[i][j] = 2  
                elif (randint(1,5) == 1) and self.a[i][j] == 0:  
                    self.a[i][j] = 3  
        self.a[1+10][1+10] = 1 
        self.a[1+10][3+10] = 1 
        self.a[2+10][3+10] = 1 
        self.a[2+10][2+10] = 1 
        self.a[3+10][2+10] = 1 
        self.draw()
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1):
                print (self.a[i][j] , end = "")
            print ()
        
        print ()
        print ()
        print ()
        print ()
        print ()
        print ()
    def step(self): 
         
        
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1): 
                  
                if self.a3[i][j] == 0:                  
                    if self.a[i][j] == 1:  # fox
                        ss = 0
                        if self.a[i-1][j-1] == 1:
                            ss = ss + 1
                        if self.a[i-1][j] == 1:
                            ss = ss + 1
                        if self.a[i-1][j+1] == 1:
                            ss = ss + 1
                        if self.a[i][j+1] == 1:
                            ss = ss + 1
                        if self.a[i+1][j+1] == 1:
                            ss = ss + 1
                        if self.a[i+1][j+1] == 1:
                            ss = ss + 1
                        if self.a[i+1][j] == 1:
                            ss = ss + 1
                        if self.a[i+1][j-1] == 1:
                            ss = ss + 1
                        if self.a[i][j-1] == 1:
                            ss = ss + 1
                        if ss > 5:
                            self.a[i][j] = 0
                            self.a3[i][j] = 1
                        elif self.a[i-1][j-1] == 2 and self.a3[i-1][j-1] == 0:  
                            self.a[i-1][j-1] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i-1][j-1] = 1  
                        elif self.a[i-1][j] == 2 and self.a3[i-1][j] == 0:  
                            self.a[i-1][j] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i-1][j] = 1  
                        elif self.a[i-1][j+1] == 2 and self.a3[i-1][j+1] == 0:  
                            self.a[i-1][j+1] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i-1][j+1] = 1  
                        elif self.a[i][j+1] == 2 and self.a3[i][j+1] == 0:  
                            self.a[i][j+1] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i][j+1] = 1  
                        elif self.a[i+1][j+1] == 2 and self.a3[i+1][j+1] == 0:  
                            self.a[i+1][j+1] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i+1][j+1] = 1  
                        elif self.a[i+1][j] == 2 and self.a3[i+1][j] == 0:  
                            self.a[i+1][j] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i+1][j] = 1  
                        elif self.a[i+1][j-1] == 2 and self.a3[i+1][j-1] == 0:  
                            self.a[i+1][j-1] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i+1][j-1] = 1  
                        elif self.a[i][j-1] == 2 and self.a3[i][j-1] == 0:  
                            self.a[i][j-1] = 1  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i][j-1] = 1
                        if randint (1,5) == 1:
                            if self.a[i-1][j-1] == 1 and self.a3[i-1][j-1] == 0: #pop 
                                if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0 :
                                    self.a[i-1][j] = 1
                                    self.a3[i-1][j-1] = 1  
                                    self.a3[i-1][j] = 1  
                                    self.a3[i][j] = 1  
                                elif self.a[i][j-1] == 0 and self.a3[i][j-1] == 1:  
                                    self.a[i][j-1] = 1  
                                    self.a3[i-1][j-1] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i][j-1] = 1  
                                      
                            elif self.a[i-1][j] == 1 and self.a3[i-1][j] == 0:  
                                if self.a[i-1][j-1] == 0 and self.a3[i-1][j-1] == 0:  
                                    self.a[i-1][j-1] = 1  
                                    self.a3[i-1][j] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i-1][j-1] = 1  
                                elif self.a[i][j-1] == 0 and self.a3 [i][j-1] == 0:  
                                    self.a[i][j-1] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i][j-1] = 1  
                                    self.a3[i-1][j] = 1  
                                elif self.a[i-1][j+1] == 0 and self.a3[i-1][j+1] == 0:  
                                    self.a[i-1][j+1] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i-1][j] = 1  
                                    self.a3[i-1][j+1] = 1 
                                elif self.a[i][j+1] == 1 and self.a3[i][j+1] == 0:  
                                    self.a[i][j+1] = 1  
                                    self.a3[i][j+1] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i][j+1] = 1  
                              
                            elif self.a[i-1][j+1] == 1 and self.a3[i-1][j+1] == 0:  
                                if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0:  
                                    self.a[i-1][j] = 1  
                                    self.a3[i-1][j] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i-1][j+1] = 1  
                                elif self.a[i][j+1] == 0 and self.a3[i][j+1] == 0:  
                                    self.a[i][j+1] = 1  
                                    self.a3[i][j+1] = 1  
                                    self.a3[i][j] = 1  
                                    self.a[i-1][j+1] = 1  
                            elif self.a[i][j+1] == 1 and self.a3[i][j+1] == 0:  
                                if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0:  
                                    self.a[i-1][j] = 1  
                                    self.a3[i-1][j] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i][j+1] = 1  
                                elif self.a[i-1][j+1] == 0 and self.a3[i-1][j+1] == 0:  
                                    self.a[i-1][j+1] = 1  
                                    self.a3[i-1][j+1] = 1  
                                    self.a3[i][j]= 1  
                                    self.a3[i][j+1] = 1  
                                elif  self.a[i+1][j] == 0 and self.a3[i+1][j] == 0: 
                                    self.a[i+1][j] = 1 
                                    self.a3[i+1][j] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i][j+1] = 1 
                                elif self.a[i+1][j+1] == 0 and self.a3[i+1][j+1] == 0: 
                                    self.a[i+1][j+1] = 1 
                                    self.a3[i+1][j+1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i][j+1] = 1 
                            elif self.a[i+1][j+1] == 1 and self.a3[i+1][j+1] == 0: 
                                if self.a[i][j+1] == 0 and self.a3[i][j+1] == 0: 
                                    self.a[i][j+1] = 1 
                                    self.a3[i][j+1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j+1] = 1 
                                elif self.a[i+1][j] == 0 and self.a3 [i+1][j] == 0: 
                                    self.a[i+1][j] = 1 
                                    self.a3[i+1][j] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j+1] = 1 
                            elif self.a[i+1][j] == 1 and self.a3[i+1][j] == 0:  
                                if self.a[i][j+1] == 0 and self.a3[i][j+1] == 0: 
                                    self.a[i][j+1] = 1 
                                    self.a3[i][j+1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j] = 1 
                                elif self.a[i+1][j+1] == 0 and self.a3[i+1][j+1] == 0: 
                                    self.a[i+1][j+1] = 1 
                                    self.a3[i+1][j+1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j] = 1 
                                elif self.a[i][j-1] == 0 and self.a3[i][j-1] == 0: 
                                    self.a[i][j-1] = 1 
                                    self.a3[i][j-1] = 1 
                                    self.a[i][j] = 1 
                                    self.a[i+1][j] = 1 
                                elif self.a[i+1][j-1] == 0 and self.a3[i+1][j-1] == 0: 
                                    self.a[i+1][j-1] = 1 
                                    self.a3[i+1][j-1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j] = 1 
                            elif self.a[i+1][j-1] == 1 and self.a3[i+1][j-1] == 0:  
                                if self.a[i][j-1] == 0 and self.a3[i][j-1] == 0: 
                                    self.a[i][j-1] = 1 
                                    self.a3[i][j-1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j-1] = 1 
                                elif self.a[i+1][j] == 0 and self.a3[i+1][j] == 0: 
                                    self.a [i+1][j] = 1 
                                    self.a3[i+1][j] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i+1][j-1] = 1 
                            elif self.a[i][j-1] == 1 and self.a3[i][j-1] == 0: 
                                if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0:  
                                    self.a[i-1][j] = 1  
                                    self.a3[i-1][j] = 1  
                                    self.a3[i][j] = 1  
                                    self.a3[i][j+1] = 1  
                                elif self.a[i-1][j-1] == 0 and self.a3[i-1][j-1] == 0:  
                                    self.a[i-1][j-1] = 1  
                                    self.a3[i-1][j-1] = 1  
                                    self.a3[i][j]= 1  
                                    self.a3[i][j-1] = 1  
                                elif  self.a[i+1][j] == 0 and self.a3[i+1][j] == 0: 
                                    self.a[i+1][j] = 1 
                                    self.a3[i+1][j] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i][j+1] = 1 
                                elif self.a[i+1][j-1] == 0 and self.a3[i+1][j-1] == 0: 
                                    self.a[i+1][j-1] = 1 
                                    self.a3[i+1][j-1] = 1 
                                    self.a3[i][j] = 1 
                                    self.a3[i][j-1] = 1 
                             
                                                     
                     
                 
                 
                          
                             
                            
                # 
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1): 
                if self.a3[i][j] == 0:                  
                     
                    if self.a[i][j] == 2: #rab 
                        if self.a[i-1][j-1] == 3 and self.a3[i-1][j-1] == 0:  
                            self.a[i-1][j-1] = 2
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i-1][j-1] = 1  
                        elif self.a[i-1][j] == 3 and self.a3[i-1][j] == 0:  
                            self.a[i-1][j] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i-1][j] = 1  
                        elif self.a[i-1][j+1] == 3 and self.a3[i-1][j+1] == 0:  
                            self.a[i-1][j+1] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i-1][j+1] = 1  
                        elif self.a[i][j+1] == 3 and self.a3[i][j+1] == 0:  
                            self.a[i][j+1] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i][j+1] = 1  
                        elif self.a[i+1][j+1] == 3 and self.a3[i+1][j+1] == 0:  
                            self.a[i+1][j+1] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i+1][j+1] = 1  
                        elif self.a[i+1][j] == 3 and self.a3[i+1][j] == 0:  
                            self.a[i+1][j] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i+1][j] = 1  
                        elif self.a[i+1][j-1] == 3 and self.a3[i+1][j-1] == 0:  
                            self.a[i+1][j-1] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i+1][j-1] = 1  
                        elif self.a[i][j-1] == 3 and self.a3[i][j-1] == 0:  
                            self.a[i][j-1] = 2  
                            self.a[i][j] = 0  
                            self.a3[i][j] = 1  
                            self.a3[i][j-1] = 1  
                        elif self.a[i-1][j-1] == 2 and self.a3[i-1][j-1] == 0: #pop 
                            if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0 :  
                                self.a[i-1][j] = 2  
                                self.a3[i-1][j-1] = 1  
                                self.a3[i-1][j] = 1  
                                self.a3[i][j] = 1  
                            elif self.a[i][j-1] == 0 and self.a3[i][j-1] == 1:  
                                self.a[i][j-1] = 2  
                                self.a3[i-1][j-1] = 1  
                                self.a3[i][j] = 1  
                                self.a3[i][j-1] = 1  
                                  
                        elif self.a[i-1][j] == 2 and self.a3[i-1][j] == 0:  
                            if self.a[i-1][j-1] == 0 and self.a3[i-1][j-1] == 0:  
                                self.a[i-1][j-1] = 2  
                                self.a3[i-1][j] = 1  
                                self.a3[i][j] = 1  
                                self.a3[i-1][j-1] = 1  
                            elif self.a[i][j-1] == 0 and self.a3 [i][j-1] == 0:  
                                self.a[i][j-1] = 2  
                                self.a3[i][j] = 1  
                                self.a3[i][j-1] = 1 
                                self.a3[i-1][j] = 1  
                            elif self.a[i-1][j+1] == 0 and self.a3[i-1][j+1] == 0:  
                                self.a[i-1][j+1] = 2  
                                self.a3[i][j] = 1  
                                self.a3[i-1][j] = 1  
                                self.a3[i-1][j+1] = 1  
                            elif self.a[i][j+1] == 1 and self.a3[i][j+1] == 0:  
                                self.a[i][j+1] = 2  
                                self.a3[i][j+1] = 1  
                                self.a3[i][j] = 1  
                                self.a3[i][j+1] = 1  
                          
                        elif self.a[i-1][j+1] == 2 and self.a3[i-1][j+1] == 0:  
                            if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0:  
                                self.a[i-1][j] = 2  
                                self.a3[i-1][j] = 1  
                                self.a3[i][j] = 1  
                                self.a3[i-1][j+1] = 1  
                            elif self.a[i][j+1] == 0 and self.a3[i][j+1] == 0:  
                                self.a[i][j+1] = 2  
                                self.a3[i][j+1] = 1  
                                self.a3[i][j] = 1  
                                self.a[i-1][j+1] = 1  
                        elif self.a[i][j+1] == 2 and self.a3[i][j+1] == 0:  
                            if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0:  
                                self.a[i-1][j] = 2  
                                self.a3[i-1][j] = 1  
                                self.a3[i][j] = 1  
                                self.a3[i][j+1] = 1  
                            elif self.a[i-1][j+1] == 0 and self.a3[i-1][j+1] == 0:  
                                self.a[i-1][j+1] = 2  
                                self.a3[i-1][j+1] = 1  
                                self.a3[i][j]= 1  
                                self.a3[i][j+1] = 1  
                            elif  self.a[i+1][j] == 0 and self.a3[i+1][j] == 0: 
                                self.a[i+1][j] = 2 
                                self.a3[i+1][j] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i][j+1] = 1 
                            elif self.a[i+1][j+1] == 0 and self.a3[i+1][j+1] == 0: 
                                self.a[i+1][j+1] = 2 
                                self.a3[i+1][j+1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i][j+1] = 1 
                        elif self.a[i+1][j+1] == 2 and self.a3[i+1][j+1] == 0: 
                            if self.a[i][j+1] == 0 and self.a3[i][j+1] == 0: 
                                self.a[i][j+1] = 2 
                                self.a3[i][j+1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j+1] = 1 
                            elif self.a[i+1][j] == 0 and self.a3 [i+1][j] == 0: 
                                self.a[i+1][j] = 2 
                                self.a3[i+1][j] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j+1] = 1 
                        elif self.a[i+1][j] == 2 and self.a3[i+1][j] == 0:  
                            if self.a[i][j+1] == 0 and self.a3[i][j+1] == 0: 
                                self.a[i][j+1] = 2 
                                self.a3[i][j+1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j] = 1 
                            elif self.a[i+1][j+1] == 0 and self.a3[i+1][j+1] == 0: 
                                self.a[i+1][j+1] = 2 
                                self.a3[i+1][j+1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j] = 1 
                            elif self.a[i][j-1] == 0 and self.a3[i][j-1] == 0: 
                                self.a[i][j-1] = 2 
                                self.a3[i][j-1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j] = 1 
                            elif self.a[i+1][j-1] == 0 and self.a3[i+1][j-1] == 0: 
                                self.a[i+1][j-1] = 2 
                                self.a3[i+1][j-1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j] = 1 
                        elif self.a[i+1][j-1] == 2 and self.a3[i+1][j-1] == 0:  
                            if self.a[i][j-1] == 0 and self.a3[i][j-1] == 0: 
                                self.a[i][j-1] = 2 
                                self.a3[i][j-1] = 1 
                                self.a3[i][j] == 1 
                                self.a3[i+1][j-1] = 1 
                            elif self.a[i+1][j] == 0 and self.a3[i+1][j] == 0: 
                                self.a [i+1][j] = 2 
                                self.a3[i+1][j] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i+1][j-1] = 1 
                        elif self.a[i][j-1] == 2 and self.a3[i][j-1] == 0:  
                            if self.a[i-1][j] == 0 and self.a3[i-1][j] == 0:  
                                self.a[i-1][j] = 2  
                                self.a3[i-1][j] = 1  
                                self.a3[i][j] = 1  
                                self.a3[i][j+1] = 1  
                            elif self.a[i-1][j-1] == 0 and self.a3[i-1][j-1] == 0:  
                                self.a[i-1][j-1] = 2  
                                self.a3[i-1][j-1] = 1  
                                self.a3[i][j]= 1  
                                self.a3[i][j-1] = 1  
                            elif  self.a[i+1][j] == 0 and self.a3[i+1][j] == 0: 
                                self.a[i+1][j] = 2 
                                self.a3[i+1][j] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i][j+1] = 1 
                            elif self.a[i+1][j-1] == 0 and self.a3[i+1][j-1] == 0: 
                                self.a[i+1][j-1] = 2 
                                self.a3[i+1][j-1] = 1 
                                self.a3[i][j] = 1 
                                self.a3[i][j-1] = 1 
         
         
         
 
 
                # 
              #  neib_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1] 
             #   if neib_sum < 2 or neib_sum > 3: 
            #        b[i][j] = 0 
           #     elif neib_sum == 3: 
          #          b[i][j] = 1 
         #       else: 
        #            b[i][j] = self.a[i][j] 
       #
           
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1):
                self.a3[i][j] = 0 
                if randint(1,50) == 1 and self.a[i][j] == 0:  
                    self.a[i][j] = 3
        #self.a = b 
  
  
    def print_field(self): 
        for i in range(self.n): 
            for j in range(self.m): 
                print(self.a[i][j], end="") 
            print() 
  
    def draw(self): 
        ''' 
       draw each element of matrix as a rectangle with white background and wall rectangle should have dself.ak grey background 
       ''' 
        color = "grey" 
        sizen = self.width // (self.n - 2) 
        sizem = self.height // (self.m - 2) 
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1): 
                print (self.a[i][j] , end = "") 
            print () 
        for i in range(1, self.n - 1): 
            for j in range(1, self.m - 1): 
                if (self.a[i][j] == 1): 
                    color = "black" 
                elif (self.a[i][j] == 2): 
                    color = "orange" 
                elif (self.a[i][j] == 3): 
                    color = "green" 
                else: 
                    color = "white" 
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) * sizen, (j) * sizem, fill=color) 
        self.step() 
        self.c.after(100, self.draw) 
  
class Player: 
    def __init__(self, c, x, y, size, color="RED"): 
        self.x = x 
        self.y = y 
        self.size = size 
        self.color = color 
        self.c = c 
        self.body = self.c.create_oval(self.x - self.size / 2, 
        self.y - self.size / 2, 
        self.x + self.size / 2, 
        self.y + self.size / 2, 
        fill=self.color) 
  
    def moveto(self, x, y): 
        self.mx = x 
        self.my = y 
        self.dx = (self.mx - self.x) / 50 
        self.dy = (self.my - self.y) / 50 
        self.draw() 
  
    def draw(self): 
  
        self.x += self.dx 
        self.y += self.dy 
        self.c.move(self.body, self.dx, self.dy) 
  
        print(abs(self.x)) 
        if abs(self.mx - self.x) > 0: 
            self.c.after(100, self.draw) 
  
  
    def distance(self, x, y): 
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5 
  
root = Tk() 
root.geometry("800x800") 
c = Canvas(root, width=800, height=800) 
c.pack() 
  
f = Field(c, 40, 40, 800, 800) 
f.print_field() 
  
''' 
p1 = Player(c, 25, 25, 20, "GREEN") 
p2 = Player(c, 375, 25, 20, "RED") 
  
p1.moveto(150, 200) 
p2.moveto(200, 300) 
''' 
  
root.mainloop() 
# c.create_oval(p.x + 5,p.y + 5,p.x+p.size + 5,p.y+p.size + 5)
