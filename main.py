"""----------------------------------------------------------Enigma project-----------------------------------------------"""
"""---------------------------
   |------- Méric Chenu------|
   |------- 20/12/2021 ------|
   ---------------------------"""
from rotor_creation import *
from encryption import *
from decryption import *


array_rotors =shuffle_alphabet(2)
message_encrypted = enigma_encryption("ce message est un test, il sert à vérifier que mon enigma fonctionne !",array_rotors)

message_decrypted = enigma_decryption(message_encrypted,array_rotors)



