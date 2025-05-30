# bpod-gui
___
**bpod-gui** is a Python package that provides a set of standardized GUIs for interacting with the *Bpod Finate State Machine* from [*Sanworks*](https://sanworks.io/).

This package relies on the **bpod-core** package created by the [*International Brain Lab*](https://internationalbrainlab.org).

___
## Development Setup
We utilize **uv** developed by [**astral**](https://github.com/astral-sh/uv) to manage dependencies, Python versions, and environments.

### Instructions:
1) Install the Python 3.13 binaries by running ```uv python install 3.13```
2) Clone the repository using ```git clone git@github.com:olfactorybehaviorlab/bpod-gui```
3) In the same directory, run ```uv sync``` to install the pinned version of the dependencies from the **uv.lock** file into a new .venv
4) In the same directory, run ```uv pip install -e .``` to install the package in _editable_ for development