Before start:

1. open PWM
-> luckfox-config
enable PWM11_M1 and PWM10_M1
-> reboot
check /sys/class/pwm/, export pwm to user space
-> echo 0 > /sys/class/pwm/pwmchip10/export
-> echo 0 > /sys/class/pwm/pwmchip11/export
In principle, it only needs to be set once

Ultra Sound Driver use (55|PWM11_IR_M1) and (54|PWM10_M1)

Scale Driver use (56|UART3_TX_M1) and (57|UART3_RX_M1)

2. start service


