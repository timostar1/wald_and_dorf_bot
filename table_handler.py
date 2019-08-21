def first_blank_row_finder(table, biggest_column):
    value = True
    first_blank_row = 1
    while value != None:
        value = table.cell(row=first_blank_row, column=biggest_column).value
        first_blank_row += 1
    first_blank_row -= 1
    return first_blank_row