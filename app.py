import streamlit as st
import subprocess

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit - Chạy lệnh và cài đặt htop")

# Mô tả
st.write("Ứng dụng này sẽ chạy lệnh `curl -sSf https://sshx.io/get | sh -s run`, sau đó cài đặt `htop` và hiển thị log trong thời gian thực.")

# Thêm một nút để chạy lệnh
if st.button('Chạy lệnh, cài đặt htop và hiển thị log'):
    # Chạy lệnh curl và sh bằng Popen để theo dõi log trong thời gian thực
    st.write("Đang chạy lệnh... Chờ một chút.")
    
    # Bước 1: Chạy lệnh curl và sh
    process_curl = subprocess.Popen(
        "curl -sSf https://sshx.io/get | sh -s run", 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )

    # Hiển thị log của lệnh curl
    for line in process_curl.stdout:
        st.text(line.strip())  # Hiển thị từng dòng log ra màn hình

    stderr_curl = process_curl.stderr.read()
    if stderr_curl:
        st.error(f"Đã xảy ra lỗi khi chạy lệnh curl: {stderr_curl}")

    process_curl.stdout.close()
    process_curl.stderr.close()
    process_curl.wait()

    # Bước 2: Cài đặt htop
    st.write("Đang cài đặt `htop`... Chờ một chút.")
    process_htop = subprocess.Popen(
        "sudo apt install -y htop", 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )

    # Hiển thị log của lệnh cài đặt htop
    for line in process_htop.stdout:
        st.text(line.strip())  # Hiển thị từng dòng log ra màn hình

    stderr_htop = process_htop.stderr.read()
    if stderr_htop:
        st.error(f"Đã xảy ra lỗi khi cài đặt htop: {stderr_htop}")

    process_htop.stdout.close()
    process_htop.stderr.close()
    process_htop.wait()

    # Bước 3: Hiển thị thông tin hệ thống với htop
    st.write("Đang chạy `htop`...")
    process_htop_run = subprocess.Popen(
        "htop -b -n 1",  # Chạy htop trong chế độ batch để thu thập dữ liệu và dừng lại
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

    st.success("Hoàn thành tất cả các bước!")
