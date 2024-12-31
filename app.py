import streamlit as st
import subprocess

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit - Chạy lệnh curl và hiển thị log")

# Mô tả
st.write("Ứng dụng này sẽ chạy lệnh `curl -sSf https://sshx.io/get | sh -s run` và hiển thị log trong thời gian thực.")

# Thêm một nút để chạy lệnh
if st.button('Chạy lệnh và hiển thị log'):
    # Chạy lệnh curl và sh bằng Popen để theo dõi log trong thời gian thực
    st.write("Đang chạy lệnh... Chờ một chút.")
    
    process = subprocess.Popen(
        "curl -sSf https://sshx.io/get | sh -s run", 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )

    # Hiển thị log trong thời gian thực
    for line in process.stdout:
        st.text(line.strip())  # Hiển thị từng dòng log ra màn hình

    # Đợi lệnh hoàn thành và xử lý lỗi nếu có
    stderr = process.stderr.read()
    if stderr:
        st.error(f"Đã xảy ra lỗi: {stderr}")
    
    process.stdout.close()
    process.stderr.close()
    process.wait()

    st.success("Lệnh đã chạy xong!")
