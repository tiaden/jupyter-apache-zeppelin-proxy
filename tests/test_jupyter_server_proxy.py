# Copyright 2020-2021 The MathWorks, Inc.

import os
import jupyter_zeppelin_proxy


def test_get_env():
    """Tests if _get_env() method returns the expected environment settings as a dict."""

    port = 10000
    assert jupyter_zeppelin_proxy._get_env(port) == f"ZEPPELIN_PORT={port}"


def test_setup_apache_zeppelin():
    """Tests for a valid Server Process Configuration Dictionary

    This test checks if the jupyter proxy returns the expected Server Process Configuration
    Dictionary for the Apache Zeppelin process.
    """
    icon_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, 'jupyter_zeppelin_proxy', 'icons', 'zeppelin.svg'
    )

    expected_apache_zeppelin_setup = {
        "command": [
            jupyter_zeppelin_proxy.get_apache_zeppelin_executable('zeppelin-daemon'),
            "start",
        ],
        "timeout": 100,
        "environment": jupyter_zeppelin_proxy._get_env,
        "new_browser_tab": True,
        "absolute_url": False,
        "launcher_entry": {
            "title": "Zeppelin",
            "icon_path": icon_path,
        },
    }

    actual_apache_zeppelin_setup = jupyter_zeppelin_proxy.setup_apache_zeppelin()

    assert expected_apache_zeppelin_setup == actual_apache_zeppelin_setup
    assert os.path.isfile(actual_apache_zeppelin_setup["launcher_entry"]["icon_path"])
