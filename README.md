<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/newpheeraphat/Backend-TSL">
  </a>

  <h3 align="center">ThaiCheckLinks Backend For Machine Learning</h3>

  <p align="center">
    The development of a backend system designed specifically for verifying the links within Thai language content using machine learning techniques
    <br />
    <a href="https://studentmahidolac-my.sharepoint.com/:w:/g/personal/apichaya_mae_student_mahidol_ac_th/EdLLgWGkPC5IvlW-lZ8QrtEBZuOILnYg4S9sLmyJsU_n_w?rtime=uV6lsCBs3Eg"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/newpheeraphat/Backend-TSL/issues">Report Bug</a>
    ·
    <a href="https://github.com/newpheeraphat/Backend-TSL/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

The Cybercrime Website Report and Verification project, Thai.CheckLinks, aims to solve the issue of cybercrime websites in Thailand by developing a website system for reporting and verifying cybercrime websites focusing on Scam, Gambling, and Fake Bank websites.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][Python-logo]][Python-url]
- [![Flask-learn][Flask-learn-logo]][Flask-learn-url]
- [![PostgreSQL][PostgreSQL-logo]][PostgreSQL-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is a section of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This guide will help you get started with running your Flask application locally on your machine. Make sure you have Python installed (version 3.11.7 or later).

- download
  <a href="https://www.python.org/downloads/">
  ```sh
  https://www.python.org/downloads/
  ```
  </a>

### Installation

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```sh
git clone https://github.com/newpheeraphat/Backend-TSL.git
cd Backend-TSL
```

### 2. Install Dependencies

Navigate to the project directory and install the required dependencies:

```sh
  pip3 install -r requirements.txt
```

### 3. Download Model

Download two models with the provided link and move them to the model folder:
<a href="https://drive.google.com/drive/u/2/folders/1ic9WeUad_XWXnQQDoE-ZJiT7pa3eTC1J"

>

```sh
  https://drive.google.com/drive/u/2/folders/1ic9WeUad_XWXnQQDoE-ZJiT7pa3eTC1J
```

</a>

### 4. Run the Development Server

After installing the dependencies, you can start the development server by running:

```sh
  python3 run.py
```

This command starts the Flask application in development mode, error reporting, and more. The server will start listening on http://localhost:8000. Open this URL in your browser to view your application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

We welcome contributions to ThaiCheckLinks Backend for Machine Learning! Here's how you can get involved:

1. Fork the Project
2. Clone the forked repository to your local machine using Git.

```sh
  git clone https://github.com/newpheeraphat/Backend-TSL.git
```

3. Create a new branch for your contributions

```sh
  git checkout -b feature/new-feature
```

4. Work on the project, implement new features, fix bugs, or improve documentation.
5. Once you're happy with your changes, commit them to your branch.

```sh
  git commit -am "Add new feature: XYZ"
```

6. Push your changes to your forked repository on GitHub.

```sh
  git push origin feature/new-feature
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

The authors express deep gratitude to Dr. Ittipon Rassameeroj for his invaluable guidance, insightful suggestions, and scholarly expertise throughout this research project. Sincere appreciation is extended to the esteemed committee members: Assoc. Prof. Dr. Vasaka Visoottiviseth, Asst. Prof. Dr. Dolvara Guna-Tilaka, Asst. Prof. Dr. Charnyote Pluempitiwiriyawej, Lect. Dr. Assadarat Khurat, and Lect. Pagaporn Pengsart. Their thorough review and constructive feedback significantly enhanced the quality of this study.

The authors are thankful to the Information Technology Crime Prevention and Suppression Division, Cyber Crime Investigation Bureau (Thai police), and Electronic Transactions Development Agency (ETDA) for generously providing resources and support essential to the research work. Special acknowledgment is extended to Assoc. Prof. Dr. Suppawong Tuarob for additional guidance and contributions to this work.

Finally, the collaborative efforts of all involved in completing this research endeavor.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Python-logo]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Flask-learn-logo]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-learn-url]: https://flask.palletsprojects.com/en/3.0.x/
[PostgreSQL-logo]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
