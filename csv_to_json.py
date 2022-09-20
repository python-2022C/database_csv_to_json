from tinydb import TinyDB
from read_data import read_csv

def csv_to_json(data:list)-> None:
    """
    Given csv list turn into tinydb database

    Arguments:
        data(list): paramenter
    Returns:
        None
    """
    # Create Database
    db = TinyDB('db.json')

    # Create Table
    table = db.table(name='Mobile')

    # fields
    ids, model, company, price = data[0]
    # docs
    list_of_docs = [{ids: row[0], model: row[1], company: row[2], price: row[3]} for row in data[1:]]

    # Insert into Table
    table.insert_multiple(documents=list_of_docs)


data = read_csv(filename='specifications.csv')
csv_to_json(data=data)