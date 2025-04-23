import pysftp
host = "test.rebex.net"
username = "demo"
password = "password"
with pysftp.Connection(host=host, username=username, password=password) as sftp:
    print("Connection successfully established")
    # Switch to a remote directory
    sftp.cwd('pub/example/')
    print("Changing to pub/example directory... ")
    sftp.get('readme.txt', 'readme.txt')
    print("File downloaded ... ")
    sftp.close()