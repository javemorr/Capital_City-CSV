# Ask Expert
# Hour of Code HK - Python Lesson 9
# Date: 16 May 2021

# Classwork:  To convert the Capital_City.txt to Capital_City.csv
    # The conversion is done with a function: def copy_file()
    # The function is included in lines 43 to 48.

from tkinter import Tk, simpledialog, messagebox

print('Ask The Expert - Capital City of The World')

# This function handles the file reading from a data file
def read_from_file():
    with open('Capital_City.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            # print(country, city)
            the_world[country] = city

root = Tk()
root.withdraw()
the_world = {}

read_from_file()
# print(the_world)

#def write_to_file():
    #with open('Mother.txt', 'a') as file:
        #for i in range(10):
            #file.write('Happy Mother\'s Day!\n')
#write_to_file()

# This function will collect user input, and store data onto a file.
def write_to_file(country_name, city_name):
    print('I am inside "write to file()"')
    print(country_name, city_name)

    with open('Capital_City.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

def copy_file():
    q_file = open('Capital_City.txt')
    q_content = q_file.read()
    with open('Capital_City.csv', 'w') as file:
        file.write(q_content.replace('/', ',') + '\n')
copy_file()

while True:

    query_country = simpledialog.askstring('Country', 'Type The Name of a Country:')
    # How to print the user input data to your console?
    # print(query_country)

    # Check if the country is listed in the database.
    if query_country in the_world:
        result = the_world[query_country]
        print(result)
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '.')
    else:
        print('This country is NOT in the database.')
        new_city = simpledialog.askstring('Teach me!', 'I don\'t know! What is the capital city of ' + query_country + '?')

    write_to_file(query_country, new_city)


# End of Program