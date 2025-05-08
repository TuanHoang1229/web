import streamlit as st
import random
import string
import hashlib

# Tính độ mạnh mật khẩu
def calculate_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    return strength

# UI
st.set_page_config(page_title="Tạo mật khẩu mạnh", page_icon="🔒")
st.title("🔐 Trình tạo mật khẩu mạnh")

length = st.number_input("Độ dài mật khẩu", min_value=6, max_value=100, value=12)

if st.button("Tạo mật khẩu"):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    st.text_input("Mật khẩu của bạn", password)
    
    strength = calculate_strength(password)
    strength_labels = ["Rất yếu", "Yếu", "Trung bình", "Mạnh", "Rất mạnh"]
    st.progress(strength * 20)
    st.success(f"Độ mạnh: {strength_labels[strength - 1] if strength else 'Rất yếu'}")

    if st.button("Lưu mật khẩu (SHA-256)"):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        with open("saved_passwords.txt", "a") as f:
            f.write(hashed + "\n")
        st.success("Đã lưu mật khẩu (dạng SHA-256) vào file.")
