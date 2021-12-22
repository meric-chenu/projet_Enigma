import random as rd

#this function creates and returns the number of rotor passed in parameters
def shuffle_alphabet(rotors_number):
    array_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    rotors_array = []
    number = 0
    while number < rotors_number:
        array_alphabet2 = array_alphabet.copy()
        rd.shuffle(array_alphabet2)
        rotors_array.append(array_alphabet2)
        number+=1
    return rotors_array