# micropython-3-wire-spi-soft



Many RGB screens, like the ST7701, use 3-wire SPI for initialization, which requires sending data in a 9-bit format. However, MicroPython does not support 9-bit SPI transmission. Therefore, I wrote a 9-bit transmission library using simple GPIO toggling. Although the speed is slower, it compensates for the lack of 9-bit SPI support in MicroPython. You can modify the initialization commands as needed. The following is specifically for the initialization commands of a 2.8-inch 640x480 ST7701 RGB screen. Since the initialization commands vary for different screens, please refer to the respective manual for your screen.

很多rgb屏比如st7701的初始化部分都是用的3线spi，需要用9bit的格式来发送数据，但是micropython并不支持9bit的spi发送，因此我通过单纯的引脚变化来写了一个9bit的发送库，虽然速度较慢，但是可以弥补micropython不能发送9bit spi的不足，可以根据需要改写自己的初始化命令，这里只针对640x480的2.8寸st7701 rgb屏的初始化命令，不同屏幕的初始化命令都不同，请自行查阅手册。