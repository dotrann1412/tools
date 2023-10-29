# VamSE - Process Controller


## Introduction

This small python 3 tool is to help `VamSE` run continuous without any corruption by start the VamSE process and observe it. This scipt is also holding some specialized tasks:
- Check for the update of new version of `VamSE - metadata` then notify the VamSE process to restart.
- Start VamSE immediately whenever it is killed.

## How to use it?

The tool can be executed in either pre-compiled executable (.exe file) or directly using python intepreter.

To make the executable, use pyinstaller from python packages:

```sh
python -m pyinstaller run.py --onefile 
```

Make sure pyinstaller has been already in your python environment before; and all requirements must be installed:

```sh
python -m pip install --upgrade pip
python -m pip install pyinstaller
python -m pip install -r requirements.txt
```

To let it able to handle VamSE process, move the executable file (or run.py) to the deployment folder of VamSE, create a `.env` file at the same directory with the following values:

```sh
public_path = [path to where metadata is stored]
```

The directory should looked like this:

```sh

- VamSE - Deployment folder
├───bin
|   ├───run.exe (or run.py)
|   └───VamSE.exe
├───resouces
├───tools
├───.env
└───config.json
```

Open CMD or Terminal at the root folder of deployment folder, then run the executable file (or run.py) with the following command:

```sh
bin/run.exe (or python bin/run.py)
```

## Contact information

For any issue, contact us via:
- Email: <SAI-libs-team@gameloft.com>