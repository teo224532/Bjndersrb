import streamlit as st
import subprocess

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit - Cài đặt và chạy htop")

# Mô tả
st.write("Ứng dụng này sẽ cài đặt `htop` và chạy nó, hiển thị log trong thời gian thực.")

# Thêm một nút để chạy các lệnh
if st.button('Cài đặt htop và chạy lệnh'):
    # Bước 1: Cài đặt htop
    st.write("Đang cài đặt `htop`... Chờ một chút.")
    
    process_htop_install = subprocess.Popen(
        "sudo apt install -y htop", 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )

    # Hiển thị log cài đặt htop
    for line in process_htop_install.stdout:
        st.text(line.strip())  # Hiển thị từng dòng log ra màn hình

    stderr_htop_install = process_htop_install.stderr.read()
    if stderr_htop_install:
        st.error(f"Đã xảy ra lỗi khi cài đặt htop: {stderr_htop_install}")

    process_htop_install.stdout.close()
    process_htop_install.stderr.close()
    process_htop_install.wait()

    # Bước 2: Chạy htop
    st.write("Đang chạy `htop` để hiển thị thông tin hệ thống...")
    
    process_htop_run = subprocess.Popen(
        "htop -b -n 1",  # Chạy htop trong chế độ batch (không giao diện, chỉ chạy 1 lần)
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )

    # Hiển thị log của lệnh htop
    for line in process_htop_run.stdout:
        st.text(line.strip())  # Hiển thị từng dòng log ra màn hình

    stderr_htop_run = process_htop_run.stderr.read()
    if stderr_htop_run:
        st.error(f"Đã xảy ra lỗi khi chạy htop: {stderr_htop_run}")

    process_htop_run.stdout.close()
    process_htop_run.stderr.close()
    process_htop_run.wait()

    st.success("Hoàn thành cài đặt và chạy htop!")
