# SES2020spring

## Introduction

This repository contains the complementary material for 项目实践 and 机器学习基础 taught at SES.
Due to the distributed and
asynchronous
nature of this study format,
we will steer the course through a series of self-contained units around programming, visualization, and simulation,
which may be your interest for your future endeavor.
This course tries to fulfill this arrangement by introducing some tools and demonstrating their capability.

A quck list of topics:

1. [Software development](#Software-Development)
2. [Machine learning](#机器学习基础)
3. [Motor](#Motor)
4. [Call For Participation](#Call-For-Participation)

## Call For Participation

### Knowledge Graph System Development for Mesoscopic Scale Neuroscience Research ###

With the progress of the whole brain mesoscopic scale imaging system, such as MOST,
studies on the brain connectome go to the next generation focusing on the finer brain structures.
However, previous research results about individual brain structure are often scattered around 
a large set of literature, it prohibits the researchers to catch up with the state-of-art research.
In this project, you will develop an end-to-end, ready-to-use search system to allow your users
to search the mesoscopic scale neuroscience terms and get back with the relevant literature,
just as the general search engine.
The corpus and the specific trained Bidirectional Encoder Representations from Transformers (BERT)
model are ready and waiting for you to present them to broader audience.

### Efficient GPU Memory Allocator Development in Rust ###

Deep learning is in its period of prosperity and the process of producing the production-ready models
have evolved into the front end and the back end, 
where the specialists construct the model for a specific task during the front end phrase
and the devleopers fine tune the model for the deployment.
In this project, you are invited to extend an existing Rust-based deep learning library
with a GPU memory allocator to allow it to run efficiently on the GPU side
and you will get yourself familar with the high performance GPU programming.
Rust is a segfault-free C-like-speed programming language even with a naive implementation.

### Text to Image Conversion for Fast Multimedia Content Prototying ###

Text and Image often come together in the multimedia content supply.
There are already amazing researches on the image-to-text conversion (image captioning).
However, the text-to-image conversion is relative challenging
as the information is usually extended in this case.
You are invited to join this project to develop a prototype system for the text-to-image conversion.
The plan starts with the existing public baseline model and 
develops a model for a specific application scenario.





## Motor

Electrical motors are used everywhere to drive the world forward.
In this section, we will try to build a motor and a driver for it.

### Build a motor driver

There are several types of electrical motors and different motor needs a different driver circuit to supply the power they run on.
There are AC motors, BLDC motor, and other types of motor, we will first start to drive DC motors with brush.

#### Drive a brush DC motor ####

The introduction for the DC motor driver project is presented here:

[pdf for introduction to the brush DC motor driver](https://github.com/pipehappy1/SES2020spring/blob/master/dc_motor/intro.pdf)

The videos that show how to use KiCAD to produce a PCB board are listed here:

1. Plot the schematic design: [@acfun](https://www.acfun.cn/v/ac20783731), [@bilibili](https://www.bilibili.com/video/BV1Ea411c73K/),
2. Assign the footprint for the component: [@acfun](https://www.acfun.cn/v/ac20784691), [@bilibili](https://www.bilibili.com/video/BV12T4y1M7ez/).
3. Layout the PCB: [@acfun](https://www.acfun.cn/v/ac20864316), [@bilibili](https://www.bilibili.com/video/BV115411G7ef/).

Please do you research and find proper components to build up the PCB board for a 4-channel DC driver.

### Build a motor


## Software Development

4 units are planned for the first 4 weeks.
Each unit will contain at least 2 parts.
The 1st part will discuss general practice and methodology around software engineering and this serves as the general topic across the board.
The second part will introduce some tools or libraries and demonstrate how to use them.
It’s highly recommended that you should do your own research about this tool or library before the class and get familiar with it.
The class time will be the Q/A time and I will stay online to answer your question through Github issues, QQ, and Wechat.

### Unit 1: Introduction to Software Engineering and Git

In the introduction to software engneering, we will cover the concept of software, software engineering, and software crisis. We also show the basic workflow of Git, the distributed version control system.

### Unit 2: Agile Programming

We will have 2 parts in this unit. In the first part, we go through an agile method called Scrum. In this second part, we will talk about Python.

### Unit 3: Object Oriented Design and Programming and Midterm Project

We will introduce the object oriented design and programming pattern in this unit. A midterm project is also in this unit.

### Unit 4: Unit Test

This unit is about software verification and validation method, focusing on unit test.

### Final Project:

Please form a team with 2~3 members and pick a project from http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/.

### Q&A

Q: Do we have a syllabus for this course? What's the goal of this course?

A: For the situation caused by the Coronavirus, we do have an alternative plan for the course for the first 4 weeks. The topics are listed above. The goal of this course is to introduce several concept and practise around software development.

Q: The videos can be more connected and the title of the video is not clear?

A: We want each video to be self-contained and independent as possible so that referece to these video in the future makes more sense without refering to the context and the background. Acfun.cn and bilibili.com are meant to be used as video host only. Title and description for the video are only available on the site where this readme resides. This makes the material for this course neutral to video hosting site.

Q: There are some parts where complementary slides are not available?

A: The programming parts are mainly screen casting.

Q: Team up may be a better choice?

A: Exercise of some units will be for individual, while other exercises require a teamwork.

Q: What about students with a computer at his/her disposal?

A: We provide reference in each unit and some reading instruction. This is for students without computers.

## 机器学习基础

### 简介

1. Machine learning and related terms.
2. Types of problem discussed in machine learning.
3. Introduction to neural networks.

[video: introduction to machine learning @acfun](https://www.acfun.cn/v/ac15348189)

[video: introduction to machine learning @bilibili](https://www.bilibili.com/video/BV1Wz4y1R7dh/)

The material is in c1_intro.

### 逻辑回归

1. logistic regression
2. stochastic gradient descent
3. input normalization
4. oversampling/undersampling

[video for logistic regression, @acfun](https://www.acfun.cn/v/ac15394923)

[video for logistic regression, @bilibili](https://www.bilibili.com/video/BV1Ta4y1i7E4/)

[pdf for logistic regression](https://github.com/pipehappy1/SES2020spring/blob/master/C2_logistic_regression.pdf)

### Exercise 1

The task in this exercise is for you to apply logistic regression on ``Breast Cancer Wisconsin (Diagnostic) Data Set''.

* You can set train/test split to 0.7/0.3 or any value you like.
* You can choose your favorite tool besides PyTorch.
* Post your answer in a pull request to this repository.
* Discuss with each other while try to work the code out by yourself.

There is a piece of code demonstrating logistic regression using PyTorch.  mlex1/lr.py

The data is available at https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

The data is also available on Kaggle: https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

Note:

* UC Irvine Machine Learning Repository is the classic goto site to find some machine learning dataset.
* Kaggle is a popular machine learning competition site.

### 人工神经网络

1. Ensamble models by bagging/stacking/boosting
2. MLP by stacking logistic regression
3. Auto difference i.e. back propagation

Videos:

* [multiLayer-perceptron @acfun](https://www.acfun.cn/v/ac15453604)
* [multiLayer-perceptron @bilibili](https://www.bilibili.com/video/BV125411s7sH/)
* [back propagation @acfun](https://www.acfun.cn/v/ac15453964)
* [back propagation @bilibili](https://www.bilibili.com/video/BV1Ai4y147Aj/)

pdfs:

* [Perceptron and multiLayer-perceptron](https://github.com/pipehappy1/SES2020spring/blob/master/c3_mlp/c3_mlp.pdf)
* [Back propagation slides from Stanford cs231n](https://github.com/pipehappy1/SES2020spring/blob/master/c3_mlp/lecture_4.pdf)
* [Back propagation slides from Stanford cs231n (source)](http://cs231n.stanford.edu/slides/2020/lecture_4.pdf)

### 卷积网络

1. Convolutional operator in convolutional neural network (CNN)
2. Other layers often used in CNN
3. Learning tricks

Videos:

* [CNN @acfun](https://www.acfun.cn/v/ac15496062)
* [CNN @bilibili](https://www.bilibili.com/video/BV16K411W7ma)

pdf:

* [CNN](http://cs231n.stanford.edu/slides/2020/lecture_5.pdf)

### 其他神经网络模型

Videos:

* [pretrained CNN @acfun](https://www.acfun.cn/v/ac15537219)
* [pretrained CNN @bilibili](https://www.bilibili.com/video/BV1of4y117sk)

pdf:

* [pretrained CNN](http://cs231n.stanford.edu/slides/2020/lecture_9.pdf)

### Exercise 2

Please go through [deep learning with PyTorch: a 60 minute blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
by yourself. You can post any question in the QQ chat group if you'd like to discuss.

* Use [conda](https://docs.conda.io/en/latest/miniconda.html) to manage and install the packages.
* Goto [PyTorch](https://pytorch.org/) to find the command to install PyTorch.

## Stock managment system

The stock managment system development is the main focus for 项目实践 in 2020 fall.
The example repository can be found in ./stock.
