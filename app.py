import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("""
    ## Welcome to Password Strength Checker!
    This app checks the strength of your password & suggests improvements to make it stronger 🔎
""")

password = st.text_input("Enter your password", type="password")
feedback = []
score = 0
strength_level = ""

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one lowercase letter")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one uppercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character")

    # Determine strength level
    if score == 5:
        strength_level = "🟢 Strong"
    elif score >= 3:
        strength_level = "🟡 Moderate"
    else:
        strength_level = "🔴 Weak"

    # Display strength level with progress bar
    st.markdown(f"### Password Strength: {strength_level}")
    st.progress(score / 5)

    if feedback:
        st.error("Password is weak! ❌ Consider the following suggestions:")
        for i in feedback:
            st.markdown(f"- {i}")
    else:
        st.success("Password is strong! ✅")
else:
    st.info("✨ Please enter your password to check its strength.")