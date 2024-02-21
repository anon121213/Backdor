import socket

def main():
    host = "" # ip который будем прослушивать
    port = 7000 # порт

    s = socket.socket() # создаем сокет
    s.bind((host,port))

    s.listen(1)
    print("Waiting for connection...")
    connection, address = s.accept() # подключаемся
    print("Connection from " + str(address))
    while True:
        try:
            toSend = input("-> ")
            connection.send(toSend.encode()) # отправляем команду
            data = connection.recv(1024).decode() # получаем результат
            print(data.encode('cp1251').decode('cp866')) # выводим на экран

        except:
            break
    print("Connection refused") # в случае, если соединение разорванно
    connection.close()

if __name__ == '__main__':
    main()
