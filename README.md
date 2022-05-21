# Apache Zeppelin Integration for Jupyter

----

The Apache Zeppelin Integration for Jupyter enables you to access Apache Zeppelin in a web browser from your Jupyter environment. 

`jupyter-apache-zeppelin-proxy` is a Python® package based on the following packages.

| Package                                                                    | Description                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy) | Extends Jupyter environments to launch Apache Zeppelin as an external process alongside the notebook server. For more information see [GUI Launchers](https://jupyter-server-proxy.readthedocs.io/en/latest/launchers.html#jupyterlab-launcher-extension). |

**NOTE:** This package *currently*, does not provide a kernel level integration with Jupyter.

To report any issues or suggestions, see the [Feedback](#feedback) section.

----
## Requirements

This package has the same requirements as its dependencies:
* See [Requirements](https://github.com/jupyterhub/jupyter-server-proxy#requirements) from `jupyter-server-proxy`
* See [Requirements](https://zeppelin.apache.org/docs/latest/quickstart/install.html#requirements) from `Apache Zeppelin`

After downloading Apache Zeppelin, make sure to create a symbolic link in PATH that points to the Apache Zeppelin daemon.

```bash
# if the downloaded Apache Zeppelin package resides at /opt/apache-zeppelin
ln -s /opt/apache-zeppelin/bin/zeppelin-daemon.sh /usr/bin/zeppelin-daemon
```

## Installation

### PyPI
This repository can be installed directly from the Python Package Index.
```bash
python -m pip install jupyter-apache-zeppelin-proxy
```

If you want to use this integration with JupyterLab®, ensure that you have JupyterLab installed on your machine by running the following command:
```bash
python -m pip install jupyterlab
```

You should then install `jupyterlab-server-proxy` JupyterLab extension. To install the extension, use the following command:

``` bash
jupyter labextension install @jupyterlab/server-proxy
```

### Building From Sources
```bash
git clone https://github.com/tiaden/jupyter-apache-zeppelin-proxy.git

cd jupyter-apache-zeppelin-proxy

python -m pip install .
```

## Usage

Upon successful installation of `jupyter-apache-zeppelin-proxy`, your Jupyter environment should present options to launch Apache Zeppelin.

* Open your Jupyter environment by starting jupyter notebook or lab
  ```bash
  # For Jupyter Notebook
  jupyter notebook

  # For Jupyter Lab
  jupyter lab 
  ```

* If you are using Jupyter Notebook, on the `New` menu, select `Zeppelin`. If you are using JupyterLab, select the Zeppelin icon on the launcher.

<p align="center">
  <img alt="image" width="600" src="https://github.com/tiaden/jupyter-apache-zeppelin-proxy/raw/master/img/apache_zeppelin_jupyter_lab.png">
</p>


## Integration with JupyterHub

To use this integration with JupyterHub®, you must install the `jupyter-apache-zeppelin-proxy` python package in the Jupyter environment launched by your JupyterHub platform. 

For example, if your JupyterHub platform launches Docker containers, then install this package in the Docker image used to launch them.

## Troubleshooting

In the environment that you have installed the package:

* Verify if java in installed (i.e. if it is in the PATH). Java (version 8 or later ) installation is required by apache zeppelin 
    ```bash
    $ which java
    /usr/bin/java
    ```

* Verify if the Apache Zeppelin daemon is discoverable (i.e. if it is in the PATH)
    ```bash
    $ which zeppelin-daemon
    /usr/bin/zeppelin-daemon
    ```

* Check if their Python version is 3.8 or higher
    ```bash
    $ python --version
    Python 3.8.10
    ```

* Ensure that `jupyter-apache-zeppelin-proxy` and the `jupyter` executables are in the same environment as the python executable.
    For example if you are using VENV to manage your python environments:
    ```bash
    $ which python
    /home/user/my-project/packages/.venv/bin/python

    $ which jupyter-apache-zeppelin-proxy
    /home/user/my-project/packages/.venv/bin/jupyter-apache-zeppelin-proxy

    $ which jupyter
    /home/user/my-project/packages/.venv/bin/jupyter
    ```
    Notice that `jupyter-apache-zeppelin-proxy`, `jupyter` and the `python` executable are in the same parent directory, in this case it is: `/home/user/my-project/packages/.venv/bin`

* Ensure that you are launching `jupyter notebook` using the same executable as listed above.

* Ensure that all three packages are installed in the same python environment
    ```bash
    # Pipe the output of pip freeze and grep for jupyter and jupyter-apache-zeppelin-proxy.
    # All two packages should be highlighted in the output.
    # If you don't see anyone of them, then either the packages missing in the output have been installed
    # in a different python environment or not installed at all.
    $ pip freeze | grep -E "jupyter|jupyter-apache-zeppelin-proxy"
    ```

* If the integration is not showing up as an option to the dropdown box in the Jupyter notebook:
    ```bash
    #Run the following commands and verify that you are able to see similar output:
    
    $ jupyter serverextension list
    config dir: /home/user/anaconda3/etc/jupyter
        jupyter_server_proxy  enabled
        - Validating...
        jupyter_server_proxy  OK
        jupyterlab  enabled
        - Validating...
        jupyterlab 2.2.6 OK
    
    $ jupyter nbextension list
    Known nbextensions:
    config dir: /home/user/anaconda3/etc/jupyter/nbconfig
        notebook section
        jupyter-js-widgets/extension  enabled
        - Validating: OK
        tree section
        jupyter_server_proxy/tree  enabled
        - Validating: OK  $ pip freeze | grep -E "jupyter|jupyter-apache-zeppelin-proxy"
    
    # IF the server does not show up in the commands above, install:
    $ pip install jupyter_contrib_nbextensions
    ```

## Feedback

We encourage you to try this repository with your environment and provide feedback.
If you encounter a technical issue or have an enhancement request, create an issue [here](https://github.com/tiaden/jupyter-apache-zeppelin-proxy/issues)
