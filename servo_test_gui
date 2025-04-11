import smbus
import time
import tkinter as tk

# I2C adresi ve PCA9685'te kullanılan register tanımları
I2C_ADDRESS = 0x40
MODE1 = 0x00
LED0_ON_L = 0x06
LED0_OFF_L = 0x08
PRESCALE = 0xFE

# I2C veriyolu başlatılıyor
bus = smbus.SMBus(1)

# PCA9685'i başlatmak için bir helper fonksiyon
def pca9685_setup():
    bus.write_byte_data(I2C_ADDRESS, MODE1, 0x00)  # Normal çalışmaya ayar
    time.sleep(0.005)

# Servo açısını belirlemek için bir helper fonksiyon
def set_servo_angle(channel, angle):
    pulse_length = 4096  # 12 bit çözünürlük
    pulse_min = 150  # Minimum darbe genişliği (~1 ms)
    pulse_max = 600  # Maksimum darbe genişliği (~2 ms)
    pulse = int(pulse_min + (angle / 180.0) * (pulse_max - pulse_min))
    bus.write_byte_data(I2C_ADDRESS, LED0_ON_L + 4 * channel, 0)
    bus.write_byte_data(I2C_ADDRESS, LED0_ON_L + 4 * channel + 1, 0)
    bus.write_byte_data(I2C_ADDRESS, LED0_OFF_L + 4 * channel, pulse & 0xFF)
    bus.write_byte_data(I2C_ADDRESS, LED0_OFF_L + 4 * channel + 1, pulse >> 8)

# Başlatma
pca9685_setup()

# GUI için Tkinter penceresi oluşturuluyor
root = tk.Tk()
root.title("Servo Motor Kontrol")

# Kanal 0 için kaydırıcı ve etiket
label0 = tk.Label(root, text="Kanal 0 Açısı")
label0.pack()
slider0 = tk.Scale(root, from_=0, to=180, orient="horizontal", command=lambda val: set_servo_angle(0, int(val)))
slider0.pack()

# Kanal 1 için kaydırıcı ve etiket
label1 = tk.Label(root, text="Kanal 1 Açısı")
label1.pack()
slider1 = tk.Scale(root, from_=0, to=180, orient="horizontal", command=lambda val: set_servo_angle(1, int(val)))
slider1.pack()

# Kanal 2 için kaydırıcı ve etiket
label2 = tk.Label(root, text="Kanal 2 Açısı")
label2.pack()
slider2 = tk.Scale(root, from_=0, to=180, orient="horizontal", command=lambda val: set_servo_angle(2, int(val)))
slider2.pack()

# Pencereyi başlat
root.mainloop()
