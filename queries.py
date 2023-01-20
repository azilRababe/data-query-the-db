# pylint:disable=C0111,C0103

# Implement query_orders to get all the orders by ascending OrderID.
def query_orders(db):
    query='SELECT * from Orders ORDER BY OrderID '
    db.execute(query)
    res= db.fetchall()
    print(res)
    return res

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query='SELECT * FROM Orders where OrderDate > ? and OrderDate <= ?'
    db.execute(query,(date_from,date_to))
    res= db.fetchall()
    print(res)
    return res

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query='SELECT *, (ShippedDate-OrderDate) as TimeDelta  from Orders order by TimeDelta'
    db.execute(query)
    res= db.fetchall()
    print(res)
    return res
