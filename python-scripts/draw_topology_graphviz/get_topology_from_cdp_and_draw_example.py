import re
from pprint import pprint

from draw_network_graph import draw_topology


def parse_sh_cdp_neighbors(command_output):
    regex = re.compile(r'(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)'
                       r'  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)')
    connect_dict = {}
    l_dev = re.search(r'(\S+)[>#]', command_output).group(1)
    connect_dict[l_dev] = {}
    for match in regex.finditer(command_output):
        r_dev, l_intf, r_intf = match.group('r_dev', 'l_intf', 'r_intf')
        connect_dict[l_dev][l_intf] = {r_dev: r_intf}
    return connect_dict


def create_network_map(filenames):
    network_map = {}
    for filename in filenames:
        with open(filename) as show_command:
            parsed = parse_cdp_neighbors(show_command.read())
            for key, value in parsed.items():
                key, value = min(key, value), max(key, value)
                network_map[key] = value
    return network_map



if __name__ == "__main__":
    infiles = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt',
               'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']
    topology = create_network_map(infiles)
    pprint(topology)
    draw_topology(topology)

