# aicte_cybersecurity

# 🔒 Image Steganography App  

This is an interactive web application that allows users to **encode** secret messages into images and **decode** hidden messages from encoded images. The app is built using **Streamlit** and **OpenCV**, ensuring an intuitive user interface and efficient image processing.

---

## 🚀 **Features**  
- **Encode Message:**  
  - Upload an image and a secret message.
  - Embed the message within the image using pixel manipulation.
  - Download the encoded image, which appears identical to the original.
  
- **Decode Message:**  
  - Upload the encoded image.
  - Enter the correct passcode and message length.
  - Retrieve the hidden message securely.

- **Security:**  
  - Uses a passcode for decoding, adding an additional layer of protection.
  - The encoded image maintains its visual integrity, preserving secrecy.

---

## 🔧 **Technology Used**  
- **Python**: Core programming language.
- **Streamlit**: Web interface framework for creating an interactive and user-friendly UI.
- **OpenCV**: For image processing and pixel manipulation.
- **NumPy**: Efficient array operations for manipulating image data.
- **ASCII Mapping**: To convert characters to ASCII values for embedding in image pixels.

---

## 📥 **Installation**  
1. **Clone the Repository**  
```bash
git clone https://github.com/pamarthivarshini/aicte_cybersecurity
```

2. **Install Dependencies**  
```bash
pip install streamlit opencv-python-headless numpy
```

3. **Run the Application**  
```bash
streamlit run stegano.py
```

---

## 🔑 **Usage**  
### **Encode Message:**
- Upload an image (JPG or PNG).
- Enter the secret message and a passcode.
- Click "Encode" to hide the message within the image.
- Download the encoded image.

### **Decode Message:**
- Upload the encoded image.
- Enter the correct passcode and the length of the hidden message.
- Click "Decode" to retrieve the secret message.
- If the passcode is incorrect, access to the hidden message is denied.

---

## 🎨 **UI Preview**  
- **Encode Mode:** Upload an image, input a secret message and passcode, and download the encoded image.
- **Decode Mode:** Upload the encoded image, enter the passcode, and reveal the hidden message.

---

## 🔒 **Security & Privacy**  
- The message is hidden within the pixel values of the image channels.
- The encoded image appears identical to the original, ensuring no suspicion of hidden content.
- Decryption requires the correct passcode and message length.

---

## 💡 **How It Works**  
- **Encoding:**  
  - The message is converted to ASCII values.
  - These values are embedded in the pixel channels sequentially.
  - The encoded image is saved without visible changes.

- **Decoding:**  
  - The pixel channels are read in the same sequence.
  - ASCII values are converted back to characters to retrieve the message.

---

## 🤩 **Wow Factors**  
- **Invisible Messaging:** The encoded image looks identical to the original.
- **Cross-Platform Accessibility:** Accessible from any device with a web browser.
- **User-Friendly Interface:** Streamlit ensures an interactive and intuitive experience.
- **Secure Communication:** A passcode is required for decryption.

---

## 👥 **End Users**  
- **Journalists and Activists:** Secure communication without detection.
- **Corporate Professionals:** Protect confidential business data.
- **General Users:** Private messaging without raising suspicion.
- **Educational Purposes:** Learn and demonstrate cryptography techniques.

---

## 🔮 **Future Scope**  
- **Video & Audio Steganography:** Extend functionality to multimedia files.
- **Advanced Encryption:** Implement stronger encryption methods.
- **Cloud Integration:** Store and share encoded images securely.
- **Mobile Application:** Develop apps for Android and iOS platforms.
- **AI Integration:** Enhance steganography techniques using machine learning.

---

## 📜 **License**  
This project is licensed under the MIT License. Feel free to use and modify the code as per your needs.

---

## 🤝 **Contributing**  
Contributions are welcome!  
- Fork the repository.  
- Create a new branch (`feature-branch-name`).  
- Make your changes and commit them.  
- Push to the branch.  
- Create a pull request.  

---

## 📧 **Contact**  
For any queries or suggestions, please contact [varshi](pamarthivarshini2@gmail.com).

---
## ⭐ **Acknowledgments**  
- Thanks to the developers of **Streamlit**, **OpenCV**, and **NumPy** for their amazing libraries.
- Special shoutout to all contributors who helped in improving this app.

---

## 🌟 **Show Your Support**  
Give this project a ⭐ if you found it useful!

---

This **Image Steganography App** is a powerful tool for secure communication and data privacy. Feel free to enhance and expand its capabilities!
