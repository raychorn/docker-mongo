# mongodb via docker-compose in windows

## Table of Contents

- [Usage](#usage)

## about

This is an incomplete effort to migrate a process that began in Linux but ran into performance issues because docker in wsl2 is just a waste of performance and time.

## Usage <a name = "usage"></a>

./docker-up.sh

For Windows use "cmd" shell.

### Install Mongo Client (Ubuntu 20.04)

Using Python to validate the mongodb installation via docker.

./makevenv.sh


C:\Python38\;C:\Python38\DLLs\;C:\Python38\Scripts\;C:\Python38\Tools\;C:\Python38\Tools\ninja\;C:\Python39\Scripts\;C:\Python39\;C:\Python38\Scripts\;C:\Python38\;C:\Python36\;C:\Python36\DLLs\;C:\Python36\Scripts\;C:\Python36\Tools\;C:\Python36\Tools\ninja\;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Python2715\;C:\Python2715\Scripts;C:\Users\Owner\AppData\Roaming\Python\Scripts;C:\Program Files (x86)\Razer Chroma SDK\bin;C:\Program Files\Razer Chroma SDK\bin;C:\Program Files (x86)\Razer\ChromaBroadcast\bin;C:\Program Files\Razer\ChromaBroadcast\bin;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\PuTTY\;C:\Windows\system32\config\systemprofile\AppData\Local\Microsoft\WindowsApps;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\Program Files\TortoiseSVN\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\msys\opt\windows_64\bin;%USERPROFILE%\.cargo\bin;C:\Program Files\dotnet;C:\tools\lxrunoffline;C:\Go\bin;C:\Program Files\Docker\Docker\resources\bin;C:\ProgramData\DockerDesktop\version-bin;C:\Program Files\Git\cmd

### Production Deployment

git clone the-repo-goes-here
Reference the host directory for the docker-compose file.
Dockerfile:
  buid the .venv
  find the mongodb ip address.
  docker-compose up -d
  setup the crontab job to restart.
  perform smoke test to ensure the web-head is running.

#### nginx

cd /etc/nginx/sites-enabled
unlink default



(c). Copyright, Ray C Horn, All Rights Reserved.