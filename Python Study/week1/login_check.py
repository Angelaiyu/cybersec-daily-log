import getpass
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
real_codename = "hackerboy"
real_password = "admin123"

for i in range(3):
    input_codename = input("请输入你的代号：")
    print("请确保密码安全，勿外泄")
    input_password = getpass.getpass("请输入密码：") # 隐藏输入的密码

    if input_codename == real_codename and input_password == real_password:
        print("身份验证成功，欢迎进入系统！")

        with open("login_log.txt", "a") as log_file:
            log_file.write(f"登录成功：时间[{timestamp}]，用户[{input_codename}]\n")

        break
    else:
        print("验证失败，请重新输入")

        with open("login_log.txt", "a") as log_file:
            log_file.write(f"尝试失败：时间[{timestamp}]，用户[{input_codename}]，密码[{input_password}]\n")
else:
    print("输入次数过多，禁止访问")



