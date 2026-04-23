import streamlit as st
from deep_translator import GoogleTranslator

# Page Setup
st.set_page_config(page_title="Language Translator", page_icon="🌐")
st.title("Language Translation Tool")
st.markdown("Translate text between any languages instantly!")

# Languages Dictionary
languages = {
    "Urdu": "ur",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Turkish": "tr",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt",
}

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

# Text Input
input_text = st.text_area("Enter text to translate", height=150, placeholder="Type something here...")

# Translate Button
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text first!")
    elif source_lang == target_lang:
        st.warning("Source and target languages are same!")
    else:
        with st.spinner("Translating..."):
            try:
                translated = GoogleTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                ).translate(input_text)

                st.success("Translation Complete!")
                st.text_area("Translated Text", value=translated, height=150)

                # Copy Button
                st.code(translated, language="")

            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Made with using Streamlit & Google Translate")
