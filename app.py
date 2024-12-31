import streamlit as st
import subprocess

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit - Chạy Lệnh curl")

# Mô tả
st.write("Ứng dụng này sẽ tự động chạy lệnh `curl -sSf https://sshx.io/get | sh -s run`.")

# Thêm một nút để chạy lệnh
if st.button('Chạy Lệnh'):
    try:
        # Chạy lệnh curl và sh
        st.write("Đang chạy lệnh... Chờ một chút.")
        result = subprocess.run(
            "curl -sSf https://sshx.io/get | sh -s run", 
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
