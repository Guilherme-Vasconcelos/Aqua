import ast

from os import popen
from os.path import basename

from aqua.utils import collect_python_files_at

PROJ_ROOT_PATH = popen('git rev-parse --show-toplevel').read().strip()
TALK_HANDLER_PATH = f'{PROJ_ROOT_PATH}/aqua/extensions/talk/talk.py'
HELP_HANDLER_PATH = f'{PROJ_ROOT_PATH}/aqua/extensions/commands/help.py'

AQUA_EXTENSIONS_FILES = collect_python_files_at(f'{PROJ_ROOT_PATH}/aqua/extensions/commands') + [TALK_HANDLER_PATH]


def test_auths_for_all_aqua_extensions():
    results = {}
    for _file in AQUA_EXTENSIONS_FILES:
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


def test_documentation_for_all_aqua_extensions():
    with open(HELP_HANDLER_PATH, 'r') as f:
        help_src_code = f.read()

    parsed_ast = ast.parse(help_src_code)

    remaining_commands_to_find_in_help = set()
    for _file in AQUA_EXTENSIONS_FILES:
        command_to_seek = '/' + basename(_file).replace('.py', '')
        if command_to_seek.startswith('/_') or command_to_seek == '/talk':
            # Internal commands do not need docs, neither does the talk handler
            continue

        remaining_commands_to_find_in_help.add(command_to_seek)

    for node in ast.walk(parsed_ast):
        if isinstance(node, ast.AugAssign):
            full_text_with_potential_command_docs = node.value.value
            for potential_command_match in remaining_commands_to_find_in_help:
                if potential_command_match in full_text_with_potential_command_docs:
                    # Match
                    remaining_commands_to_find_in_help.remove(potential_command_match)
                    break

    assert len(remaining_commands_to_find_in_help) == 0
