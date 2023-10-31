# What is the Playfair cipher?

The Playfair cipher is a substitution cipher that encrypts plaintext in pairs of letters, called digraphs. It is a relatively simple cipher to implement and break, but it was widely used in the 19th century for military and diplomatic communications.

## How does the Playfair cipher work?

The Playfair cipher uses a 5x5 key matrix, which is generated from a keyword. The keyword is written across the top row of the matrix, from left to right, skipping any duplicate letters. The remaining letters of the alphabet are then filled in the matrix, in alphabetical order.

To encrypt plaintext, the plaintext is divided into digraphs. If the plaintext contains an odd number of letters, a filler letter (usually Z) is added to the end. Each digraph is then encrypted by replacing it with the pair of letters in the corresponding row and column of the key matrix. If the two letters of the digraph are in the same row or column, they are replaced by the letters to their right, respectively.

To decrypt ciphertext, the ciphertext is divided into digraphs and the reverse process is performed. Each digraph is replaced with the pair of letters in the corresponding row and column of the key matrix. If the two letters of the digraph are in the same row or column, they are replaced by the letters to their left, respectively.

## What is plaintext?

Plaintext is the original message that is to be encrypted. It is also referred to as the unencrypted message.

## What is a key?

A key is a secret piece of information that is used to encrypt or decrypt a message. In the case of the Playfair cipher, the key is a keyword that is used to generate the key matrix.

## How to use this source code

To use this source code, simply compile it and provide the plaintext and key as arguments to the program. The program will then encrypt or decrypt the plaintext, depending on the mode that you specify.

to edit plain_text and the key, you can open main.py

## to run the code:

    python main.py
    
# Conclusion

The Playfair cipher is a simple but effective substitution cipher. It is easy to implement and use, and it can be used to encrypt and decrypt messages of any length.

# Sample output
![img_sample](https://github.com/MuhammadAinurR/playfair-cipher/blob/main/output/output1.png)
![img_sample2](https://github.com/MuhammadAinurR/playfair-cipher/blob/main/output/output2.png)
