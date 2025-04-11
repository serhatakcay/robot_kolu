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
    try:
        bus.write_byte_data(I2C_ADDRESS, MODE1, 0x00)  # Normal çalışmaya ayar
        time.sleep(0.005)
        print("PCA9685 başarıyla başlatıldı.")
    except Exception as e:
        print(f"PCA9685 başlatılamadı: {e}")

# Servo açısını belirlemek için bir helper fonksiyon
def set_servo_angle(channel, angle):
    try:
        pulse_length = 4096  # 12 bit çözünürlük
        pulse_min = 150  # Minimum darbe genişliği (~1 ms)
        pulse_max = 600  # Maksimum darbe genişliği (~2 ms)
        pulse = int(pulse_min + (angle / 180.0) * (pulse_max - pulse_min))
        
        # Debug: Servo açısını yazdırıyoruz
        print(f"Kanal {channel} için {angle} dereceye ayar yapılıyor.")
        
        bus.write_byte_data(I2C_ADDRESS, LED0_ON_L + 4 * channel, 0)
        bus.write_byte_data(I2C_ADDRESS, LED0_ON_L + 4 * channel + 1, 0)
        bus.write_byte_data(I2C_ADDRESS, LED0_OFF_L + 4 * channel, pulse & 0xFF)
        bus.write_byte_data(I2C_ADDRESS, LED0_OFF_L + 4 * channel + 1, pulse >> 8)
        
    except Exception as e:
        print(f"Motor kontrol hatası: {e}")

# Başlatma
pca9685_setup()

# Kanal açılarını tutan sözlük
angles = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

# Butonlara tıklanınca kanalın açısını arttırma veya azaltma fonksiyonu
def increase_angle(channel):
    if angles[channel] < 180:
        angles[channel] += 5
        set_servo_angle(channel, angles[channel])
        print(f"Kanal {channel} açısı: {angles[channel]}")

def decrease_angle(channel):
    if angles[channel] > 0:
        angles[channel] -= 5
        set_servo_angle(channel, angles[channel])
        print(f"Kanal {channel} açısı: {angles[channel]}")

# GUI başlatma
root = tk.Tk()
root.title("Servo Kontrol")

# Kanal butonları ve + / - butonları
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.LEFT, padx=10)

# Kanal 0 butonları
btn_kanal_0 = tk.Button(frame_left, text="Kanal 0", command=lambda: select_channel(0))
btn_kanal_0.grid(row=0, column=0, pady=5)

btn_plus_0 = tk.Button(frame_right, text="+", command=lambda: increase_angle(0))
btn_plus_0.grid(row=0, column=1, pady=5)

btn_minus_0 = tk.Button(frame_right, text="-", command=lambda: decrease_angle(0))
btn_minus_0.grid(row=0, column=2, pady=5)

# Kanal 1 butonları
btn_kanal_1 = tk.Button(frame_left, text="Kanal 1", command=lambda: select_channel(1))
btn_kanal_1.grid(row=1, column=0, pady=5)

btn_plus_1 = tk.Button(frame_right, text="+", command=lambda: increase_angle(1))
btn_plus_1.grid(row=1, column=1, pady=5)

btn_minus_1 = tk.Button(frame_right, text="-", command=lambda: decrease_angle(1))
btn_minus_1.grid(row=1, column=2, pady=5)

# Kanal 2 butonları
btn_kanal_2 = tk.Button(frame_left, text="Kanal 2", command=lambda: select_channel(2))
btn_kanal_2.grid(row=2, column=0, pady=5)

btn_plus_2 = tk.Button(frame_right, text="+", command=lambda: increase_angle(2))
btn_plus_2.grid(row=2, column=1, pady=5)

btn_minus_2 = tk.Button(frame_right, text="-", command=lambda: decrease_angle(2))
btn_minus_2.grid(row=2, column=2, pady=5)

# Kanal 3 butonları
btn_kanal_3 = tk.Button(frame_left, text="Kanal 3", command=lambda: select_channel(3))
btn_kanal_3.grid(row=3, column=0, pady=5)

btn_plus_3 = tk.Button(frame_right, text="+", command=lambda: increase_angle(3))
btn_plus_3.grid(row=3, column=1, pady=5)

btn_minus_3 = tk.Button(frame_right, text="-", command=lambda: decrease_angle(3))
btn_minus_3.grid(row=3, column=2, pady=5)

# Kanal 4 butonları
btn_kanal_4 = tk.Button(frame_left, text="Kanal 4", command=lambda: select_channel(4))
btn_kanal_4.grid(row=4, column=0, pady=5)

btn_plus_4 = tk.Button(frame_right, text="+", command=lambda: increase_angle(4))
btn_plus_4.grid(row=4, column=1, pady=5)

btn_minus_4 = tk.Button(frame_right, text="-", command=lambda: decrease_angle(4))
btn_minus_4.grid(row=4, column=2, pady=5)

# Kanal seçildiğinde yapılacak işlemler
def select_channel(channel):
    print(f"Kanal {channel} seçildi.")

root.mainloop()
