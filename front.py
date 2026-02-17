import requests
import streamlit as st

api = 'http://127.0.0.1:8000/predict/'

st.title('Student Performance Prediction')

gender = st.selectbox('Gender', ['male', 'female'])

race_ethnicity = st.selectbox(
    'Race / Ethnicity',
    ['group A', 'group B', 'group C', 'group D', 'group E']
)

parental_level_of_education = st.selectbox(
    'Parental level of education',
    ["bachelor's degree", 'high school', "master's degree",
     'some college', 'some high school']
)

lunch = st.selectbox('Lunch', ['standard', 'free/reduced'])

test_preparation_course = st.selectbox(
    'Test preparation course',
    ['none', 'completed']
)

math_score = st.number_input('Math score', min_value=0, max_value=100, step=1)
reading_score = st.number_input('Reading score', min_value=0, max_value=100, step=1)

student_dict = {
    'gender': gender,
    'race_ethnicity': race_ethnicity,
    'parental_level_of_education': parental_level_of_education,
    'lunch': lunch,
    'test_preparation_course': test_preparation_course,
    'math_score': math_score,
    'reading_score': reading_score
}

if st.button('Predict'):
    try:
        response = requests.post(api, json=student_dict)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted score: {result['predict']}")
        else:
            st.error(f"Error: {response.status_code}")
    except requests.exceptions.RequestException:
        st.error('Cannot connect to the API')