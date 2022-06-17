# Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar(cipher_text, shift_amount, cipher_direction):

    # dealing with the case when the shift number is higher than the number of letters
    # with 26 letters, the result of a shift by 27 is the same as a shift by 1
    if shift_amount > len(alphabet):
        shift_amount = shift_amount % len(alphabet)

    # for decoding
    if cipher_direction == "decode":
        shift_amount = len(alphabet) - shift_amount

    text_out = ""

    for char in cipher_text:
        if char in alphabet:
            index_in = alphabet.index(char)
            index_out = index_in + shift_amount

            # if the new index would end up beyond the list, roll over to the beginning
            if index_out > len(alphabet) - 1:
                index_out -= len(alphabet)

            text_out += alphabet[index_out]

        # if not a letter, just copy the original character
        else:
            text_out += char

    return text_out



# repeat unless the user enters "no"
while True:
    print("Type \"encode\" to encrypt, type \"decode\" to decrypt:")
    direction = ""
    while True:
        direction = input("> ").lower()
        if direction == "encode" or direction == "decode":
            break
        else:
            print("Invalid choice. Please enter \"encode\" or \"decode\".")

    print("Enter your message:")
    text = input("> ").lower()

    print("Type the shift number:")

    shift = 0
    while True:
        shift_str = input("> ")
        if shift_str.isdigit():
            shift = int(shift_str)
            # reject any number that would result in a shift by 0 characters (i.e. 0 and multiplies of 26)
            if shift % len(alphabet) == 0:
                print(f"Invalid choice. Shifting by {shift} would result in an identical message.")
            else:
                break
        else:
            print("Invalid choice. Please enter a positive integer.")

    result = caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)

    # printing the result
    print(f"The message \"{text}\" {direction}d using a shift of {shift} is \"{result}\".")

    # condition to break out of the infinite loop
    print("Type \"yes\" if you want to go again. Otherwise type \"no\".")
    choice = input("> ").lower()
    # skip checking the input, just keep going until "no" is entered
    if choice == "no":
        break

print("Goodbye.")
