# Wanted Job Classifier

'Wanted Job Classifier' is web application for classifying jobs in four domains. [Wantedlab, Inc.](https://www.wanted.co.kr/) is the online social career platform which drives the foremost innovating platform with more than 2 million users,  10,000 companies from all over the country. Dataset is provided by Wantedlab.

[The entire process of machine learning pipeline is written in Google Colab notebook](https://github.com/gvsteve24/wanted_jd_classifier/blob/master/wanted_lab_0722_accuracy_trigram.ipynb).

### Stacks and skills

* Front-end: [React.js](https://reactjs.org/), HTML5, CSS3, styled-component
* Back-end: [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Flask-SQLalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/), [Flask-Praetorian](https://flask-praetorian.readthedocs.io/en/latest/)
* Machine-learning: Python, [Scikit-learn](https://scikit-learn.org/stable/), Pandas

### Ground truth labels

* Business Management / Administration (경영, 비즈니스)
* Programming / Development (개발)
* Design (디자인)
* Marketing / Advertisement (마케팅, 광고)

<img src="https://user-images.githubusercontent.com/28102768/126655568-e328d023-4623-49ec-b43c-fe57d9ec3018.png" alt="image" style="zoom: 67%;" />



# Model Serving Process

<img src="https://user-images.githubusercontent.com/28102768/126660446-ac81cfd6-5255-4a7e-9961-05ff14d6fe13.png" alt="image" style="zoom: 67%;" />



# Web Application Pages

### Login page

![image](https://user-images.githubusercontent.com/28102768/126637924-88f56e9b-52d7-4791-9e13-13a8a1d58d67.png)

### Logged-in page (token is returned)

![image](https://user-images.githubusercontent.com/28102768/126638290-46140dbb-537b-432b-a654-5af54bd4ae8f.png)

### Inference page

![image](https://user-images.githubusercontent.com/28102768/126661513-6efd1b8c-41c0-4892-b62f-85fd273d230e.png)

### Inference page - 1 (example inputs and corresponding result as development)

![image](https://user-images.githubusercontent.com/28102768/126637822-05d2f8d1-593b-4e16-bf9f-b3a2b75e0a4e.png)

### Inference page - 1 (example inputs and corresponding result as design)

![image](https://user-images.githubusercontent.com/28102768/126638715-7e1c6c10-e792-4085-be20-a340f7e091c6.png)

### Unauthorized page

![image](https://user-images.githubusercontent.com/28102768/126661299-b1e6ebb0-382e-4772-a966-0b202e6355b8.png)

# Getting Started

1. Clone repository

   ```bash
   $ git clone https://github.com/gvsteve24/wanted_jd_classifier
   ```

2. Check environment information 

   * Python version _ 3.8.5
   * Java version _ jdk-16.0.2
   * Windows 10, 64 bit version installed

3. Check important packages (Python virtual environment is strongly recommended)

   ```bash
   beautifulsoup4     4.6.0
   blinker            1.4
   certifi            2021.5.30
   charset-normalizer 2.0.3
   click              7.1.2
   colorama           0.4.4
   customized-konlpy  0.0.64
   Flask              1.1.4
   flask-buzz         0.1.15
   Flask-Cors         3.0.10
   Flask-Mail         0.9.1
   flask-praetorian   1.2.0
   Flask-SQLAlchemy   2.5.1
   greenlet           1.1.0
   idna               3.2
   inflection         0.3.1
   itsdangerous       1.1.0
   Jinja2             2.11.3
   joblib             1.0.1
   JPype1             1.3.0
   konlpy             0.5.2
   lxml               4.6.3
   MarkupSafe         2.0.1
   numpy              1.21.1
   oauthlib           3.1.1
   passlib            1.7.4
   pendulum           2.1.2
   pip                21.1.3
   py-buzz            1.0.3
   PyJWT              2.1.0
   PySocks            1.7.1
   python-dateutil    2.8.2
   python-dotenv      0.18.0
   pytzdata           2020.1
   requests           2.26.0
   requests-oauthlib  1.3.0
   scikit-learn       0.22.2.post1
   scipy              1.7.0
   setuptools         47.1.0
   six                1.16.0
   SQLAlchemy         1.4.21
   threadpoolctl      2.2.0
   tweepy             3.10.0
   urllib3            1.26.6
   Werkzeug           1.0.1
   wrapt              1.12.1
   ```

   Most version information is provided in requirements.txt file.

4. Move to the cloned repository at local drive

   ```bash
   $ cd wanted_jd_classifier
   ```

5. Run script for running local flask server

   ```bash
   $ yarn start-api
   ```

6. Run script for running local client server

   * note: open new terminal before run this command

   ```bash
   $ yarn start
   ```

7. Checkout test id and password

   **TEST ID**: Wanted
   **TEST PASSCODE**: strongpassword

8. Enjoy Hacking!



# Model Accuracy Table 

* [Tf-Idf Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn-feature-extraction-text-tfidfvectorizer) is used to make document numerical value.
* Input document for vectorization is scored providing 'preferred points.'

* Each row represents the sub-document for model to evaluate.

| Model                | SVM      | SVM     | SVM      | Naive Bayes | Naive Bayes | Naive Bayes |
| -------------------- | -------- | ------- | -------- | ----------- | ----------- | ----------- |
| **N-gram**           | Uni-gram | Bi-gram | Tri-gram | Uni-gram    | Bi-gram     | Tri-gram    |
| **Position**         | 86.90    | 86.97   | 86.97    | 86.70       | 86.12       | 86.38       |
| **Main Tasks**       | 89.91    | 90.24   | 90.37    | 86.97       | 87.95       | 87.56       |
| **Requirements**     | 84.15    | 84.61   | 84.48    | 83.04       | 81.93       | 81.79       |
| **Preferred Points** | 78.52    | 78.98   | 78.65    | 77.67       | 78.26       | 77.93       |



## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn start-api`

Runs api based on Flask. This will run the server on your local machine http://localhost:5000 

Every http request from port 3000 is proxied to http://localhost:5000 .

