import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv", sep=";")
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Images.jpg")

with col2:
    st.title("GunZeux_71")
    contents = """I am a reliable and versatile product designer with over 3 years of hands-on experience in product design and development, primarily specializing in the creation and enhancement of mechanical components. My work integrates a deep understanding of mechanical engineering principles with cross-disciplinary expertise in electronics and programming, enabling me to deliver comprehensive, high-end product solutions tailored to automation.

With a strong foundation in mechanical systems and the ability to blend this knowledge with electronics, I’ve successfully contributed to projects that bridge hardware and software, leading to innovative and efficient designs. My proficiency in programming allows me to incorporate advanced automation features, ensuring that the products I design are not only functional but also cutting-edge.

I am passionate about continuous learning and remain committed to expanding my skill set in emerging technologies. My career is driven by the desire to work in dynamic, challenging environments that foster creativity and push the boundaries of what’s possible in product design.


 """
    st.info(contents)

st.write("Some of the projects that i have done in the Past: ")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
print(df.columns)
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])

