Developer Environment Setup
===========================

Installing UV
-------------

We utilize Astral's `UV <https://github.com/astral-sh/uv>`__ as the package manager for this project. UV is
an all-in-one tool for managing depedencies and creating reproducable environments using a sharable `uv.lock` file.
To install UV select your OS and run the command:

.. tab-set::

   .. tab-item:: Linux and macOS

      .. code-block:: console

         $ curl -LsSf https://astral.sh/uv/install.sh | sh

   .. tab-item:: Windows

      .. code-block:: pwsh-session

         PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

See `UV's documentation <https://docs.astral.sh/uv/>`__ for more details.

Installing ``bpod-gui``
-----------------------

At this time, ``bpod-gui`` is not available via PyPi and must be cloned from GitHub using the below command:

    >>> git clone https://github.com/olfactorybehaviorlab/bpod-gui

``bpod-gui`` is created using ``qtpy`` to allow developers to utilize their preferred Qt Python bindings.
Each binding has a different license--some of which require a purchase for commercial use-cases. The available bindings are:

    #. `PySide6 <https://pypi.org/project/PySide6/>`__
    #. `PySide2 <https://pypi.org/project/PySide2/>`__
    #. `PyQt5 <https://pypi.org/project/PyQt5/>`__
    #. `PyQt6 <https://pypi.org/project/PyQt6/>`__

Using **UV** we can simultaneously create a virtual environment, install the required core depdencies, and install any
extra/optional depdencies. Select the Qt binding package you would like to use and run the included command from within
the cloned ``bpod-gui`` repository:

.. tab-set::

   .. tab-item:: Package only (no Qt Bindings)

      .. code-block:: console

         $ uv sync

   .. tab-item:: PySide6

      .. code-block:: console

         $ uv sync --extra pyside6

   .. tab-item:: PySide2

      .. code-block:: console

         $ uv sync --extra pyside2

   .. tab-item:: PyQt5

      .. code-block:: console

         $ uv sync --extra pyqt5

   .. tab-item:: PyQt6

      .. code-block:: console

         $ uv sync --extra pyqt6

Documentation Build
-------------------

We use `Sphinx <https://www.sphinx-doc.org/>`_ to build our documentation

To install the documentation depedencies, run the following command:

.. code-block:: console

    $ uv sync --no-default-groups --extra docs

Once the dependencies are installed, the HTML needs to be built. If the documentation only needs to be built once, use
*sphinx-build.* However, if developing new documentation, *sphinx-autobuild* can be used to automatically regenerate the
HTML as changes are made. Select the method you would like to use and run the command:

.. tab-set::

   .. tab-item:: sphinx-build

      .. code-block:: console

         $ uv run sphinx-build docs/source docs/build

   .. tab-item:: sphinx-autobuild

      .. code-block:: console

         $ uv run sphinx-autobuild docs/source docs/build

