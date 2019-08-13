def save_numbers(number_of_people: int, number_of_vegans: int):
    success = False
    if ((type(number_of_people) == type(number_of_vegans) == type(0)) and
            0 <= number_of_vegans <= number_of_people <= 500):
        f = open('numbers.txt', 'w')
        f.write(str(number_of_people) + '\n')
        f.write(str(number_of_vegans))
        f.close()
        success = True
        return success
    else:
        return success

def read_numbers():
    with open('numbers.txt', 'r') as file:
        string = file.read()
        number_of_people, number_of_vegans = [int(i) for i in string.split("\n")]
        return number_of_people, number_of_vegans














