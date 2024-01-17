> _This repository contains data engineering and data science projects and exercises using open data sources as part of the [AMSE](https://oss.cs.fau.de/teaching/specific/amse/)/[SAKI](https://oss.cs.fau.de/teaching/specific/saki/) course, taught by the [FAU Chair for Open-Source Software (OSS)](https://oss.cs.fau.de/) in the Winter'23/24 semester. This repo is forked from [2023-amse-template repository](https://github.com/jvalue/2023-amse-template)._

![bicycle-riding](img/bicycle_riding.jpg)

# Exploring the Impact of Weather and Climate on Bicycle sharing in London

This project aims to analyze **the Impact of Weather and Climate on Bicycle sharing in London** generated from several data collectors throughout the city to determine if London is a suitable city for an enthusiastic cyclist to live in. The project is using two open data sources: [Bicycle sharing Data in London](https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset), which contains information on bicycle traffic in London, and [Weather and Climate Data of London]https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data), which provides weather and climate data of London. For details see the [project plan](/project/project-plan.md).

## Project Structure

```bash
project/
├── config/                     # Configuration files and settings
│   ├── __init__.py
│   ├── basepipeline.py         # Configuration variables
│   └── kaggle.json             # Source information
├── data/                       # Data directory
│   ├── mian.sqlite             # Processed data
├── etl_pipeline.py             # ETL (Extract, Transform, Load) pipeline modules
├── tests_pipe.py               # all the unittests are wriiten here
├── tests.sh                    # Bash script for running all the test cases
├── exploration.ipynb           # Notebook for data exploration
├── report.ipynb                # Notebook for final project report
└── project-plan.md             # Project plan and documentation
```

**Important files of the project and their roles:**

- `project/etl_pipeline.py`: It will run an automated ETL pipeline that creates an SQLite database named `main.sqlite` that contains two tables representing two open data sources of the project.
- `project/tests.sh`: A bash script that will execute the component and system-level testing for the project by calling two other Python scripts, `project/test_pipe.py`.
- `project/report.ipynb`: This Jupyter notebook serves as the final report for the project, providing a comprehensive exploration of all aspects and findings. The report primarily investigates the impact of weather conditions in London on bicycle traffic throughout the year, addressing various key questions, based on the data in `main.sqlite`. See the [report](project/report.ipynb) and [slides](project/slides.pdf).

**Project Pipeline using GitHub Action:** <br>

A project pipeline has been implemented using a GitHub action defined in [.github/workflows/ci-tests.yml](.github/workflows/ci-tests.yml). This pipeline is triggered whenever changes are made to the `project/` directory and pushed to the GitHub repository, or when a pull request is created and merged into the `main` branch. The `ci-tests.yml` workflow executes the `project/tests.sh` test script, and in case of any failures, it sends an error message

## Project Setup

1. Clone this git repository
```bash
git clone https://github.com/RifatPiyal/MADE-Project.git
```
2. Install [Python](https://www.python.org/). Then create a virtual environment inside the repo and activate it.
```bash
python3 -m venv <env_name>
source <env_name>/bin/activate
```
3. Download and install the required Python packages for the project.
```bash
pip install -r requirements.txt
```
4. To run the project, go to the `project/` directory and run the `etl_pipeline.py` script. It will run the whole ETL pipeline and generate an SQLite database named `main.sqlite` that contains two tables, `bike_data` and `weather`, representing two open data sources of the project.
```bash
cd project/
python3 etl_pipeline.py
```
5. To run the test script which will execute the component and system-level testing for the project, run the following command.
```bash
chmod +x tests.sh
sh tests.sh
```
6. Finally, run and explore the `project/report.ipynb` project notebook.

## Exercises (not part of the project)

During the semester we had to complete exercises, sometimes using [Python](https://www.python.org/), and sometimes using [Jayvee](https://github.com/jvalue/jayvee). Automated exercise feedback is provided using a GitHub action that is defined in [.github/workflows/exercise-feedback.yml](.github/workflows/exercise-feedback.yml).

1. [exercises/exercise1.jv](exercises/exercise1.jv)
2. [exercises/exercise2.py](exercises/exercise2.py)
3. [exercises/exercise3.jv](exercises/exercise3.jv)
4. [exercises/exercise4.py](exercises/exercise4.py)
5. [exercises/exercise5.jv](exercises/exercise5.jv)

The exercise feedback is executed whenever we make a change in files in the `exercise/` directory and push our local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, and open the `exercise-feedback` job and `Exercise Feedback` step.
