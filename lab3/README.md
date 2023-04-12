# Lab 3: Data Visualization

This project visualize the data of google play store apps to drive app-making businesses to success.

## Installation

install conda environment

```
conda env create -f visible.yaml
conda activate visible
```

## Run

```
python dashboard.py 
```

## Requirements

 Design and implement a Dashboard for one of three datasets

 The dashboard should contain at least three graphs (e.g. scatter plot, bar chart, pie chart, line chart, etc) which reveal certain information respectively

## Project Structure

```
│  .gitignore
│  dashboard.py
│  README.md
│  visible.yaml
│
├─data
│      googleplaystore.csv
│
└─img
```

## Dataset

The project choose Google Play Store Apps as dataset.

The data includes:

- App: The name of app
- Category: The category of the app
- Rating: User rating of the app
- Reviews: The review of app
- Installs: Number of app downloads
- Type: Free or Paid
- Price: The price of app
- Content Rating: Who the app is for
- Genres: Genres of app
- Last Update: The date of last update
- Current Version: The current version of app
- Android Ver: Android version of the app adaptation

## Dash Board

- Overview

![image-20220602031840225](img/1.png)

![image-20220602031903525](img/2.png)

- Category and Type

  ![image-20220602032050086](img/3.png)

- Target group of the corresponding catalog

  ![image-20220602032318776](img/4.png)

- Apps' reviews and installs(With specific category / type / target group)

  ![image-20220602032359995](img/5.png)

- Installations of different Android version(With specific category / type / target group)

  ![image-20220602032435939](img/6.png)

- Installations of different rates(With specific category / type / target group)

  ![image-20220602032513179](img/7.png)

- Installations of different app sizes(With specific category / type / target group)

  ![image-20220602032539534](img/8.png)
