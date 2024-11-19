import random
import streamlit as st # pip install streamlit

secret_word = random.choice(["hello"])
letters_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Variables
answer = ['_'] * len(secret_word)
chances = 6

# Screen of the game
st.title("Hangman Game")
st.write("Guess the word:")
st.write(" ".join(answer))
st.write(f"Chances left: {chances}")

while chances > 0:
    # Print actual answer
    st.header("Secret word: " + " ".join(answer))
    
    # Ask for a letter
    letter = st.text_input("Enter a letter:", value="", key="")
    if letter:
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            st.error("Please enter a single letter.")

    
    # Check if the letter is in the word
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                answer[i] = letter
            
    else: 
        chances -= 1
        st.error(f'Letter {letter} is not in the word! {chances} chances remaining.')
        
    # check if the word is discovered
    if "_" not in answer:
        st.success("Congratulations! You won!")
        break

if chances == 0:
    st.error("You lost! The word was: " + secret_word)