import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['fatto123', 'fatto123', 'fatto123', 'fatto123', 'fatto123', 'fatto123']).generate()
print(hashed_passwords)