import subprocess

import click

'''
В предыдущих вариантах функция ping_ip использовалась для создания CLI-интерфейса.
Однако, в этом случае функция перестает быть обычной функцией Python и становится
интерфейсом командной строки.
Поэтому, например, мы не сможем возвращать значения в функции и получать их -
для интерфейса командной строки это просто не имеет смысла.

В этом примере создана отдельная функция parse_cli_args, которая уже внутри вызывает
функцию ping_ip
'''

@click.command()
@click.argument('ip_address')
@click.option('count', '-c', default=2, show_default=True)
def parse_cli_args(ip_address, count):
    '''Скрипт пингует указанный адрес'''
    pingable, output = ping_ip(ip_address, count)
    if pingable:
        click.echo('Хост {ip} пингуется'.format(ip=ip_address))
    else:
        click.echo('Хост {ip} не пингуется'.format(ip=ip_address))
    click.echo(output)


def ping_ip(ip_address, count):
    '''
    Ping IP address and return tuple:
    On success: (return code = 0, command output)
    On failure: (return code, error output (stderr))
    '''
    reply = subprocess.run('ping -c {count} -n {ip}'
                           .format(count=count, ip=ip_address),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout+reply.stderr

if __name__ == '__main__':
    parse_cli_args()

