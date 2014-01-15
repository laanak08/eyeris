import datetime
def from_webform(ds):
    """ Converts date and time input from
    the web format into a datetime object"""
    dt = datetime.datetime.strptime(ds, '%d-%b-%Y %H:%M:%S')
    return dt

def to_mwaFormat(dt):
    """Takes a datetime objects and returns a string to
    that conforms the mwa extract function"""
    st = dt.strftime('%m/%d/%y %I:%M %p')
    return st

def from_mwaExtract(ds, ts):
    """Creates a datetime string from two columns in mwa extract
    designed to be inserted in SQLite in ISO datetime. Designed for speed
    YYYY-MM-DD HH:MM:SS is the goal input us MM-DD-YYYY  rest"""
    (m, d, y) = ds.split('/')
    return y+'-'+m+'-'+d+' '+ts

if __name__ == '__main__':
    test = from_webform('12-Jan-2012 23:59:59')
    print test


    mwastime = to_mwaFormat(test)
    print mwastime

    mwacols = ['04/03/2013','09:29:00']
    st = from_mwaExtract(mwacols[0],mwacols[1])
    print st
