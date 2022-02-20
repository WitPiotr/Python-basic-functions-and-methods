#Import required libraries
try:
    from faker import Faker
    import pandas as pd
    import time
    # from faker.providers.ssn.pl_PL.__init__ import *
except:
    print("You can't import library.")


def generate_ssns(record_number):
    # Function generates and return chosen quantity of PESELs
    # parameter: record_number - define how many PESEL numbers will be generated

    # Implementation Faker library:
    fake = Faker('pl_PL')

    # Create temporary list:
    list_tmp = []

    # Creating list of PESELs
    for i in range(record_number):
        list_tmp.append(fake.ssn())

    # Transposition list on series object:
    pesels = pd.Series(data=list_tmp, dtype=object)
    return pesels

def generate_unique_ssns(date_from, date_to, sex):
    # Function generates and return PESELs including the date range and sex
    # parameter: date_from - start date
    # parameter: date_to - end date
    # parameter: sex

    # Implementation Faker library:
    fake = Faker('pl_PL')

    # Create temporary list:
    list_tmp = []
    dates_tmp = pd.Series(pd.date_range(start=date_from, end=date_to))

    # Creating list of PESELs
    for i in dates_tmp:
        list_tmp.append(fake.pesel(i, sex=sex))

    # Transposition list on series object:
    pesels = pd.Series(data=list_tmp, dtype=object)
    return pesels

def validate_ssn(pesel, sex, birthday):
    # Function validates PESEL number including: sex and birthday
    # parameter: PESEL - Universal Electronic System for Registration of the Population in Poland
    # parameter: sex
    # parameter: birthday

    # Taking necessary items from the PESEL
    year_pesel = str(pesel)[0:2]
    month_pesel = int(str(pesel)[2:4])
    day_pesel = int(str(pesel)[4:6])
    sex_pesel = int(str(pesel)[-2])

    # Validate birthday
    if birthday !="":
        birthday_tmp = pd.date_range(start=birthday, end=birthday)
        fake = Faker('pl_PL')
        for i in birthday_tmp:
            pesel_generate = fake.pesel(i, sex=sex)

        if str(pesel_generate)[0:6] == str(pesel)[0:6]:
            correctness_date = "Yes"
        else:
            correctness_date = "No"

    else:

        try:

            if month_pesel > 0 and month_pesel <= 12:
                year = int("19" + year_pesel)
                month = int(month_pesel)
            elif month_pesel - 20 > 0 and month_pesel - 20 <= 12:
                year = int("20" + year_pesel)
                month = int(month_pesel) - 20
            elif month_pesel - 40 > 0 and month_pesel - 40 <= 12:
                year = int("21" + year_pesel)
                month = int(month_pesel) - 40
            elif month_pesel - 60 > 0 and month_pesel - 60 <= 12:
                year = int("22" + year_pesel)
                month = int(month_pesel) - 60
            elif month_pesel - 80 > 0 and month_pesel - 80 <= 12:
                year = int("18" + year_pesel)
                month = int(month_pesel) - 80
            day = int(day_pesel)
            df = pd.DataFrame({'year': [year],
                               'month': [month],
                               'day': [day]})

            print(pd.to_datetime(df))
            correctness_date = "Yes"

        except:
            correctness_date = "No"

    # Validate sex
    if sex != "":

        if sex_pesel % 2 == 0 and sex == "F":
            correctness_sex = "Yes"
        elif sex == "M" and (sex_pesel == 1 or sex_pesel == 3 or sex_pesel == 5 or sex_pesel == 7 or sex_pesel == 9):
            correctness_sex = "Yes"
        else:
            correctness_sex = "No"
    else:
        correctness_sex = "Yes"

    # Validate number quantity
    if len(str(pesel)) == 11:
        correctness_number_quantity = "Yes"
    else:
        correctness_number_quantity = "No"


    # Validate PESEL
    if correctness_number_quantity == "Yes"  and correctness_date == "Yes" and correctness_sex == "Yes":
        print("PESEL is correct\n")
    else:
        print("PESEL isn't correct\n")

print("Task 1.1:\t")
task_1_1 = generate_ssns(5)
print(task_1_1)
print("--------------------------------------------------------------------------\t\n")

print("Task 1.2:\t")
print("Printing PESELs for males:")
task_1_2_m = generate_unique_ssns('2000-03-14', '2000-03-22', "M")
print(task_1_2_m)
print("Printing PESELs for females:")
task_1_2_f = generate_unique_ssns('1994-03-14', '1994-03-18', "F")
print(task_1_2_f)
print("--------------------------------------------------------------------------\t\n")

print("Loops:")
# loop 10 generate_ssns
print("Time of generate_ssns loop 10:")

# It's a possibility to print function result:
# vals  = [print(generate_ssns(5)) for i in range(10)]

start_time = time.time()
f  = [generate_ssns(1) for i in range(10)]
print(" %s seconds \n" % (time.time() - start_time))


# Loop 100 generate_ssns
print("Time of generate_ssns loop 100:")
start_time = time.time()
f  = [generate_ssns(1) for i in range(100)]
print(" %s seconds \n" % (time.time() - start_time))


# Loop 1000 generate_ssns
print("Time of generate_ssns loop 1000:")
start_time = time.time()
f  = [generate_ssns(1) for i in range(1000)]
print(" %s seconds \n" % (time.time() - start_time))


# Loop 10 generate_unique_ssns
print("Time of generate_unique_ssns loop 10:")
start_time = time.time()
f  = [generate_unique_ssns('1994-03-14', '1994-03-18', "F") for i in range(10)]
print(" %s seconds \n" % (time.time() - start_time))

# Loop 100 generate_unique_ssns
print("Time of generate_unique_ssns loop 100:")
start_time = time.time()
f  = [generate_unique_ssns('1994-03-14', '1994-03-18', "F") for i in range(100)]
print(" %s seconds \n" % (time.time() - start_time))

# Loop 1000 generate_unique_ssns
print("Time of generate_unique_ssns loop 1000:")
start_time = time.time()
f  = [generate_unique_ssns('1994-03-14', '1994-03-18', "F") for i in range(1000)]
print(" %s seconds " % (time.time() - start_time))
print("--------------------------------------------------------------------------\t\n")

print("Task 1.3")
print("Times of execution of both functions are similar to each other despite bigger amount of input values\nfor function: 'generate_unique_ssns',that's why it isn't necessary to create function: generate_unique_ssns_opt")

print("Task 1.4\n")

print("Example 1 - correct PESEL, sex female:")
validate_ssn(94052006067, "F", '1994-05-20')

print("Example 2 - correct PESEL sex male:")
validate_ssn(94052006057, "M", '1994-05-20')

print("Example 3 - incorrect sex:")
validate_ssn(94052006067, "M", '1994-05-20')

print("Example 4 - incorrect birthday:")
validate_ssn(94052006067, "F", '1996-05-20')

print("Example 5 - incorrect birthday and sex:")
validate_ssn(94052006067, "M", '1996-05-20')

print("Example 6 - correct PESEL, birthday >= 2000 to 2099:")
validate_ssn('05252006067', "F", '2005-05-20')

print("Example 7 - correct PESEL, birthday >= 2100 to 2199:")
validate_ssn('30471506077', "M", '2130-07-15')

print("Example 8 - correct PESEL, birthday >= 2200 to 2299:")
validate_ssn('30671506077', "M", '2230-07-15')

print("Example 9 - correct PESEL, birthday >= 1800 to 1899:")
validate_ssn('99871506077', "M", '1899-07-15')

print("Example 10 - incorrect birthday, birthday >= 1800 to 1899:")
validate_ssn('99871506077', "M", '1905-07-15')

print("Example 11 - incorrect sex, birthday >= 1800 to 1899:")
validate_ssn('99871506077', "F", '1899-07-15')
