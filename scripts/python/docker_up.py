import os
import sys
import traceback

import re

def show_environ():
    print('BEGIN: os.environ')
    for k,v in os.environ.items():
        print('{} -> {}'.format(k,v))
    print('END!!! os.environ')


def run_this(args, callback=None):
    import logging
    import subprocess
    try:
        pipe = subprocess.Popen(args, shell=True, env=os.environ, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except Exception as e:
        logging.error(str(e))
        return False
    while (1):
        s = pipe.stdout.read()
        if s:
            if (callable(callback)):
                try:
                    callback(s)
                except Exception:
                    traceback.print_exc(file=sys.stdout)
                print(s,)
        if pipe.returncode is None:
            pipe.poll()
        else:
            break
    if not 0 == pipe.returncode:
        return False
    return True


if (__name__ == '__main__'):
    '''
        set PATH=C:\Program Files\Docker\Docker\resources\bin;C:\ProgramData\DockerDesktop\version-bin;

        docker-compose up -d
        CID=$(docker ps -qf "name=mongodb")
        echo "CID=$CID"
        if [[ ! $CID. == . ]]
        then
            echo "Update $CID"
            docker update --restart unless-stopped --cpus="2.5" --memory="2g" --memory-swap="2.5g" $CID
        fi
    '''
    __ID__ = []
    
    regex_ID = r"^(.*?)'(?P<id>[0-9a-z]+)\\+(.*?).'"
    
    def handle_stdout(s):
        if (len(__ID__) == 0):
            matches = re.finditer(regex_ID, str(s), re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                d = match.groupdict()
                __ID__.append(d.get('id'))
                if (len(__ID__) > 0):
                    print('ID: {}'.format(__ID__[0]))
    
    if (0):
        show_environ()
    
    __is__ = len(__ID__) == 0
    if (not __is__):
        args = ['docker','ps', '--format', '{{.ID}}', '--filter', 'name=mongodb']
        print(run_this(args, callback=handle_stdout))

    if (__is__):
        args = ['docker-compose','up','-d']
        print(run_this(args))

    if (__is__):
        args = ['docker','ps', '--format', '{{.ID}}', '--filter', 'name=mongodb']
        print(run_this(args, callback=handle_stdout))

    if (__is__):
        cmd = 'docker update --restart unless-stopped --cpus="2.5" --memory="2g" --memory-swap="2.5g" {}'.format(__ID__[0])
        args = [cmd.split()]
        print( run_this(args))

    