import click

@click.command()
@click.option('--verbose', is_flag=True, help='Will print verbose messages.')
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.argument('country')
def cli(verbose, name, country):
    """This is an example script to learn Click."""
    if verbose:
        click.echo('We are in the verbose mode.')
    click.echo("Hi!")
    click.echo("Hello {0}".format(country))
    for n in name:
        click.echo('Bye {}'.format(n))


if __name__ == '__main__':
    cli()
