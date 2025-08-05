# 📘 渗透测试入门笔记：Burp Suite 与 HTTP基础
🗓️ 日期：2025-08-05

---

## 🎯 今日学习内容概览

- Burp Suite 安装与配置  
- 上游代理设置  
- HTTP 协议基础知识  
- GET 与 POST 请求  
- Cookie 与 Session 的区别  
- MIME 类型  
- 常见 HTTP 请求头与响应头  
- HTTP 与 HTTPS 的区别  
- 域名解析流程：DNS、Hosts 文件  

---

## 🛠️ Burp Suite 配置笔记

### ✅ 安装流程

- 下载地址：[https://portswigger.net/burp](https://portswigger.net/burp)  
- 安装后启动即可使用社区版或专业版（如有授权）  

### ✅ 安装 Burp 的 CA 证书

- 打开浏览器，访问 `http://burpsuite`，下载 Burp 提供的证书  
- 在浏览器中导入证书（建议仅导入到受信任根证书中）  

### ✅ 设置上游代理（Upstream Proxy）

- 用于将 Burp 请求再转发到其他代理（如使用 clash、v2ray 时）  
- 路径：Burp > User Options > Connections > Upstream Proxy Servers  

---

## 🌐 HTTP 协议基础

### 🔁 HTTP 工作流程（简化流程图）

1. 客户端向服务器发起请求（Request）  
2. 服务器处理请求并返回响应（Response）  
3. 客户端接收响应数据  

### 🧾 请求方法：GET 与 POST 的区别

| 对比项 | GET | POST |
|--------|-----|------|
| 参数位置 | URL 中 | 请求体中 |
| 安全性 | 暴露参数，不安全 | 参数不易被直接看到 |
| 长度限制 | 有限制 | 较大 |
| 用途 | 查询数据 | 提交数据 |

---

## 🍪 Cookie 与 Session 的区别

| 特性 | Cookie | Session |
|------|--------|---------|
| 存储位置 | 客户端（浏览器） | 服务器端 |
| 安全性 | 容易被盗取 | 相对更安全 |
| 生命周期 | 可自定义 | 关闭浏览器或超时失效 |
| 通信方式 | 每次请求自动带上 | 通过 Session ID 管理 |

---

## 🧾 MIME 类型（媒体类型）

常见 MIME 类型：
- `text/html`：网页  
- `application/json`：接口数据  
- `image/png`：图片  
- `multipart/form-data`：表单上传文件  

---

## 🧠 常见 HTTP 请求头

- `Host`：主机地址  
- `User-Agent`：客户端类型  
- `Referer`：请求来源  
- `Cookie`：携带客户端的 Cookie  
- `Content-Type`：提交数据的格式（如 JSON 或表单）  

---

## 📥 HTTP 响应结构

- **状态行**：例如 `HTTP/1.1 200 OK`  
- **响应头**：
  - `Server`：服务器类型  
  - `Content-Type`：返回的数据类型  
  - `Set-Cookie`：服务器设置 Cookie  

---

## 🔐 HTTP 与 HTTPS 的区别

| 项目 | HTTP | HTTPS |
|------|------|-------|
| 安全性 | 明文传输 | 加密传输（SSL/TLS） |
| 默认端口 | 80 | 443 |
| URL 前缀 | http:// | https:// |

---

## 🌍 域名解析基础

- **DNS (Domain Name System)**：将域名解析为 IP 地址的系统  
- **Hosts 文件**：本地优先解析表，可以绕过 DNS  
- DNS 查询流程：
  1. 浏览器缓存 → 系统缓存 → Hosts → DNS 服务器  

---

## ✅ 今日反思与总结

- Burp 是渗透测试必备工具，配置代理与证书是基础操作  
- HTTP 是 Web 渗透的基础，需掌握每个字段的作用  
- 推荐每天都进行实践练习，例如抓一个 GET/POST 请求并分析它的结构  

---

📌 如果你觉得今天内容比较杂，可以在后续每次学习后，按模块深入整理，逐步形成自己的渗透知识库。
