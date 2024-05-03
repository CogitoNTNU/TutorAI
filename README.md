# TutorAI

<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/SverreNystad/TutorAI/django.yml)
![GitHub top language](https://img.shields.io/github/languages/top/SverreNystad/TutorAI)
![GitHub language count](https://img.shields.io/github/languages/count/SverreNystad/TutorAI)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Version](https://img.shields.io/badge/version-1.0.0-blue)](https://img.shields.io/badge/version-1.0.0-blue)

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

TutorAI is a language agent capable of assisting with learning academic subjects. The project revolves around building an application that ingests a textbook in most formats and facilitates efficient learning of the course material.

### Features

TutorAI is designed to be an interactive and comprehensive educational tool aimed at enhancing the learning experience for users of all ages. Below are the features that we are excited to introduce:

- **Document upload**: This functionality enables users to upload documents directly into TutorAI. The application will integrate these documents seamlessly, allowing for an interactive and integrated learning experience. The document upload feature support a wide range of file formats, including PDF, DOC, DOCX, PNG, JPG JPEG PPM, TIFF, BMP and more. For example, a user can upload one ore more PDF files containing the course material, and TutorAI will process the content and be able to use it.
- **Information search**: Empower your learning with the ability to conduct in-depth searches within uploaded PDFs. Whether it's a quick fact verification or a deep dive into complex topics, TutorAI makes comprehensive information access simple and efficient.
- **Learning plans**: These plans will be tailored to the user's learning pace, style, and goals, offering a structured path to mastering the subject.
- **Flashcards and Memory aids**: Enhance memory retention with our range of digital memory aids, including customizable flashcards. These interactive tools are designed to make study sessions more productive and engaging. The flashcards are also exportable to Anki, and Quizlet.
- **Quiz and test generation**: Automatic generation of quizzes and tests based on the material in the PDF
- **Quiz and test grading**: Automatic grading of quizzes and tests. This feature will provide feedback on performance, allowing users to track their progress and identify areas for improvement.
- **Compendium**: A comprehensive database of knowledge that can be accessed and searched by users. This feature will provide a wealth of information on a wide range of topics, making learning more accessible and engaging.
- **Study streaks**: This gamified element aims to motivate users to engage with their learning material regularly, making education a daily habit, and exams passed easily.

## Setup

To setup the project, one needs to have all the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

### Prerequisites

- Ensure that git is installed on your machine. [Download Git](https://git-scm.com/downloads)
- Ensure Python 3.9 or newer is installed on your machine. [Download Python](https://www.python.org/downloads/)
- Docker is used for the backend and database setup. [Download Docker](https://www.docker.com/products/docker-desktop)

### Clone the repository

```bash
git clone https://github.com/CogitoNTNU/TutorAI.git
cd TutorAI
```

## Setup the backend

To setup the backend one can either automatically setup the backend using docker or manually setup the backend.

### Docker

For ease of use and version management control, we use Docker to keep track of our containers and virtual environments.

```bash
cd backend
docker-compose build
docker-compose up
```

### Manual

#### Virtual Environment (Recommended)

<details> 
<summary><strong>🚀 A better way to set up repositories </strong></summary>

A virtual environment in Python is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Using a virtual environment for your project ensures that the project's dependencies are isolated from the system-wide Python and other Python projects. This is especially useful when working on multiple projects with differing dependencies, as it prevents potential conflicts between packages and allows for easy management of requirements.

1.  **To set up and use a virtual environment for TutorAI:**
    First, install the virtualenv package using pip. This tool helps create isolated Python environments.

    ```bash
    pip install virtualenv
    ```

2.  **Create virtual environment**
    Next, create a new virtual environment in the project directory. This environment is a directory containing a complete Python environment (interpreter and other necessary files).

    ```bash
    python -m venv venv
    ```

3.  **Activate virtual environment**
    To activate the environment, run the following command: \* For windows:
    `bash
        source ./venv/Scripts/activate
        `

        * For Linux / MacOS:
            ```bash
            source venv/bin/activate
            ```

    </details>

#### Install dependencies

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
   You will need to add the following environment variables to the `.env` file:

   - OPENAI_API_KEY: Your OpenAI API key

   ```bash
   echo "OPENAI_API_KEY=YOUR_API_KEY" > .env # Remember to change YOUR_API_KEY to your actual API key
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

```bash
docker-compose run tutorai python manage.py test flashcards
```

### Frontend
To run all the tests, run the following command in the `frontend` directory of the project:

```bash
npm run test
```

## Contributors


<table align="center">
  <tr>
    <td align="center">
    <a href="https://github.com/henrik392">
        <img src="https://github.com/henrik392.png?size=100" width="100px;"/><br />
        <sub><b>Henrik Halvorsen Kvamme</b></sub>
    </a>
    </td>
    <td>
      <td align="center">
        <a href="https://github.com/kaamyashinde">
            <img src="https://github.com/kaamyashinde.png?size=100" width="100px;"/><br />
            <sub><b>Kaamya Shinde</b></sub>
        </a>
    </td>
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
      <a href="https://github.com/Parleenb">
          <img src="https://github.com/Parleenb.png?size=100" width="100px;"/><br />
          <sub><b>Parleen Brar</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/sandviklee">
          <img src="https://github.com/sandviklee.png?size=100" width="100px;"/><br />
          <sub><b>Simon Sandvik Lee</b></sub>
      </a>
    </td>
    <td align="center">
        <a href="https://github.com/LockedInTheSkage">
            <img src="https://github.com/LockedInTheSkage.png?size=100" width="100px;"/><br />
            <sub><b>Skage  Reistad</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/SverreNystad">
            <img src="https://github.com/SverreNystad.png?size=100" width="100px;"/><br />
            <sub><b>Sverre Nystad</b></sub>
        </a>
    </td>
    <td align="center">
      <a href="https://github.com/tobiasfremming">
          <img src="https://github.com/tobiasfremming.png?size=100" width="100px;"/><br />
          <sub><b>Tobias Fremming</b></sub>
      </a>
    </td>
  </tr>
</table>

This project would not have been possible without the hard work and dedication of all of the contributors. Thank you for the time and effort you have put into making TutorAI a reality.

<div align="center">
    <img src="docs/images/tutorai_team.jpg" width="50%" alt="Cogito Team Image" style="display: block; margin-left: auto; margin-right: auto;">
</div

## License

Licensed under the [MIT License](LICENSE). Because this is a template repository, you need to change the license if you want to use it for your own project.
