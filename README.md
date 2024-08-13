# Air Rocket Logger
This is some simple code to log data from an air rocket.

## Components
All components are bought from Pimoroni
- [Pico LiPo (16MB)](https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39335427080275)
- [ICM20948 Motion Sensor Breakout](https://shop.pimoroni.com/products/icm20948?variant=27843993960531)
- [JST-SH Cable (male to male), any length is fine](https://shop.pimoroni.com/products/jst-sh-cable-qwiic-stemma-qt-compatible?variant=31910609813587)
- [LiPo Battery (150mA)](https://shop.pimoroni.com/products/lipo-battery-pack?variant=20429081991)
- Any USB-C cable, for loading the code and accessing the data

## Assembly
1. If you haven't already, install [CircuitPython](https://adafruit-circuit-python.s3.amazonaws.com/bin/pimoroni_picolipo_16mb/en_GB/adafruit-circuitpython-pimoroni_picolipo_16mb-en_GB-8.2.9.uf2) on your Pico, by dragging and dropping the `.uf2` file onto the drive named `RPI-RP2`. The drive should disappear, then re-mount under the new name `CIRCUITPY`. You'll need v8.2.9 to run, which the previous link should download.
2. Use the JST cable to connect the Pico and the motion sensor
3. Copy and paste the whole `libs/`, `code.py`, and `boot.py` from this repository to the Pico's drive, ideally in that order.
4. Unplug the Pico from your computer, and plug in the battery to the slot on the Pico
5. If the white LED does not come on, quickly press the POWER button on the Pico once
6. Allow the Pico to log some data for 10+ seconds
7. Remove the battery, and plug the Pico back into your computer. The data should be stored in `data.csv`, which you should copy to a different location on your machine

## Important Notes
- `data.csv` is appended to every time the Pico runs, and will print a new header line every time this occurs. Be careful you're only using the dataset you want to use
- Sometimes the Pico won't boot up properly, I have no idea why. It seems to happen both on battery, and when plugging into the computer, and is easily fixed by just pressing the POWER button. If the white light isn't on, data won't be logged, and it won't show up as a drive on your computer
- Data is read from the motion sensor as quick as it can (up to 20 times per second), and written to `data.csv` every 5 seconds, to make sure it doesn't get stuck. It's important to wait at least 5s after you've collected your useful data, to make sure it's all written to the log.
- In testing, the median time between readings was around 0.142s, although this occasionally has a spike of up to 0.5s when writing data to the flash. This spike can be reduced by modifying the timeout on line 20 in `code.py` from 5 to a higher value, although this will also affect how long you have to wait before depowering the Pico. See the chart below for experimental results.

## Modifying the Code
By default, the Pico will be configured such that the code itself can write to its flash, which causes it to be mounted as a read-only file system when you plug it into a computer. To change the code (or to delete `data.csv`), unplug the Pico from your computer, and use a jumper cable or bit of wire to short pin 0 to any ground connection (there's one labelled "-" two pins away). Keep this connection shorted when you plug it back into your computer, and the Pico should mount itself in writeable mode. No data can be written to the log file while the Pico is in this mode.

## Libraries
Libraries in the `libs/` directory are from [Adafruit's CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle), and are redistributed for convenience of install. The most up-to-date versions can be found in their original repository.
