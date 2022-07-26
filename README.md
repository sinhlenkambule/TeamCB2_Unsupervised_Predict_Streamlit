# Streamlit-based Recommender System
#### EXPLORE Data Science Academy Unsupervised Predict

## 1) Overview

![Movie_Recommendations](resources/imgs/Image_header.png)

This repository forms the basis of *Task 2* for the **Unsupervised Predict** within EDSA's Data Science course. It hosts template code which will enable students to deploy a basic recommender engine based upon the [Streamlit](https://www.streamlit.io/) web application framework.

As part of the predict, students are expected to expand on this base template; improving (and fixing) the given base recommender algorithms, as well as providing greater context to the problem and attempted solutions through additional application pages/functionality.    

#### 1.1) What is a Recommender System?

[![What is an API](resources/imgs/What_is_a_recommender_system.png)](https://youtu.be/Eeg1DEeWUjA)

Recommender systems are the unsung heroes of our modern technological world. Search engines, online shopping, streaming multimedia platforms, news-feeds - all of these services depend on recommendation algorithms in order to provide users the content they want to interact with.

At a fundamental level, these systems operate using similarity, where we try to match people (users) to things (items). Two primary approaches are used in recommender systems are content-based and collaborative-based filtering.  In content-based filtering this similarity is measured between items based on their properties, while collaborative filtering uses similarities amongst users to drive recommendations.

Throughout the course of this Sprint, you'll work on defining this brief explanation further as you come to understand the theoretical and practical aspects of recommendation algorithms.     

#### 1.2) Description of contents

Below is a high-level description of the contents within this repo:

| File Name                             | Description                                                       |
| :---------------------                | :--------------------                                             |
| `edsa_recommender.py`                 | Base Streamlit application definition.                            |
| `recommenders/collaborative_based.py` | Simple implementation of collaborative filtering.                 |
| `recommenders/content_based.py`       | Simple implementation of content-based filtering.                 |
| `resources/data/`                     | Sample movie and rating data used to demonstrate app functioning. |
| `resources/models/`                   | Folder to store model and data binaries if produced.              |
| `utils/`                              | Folder to store additional helper functions for the Streamlit app |
