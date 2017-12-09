# -*- coding: utf-8 -*-
#на основе примера https://github.com/natenka/pyneng-examples-exercises/blob/master/examples/12_useful_modules/argparse/parse_dhcp_snooping.py
import argparse
import click

# Default values:
DFLT_DB_NAME = 'dhcp_snooping.db'
DFLT_DB_SCHEMA = 'dhcp_snooping_schema.sql'


@click.group()
def main_args():
    pass

@main_args.command(help='create new db')
@click.option('--name', '-n', default=DFLT_DB_NAME,
              show_default=True, help='db filename')
@click.option('--schema', '-s', default=DFLT_DB_SCHEMA,
              show_default=True, help='db schema filename')
def create_db(**kwargs):
    print('Creating DB {} with DB schema {}'.format(kwargs['name'],
                                                    kwargs['schema']))


@main_args.command(help='add data to db')
#-1 означает, что может передаваться любое количество аргументов
@click.argument('files', nargs=-1)
@click.option('--db_file', default=DFLT_DB_NAME, show_default=True, help='db name')
@click.option('--add_sw_data', '-s', is_flag=True, default=False,
              help='add switch data if set, else add normal data')
def add(**kwargs):
    #По умолчанию nargs=-1 не требует чтобы был хотя бы один файл
    #это можно исправить указав required=True
    if kwargs['files']:
        if kwargs['add_sw_data']:
            print('Adding switch data to database')
        else:
            print('Reading info from file(s) \n{}'.format(', '.join(kwargs['files'])))
            print('\nAdding data to db {}'.format(kwargs['db_file']))


@main_args.command(help='get data from db')
@click.option('--db_file', default=DFLT_DB_NAME, show_default=True, help='db name')
@click.option('--key', '-k',
              type=click.Choice(['mac', 'ip', 'vlan', 'interface', 'switch']),
              help='host key (parameter) to search')
@click.option('--value', '-v', help='value of key')
@click.option('--show_db_content', '-a', is_flag=True, default=False,
              help='show db content')
def get(**kwargs):
    if kwargs['key'] and kwargs['value']:
        print('Geting data from DB: {}'.format(kwargs['db_file']))
        print('Request data for host(s) with {} {}'.format(kwargs['key'], kwargs['value']))
    elif kwargs['key'] or kwargs['value']:
        print('Please give two or zero args\n')
    else:
        print('Showing {} content...'.format(kwargs['db_file']))


if __name__ == '__main__':
    main_args()


'''
$ python parse_dhcp_snooping.py
Usage: parse_dhcp_snooping.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add        add data to db
  create_db  create new db
  get        get data from db

$ python parse_dhcp_snooping.py --help
Usage: parse_dhcp_snooping.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add        add data to db
  create_db  create new db
  get        get data from db


$ python parse_dhcp_snooping.py create_db --help
Usage: parse_dhcp_snooping.py create_db [OPTIONS]

  create new db

Options:
  -n, --name TEXT    db filename  [default: dhcp_snooping.db]
  -s, --schema TEXT  db schema filename  [default: dhcp_snooping_schema.sql]
  --help             Show this message and exit.

$ python parse_dhcp_snooping.py create_db
Creating DB dhcp_snooping.db with DB schema dhcp_snooping_schema.sql

$ python parse_dhcp_snooping.py create_db --name dhcp_db.sqlite
Creating DB dhcp_db.sqlite with DB schema dhcp_snooping_schema.sql


$ python parse_dhcp_snooping.py add --help
Usage: parse_dhcp_snooping.py add [OPTIONS] [FILES]...

  add data to db

Options:
  --db_file TEXT     db name  [default: dhcp_snooping.db]
  -s, --add_sw_data  add switch data if set, else add normal data
  --help             Show this message and exit.

$ python parse_dhcp_snooping.py add file1.txt file2.txt
Reading info from file(s)
file1.txt, file2.txt

Adding data to db dhcp_snooping.db

$ python parse_dhcp_snooping.py add file1.txt file2.txt --add_sw_data
Adding switch data to database



$ python parse_dhcp_snooping.py get --help
Usage: parse_dhcp_snooping.py get [OPTIONS]

  get data from db

Options:
  --db_file TEXT                  db name  [default: dhcp_snooping.db]
  -k, --key [mac|ip|vlan|interface|switch]
                                  host key (parameter) to search
  -v, --value TEXT                value of key
  -a, --show_db_content           show db content
  --help                          Show this message and exit.

$ python parse_dhcp_snooping.py get -a
Showing dhcp_snooping.db content...

$ python parse_dhcp_snooping.py get -k
Error: -k option requires an argument

$ python parse_dhcp_snooping.py get -k vlan
Please give two or zero args

$ python parse_dhcp_snooping.py get -k vlan -v 10
Geting data from DB: dhcp_snooping.db
Request data for host(s) with vlan 10

'''
