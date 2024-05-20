import streamlit as st
import pandas

st.set_page_config(layout="wide")


st.title('The Best Company')

content = """The Best Company isn't your typical corporation. Founded in 1972 with the motto "Bringing out the best in everything," it's a global company built on the philosophy that amazing products and experiences shouldn't be a luxury. The Best Company isn't without its competitors, but their focus on quality, surprising customers, and giving back to the community has earned them a fiercely loyal following.  They may not be the biggest company in the world, but they strive to be the best, according to their own unique definition."""
st.write(content)

st.subheader("Our Team")

col1,empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row["first name"])
        st.write(row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
        

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"])
        st.write(row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
        

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(row["first name"])
        st.write(row["last name"])
        st.write(row["role"])
        st.image("images/" + row["image"])
        



