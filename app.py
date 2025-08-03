import streamlit as st

st.set_page_config(page_title="Debug Mode", layout="centered")

st.title("🧪 Debugging App Startup")

try:
    st.write("Trying to import login module...")
    from auth.login import login_page
    st.success("✅ auth.login imported successfully")

    st.write("Trying to import classifier...")
    from router.classifier import classify_query
    st.success("✅ router.classifier imported successfully")

    st.write("Trying to import joblib and others...")
    import joblib
    import openai
    import os
    st.success("✅ All core modules imported")

    st.write("Trying to read secrets...")
    st.code(f"OPENAI_API_KEY = {st.secrets['OPENAI_API_KEY'][:5]}...")
    st.success("✅ Secrets loaded")

except Exception as e:
    st.error("❌ App crashed at startup")
    st.exception(e)
