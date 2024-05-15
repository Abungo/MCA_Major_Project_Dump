from machine import Pin, SPI
from nrf24l01 import NRF24L01
import utime

# Pin configuration
ce = Pin(15, Pin.OUT)
csn = Pin(2, Pin.OUT)
spi = SPI(1, baudrate=1000000, polarity=0, phase=0)

# NRF24L01 setup
nrf = NRF24L01(spi, csn, ce, payload_size=32)
nrf.open_tx_pipe(b'\xd7\xd7\xd7\xd7\xd7')
nrf.open_rx_pipe(1, b'\xe7\xe7\xe7\xe7\xe7')
nrf.start_listening()

def receive_data():
    if nrf.any():
        while nrf.any():
            buf = nrf.recv()
            print("Received: ", buf)
    utime.sleep(1)

while True:
    receive_data()
    utime.sleep(1)