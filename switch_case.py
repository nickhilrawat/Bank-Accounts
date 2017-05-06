# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:00:08 2017

@author: Tanya
"""
import SignUp
import SignIn
import AdminSignIn
import Quit
num=input("Enter the number")
# define the function blocks
options = {
        1 : SignUp,
        2 : SignIn,
        3 : AdminSignIn,
        4 : Quit,
}

options[num]()