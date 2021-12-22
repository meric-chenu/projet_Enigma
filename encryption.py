array_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]


#Messages encryption with 2 rotors without movement
def simple_encryption(message,array_rotors):
    message = message.upper()
    message_encrypted = ""
    for i in range(len(message)):
        """if it's a space or a special character"""
        if(message[i] not in array_alphabet):

            message_encrypted+=message[i]
        else:

            index_rotor1 = array_alphabet.index(message[i])
            letter_rotor1 = array_rotors[0][index_rotor1]
            index_letter_rotor1 = array_alphabet.index(letter_rotor1)
            message_encrypted+=array_rotors[1][index_letter_rotor1]
    return message_encrypted

def rotation_left_rotor(rotor):
    index = len(rotor)-1
    letter_memory = None
    letter_memory2 = None
    first_letter = rotor[0]
    while index >= 0:
        if(index != 0):
            if(index == len(rotor)-1):
                current_index = rotor[index]
                letter_memory = rotor[index-1]
                rotor[index-1] = current_index
            else:
                current_index = rotor[index]
                letter_memory2 = rotor[index-1]
                rotor[index-1] = letter_memory
                letter_memory = letter_memory2
        else:
            rotor[len(rotor)-1] = first_letter

        index-=1
    return rotor
def enigma_encryption(message,array_rotors):
    print("message initial à crypter : ",message)
    rotor1 = array_rotors[0].copy()
    rotor2 = array_rotors[1].copy()
    message = message.upper()
    message_encrypted = ""
    counter_rotation = 0
    for i in range(len(message)):
        """if it's a space or a special character"""
        if (message[i] not in array_alphabet):

            message_encrypted += message[i]
        else:
            index_rotor1 = array_alphabet.index(message[i])
            letter_rotor1 = rotor1[index_rotor1]
            index_letter_rotor1 = array_alphabet.index(letter_rotor1)
            message_encrypted += rotor2[index_letter_rotor1]
            rotor1 = rotation_left_rotor(rotor1).copy()
            counter_rotation+=1
            if(counter_rotation == 26):
                rotor2 = rotation_left_rotor(rotor2).copy()
                counter_rotation = 0
    print("message_encrypted : ",message_encrypted)
    return message_encrypted