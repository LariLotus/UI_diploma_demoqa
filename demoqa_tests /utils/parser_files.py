from demoqa_tests.utils import path


def read_txt_file(name_txt_file):
    with open(path.to_resources(name_txt_file)) as file:
        return file.read().split('\n')


