# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:21:46 2023

@author: Sanchita Gunjal
"""

def make_pizza(size,*toppings):
    print(f"\nmaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
