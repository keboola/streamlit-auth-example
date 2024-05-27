import streamlit as st
from keboola_streamlit import KeboolaStreamlit

#Required ROLE id
REQUIRED_ROLE_ID = st.secrets['REQUIRED_ROLE_ID']
STORAGE_API_TOKEN = st.secrets['STORAGE_API_TOKEN']
KEBOOLA_HOSTNAME = st.secrets['KEBOOLA_HOSTNAME']

kst = KeboolaStreamlit(KEBOOLA_HOSTNAME, STORAGE_API_TOKEN)

kst.set_dev_mockup_headers({
    'X-Kbc-User-Email': 'vojta@dev.com',
    'X-Kbc-User-Roles': ['123', '30e3f1fb-5028-4c1c-9a98-ebaf8b668898', 'abc'],
    'X-Forwarded-Host': 'https://mock-server/non-existing-app'
})


kst.authCheck(REQUIRED_ROLE_ID)

if st.button('Send event'):
    kst.createEvent(123, {'data':'content'})