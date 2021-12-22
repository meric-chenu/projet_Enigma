from encryption import rotation_left_rotor

array_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]


def simple_decryption(message_encrypted,array_rotors):
    message_decrypted = ""
    for i in range(len(message_encrypted)):
        if(message_encrypted[i] not in array_alphabet):
            message_decrypted+=message_encrypted[i]
        else:
            index_letter_rotor2 = array_rotors[1].index(message_encrypted[i])
            letter_rotor2_decrypted = array_alphabet[index_letter_rotor2]
            index_letter_rotor1 =array_rotors[0].index(letter_rotor2_decrypted)
            message_decrypted+=array_alphabet[index_letter_rotor1]
    return message_decrypted


def rotation_right_rotor(rotor):
    letter_memory = None
    letter_memory2 = None
    final_letter = rotor[len(rotor)-1]
    for index in range(len(rotor)):
        if(index != len(rotor)-1):
            if(index == 0):
                current_index = rotor[index]
                letter_memory = rotor[index+1]
                rotor[index+1] = rotor[index]
            else:
                current_index = rotor[index]
                letter_memory2 = rotor[index+1]
                rotor[index+1] = letter_memory
                letter_memory = letter_memory2
        else:
            rotor[0] = final_letter
    return rotor

def enigma_decryption(message_encrypted,array_rotors):
    rotor1 = array_rotors[0].copy()
    rotor2 = array_rotors[1].copy()
    counter_rotation = 0
    #--------------------------------------------------Decryption--------------------------------------------------------
    message_decrypted = ""
    for index in range(len(message_encrypted)):
        if (message_encrypted[index] not in array_alphabet):
            message_decrypted += message_encrypted[index]
        else:
            index_letter_rotor2 = rotor2.index(message_encrypted[index])
            letter_rotor2_decrypted = array_alphabet[index_letter_rotor2]
            index_letter_rotor1 = rotor1.index(letter_rotor2_decrypted)
            message_decrypted += array_alphabet[index_letter_rotor1]
            rotor1 = rotation_left_rotor(rotor1).copy()
            counter_rotation+=1
            if (counter_rotation == 26):
                rotor2 = rotation_left_rotor(rotor2).copy()
                counter_rotation = 0


    print("message_decrypted : ",message_decrypted)
    return message_decrypted

