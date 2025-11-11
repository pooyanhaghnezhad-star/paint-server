import socket
import threading

clients = []

def handle_client(conn):
    while True:
        try:
            data = conn.recv(1024)
            for client in clients:
                if client != conn:
                    client.send(data)
        except:
            clients.remove(conn)
            conn.close()
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))  # گوش دادن روی همه آدرس‌ها و پورت ۱۲۳۴۵
server.listen()

print("سرور اجرا شد و منتظر اتصال کلاینت‌هاست...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn,)).start()
