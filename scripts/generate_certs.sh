mkdir certs
cd certs

openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")


openssl pkcs12 -export -name localhostServerCert -in localhost.crt -inkey localhost.key -out cert.p12

keytool -importkeystore -destkeystore localhostKeystore.jks -srckeystore cert.p12 -srcstoretype pkcs12 -alias localhostServerCert

keytool -importkeystore -srckeystore localhostKeystore.jks -destkeystore keystore.jks
