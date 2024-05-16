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

- [TutorAI](#tutorai)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Quick Start](#quick-start)
    - [Prerequisites](#prerequisites)
    - [Clone the repository](#clone-the-repository)
    - [Configuration](#configuration)
    - [Usage](#usage)
  - [📖 Documentations](#-documentations)
  - [Contributors](#contributors)
  - [License](#license)

</details>

## Introduction
TutorAI is an interactive language agent designed to assist with learning academic subjects. It facilitates efficient learning by allowing users to upload textbooks in various formats and interact with the course material.

### Features
TutorAI offers a comprehensive set of features to enhance the learning experience:

- **Document upload**: Upload course material in various formats to enable TutorAI to process and interact with the content. Supported formats include PDF, DOC, DOCX, PNG, JPG, JPEG, PPM, TIFF, BMP, and more.
- **Information search**: Retrieve relevant citations and incorporate them into responses to user questions. This ensures comprehensive, accurate, and well-cited information, enhancing the learning process.
- **Learning plans**: Tailored to the user's pace, style, and goals, offering structured paths to mastery.
- **Flashcards and Memory aids**: Enhance memory retention with customizable digital flashcards, exportable to Anki and Quizlet.
- **Quiz and test generation**: Automatically generate quizzes and tests based on the uploaded material.
- **Quiz and test grading**: Receive automatic grading and feedback on quizzes and tests to track progress and identify improvement areas.
- **Compendium**: Generate a summary of the uploaded material, making it easier to review and understand the content.
- **Study streaks**: Motivate regular engagement with learning material through gamified elements, making education a daily habit, and exams passed easily.

## Quick Start

### Prerequisites
- Ensure that git is installed on your machine. [Download Git](https://git-scm.com/downloads)
- Docker is used for the backend and database setup. [Download Docker](https://www.docker.com/products/docker-desktop)

### Clone the repository

```bash
git clone https://github.com/CogitoNTNU/TutorAI.git
cd TutorAI
```

### Configuration
Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
OPENAI_API_KEY = 'your_openai_api_key'
MONGODB_URI = 'your_secret_key'
```

Optionally, you can add the following environment variables to customize the project:

```bash
GPT_MODEL = 'gpt-3.5-turbo' # OpenAI model to use
```


### Usage
To start TutorAI, run the following command in the root directory of the project:

```bash
docker compose up --build
```

Then navigate to `http://localhost:3000` in your browser to access the UI of the frontend.

To access the backend, navigate to `http://localhost:8000` in your browser.

## 📖 Documentations

- [Developer Setup Guild](docs/manuals/setup)
- [Testing](docs/manuals/testing.md)
- [Architecture](docs/architecture/architectural_design.md)

## Contributors

<table align="center">
  <tr>
    <td align="center">
        <a href="https://github.com/henrik392">
            <img src="https://github.com/henrik392.png?size=100" width="100px;"/><br />
            <sub><b>Henrik Halvorsen Kvamme</b></sub>
        </a>
    </td>
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
</div>



## License
Licensed under the [MIT License](LICENSE).
