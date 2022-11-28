from random import choice
hours = ['Open 9 to 5 daily', "closed after 6"]

def pick():   #open or closed
    """Return random hours"""
    return choice(hours)