import subprocess

import click


@click.command()
@click.argument('ip_address')
@click.option('count', '-c', default=2, show_default=True)
def parse_cli_args(ip_address, count):
    '''Скрипт пингует указанный адрес'''
    pingable, output = ping_ip(ip_address, count)
    if pingable:
        click.echo(click.style('### Хост {ip} доступен'.format(ip=ip_address),
                               fg='green', bold=True))
    else:
        click.echo(click.style('### Хост {ip} недоступен'.format(ip=ip_address),
                               fg='red', bold=True))
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

