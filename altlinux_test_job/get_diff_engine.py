import requests
import json


def make_request(first_branch, second_branch):
    first_package_data = requests.get(f'https://rdb.altlinux.org/api/export/branch_binary_packages/{first_branch}').json()
    second_package_data = requests.get(f'https://rdb.altlinux.org/api/export/branch_binary_packages/{second_branch}').json()

    return first_package_data, second_package_data


def get_diff(first_branch, second_branch):
    first_packages = {package['name']: package for package in first_branch['packages']}
    second_packages = {package['name']: package for package in second_branch['packages']}

    diff = {'only_in_first': [], 'only_in_second': [], 'best_version_in_first': []}

    for package_name, package in (first_packages | second_packages).items():
        if package_name not in second_packages:
            diff['only_in_first'].append(package)
        elif package_name not in first_packages:
            diff['only_in_second'].append(package)
        elif first_packages[package_name]['version'] > second_packages[package_name]['version']:
            diff['best_version_in_first'].append(package)

    return diff


def format_to_json(diff, output_file):
    with open(output_file, 'w') as file:
        file.write(json.dumps(diff))


def generate_diff(first_branch, second_branch, output_file):
    first_package_data, second_package_data = make_request(first_branch, second_branch)
    diff = get_diff(first_package_data, second_package_data)
    result = format_to_json(diff, output_file)

    return result