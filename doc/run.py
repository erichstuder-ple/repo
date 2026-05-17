#!/usr/bin/env python3

import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent / 'project_management'))
from executor import Executor # type: ignore


if __name__ == "__main__":
    additional_arguments = [
        {
            'flag': '-b',
            'name': '--build',
            'help': 'build documentation'
        },
        {
            'flag': '-a',
            'name': '--autobuild',
            'help': 'start sphinx-autobuild'
        }
    ]

    ex = Executor(additional_arguments, description='Documentation')

    if ex.arguments.build:
        # commands = 'make html SPHINXOPTS="--fail-on-warning"'
        commands = 'sphinx-build source build'
    elif ex.arguments.autobuild:
        # commands = 'sphinx-autobuild '+ ('' if ex.arguments.verbose else '-q') +' --port 8000 --host 0.0.0.0 '
        # commands += '--watch ../software/firmware/src --watch ../features '
        # commands += '--re-ignore auto_generated source _build/html'
        commands = 'sphinx-autobuild source _build'
    else:
        commands = None

    try:
        ex.run(commands)
    except KeyboardInterrupt:
        print('  Interrupted by user')
