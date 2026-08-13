import pandas as pd

def highest_salary(employees, departments):
      
      for i in employees:
            if i["salary"]<0:
                  return f"ERROR  the employees must have postive values"
            else:
                  for j in departments:
                        if j["id"] == i["departmentID"]:
                              i["job"] = j["name"]
      
      emp = pd.DataFrame(employees)
      
      mx = emp.groupby("job")["salary"].transform("max")
      
      hightest_paid = emp[emp["salary"] == mx]
      return hightest_paid
      

