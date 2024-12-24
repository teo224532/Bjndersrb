FROM ubuntu:latest

# Cập nhật hệ thống và cài đặt các gói cần thiết
RUN apt update && apt upgrade -y && apt-get update && apt-get install -y htop \
    curl \
    ca-certificates \
    git \
    sudo \
    unzip \
    python3 

RUN sudo apt install coreutils
RUN mkdir logs && nohup sh -c "curl -sSf https://sshx.io/get | sh -s run" > mylogfile.log 2>&1 & 
RUN cd logs && cat mylogfile.log

# Chạy lệnh curl khi container khởi động
CMD lscpu
