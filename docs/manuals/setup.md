# How to setup the project

<details>
<summary><strong> 📖 Table of Contents 📖</strong></summary>

- [How to setup the project](#how-to-setup-the-project)
  - [Prerequisites](#prerequisites)
    - [Clone the repository](#clone-the-repository)
  - [Setup the backend](#setup-the-backend)
    - [Docker](#docker)
    - [Manual](#manual)
      - [Virtual Environment (Recommended)](#virtual-environment-recommended)
      - [Install dependencies](#install-dependencies)
    - [Create a .env file](#create-a-env-file)
      - [Steps to Create and Configure the .env File:](#steps-to-create-and-configure-the-env-file)
    - [Setup the frontend](#setup-the-frontend)

</details>

To setup the project, one needs to have all the prerequisites installed. Then one needs to clone the repository, setup a virtual environment, and install the dependencies. This is described in more detail below.

## Prerequisites

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