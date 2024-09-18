# type: ignore
import time
import board
import busio
import adafruit_icm20x

i2c = busio.I2C(board.GP5, board.GP4)
icm = adafruit_icm20x.ICM20948(i2c, 0x68)
icm.accelerometer_data_rate_divisor = 1

buffer = ""

with open("data.csv", "a") as f:
    f.write("t_sec,acc_x,acc_y,acc_z,gyro_x,gyro_y,gyro_z\n")
    i = 0
    while True:

        # Save to the buffer
        buffer += "%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f\n" % (time.monotonic(), icm.acceleration[0], icm.acceleration[1], icm.acceleration[2], icm.gyro[0], icm.gyro[1], icm.gyro[2])

        # Write to the flash at a slower rate (every 5 sec)
        if(int(time.monotonic()) % 5 == 0):
            f.write(buffer)
            buffer = ""
            f.flush()

        time.sleep(0.05)