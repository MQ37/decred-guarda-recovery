import base58

def main():
    guarda_private_key = input("Enter your Guarda private key: ")
    guarda_private_key_decoded = base58.b58decode(guarda_private_key)
    guarda_private_key_hex = guarda_private_key_decoded.hex()

    wif_key = guarda_private_key_hex[4:64+4]
    print("Your WIF key is: ", wif_key)

if __name__ == '__main__':
    main()
