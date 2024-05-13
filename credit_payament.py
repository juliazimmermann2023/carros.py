from config import *
from payament_times.in_time import *
from payament_times.six_months import sixmonths
from payament_times.three_months import three_months
from payament_times.twelve_months import twelvemonths
def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif(time_option == 2):
        return (three_months(desired_car))
    elif(time_option == 3):
        return (sixmonths(desired_car))
    elif(time_option == 4):
        return (twelvemonths(desired_car))