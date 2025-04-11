import smbus
import time

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

try:
    print("Robot kolu başlangıç pozisyonuna getiriliyor...")
    while True:
        # Kanal 0
        for angle in range(0, 6, 1):
            set_servo_angle(1, angle) #Kanal 0'ı kontrol ettiğimizi belirttik
            print(f"Kanal 1 açısı: {angle}")
            time.sleep(0.2) #hareket hizi

        # Kanal 2
        for angle in range(0, 6, 1):
            set_servo_angle(2, angle)
            print(f"Kanal 2 açısı: {angle}")
            time.sleep(0.2)

        # Kanal 0
        for angle in range(30, -1, -5):
            set_servo_angle(0, angle)
            print(f"Kanal 0 açısı: {angle}")
            time.sleep(0.2)  # Hareket hızı

except KeyboardInterrupt:
    print("Robot kolu başlangıç pozisyonuna geldi.")
