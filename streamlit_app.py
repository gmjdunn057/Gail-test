import streamlit as st
import random

st.title("🎈 My test app")
st.write(
    "Guess a number between 1-100"
)
if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(1,100)
    st.session_state.guess = False

guess = st.number_input('Input a number between 1 and 100',min_value=1, max_value=100)

if st.button('Submit Guess'):
    st.write('You guessed '(str(guess)))
    if guess < st.session_state.secret:
        st.warning('Sorry, too low')
    elif guess > st.session_state.secret:
        st.warning('Sorry, too high')
    else:
        st.success('Yay! You guessed it!')
if guess==st.session_state.secret:
    if st.button('Play again'):
        st.session_state.secret = random.randint(1,100)
        st.rerun()    
