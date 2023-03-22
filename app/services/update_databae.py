from pynubank import Nubank, MockHttpClient

def update_datebase(cpf, password):
	# run as mock when not in production
  nu = Nubank(MockHttpClient())
  nu.authenticate_with_cert(
    cpf,
    password,
    "certs/cert.p12"
  )
