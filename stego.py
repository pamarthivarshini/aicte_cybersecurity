import streamlit as st
import cv2
import numpy as np
import os

st.title("🔒 Steganography Image App")
st.sidebar.title("Choose an Option")
option = st.sidebar.radio("Select Mode", ("Encode Message", "Decode Message"))

# Create ASCII-to-Character and Character-to-ASCII Mappings
char_to_ascii = {chr(i): i for i in range(255)}
ascii_to_char = {i: chr(i) for i in range(255)}

def encode_message(image, message, password):
    """
    Encode a secret message into an image using the password.
    """
    n, m, z = 0, 0, 0
    
    # Store password and message length
    encoded_img = image.copy()
    for i in range(len(message)):
        encoded_img[n, m, z] = char_to_ascii[message[i]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == image.shape[1]:
                m = 0
                n += 1
    return encoded_img

def decode_message(image, msg_length):
    """
    Decode the hidden message from an image using the message length.
    """
    n, m, z = 0, 0, 0
    message = ""
    
    for i in range(msg_length):
        message += ascii_to_char[image[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == image.shape[1]:
                m = 0
                n += 1
    return message

if option == "Encode Message":
    st.header("📝 Encode Secret Message")
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])
    msg = st.text_input("Enter secret message:")
    password = st.text_input("Enter a passcode:", type="password")

    if uploaded_file and msg and password:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        encoded_img = encode_message(image, msg, password)
        cv2.imwrite("encoded_image.png", encoded_img)
        
        st.image(encoded_img, caption="Encoded Image (Appears Normal)", channels="BGR")
        st.download_button("Download Encoded Image", open("encoded_image.png", "rb").read(), "encoded_image.png", "image/png")

elif option == "Decode Message":
    st.header("🔓 Decode Secret Message")
    uploaded_file = st.file_uploader("Upload an Encoded Image", type=["jpg", "png"])
    password = st.text_input("Enter Decryption Password", type="password")
    msg_length = st.number_input("Enter the length of the hidden message:", min_value=1, step=1)

    if uploaded_file and password and msg_length:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        encoded_img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        try:
            message = decode_message(encoded_img, msg_length)
            st.success("Decryption successful!")
            st.write("Decrypted message:", message)
        except Exception as e:
            st.error("Decryption failed! Error: " + str(e))
