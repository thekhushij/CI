import streamlit as st

#building ui
st.title('Power Calculator')
st.write('Enter a number to calculate its square ,cube and fith power.')

#get user input 
n = st.number_input('Enter an integer', value=1 ,step=1)

#calculate results
square = n ** 2
cube = n ** 3
fith = n ** 5

#display results
st.write(f"The square of {n} is : {square}")
st.write(f"The cube of the {n} is:{cube}")
st.write(f"The fith power of the {n} is :{fith}")

#use : python3 -m streamlit run file_name : to run the file 
