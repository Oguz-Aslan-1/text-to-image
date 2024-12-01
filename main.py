import streamlit as st
import easyocr
from PIL import Image
import numpy as np

def extract_text_from_image(image):
    reader = easyocr.Reader(['en', 'tr'])
    results = reader.readtext(np.array(image))
    extracted_text = [text[1] for text in results]
    return extracted_text

def main():
    st.title("Menu Text Extractor")
    st.write("Upload a photo of a menu to extract the text")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Menu Image', use_column_width=True)
        
        if st.button('Extract Text'):
            with st.spinner('Extracting text from image...'):
                extracted_text = extract_text_from_image(image)
                
                st.subheader("Extracted Menu Items:")
                for idx, text in enumerate(extracted_text, 1):
                    st.write(f"{idx}. {text}")
                
                # Create a downloadable text file
                text_content = '\n'.join(extracted_text)
                st.download_button(
                    label="Download extracted text",
                    data=text_content,
                    file_name="menu_items.txt",
                    mime="text/plain"
                )

if __name__ == '__main__':
    main()
