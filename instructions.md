
Инструкции
==========

Обзор
-----

In this project you are asked to create an ML-service to solve any kind of task.

You should define the task you are going to solve. Task definition should contain input and output description, approach chosen to solve (model description), dataset for model training and runtime architecture for the resulting service.

You can publish your code on private GitHub repo.

Details for the project structure:

    1. Project documentation
    1.1. design document
    1.2. run instructions (env, commands)
    1.3. architecture, losses, metrics

    2. Data set
    3. Model training code.
    3.1. Jupyter Notebook
    3.2. MLFlow project

    4. Service deployment and usage instructions
    4.1. dockerfile or docker-compose file
    4.2. required services: databases
    4.3. client for service
    4.4. model

Useful links:
Datasets: http://kaggle.com/
Finished Models: https://paperswithcode.com/
GPU Learning (limited, but suitable for Learning Transfer): http://colab.research.google.com/
Recommended Models for Learning Transfer:

    text - BERT
    images - Big Transfer

Project examples:

    Image or text classification and semantics analysis
    Lyrics generator with musician style (RNN model)
    Image super resolution (CNN)
    Image inpainting or generation (GAN, vAE, DDPMs)
    Image Style Transfer (GAN model)
    House price prediction based on image and table information
    Tags generation for StackOverflow questions

Критерии рецензии
-----------------

    1. Design document and dataset description - 1 point max
    2. Model training code - 2 points max
    2.1. Jupyter Notebook - 1 point
    2.2. MLFlow project - 2 points
    3. Dockerfile - 6 points max
    3.1. docker-compose for full architecture
    3.1.1. synchronous projects - 1 point
    3.1.2. asynchronous project - 2 points
    3.2. client
    3.2.1. REST API / Telegram Bot - 1 point
    3.2.2. HTML Frontend - 2 points
    3.3. model
    3.3.1. transfer learning - 1 point
    3.3.2. trained from scratch - 2 points


Total: 9 points
Pass: 5 points
Excellent: 7 points
