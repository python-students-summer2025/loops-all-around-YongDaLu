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
    for i in range(num_bottles, 0, -1):
            if i == 1:
                print(f'{i} bottle of beer on the wall, {i} bottle of beer.')
                print('Take it down, pass it around, no more bottles of beer on the wall!\n')    
            else:
                if i == 1:
                    b1 = 'bottle'
                else:
                    b1 = 'bottles'
                if i-1 == 1:
                    b2 = 'bottle'
                else:
                    b2 = 'bottles'
                
                print(f'{i} {b1} of beer on the wall, {i} {b1} of beer.')
                print(f'Take one down, pass it around, {i-1} {b2} of beer on the wall.\n')
