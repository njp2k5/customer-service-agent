import streamlit as st

st.set_page_config(page_title="Debug Boot", layout="centered")
st.title("🔎 Streamlit Startup Debug")

# Validate secrets
try:
    key = st.secrets.get("OPENAI_API_KEY", None)
    st.text(f"OpenAI key loaded: {bool(key)}")
except Exception as e:
    st.error(f"Secrets load error: {e}")

# Validate module imports
modules = {
    "auth.login": "from auth.login import login_page",
    "router.classifier": "from router.classifier import classify_query",
}

for mod, code in modules.items():
    try:
        exec(code, globals())
        st.success(f"✅ {mod} imported successfully")
    except Exception as e:
        st.error(f"❌ {mod} import failed: {e}")

# Test joblib
try:
    import joblib
    st.success("✅ joblib available")
except Exception as e:
    st.error(f"❌ joblib import failed: {e}")
