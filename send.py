from machine import Pin, SPI
from nrf24l01 import NRF24L01
import utime

# Pin configuration
ce = Pin(15, Pin.OUT)
csn = Pin(2, Pin.OUT)
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)

# NRF24L01 setup
nrf = NRF24L01(spi, csn, ce, payload_size=32)
nrf.open_tx_pipe(b'\xe7\xe7\xe7\xe7\xe7')
nrf.open_rx_pipe(1, b'\xd7\xd7\xd7\xd7\xd7')
nrf.start_listening()

def send_data():
    nrf.stop_listening()
    message = b'Hello World!'
    nrf.send(message)
    print("Sent: ", message)
    utime.sleep(1)
    nrf.start_listening()

while True:
    send_data()
    utime.sleep(1)