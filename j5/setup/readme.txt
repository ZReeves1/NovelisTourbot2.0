## final bluetooth config:
sudo nano /lib/systemd/system/bluetooth.service
## And add a -C:
ExecStart=/usr/lib/bluetooth/bluetoothd -C
