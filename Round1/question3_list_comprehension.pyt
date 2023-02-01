from datetime import datetime, timedelta

def compute_prev_date(dates_list:list):
    """
    This method takes in a list of dates 
    and returns a list with the corresponding 
    previous days of the dates in the input list.
    The output list has a different format from 
    the input list. 
    """
    #Converts the list of string into datetime
    fomat_list = [datetime.strptime(d,'%Y-%m-%d') for d in dates_list ]

    #computes the previous date of the dates contained in the dates list
    previous_list = [datetime.date(d) - timedelta(1) for d in fomat_list ]

    #returns the previous day list in the specified format
    print( [datetime.strftime(d,'%d %b %Y') for d in previous_list])

#prints the dates previous day in the specified format
date_list = ['1999-01-21', '2022-12-30', '2099-09-17']
compute_prev_date(date_list)