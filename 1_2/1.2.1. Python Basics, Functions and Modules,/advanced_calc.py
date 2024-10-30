# advanced calculator (3)

# Todo:
# create virtual environment for this project
# python -m venv myenv

import calculator_module as basic_calc
# importing calculator_module for further processing
def advanced_calc():
    addition_solution = basic_calc.addition(1,2)
    sub_solution=basic_calc.sub(1,2)
    multiplication_solution=basic_calc.multiply(1,2)
    
    print(f"{addition_solution},{sub_solution},{multiplication_solution}")
    
advanced_calc()