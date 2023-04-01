from ftplib import FTP

file = open("./main.py", "rb")

print(file)

filename = file.name

print(filename)

ftp_server = FTP("sg.storage.bunnycdn.com", "script-slayer-zone",
                 "80766680-ea9e-4841-be2de97f101f-935b-4f96")
ftp_server.storbinary(f"STOR {filename}", file)
ftp_server.quit()
file.close()
