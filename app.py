import streamlit as st
import subprocess

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit - Thông tin CPU")

# Mô tả
st.write("Ứng dụng này sẽ chạy lệnh `lscpu` để hiển thị thông tin về CPU của hệ thống.")

# Thêm một nút để chạy lệnh
if st.button('Chạy lệnh lscpu'):
    try:
        # Chạy lệnh lscpu
        st.write("Đang thu thập thông tin CPU... Chờ một chút.")
        result = subprocess.run(
            "lscpu", 
            shell=True, 
            check=True, 
            text=True, 
            capture_output=True
        )
        # Hiển thị kết quả
        st.success("Lệnh đã chạy thành công!")
        st.text(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"Đã xảy ra lỗi khi chạy lệnh: {e}")
        st.text(e.stderr)
