# Copyright 2020-2021 The MathWorks, Inc.

import os
from pathlib import Path

import jupyter_apache_zeppelin_proxy


def test_get_env():
    """Tests if _get_env() method returns the expected environment settings as a dict."""

    port = 10000
    assert jupyter_apache_zeppelin_proxy._get_env(port) == {"ZEPPELIN_PORT": "10000"}


def test_setup_apache_zeppelin():
    """Tests for a valid Server Process Configuration Dictionary

    This test checks if the jupyter proxy returns the expected Server Process Configuration
    Dictionary for the Apache Zeppelin process.
    """
    icon_path = str(Path(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, 'jupyter_apache_zeppelin_proxy', 'icons', 'zeppelin.svg'
    )).resolve())

    expected_apache_zeppelin_setup = {
        "command": jupyter_apache_zeppelin_proxy._get_cmd,
        "timeout": 500,
        "environment": jupyter_apache_zeppelin_proxy._get_env,
        "new_browser_tab": True,
        "absolute_url": False,
        "launcher_entry": {
            "title": "Zeppelin",
            "icon_path": icon_path,
        },
    }

    actual_apache_zeppelin_setup = jupyter_apache_zeppelin_proxy.setup_apache_zeppelin()

    assert expected_apache_zeppelin_setup == actual_apache_zeppelin_setup
    assert os.path.isfile(actual_apache_zeppelin_setup["launcher_entry"]["icon_path"])
