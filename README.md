# Reproducing Parkinson Disease Stage Classification
The reproducibility crisis is a methodological and sociological problem that refers to the growing evidence that scientific study results often cannot be reproduced. Therefore, government officials and scientists spend time and money generating inaccurate results that only minimize the chances of progressive work being done. This is a major concern for the biomedical community as it impacts the validity of results in a preclinical setting. Reproducibility, with respect to machine learning, means that running a computational model several times always produces the same results. However, data changes, software environments, software versions and numerous factors vary the output of a model. In this repository, we will be reproducing the low-risk (stable) or high-risk (progression) Parkinson's disease stage using the Hoehn-Yahr Scale.

## Setup
In order to run the code, make sure you have Conda installed in your machine in order to use our environment. From there, run the following commands

```
conda env create --name reproducibility --file=environment.yml
conda activate reproducibility
```

Once you have your environment setup, you can run the machine learning pipeline using:

```
cd ml
python run.py
```

**Warning: this operation could take a long time!**

## Notebook
You can review the machine learning pipeline by accessing this [notebook](ml/ml-pipeline-notebook.ipynb)

## Meeting Notes
The following log is dedicated to keep track of meetings & discussions from the authors of this project. They can be found [here](/MEETING_LOGS.md).

### Credits
| Name | Role |
| --- | --- |
| **Mohanad Arafe** | Author |
| **Dr. Tristan Glatard** | Supervisor |
| **Dr. Jean-Baptiste Poline** | Supervisor |
