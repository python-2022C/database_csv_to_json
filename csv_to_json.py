from tinydb.database import Document
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

    # filtrs
    ids, model, company, price = data[0]
    # docs
    list_of_docs = [{model: " ".join(row[1].split()[:2]), company: row[2], price: row[3]} for row in data[1:]]

    # Clear data
    table.truncate()
    
    # Insert into Table
    table.insert_multiple(documents=list_of_docs)


data = read_csv('specifications.csv')
csv_to_json(data)