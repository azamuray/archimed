# Archimed

### Description

``Archimed`` - проект для оживления статуи Архимеда, которая изначально была куплена для интерьера

С помощью Arduino, Raspberry Pi и OpenCV мы с моим коллегой по реализации безумных идей [Арби Башаевым](https://github.com/Arbios "Senior Swift Developer") смогли сделать так, чтоб статуя поворачивала голову в сторону того, кто попадает в объектив камеры

Для обычного смертного выглядит криповато, когда бездушная статуя следит за ним, но для программистов все это нули и единицы

### Setup

Необходимо подключить плату Arduino через USB и запустить файл "ardu.ino" в Arduino IDE

### Run

После шага Setup необходимо в терминале запустить следующий скрипт, который установит необходимые зависимости и активирует Архимеда

    $ ./run.sh

### Stop

Для остановки необходимо либо в терминале нажать Ctrl+C, либо в окне камеры нажать ESC
