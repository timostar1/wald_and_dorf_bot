def conservation_of_quantity(number_of_people, number_of_vegans):
    success = False
    f = open('quantity.txt', 'w')
    f.write(str(number_of_people) + '\n')
    f.write(str(number_of_vegans))
    f.close()
    success = True
    return success










