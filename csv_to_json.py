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
    table = db.table(name='Mobiles')

    for i in data[1:]:
        # ponename
        ponename = ' '.join(i[1].split()[:2])
        # Documents
        doc = Document(value={"model":ponename, "company":i[2], "price":i[3]}, doc_id=i[0])
        table.insert(doc)


data = read_csv('specifications.csv')
csv_to_json(data)