
На некоторых устройствах нельзя избавиться от постраничного просмотра (paging) команды и надо нажимать пробел или подобное.
В циско это выглядит так (если отключение есть, это делается командой terminal length 0):
```
mmi polling-interval 60
no mmi auto-configure
 --More--
```

Пример считывания команды sh run без отключения paging.
```python
import telnetlib
import time


USER = PASSWORD = ENABLE_PASS = 'cisco'.encode('utf-8')

t = telnetlib.Telnet('192.168.100.1')

t.read_until(b'Username:')
t.write(USER + b'\n')

t.read_until(b'Password:')
t.write(PASSWORD + b'\n')
t.write(b'enable\n')

t.read_until(b'Password:')
t.write(ENABLE_PASS + b'\n')

t.read_until(b'#')


t.write(b'sh run\n')
result = ''

while True:
    output = t.read_very_eager().decode('utf-8')
    #print('"{}"'.format(output))
    if '#' in output:
        break
    result += output
    t.write(b' ')
    time.sleep(1)

print(result)
```
