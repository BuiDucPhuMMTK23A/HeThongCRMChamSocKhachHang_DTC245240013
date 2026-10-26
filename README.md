# Hệ thống CRM Chăm sóc Khách hàng

**Sinh viên thực hiện:** Bùi Đức Phú - DTC245240013 - MMT-K23A

## 1. Giới thiệu
Hệ thống CRM quản lý khách hàng và tương tác, triển khai bằng Docker Compose.

## 2. Công nghệ sử dụng
- **Backend:** Django (Python)
- **Database:** PostgreSQL + pgAdmin
- **Reverse Proxy:** Nginx
- **Giám sát:** Prometheus + Grafana
- **Log tập trung:** Loki + Promtail

## 3. Hướng dẫn khởi chạy
Yêu cầu máy đã cài Docker và Docker Compose.
1. Clone repo: `git clone <LINK_REPO_CUA_BAN>`
2. Di chuyển vào thư mục: `cd crm_project`
3. Khởi chạy hệ thống: `sudo docker compose up -d`
4. Kiểm tra trạng thái: `sudo docker ps`

## 4. Các cổng truy cập mặc định
- Web CRM: `http://localhost/admin`
- pgAdmin: `http://localhost:5050`
- Grafana: `http://localhost:3000`
- Prometheus: `http://localhost:9090`

## 5. Lưu ý bảo mật
Trong môi trường Production thực tế sẽ sử dụng file `.env.example` và `.gitignore` để bảo mật mật khẩu, đồng thời đóng các cổng public không cần thiết.
