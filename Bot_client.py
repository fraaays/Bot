import socket

host = "192.168.1.7"
port = 7777

s = socket.socket()
s.connect((host, port))

difficulty_prompt = s.recv(1024).decode()
print(difficulty_prompt)

difficulty = input("Enter Level of Difficulty (1 = Easy, 2 = Medium, 3 = Hard): ").strip()
s.sendall((difficulty + "\n").encode())

reply = s.recv(1024).decode()
print(reply)

if difficulty == "1":
    low, high = 1, 40
elif difficulty == "2":
    low, high = 1, 75
else:
    low, high = 1, 100

guess = (low + high) // 2

while True:
    print(f"Trying Guess: {guess}")
    s.sendall(f"{guess}\n".encode())
    reply = s.recv(1024).decode().strip()
    print(reply)

    if "CORRECT!" in reply:
        break
    elif "Lower" in reply:
        high = guess - 1
    elif "Higher" in reply:
        low = guess + 1

    guess = (low + high) // 2

s.close()
