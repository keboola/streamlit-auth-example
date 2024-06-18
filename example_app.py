import streamlit as st
from keboola_streamlit import KeboolaStreamlit

#Required ROLE id
REQUIRED_ROLE_ID = st.secrets['REQUIRED_ROLE_ID']
STORAGE_API_TOKEN = st.secrets['STORAGE_API_TOKEN']
KEBOOLA_HOSTNAME = st.secrets['KEBOOLA_HOSTNAME']

kst = KeboolaStreamlit(KEBOOLA_HOSTNAME, STORAGE_API_TOKEN)

kst.set_dev_mockup_headers({
    'X-Kbc-User-Email': 'user@dev.com',
    'X-Kbc-User-Roles': ['123', '11111111-2222-3333-4444-1234567890', 'abc'],
    'X-Forwarded-Host': 'https://mock-server/non-existing-app'
})

kst.auth_check(REQUIRED_ROLE_ID)

if st.button('Create Event'):
    kst.create_event()

table_id = st.text_input("Table ID")

submitted_get = st.button("Submit")
if submitted_get:
    df = kst.get_data(table_id)
    if not df.empty: 
        st.dataframe(df,use_container_width=True)
        st.session_state['data'] = df
    else:
        st.error("No data retrieved for the given Table ID.")

submitted_load = st.button("Load")
if submitted_load:
    if 'data' in st.session_state and not st.session_state['data'].empty:
        kst.load_data(table_id, st.session_state['data'])
else:
    st.error("No data available to load.")

st.session_state['uploaded_file'] = kst.add_keboola_table_selection()

if not st.session_state['uploaded_file'].empty:
    st.dataframe(st.session_state['uploaded_file'], use_container_width=True)