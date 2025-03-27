from art import text2art, lprint
from colorama import Fore, init
from rich.console import Console
from typing import List, Dict

# Paramètres
init(autoreset=True)
colors = [Fore.GREEN, Fore.RED, Fore.YELLOW]
word = "BIENVENUE !"
letter_style = text2art
intro = "\n" + Fore.BLUE + "Vous allez utiliser un algorithme appartenant à la cryptographie symétrique : " + \
    "\n" + "\n".join([Fore.BLUE + line for line in text2art("ENIGMA", font="straight").splitlines()])
option_question = Fore.BLUE + \
    "Vous pouvez choisir de crypter (tapez C) ou de  décrypter (tapez D) une chaîne de caractères "

rotor_question = Fore.BLUE + \
    "Veuillez choisir la configuration des rotors (ex = abc) : "
word_question = Fore.BLUE + "Veuillez entrez la chaîne de caractères "


def coloring_letters(colors, word, letter_style):
    art_lines = []
    for i, letter in enumerate(word):
        art_letter = letter_style(letter)
        art_letter_lines = art_letter.splitlines()

        while len(art_lines) < len(art_letter_lines):
            art_lines.append("")

        for j in range(len(art_letter_lines)):
            art_lines[j] += colors[i % len(colors)] + art_letter_lines[j] + "  "

    for line in art_lines:
        print(line)

def init():
    coloring_letters(colors, word, letter_style)
    lprint(length=87, height=2, char="-")
    return print(intro)


class EnigmaMachine:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.rotor1 = list('ekmflgdqvzntowyhxuspaibrcj')
        self.notch1 = 'q'
        self.rotor2 = list('ajdksiruxblhwtmcqgznpyfvoe')
        self.notch2 = 'e'
        self.rotor3 = list('bdfhjlcprtxvznyeiwgakmusqo')
        self.notch3 = 'v'
        self.reflector = {
            'a': 'y', 'y': 'a', 'b': 'r', 'r': 'b', 'c': 'u', 'u': 'c',
            'd': 'h', 'h': 'd', 'e': 'q', 'q': 'e', 'f': 's', 's': 'f',
            'g': 'l', 'l': 'g', 'i': 'p', 'p': 'i', 'j': 'x', 'x': 'j',
            'k': 'n', 'n': 'k', 'm': 'o', 'o': 'm', 't': 'z', 'z': 't',
            'v': 'w', 'w': 'v'
        }
        self.rotor1_pos = 0
        self.rotor2_pos = 0
        self.rotor3_pos = 0
        self.initial_pos1 = 0
        self.initial_pos2 = 0
        self.initial_pos3 = 0

    def set_rotor_positions(self, pos1: str, pos2: str, pos3: str):
        self.rotor1_pos = self.alphabet.index(pos1.lower())
        self.rotor2_pos = self.alphabet.index(pos2.lower())
        self.rotor3_pos = self.alphabet.index(pos3.lower())
        self.initial_pos1 = self.rotor1_pos
        self.initial_pos2 = self.rotor2_pos
        self.initial_pos3 = self.rotor3_pos


    def reset_rotors(self):
        self.rotor1_pos = self.initial_pos1
        self.rotor2_pos = self.initial_pos2
        self.rotor3_pos = self.initial_pos3

    def rotate_rotors(self):
        rotor1_at_notch = self.alphabet[self.rotor1_pos] == self.notch1
        rotor2_at_notch = self.alphabet[self.rotor2_pos] == self.notch2
        if rotor2_at_notch:
            self.rotor2_pos = (self.rotor2_pos + 1) % 26
            self.rotor3_pos = (self.rotor3_pos + 1) % 26
        elif rotor1_at_notch:
            self.rotor2_pos = (self.rotor2_pos + 1) % 26
        self.rotor1_pos = (self.rotor1_pos + 1) % 26

    def apply_rotor_forward(self, char: str, rotor: list, offset: int) -> str:
        pos = (self.alphabet.index(char) + offset) % 26
        char = rotor[pos]
        pos = (self.alphabet.index(char) - offset) % 26
        return self.alphabet[pos]

    def apply_rotor_backward(self, char: str, rotor: list, offset: int) -> str:
        pos = (self.alphabet.index(char) + offset) % 26
        char = self.alphabet[pos]
        pos = rotor.index(char)
        pos = (pos - offset) % 26
        return self.alphabet[pos]

    def apply_reflector(self, char: str) -> str:
        return self.reflector[char]

    def process_char(self, char: str, rotate: bool) -> str:
        if char not in self.alphabet:
            return char
        if rotate:
            self.rotate_rotors()
        char = self.apply_rotor_forward(char, self.rotor1, self.rotor1_pos)
        char = self.apply_rotor_forward(char, self.rotor2, self.rotor2_pos)
        char = self.apply_rotor_forward(char, self.rotor3, self.rotor3_pos)
        char = self.apply_reflector(char)
        char = self.apply_rotor_backward(char, self.rotor3, self.rotor3_pos)
        char = self.apply_rotor_backward(char, self.rotor2, self.rotor2_pos)
        char = self.apply_rotor_backward(char, self.rotor1, self.rotor1_pos)
        return char

    def encrypt(self, text: str) -> str:
        result = ""
        for i, c in enumerate(text.lower()):
            rotate = (i > 0)
            result += self.process_char(c, rotate)
        return result

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)


def user_selection(option, pos_rotor, enigma):
    if option == "C" or option == "c":
        enigma.set_rotor_positions(pos_rotor[0], pos_rotor[1], pos_rotor[2])  
        enigma.reset_rotors() 
        text = input(word_question + " à crypter : ")
        
        if not all(c.isalpha() or c == ' ' for c in text):  
            print(Fore.RED + "❌ Erreur : Entrez uniquement des lettres (a-zA-Z) et des espaces.")
            return user_selection(option, pos_rotor, enigma)
        
        return enigma.encrypt(text)
    
    elif option == "D" or option == "d":
        enigma.set_rotor_positions(pos_rotor[0], pos_rotor[1], pos_rotor[2])  
        enigma.reset_rotors()  
        text = input(word_question + " à décrypter : ")

     
        if not all(c.isalpha() or c == ' ' for c in text):  
            print(Fore.RED + "❌ Erreur : Entrez uniquement des lettres (a-zA-Z) et des espaces.")
            return user_selection(option, pos_rotor, enigma)

        return enigma.decrypt(text)
    
    else:
        print(Fore.RED + "❌ Entrez correctement la lettre soit C ou D !")
        return user_selection(input(Fore.BLUE + "Réssayer : "), pos_rotor, enigma)



def main():
    enigma = EnigmaMachine()

    init()

    while True:
        try:
            positions = input(
                rotor_question).lower()
            if len(positions) != 3 or not all(c in enigma.alphabet for c in positions):
                raise ValueError(Fore.RED +"❌ Entrez exactement 3 lettres de l'alphabet sans accents et sans espaces.")
            enigma.set_rotor_positions(
                positions[0], positions[1], positions[2])
            break
        except ValueError as e:
            print(f"{e}")

    while True:
        choice = input(option_question +"(q pour quitter): ").lower()
        if choice == 'q':
            break

        if choice not in ['c', 'd']:
            print(Fore.RED +"❌ Entrez correctement la lettre soit C ou D !")
            continue

        result = user_selection(choice, positions, enigma)

        if choice == 'c':
            print(Fore.BLUE + "Texte chiffré :" + Fore.GREEN + f"{result}")
            choice = input(Fore.BLUE + \
                                   
                                   "Souhaitez-vous déchiffrer ce texte ? (oui/non) : ").lower()
            if choice == 'oui':
                enigma.reset_rotors()
                print(Fore.BLUE + "Texte déchiffré : " + Fore.GREEN + f"{enigma.decrypt(result)}")
       
        elif choice == 'd':
            print(Fore.BLUE + "Texte déchiffré :" + Fore.GREEN + f"{result}")
            choice = input(Fore.BLUE + \
                                   
                                   "Souhaitez-vous chiffrer ce texte ? (oui/non) : ").lower()
            if choice == 'oui':
                enigma.reset_rotors()
                print(Fore.BLUE + "Texte chiffré : " + Fore.GREEN + f"{enigma.encrypt(result)}")
        else:
            print(Fore.BLUE + "Texte chiffré : " + Fore.GREEN + f"{result}")

       
        if choice == 'q':
            break


main()
