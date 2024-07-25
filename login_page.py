#import streamlit as st; 
#username=st.text_input("Username"); 
#password=st.text_input("Password",type='password'); st.button("Login") and st.success("Logged In as {}".format(username)) if username=="your_username" and password=="your_password" else st.error("Invalid credentials")


#import streamlit as st

#username = st.text_input("Username")
#password = st.text_input("Password", type='password')

#if st.button("Login"):
 #   if username == "sudarshan" and password == "Sa@12345":
  #      st.success("Logged In as {}".format(username))
   # else:
    #    st.error("Invalid credentials")

import streamlit as st

# Set page title and favicon (optional)
st.set_page_config(page_title="Login Page", page_icon="🔒")

# Title
st.title("Create a Login Page")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type='password')

if st.button("Login"):
    if username == "Shan" and password == "Sa@1234":
        st.success("Logged In as {}".format(username))
    else:
        st.error("Invalid credentials")
