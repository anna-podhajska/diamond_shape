#practising loops in python#

space = ' '
number_of_stars_in_row = 0  # in a row
spaces_number = 0
gwiazdka = "*"

raw = raw_input('Determine the width of the shape by providing a number: ')

try:

    max_no_of_stars = int(raw)

except:
    print ' error '

spaces_number = int(raw)

upper_part = True
lower_part = False

while upper_part:

	number_of_stars_in_row = number_of_stars_in_row + 1
	spaces_number = spaces_number - 1

	print spaces_number * space,
	print '*',
	print (number_of_stars_in_row * gwiazdka) * 2,
	print '*'

	if number_of_stars_in_row == max_no_of_stars:
		lower_part = True
		upper_part = False

while lower_part:

	number_of_stars_in_row = number_of_stars_in_row - 1
	spaces_number = spaces_number + 1

	print spaces_number * space,
	print '*',
	print (number_of_stars_in_row * gwiazdka) * 2,
	print '*'

	if spaces_number == max_no_of_stars: break
	#lower_part = False
            #upper_part = True
