import streamlit as st
from st_keyup import st_keyup
from email_validator import validate_email, EmailNotValidError

st.set_page_config(page_title='Email Validator', page_icon=':email:', layout='wide')

remove_default_lauout = '''
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
'''
st.markdown(remove_default_lauout,unsafe_allow_html=True)
st.markdown('---')
st.markdown('# Email Validation :email:')
st.markdown('---')

email = st_keyup('Email')

if not email:
      pass
else:
     try:
         email_valid = validate_email(email, )
         st.markdown(f'<p style="color: green;">{email}</p>',unsafe_allow_html=True)
         st.markdown('`Valid Email`')
     except EmailNotValidError as e:
         st.markdown(f'<p style="color: red;">{email}</p>',unsafe_allow_html=True)
         st.error(str(e))  