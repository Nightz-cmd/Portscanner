import socket
import os

# Examples

PORT_NAMES = {
    21: "FTP", # File transfers
    22: "SSH", # Remote secure logins
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS", # Web traffic
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    27017: "MongoDB",
    5000: "Flask/Dev",
    6379: "Redis",
    9200: "Elasticsearch",
    139: "NetBIOS",
    135: "RPC",
    389: "LDAP",
    636: "LDAPS",
    25: "SMTP",
    465: "SMTPS",
    587: "SMTP-TLS",
    993: "IMAPS",
    995: "POP3S",
}

def main():
    """"Main entry point"""
    print(f"""
          _________________________________________________________________
                                          ! Walker
                                      Advanced Portscanner 
                                        Made by Walker!
          __________________________________________________________________
          """)
main()


for port in PORT_NAMES:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)

    status = s.connect_ex(('185.185.50.58', port))

    if status == 0:
        print(f'{port} IS OPEN. SERVICE: {PORT_NAMES[port]}')
    else:
       print(f'{port} IS CLOSED. SERVICE: {PORT_NAMES[port]}')
