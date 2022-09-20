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
    with open(file=filename) as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        return rows