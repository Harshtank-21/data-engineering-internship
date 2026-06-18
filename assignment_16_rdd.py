from pyspark import SparkContext

sc = SparkContext("local", "EmployeeRDD")
sc.setLogLevel("ERROR")

lines = sc.textFile("employees.csv")
header = lines.first()
data = lines.filter(lambda row: row != header)

def parse(line):
    parts = line.split(",")
    return (int(parts[0]), parts[1], parts[2], int(parts[3]))

employees = data.map(parse)

# Sort by salary descending
sorted_emp = employees.sortBy(lambda x: x[3], ascending=False)
print("Employees sorted by salary (descending):")
for emp in sorted_emp.collect():
    print(f"  ID:{emp[0]} Name:{emp[1]} Dept:{emp[2]} Salary:{emp[3]}")

# Total salary per department
dept_salary = employees.map(lambda x: (x[2], x[3]))
dept_totals = dept_salary.reduceByKey(lambda a, b: a + b)
print("\nDepartment-wise total salary:")
for dept, total in dept_totals.collect():
    print(f"  {dept}: {total}")

# Top 3 highest paid employees
top3 = sorted_emp.take(3)
print("\nTop 3 highest paid employees:")
for emp in top3:
    print(f"  ID:{emp[0]} Name:{emp[1]} Dept:{emp[2]} Salary:{emp[3]}")

top3_rdd = sc.parallelize(top3)
top3_rdd.map(lambda x: f"{x[0]},{x[1]},{x[2]},{x[3]}").saveAsTextFile("top3_output")

sc.stop()
