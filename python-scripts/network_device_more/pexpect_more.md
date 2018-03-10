На некоторых устройствах нельзя избавиться от постраничного просмотра (paging) команды и надо нажимать пробел или подобное.
В циско это выглядит так (если отключение есть, это делается командой terminal length 0):
```
mmi polling-interval 60
no mmi auto-configure
 --More--
```

Пример считывания команды sh run без отключения paging.
```python
import pexpect
import time

USER = PASSWORD = ENABLE_PASS = 'cisco'


ssh = pexpect.spawn('ssh {}@{}'.format(USER, '192.168.100.1'))

ssh.expect('Password:')
ssh.sendline(PASSWORD)

ssh.expect('[#>]')
ssh.sendline('enable')

ssh.expect('Password:')
ssh.sendline(ENABLE_PASS)

ssh.expect('#')



ssh.sendline('sh run')
result = ''

while True:
    match = ssh.expect(['More', '#'])
    output = ssh.before.decode('utf-8')
    #print('"{}"'.format(output))
    result += output
    if match == 1:
        break
    ssh.send(' ')
    time.sleep(1)

print(result)
```
