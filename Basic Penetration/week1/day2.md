
# ✅ Day2：SQL 注入基础与回显注入实战学习笔记

> 本日学习重点：掌握 SQL 注入的基本原理、分类、常见工具使用、以及完整的回显注入利用流程。

---

## 🧠 一、SQL 注入基础知识

### 1. 漏洞原理

SQL 注入（SQL Injection）是一种通过将恶意 SQL 语句插入到输入字段中，从而操控后端数据库执行非预期操作的攻击方式。通常由于开发者拼接 SQL 语句时未对用户输入进行严格过滤，导致注入点形成。

### 2. 危害

- 获取敏感信息（如用户数据、密码等）
- 绕过身份认证
- 修改、删除数据库内容
- 写入 WebShell，控制服务器
- 持久化后门注入
- 执行系统命令（某些场景下）

### 3. SQL 注入分类（常见）

| 类型 | 描述 |
|------|------|
| 回显注入 | 结果直接显示在页面上，可快速提取数据 |
| 报错注入 | 通过构造语句抛出数据库错误信息，读取内部信息 |
| 布尔盲注 | 利用返回页面的差异判断条件真假 |
| 时间盲注 | 利用 `sleep()` 等延时函数判断条件真假 |
| 堆叠注入 | 多语句注入，如：`1;DROP TABLE users`（需数据库支持）|

---

## 🗃️ 二、MySQL 常用系统表与结构

### 1. 常用系统表（information_schema）

| 系统表 | 说明 |
|--------|------|
| `schemata` | 所有数据库名称 |
| `tables` | 所有数据表名 |
| `columns` | 所有字段名 |
| `users`（非系统）| 通常用于登录验证的信息表 |

### 2. 数据库命令行操作（MySQL CLI）

```sql
SHOW DATABASES;
USE testdb;
SHOW TABLES;
DESC users;
SELECT column_name FROM information_schema.columns WHERE table_name='users';
SELECT * FROM users;
```

---

## 🔧 三、图形化数据库管理工具

### 1. Navicat
- 本地可视化客户端，支持连接远程数据库
- 支持表结构设计、SQL 编辑、数据查询、导出导入等功能

### 2. phpMyAdmin
- Web 版数据库管理工具，常见于 Web 后台

### 3. adminer.php
- 单文件数据库管理器，上传即用，适合测试环境中使用

---

## 🕵️‍♂️ 四、回显注入（Echo-Based Injection）

### ✅ 1. 寻找注入点

- URL 参数、POST 数据、Cookie、Header 等
- 基本测试：`1'`，`1 and 1=1` vs `1 and 1=2`

### ✅ 2. 判断注入类型

- 字符型：`1' and '1'='1`
- 数字型：`1 and 1=1`

### ✅ 3. 判断字段数量

```sql
?id=1 ORDER BY N
```

### ✅ 4. 联合查询测试

```sql
?id=1 UNION SELECT 1,2,3,...
```

---

## 🧪 五、信息提取流程（information_schema）

### 当前数据库名

```sql
UNION SELECT 1,2,database()
```

### 所有数据库名

```sql
SELECT schema_name FROM information_schema.schemata
```

### 所有表名

```sql
SELECT table_name FROM information_schema.tables WHERE table_schema='数据库名'
```

### 所有字段名

```sql
SELECT column_name FROM information_schema.columns WHERE table_name='表名'
```

### 查询敏感信息

```sql
UNION SELECT 1,username,password FROM users
```

---

## 🔧 六、常用函数说明

| 函数名 | 作用 |
|--------|------|
| `version()` | 数据库版本 |
| `user()` | 当前连接数据库的用户 |
| `database()` | 当前数据库 |
| `concat()` | 字符拼接 |
| `group_concat()` | 多行合并 |
| `sleep(n)` | 延迟 |
| `load_file()` | 读取文件 |
| `outfile` | 写文件（配合写 shell）|

---

## 📝 七、学习小结

- 掌握了 SQL 注入的基本分类与利用流程
- 理解了信息架构表（information_schema）在注入中的作用
- 学会了判断注入点、类型、字段数、信息提取的完整流程
- 熟悉了 Navicat、phpMyAdmin、adminer.php 等常用数据库管理工具

---

🎯 **下一步建议：**  
- 学习报错注入与盲注技术  
- 熟练使用 sqlmap 工具自动化注入  
- 尝试实战演练，如 DVWA、bWAPP 靶场
