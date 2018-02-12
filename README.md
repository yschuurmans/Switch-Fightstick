# Switch-Fightstick
[![Thumbnail](https://pbs.twimg.com/ext_tw_video_thumb/954858389539975168/pu/img/8h6tH3_nI0g9VY9R.jpg)](https://twitter.com/ebith/status/954858876028907521)

## Requirement
- ATMega32U4 Board or see [shinyquagsire23/Switch-Fightstick's README](https://github.com/shinyquagsire23/Switch-Fightstick/blob/master/README.md)
- USB to serial adapter
- USB micro-b cable * 2

## Usage
[NintendoSwitchをPCから操作する - おいら屋ファクトリー](https://blog.feelmy.net/control-nintendo-switch-from-computer/)(in Japanese)

### On MacOS
```sh
brew install avr-dude osx-cross/avr/avr-gcc
git clone --recursive https://github.com/ebith/Switch-Fightstick.git
cd Switch-Fightstick
make
avrdude -pm32u4 -cavr109 -D -P$(ls /dev/tty.usbmodem*) -b57600 -Uflash:w:Joystick.hex # need reset

pip install pyserial
./example/rapid-fire-a-button.py /dev/tty.usbserial*
```
