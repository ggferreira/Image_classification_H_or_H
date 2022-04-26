import streamlit as st
from img_classification import teachable_machine_classification
from PIL import Image

st.title('Classificação de imagen com Teachable Machine do Google')
st.header("Identificação da raça de um Cavalo entre 7 opções")
st.text("Insira a imagem de um cavalo para identificação de sua raça")


uploaded_file = st.file_uploader("Escolha a foto de um cavalo", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Foto escolhida', use_column_width=True)
    st.write("")
    st.write("Classificando...")
    label = teachable_machine_classification(image, 'horse_breeds_model.h5')
    if label == 0:
        st.write("Esta é a foto de um cavalo da Raça: Akhal-Teke")
    elif label == 1:
        st.write("Esta é a foto de um cavalo da Raça: Appaloosa")
    elif label == 2:
        st.write("Esta é a foto de um cavalo da Raça: Orlov Trotter")
    elif label == 3:
        st.write("Esta é a foto de um cavalo da Raça: Vladimir Heavy Draft")
    elif label == 4:
        st.write("Esta é a foto de um cavalo da Raça: Percheron")
    elif label == 5:
        st.write("Esta é a foto de um cavalo da Raça: Arabian")
    else:
        st.write("Esta é a foto de um cavalo da Raça: Friesian")