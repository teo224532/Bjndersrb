import streamlit as st
import subprocess
import os

# Tiêu đề ứng dụng
st.title("Ứng dụng Streamlit - Cài đặt và chạy htop không cần root")

# Mô tả
st.write("Ứng dụng này sẽ tải mã nguồn của `htop`, biên dịch và chạy nó mà không cần quyền root.")

# Thêm một nút để chạy các lệnh
if st.button('Tải và chạy htop mà không cần root'):
    # Bước 1: Cài đặt các công cụ cần thiết (không cần root)
    st.write("Đang tải và biên dịch `htop`... Chờ một chút.")
    
    # Tải mã nguồn của htop
    subprocess.run("wget https://github.com/htop-dev/htop/archive/refs/tags/3.2.0.tar.gz", shell=True)

    # Giải nén mã nguồn
    subprocess.run("tar -xvzf 3.2.0.tar.gz", shell=True)

    # Chuyển đến thư mục mã nguồn
    os.chdir("htop-3.2.0")

    # Biên dịch và cài đặt htop
    subprocess.run("./autogen.sh", shell=True)
    subprocess.run("./configure --prefix=$HOME/htop", shell=True)  # Cài đặt vào thư mục người dùng
    subprocess.run("make", shell=True)
    subprocess.run("make install", shell=True)

    # Cài đặt thành công, bây giờ chạy htop
    st.write("Đang chạy `htop` từ thư mục người dùng...")
    process_htop_run = subprocess.Popen(
        "$HOME/htop/bin/htop -b -n 1",  # Chạy htop từ thư mục người dùng
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

    st.success("Hoàn thành việc tải, biên dịch và chạy htop mà không cần quyền root!")
