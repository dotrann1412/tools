import subprocess, os, argparse, sys, time, json, shutil, traceback

def main(options):
    exe, cwd = options.executable if options.executable else options.command, options.working_directory

    if not exe:
        print('[ERROR] Neither -c and -exe were not specified correctly')
        return 1

    if not cwd:
        cwd = os.getcwd()
        print(f'[WARNING] Working directory was not specified, use {cwd} instead.')

    elif not os.path.exists(cwd):
        print('[ERROR] The provided working directory does not exist')
        return 1

    max_try = options.max_try

    while max_try == -1 or max_try > 0:
        if max_try != -1:
            print(f'Trying {max_try}...')

        try:
            p = subprocess.Popen(
                exe, 
                cwd = cwd, 
                shell = True, 
                stdout = sys.stdout, 
                stderr = sys.stderr
            )

            p.communicate() 
        except Exception as er:
            traceback.print_exc()
            time.sleep(60)             
        finally:
            if p is not None: 
                p.kill()

            if max_try != -1:
                max_try -= 1
    else:
        print('[STATUS] Tried exceeded max times')

    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process controller')

    parser.add_argument('-wd', '--working-directory', type=str, help='Root folder', default = os.getcwd())   
    parser.add_argument('-c', '--command', type=str, help="Command to run", required = False)
    parser.add_argument('-exe', '--executable', type=str, help='Path to your executable file', required = False)
    parser.add_argument('-mx', '--max-try', type=int, default=-1, help="Max time to re-try the process")

    sys.exit(main(parser.parse_args()))