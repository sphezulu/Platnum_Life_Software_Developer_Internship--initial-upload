from datetime import datetime

def is_date_format_correct(date:str)->bool:

    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """
    #your code here#
    #intialising and assignment of the format variable#
    format = "%Y-%m-%d"
    match = True

    #tries to match the input string with the specified format and returns the results#
    try:
        match = bool(datetime.strptime(date,format))
    except ValueError:
        match = False

    return match

#prints the whether or not the date is in a specified format     
print (is_date_format_correct('20-09-99'))