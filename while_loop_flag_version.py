def get_starting_number():
    while True:
        bottle = input('How many bottles of beer on the wall?')
        if bottle.isnumeric():
            bottle = int(bottle)
            if bottle >= 1:
                return bottle
            else:
                print('Please Enter the number of bottle 1 or greater.')
        else:
            print('Please enter a vaild integer of 1 or greater.')
        
def sing(num_bottles):
    count = num_bottles
    sing = True
    while sing:
        if count == 1:
            print(f'{count} bottle of beer on the wall, {count} bottle of beer.')
            print('Take it down, pass it around, no more bottles of beer on the wall!\n')
            sing = False
        else:
            next_bottle = count - 1
            if next_bottle == 1:
                b = 'bottle'
            else:
                b = 'bottles'
            print(f'{count} bottles of beer on the wall, {count} bottles of beer.')
            print(f'Take one down, pass it around, {next_bottle} {b} of beer on the wall.\n')
        count = count - 1