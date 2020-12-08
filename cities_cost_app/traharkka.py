'''
this is Lauri Suutari's project for Data Algorithms course @ uni oulu
'''

start = 0
end = 0
cities = 0
cost = 0

data = []
def file_open():
    '''
    opens the file for the project.
    '''
    temp = []
    file = open("graph1.txt", "r")
    string = file.readlines()
    for line in string:
        temp.append(line.rstrip('\n'))
    data = temp
    return data

def file_separate(sequence):
    '''
    separates each number in sequence for further work
    by first turning it into a string, then splitting
    each element and joining them into a list.
    '''
    temp = ' '.join([str(number) for number in sequence])
    temp = temp.split(' ')
    return temp

def fixing_sep_list(sequence):
    '''
    removes the first 2 indexes from the
    separated list. (place-bo for now)
    '''
    fixed_sep_list = sequence
    fixed_sep_list.pop(0)
    fixed_sep_list.pop(0)
    return fixed_sep_list

def find_cities(sequence):
    temp = []
    for city in sequence:
        if city not in temp:
            temp.append(city)
    print(temp)
    return temp

if __name__ == "__main__":

    data = file_open()
    sep_list = file_separate(data)
    start = sep_list[2]
    end = sep_list[-1]
    fixed_sep_list = fixing_sep_list(sep_list) 
    cost = fixed_sep_list[2::3]

    #this is a list made just to find the number of cities
    fsl_wo_cost = [item for item in fixed_sep_list if item not in cost]

    cities = find_cities(fsl_wo_cost)
    



    