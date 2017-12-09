import subprocess

import click


@click.command()
@click.option('--ip_address', '-a', required=True)
@click.option('--count', '-c', default=2, show_default=True)
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
        click.echo(reply.stdout)
        return 0
    else:
        click.echo(reply.stdout)
        click.echo(reply.stderr)
        return reply.returncode

if __name__ == '__main__':
    ping_ip()

