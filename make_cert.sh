# https用にオレオレ証明書を./certに発行
sudo apt install openssl
sudo apt install python3-openssl
mkdir cert
cd cert
openssl genrsa 2048 > server.key
openssl req -new -key server.key > server.csr
openssl x509 -days 365 -req -signkey server.key < server.csr > server.crt