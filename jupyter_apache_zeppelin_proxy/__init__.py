import os
import shutil


def _get_env(port):
    # Start Apache Zeppelin in ZEPPELIN_NOTEBOOK_DIR env variable if set.
    # If not, start in user home directory

    working_dir = os.getenv("ZEPPELIN_WORKDIR", os.path.expanduser('~'))
    return {"ZEPPELIN_PORT": str(port), "ZEPPELIN_NOTEBOOK_DIR": str(working_dir)}


def _get_cmd():
    executable = "zeppelin-daemon"
    cmd = [
        get_apache_zeppelin_executable(executable),
        'start'
    ]
    return cmd


def get_apache_zeppelin_executable(executable):
    # Find Apache Zeppelin daemon
    # the installation process should place it on the path
    if shutil.which(executable):
        return executable
    raise FileNotFoundError(f'Could not find {executable} in PATH')


def get_icon_path():
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'icons', 'zeppelin.svg'
    )


def setup_apache_zeppelin():
    server_process = {
        'command': _get_cmd,
        'environment': _get_env,
        'timeout': 500,
        'new_browser_tab': True,
        'absolute_url': False,
        'launcher_entry': {
            'title': 'Zeppelin',
            'icon_path': get_icon_path()
        }
    }
    return server_process
