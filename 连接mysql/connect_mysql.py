import pymysql
db = pymysql.connect(host="127.0.0.1",user="root",password="Allen007007",database='ibm_db')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print(data)
cursor.execute("select * from employee")
result = cursor.fetchall()
for row in result:
    id = row[0]
    name = row[1]
    gender = row[2]
    age = row[3]
    department = row[4]
    region = row[5]
    salary = row[6]
    birth = row[7]
    print("id=%d, name=%s,gender=%s, age=%d, department=%s, region=%s, salary=%.2f, birth=%s" 
      % (id, name,gender, age, department, region, salary, birth))


