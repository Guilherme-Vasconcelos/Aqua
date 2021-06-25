import ast

from os import popen
from os.path import basename

from aqua.utils import collect_python_files_at

PROJ_ROOT_PATH = popen('git rev-parse --show-toplevel').read().strip()
TALK_HANDLER_PATH = f'{PROJ_ROOT_PATH}/aqua/extensions/talk/talk.py'


def test_auths_for_all_aqua_extension_commands():
    files_to_analyze = collect_python_files_at(f'{PROJ_ROOT_PATH}/aqua/extensions/commands') + [TALK_HANDLER_PATH]

    results = {}
    for _file in files_to_analyze:
        with open(_file, 'r') as f:
            command_to_seek = basename(_file).replace('.py', '')
            src_code = f.read()

        parsed_ast = ast.parse(src_code)

        found_auth = False
        for node in ast.walk(parsed_ast):
            if isinstance(node, ast.FunctionDef) and node.name == command_to_seek:
                # If the command was found, then it MUST have auth
                for child_node in ast.iter_child_nodes(node):
                    if isinstance(child_node, ast.Name):
                        if child_node.id == 'authorize':
                            found_auth = True
                            results[command_to_seek] = 'OK'

        if not found_auth:
            results[command_to_seek] = 'FAILED'
            print(f'{command_to_seek} has no auth.')

    assert 'FAILED' not in results.values()
