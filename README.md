# TutorAI
<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/TutorAI/main.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/TutorAI)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/TutorAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Version](https://img.shields.io/badge/version-0.0.1-blue)](https://img.shields.io/badge/version-0.0.1-blue)

<img src="docs/images/TutorAI.png" width="50%" alt="Cogito Image" style="display: block; margin-left: auto; margin-right: auto;">
</div>

<details> 
<summary><b>📋 Table of contents </b></summary>

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Tests](#tests)
5. [Repository Structure](#repository-structure)
6. [Contributors](#contributors)
7. [License](#license)

</details>

## Introduction
TutorAI is a language agent capable of assisting with learning academic subjects. The project revolves around building an application that ingests a textbook in PDF format and facilitates efficient learning of the course material.

### Planned Features
TutorAI is designed to be an interactive and comprehensive educational tool aimed at enhancing the learning experience for users of all ages. Below are the planned features that we are excited to introduce:

* **PDF upload**: This functionality enables users to upload PDF documents directly into TutorAI. The application will integrate these documents seamlessly, allowing for an interactive and integrated learning experience.
* **Information search**: Empower your learning with the ability to conduct in-depth searches within uploaded PDFs. Whether it's a quick fact verification or a deep dive into complex topics, TutorAI makes comprehensive information access simple and efficient.
* **Learning plans**: These plans will be tailored to the user's learning pace, style, and goals, offering a structured path to mastering the subject.
* **Flashcards and Memory aids**: Enhance memory retention with our range of digital memory aids, including customizable flashcards. These interactive tools are designed to make study sessions more productive and engaging.
* **Quiz and test generation**: Automatic generation of quizzes and tests based on the material in the PDF
* **Study streaks**: This gamified element aims to motivate users to engage with their learning material regularly, making education a daily habit, and exams passed easily.

## Setup
To setup the project, one needs to have all the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites
- Ensure that git is installed on your machine. [Download Git](https://git-scm.com/downloads)
- Ensure Python 3.9 or newer is installed on your machine. [Download Python](https://www.python.org/downloads/)
- Familiarity with basic Python package management and virtual environments is beneficial.

### Clone the repository
```bash
git clone https://github.com/CogitoNTNU/TutorAI.git
cd TutorAI
```
## Setup the backend

### Virtual Environment (Recommended)

<details> 
<summary><strong>🚀 A better way to set up repositories </strong></summary>

A virtual environment in Python is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Using a virtual environment for your project ensures that the project's dependencies are isolated from the system-wide Python and other Python projects. This is especially useful when working on multiple projects with differing dependencies, as it prevents potential conflicts between packages and allows for easy management of requirements.

1. **To set up and use a virtual environment for TutorAI:**
    First, install the virtualenv package using pip. This tool helps create isolated Python environments.
    ```bash
    pip install virtualenv
    ```

2. **Create virtual environment**
    Next, create a new virtual environment in the project directory. This environment is a directory containing a complete Python environment (interpreter and other necessary files).
    ```bash
    python -m venv venv
    ```

4. **Activate virtual environment**
    To activate the environment, run the following command:
    * For windows:
        ```bash
        source ./venv/Scripts/activate
        ```

    * For Linux / MacOS:
        ```bash
        source venv/bin/activate
        ```
</details>

### Install dependencies
With the virtual environment activated, install the project dependencies:
```bash
pip install -r requirements.txt
```
The requirements.txt file contains a list of packages necessary to run TutorAI. Installing them in an activated virtual environment ensures they are available to the project without affecting other Python projects or system settings.

### Create a .env file
For secure and efficient management of environment-specific variables, TutorAI utilizes a `.env` file. This file is used to store sensitive information, such as API keys, which should not be hard-coded into the source code or shared publicly. The `.env` file is particularly crucial for maintaining the confidentiality of your API keys and other sensitive data.

**Important:** The `.env` file should never be committed to version control (e.g., GitHub). Always include `.env` in your `.gitignore` file to prevent accidental upload of sensitive information.

#### Steps to Create and Configure the .env File:

1. **Create the .env File:**
   In the root directory of the project, create a new file named `.env`. This file will be used to store environment variables.
   ```bash
    touch .env
    ```

2. **Add Environment Variables:**
    ```bash
    echo "API_KEY=YOUR_API_KEY" > .env # Remember to change YOUR_API_KEY to your actual API key
    ```

3. **Obtaining an API Key:**
    If you don't have an API key from OpenAI, you can obtain one by visiting [OpenAI API Keys](https://platform.openai.com/api-keys). Follow their instructions to generate a new API key.

    By following these steps, you'll ensure that your application has all the necessary environment-specific configurations, while keeping sensitive data secure and out of version control.


### Setup the frontend
The frontend is built using React and TypeScript. To install the dependencies, run the following command in the root directory of the project:
```bash
cd frontend
npm install
```

## Usage
### Frontend
To run the client, run the following command in the root directory of the project:
```bash	
cd frontend
npm run dev
```
### Backend
To run server, run the following command in the root directory of the project:
```bash
cd backend
python manage.py runserver
```

## Tests
### Backend
To run all the tests, run the following command in the `backend` directory of the project:
```bash
python manage.py test
```
### Frontend
There are currently no tests for the frontend.



## Contributors

<table align="center">
  <tr>
    <td align="center">
        <a href="https://github.com/Knolaisen">
            <img src="https://github.com/Knolaisen.png?size=100" width="100px;" alt="Kristoffer Nohr Olaisen"/><br />
            <sub><b>Kristoffer Nohr Olaisen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/olavsl">
            <img src="https://github.com/olavsl.png?size=100" width="100px;" alt="Olav Selnes Lorentzen"/><br />
            <sub><b>Olav Selnes Lorentzen</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/SverreNystad">
            <img src="https://github.com/SverreNystad.png?size=100" width="100px;"/><br />
            <sub><b>Sverre Nystad</b></sub>
        </a>
    </td>
      <td align="center">
        <a href="https://github.com/sandviklee">
            <img src="https://github.com/sandviklee.png?size=100" width="100px;"/><br />
            <sub><b>Simon Sandvik Lee</b></sub>
        </a>
    </td>
  </tr>
</table>

## License
Licensed under the [MIT License](LICENSE). Because this is a template repository, you need to change the license if you want to use it for your own project.

