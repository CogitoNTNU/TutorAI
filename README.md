# PROJECT NAME

<div align="center">

![Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/USERNAME/REPONAME/python-package.yml)
[![codecov.io](https://codecov.io/github/USERNAME/REPONAME/coverage.svg?branch=main)](https://codecov.io/github/USERNAME/REPONAME?branch=main)
![top language](https://img.shields.io/github/languages/top/USERNAME/REPONAME)
![GitHub language count](https://img.shields.io/github/languages/count/USERNAME/REPONAME)
[![Project Version](https://img.shields.io/badge/version-0.0.1-blue)](https://img.shields.io/badge/version-0.0.1-blue)

</div>

<details>
  <summary> <b> Table of Contents </b> </summary>
  <ol>
    <li>
    <a href="#standard_python_application"> PROJECT NAME </a>
    </li>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Installation">Installation</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#Tests">Tests</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Introduction



## Usage

```bash
python src/main.py
```

## Installation
To install the PROJECT NAME, one needs to have all the prerequisites installed and set up, and follow the setup guild. The following sections will guide you through the process.
### Prerequisites
- Python 3.9 or higher
  

### Setup
1. Clone the repository
```bash
git clone https://github.com/USERNAME/REPONAME.git
cd PROJECT NAME
```
2. Create and run a virtual environment (optional but recommended).

    Create the virtual by running the following command.
    ```bash
    python -m venv venv
    ```
    To use the virtual environment run the following command
    #### On Windows:
    ```bash
    source venv/Scripts/activate
    ```
    #### On macOS and Linux: 
    ```bash
    source venv/bin/activate
    ```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Create a file called `.env` in the root directory of the project. Add the following lines to the file:
```bash
touch .env
echo "SECRET=SECRET_VALUE" > .env # Remember to change SECRET_VALUE to your actual key
```

## Tests
To run all the tests, run the following command in the root directory of the project:
```bash
pytest --cov
coverage html # To generate a coverage report
```
If you do not want to run api tests, run the following command instead:
```bash
pytest -m "not apitest" --cov
```

### License
Licensed under the [MIT License](LICENSE). Because this is a template repository, you need to change the license if you want to use it for your own project.

