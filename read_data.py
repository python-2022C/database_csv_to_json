import csv

def read_csv(filename:str)->list:
    """
    CSV file name is given split by comma and new line,
    then add to list

    Arguments:
        filename(str): parameter
    Returns:
        list: nested list
    """
    # Open CSV file
    with open(filename) as csvfile:
        CSV = csv.reader(csvfile)
        return list(CSV)
