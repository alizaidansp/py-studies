from datetime import datetime

def your_age_in_the_future(age, year):
    current_year = datetime.now().year
    real_age=current_year-year
    if real_age < age:
        return f'you are not born yet'
    elif real_age == age:
        age_in_ten_years=real_age+10
        return f'you are now {age} years old and you will be {age_in_ten_years} years old in 10 years'
    else:
        return f'you are {real_age} years old'
    return age

def school_age_calculator(age, name):
    if age < 5:
        return f'enjoy the time, {name} is too young to go to school at age {age}'
    elif age == 5:
        return f'congratulations {name} is now 5 years old and can start school'
    else:
        return f'{name} is {age} years old and can go to school'
        
    


# print(school_age_calculator(500,"ALi Usman Zaidan"))
print(your_age_in_the_future(24,2000))