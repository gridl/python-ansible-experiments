from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint

import yaml
import tqdm
from netmiko import ConnectHandler


def conn_ssh_threads(function, devices, command, limit=3, progress_bar=True):
    result_dict = {}

    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ssh = [executor.submit(function, device, command)
                      for device in devices]
        done_tasks = as_completed(future_ssh)
        if progress_bar:
            success_bar = tqdm.tqdm(total=len(devices), desc='Correct'.rjust(10))
            done_tasks = tqdm.tqdm(done_tasks, total=len(devices), desc='All'.rjust(10))
        for task in done_tasks:
            task_ok, result = task.result()
            if task_ok:
                success_bar.update(1)
            result_dict.update(result)
        success_bar.close()

    return result_dict


def send_show_command(device, show_command):
    result = {}
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result[device['ip']] = ssh.send_command(show_command)

    if device['ip'] == '192.168.100.1':
        return False, result
    else:
        return True, result



if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.load(f)

    results = conn_ssh_threads(send_show_command, devices, 'sh ip int br')
    print()

