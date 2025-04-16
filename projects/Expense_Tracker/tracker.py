import pymysql

#connect to Mysql
connection = pymysql.connect(host='localhost',
                             user='bharath',
                             password='12345678',
                             db='expense_tracker',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()

cursor.execute('select * from expenses')
result = cursor.fetchall()
print(result)

def get_category_id(name):
    cursor.execute('select id from categories where name = %s',(name))
    result = cursor.fetchone()
    print(result['id'])
def add_expense():
    amount = float(input('Enter the amount : '))
    description = input('Enter the description : ')
    date = input('Enter date in (YYYY-MM-DD) : ')
    category = input('Enter Category : ')


get_category_id('Food')