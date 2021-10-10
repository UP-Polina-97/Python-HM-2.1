from application import salary
from application import people
import datetime
from datetime import date


if __name__ == '__main__':
    today = date.today()
    print(f"Today is the {today}")
    f = salary.calculate_salary(23000)
    print(f)
    W = people.get_employees()
    print (W)


