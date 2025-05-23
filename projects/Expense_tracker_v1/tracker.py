import pymysql

#connect to Mysql
connection = pymysql.connect(host='localhost',
                             user='Priya',
                             password='654321',
                             db='expense_tracker',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()

# cursor.execute('select * from expenses')
# result = cursor.fetchall()
# print(result)

def get_category_id(name):
    cursor.execute('select id from categories where name = %s',(name))
    result = cursor.fetchone()
    if result:
        print(result['id'])
        return result['id']
    else:
        return None


def add_expense():
    amount = float(input('Enter the amount : '))
    description = input('Enter the description : ')
    date = input('Enter date in (YYYY-MM-DD) : ')
    category = input('Enter Category : ')

    cat_id = get_category_id(category)
    if not cat_id:
        print('Category not found in our database')
        print('First add the category to the database')
        return None
    cursor.execute('Insert into expenses(amount,description,date,category_id) values (%s , %s, %s, %s)',(amount,description,date,cat_id))
    connection.commit()
    print('Expense added successfully')

def view_expenses():
    cursor.execute('''select e.Id,e.amount, e.description, e.date, c.name as category
                        from expenses e
                        inner join categories c on e.category_id = c.Id''')
    result = cursor.fetchall()
    print("ID | Amount | Description | Date | category")
    for exp in result:
        print(str(exp['Id']) + "|" + str(exp['amount']) + "|" + str(exp['description']) + '|' + str(exp['date']) + "|" + str(exp['category']))
    
def add_category():
    try:
        name = input('Enter the new category name : ')
        cursor.execute('Insert into categories (name) values (%s)',(name))
        connection.commit()
        print('Category added')
    except Exception as e:
        print('Category already added')

def delete_expense():
    category = input('Enter category to delete (will delete all entries of that category)')
    cat_id = get_category_id(category)
    if not cat_id:
        print('category is not found in our database')
        return None
    
    cursor.execute("Delete from expenses where category_id = %s",(cat_id))
    connection.commit()
    print('Expense deleted successfully')

def filter_by_category():
    category = input('Enter the category name : ')
    cat_id = get_category_id(category)
    if not cat_id:
        print('Category not found in our database')
        return None
    
    cursor.execute('''select e.Id,e.amount, e.description, e.date, c.name as category
                        from expenses e
                        inner join categories c on e.category_id = c.Id where e.category_id = %s''',(cat_id))
    result = cursor.fetchall()
    print("ID | Amount | Description | Date | category")
    for exp in result:
        print(str(exp['Id']) + "|" + str(exp['amount']) + "|" + str(exp['description']) + '|' + str(exp['date']) + "|" + str(exp['category']))
        
def count_by_month():
    month = input('Enter the month(in words format): ')
    
    cursor.execute(''' select monthname(date) as month,count(*) as total_count from expenses 
                   where monthname(date) = %s group by month''',(month))
    result = cursor.fetchall()
    print(result)
    if not result:
        print('No expenses for this month')
        return None
