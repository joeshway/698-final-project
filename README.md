# PreSetup
## GitHub
GitHub is the place that will store all of your hard work and allow you to access it, download it, and change it from anywhere. It also keeps proivious versions if you realy mess up, so you can revert back.

### Interwebs setup
1. Go to [github](https://www.github.com) and either sign in or create an account
2. Over toward the right of the page, click on **New Repository**
3. Give the repository(repo) a short meaningful name. In this instance I named the repo **698-final-project**.
4. You can add a description if you want but leave everything else the same, and hit **Create Repository**.

### Local Setup
**Before Starting:** To get farmiliar with git and git commands I recomend going to [learngitbranching.js.org](http://learngitbranching.js.org/)
1. Use Ubuntu, it makes everything easier.
2. open up a terminal and cd to the place you would like your local repo to live
3. Now type `mkdir 698-final-project` then cd into that folder
4. now type `echo "# Super-awesome-readme-file" >> README.md`
  * This creates a readlme file and adds a heading to it
5. now type `git init`
  * This initializes git in the directory
6. now type `git add README.md`
  * This stages the readme file to be commited
7. now type `git commit -m "first commit"`
  * This commits the readme file with the meassge first _commit_
8. now type `git remote add origin https://github.com/joeshway/I-need-a-repo.git`
  * This adds your online repo as a remote
9. finally type `git push -u origin master`
  * This pushes your local files to the online repo

This will setup an empty github repo to use
***
## Docker Cloud
Docker Cloud is the testing plateform. It will check to see if your repo passes tests that you define and it is where we will be pulling versions from on the web server

1. Go to [Docker Cloud](https://cloud.docker.com) and either sign in or crete an account
2. If you have already connected Docker cloud to Git Hub go to step 7
3. Click on your user name in the top right and select **Cloud Settings from the dropdown
4. Go to **Source Providers** and click on the little plug icon to the right of GitHub
5. Sign in to GitHub
6. Click on the docker cloud icon in the top left
7. At the bottom of the page select **Create Repository**
8. Give it th esame name as your GitHub repo
9. Select the GitHub icon below, and and select the organization, and repo you setup in GitHub
10. Under that click on **Click here to customize the build settings**
11. It should have one setup already for master making a latest tag... leave that one alone and select the + next to build rules.
12. Change the new rule to have the settings below
  - **Source Type:** Tag
  - **Source:** /^[0-9.]+$/
  - **Docker Tag:** release-{sourceref}
  - **Dockerfile location:** Dockerfile
  - **Build Caching:** on
  ![What it should look like... there should be an image here](markdown-stuff/docker-settings.png)
13. Now hit the **Create** button at the bottom
14. Lastly go to **builds** for the repo, it should be near the top center of the page.
15. Click **Configure Automated Builds**
16. Set **AUTOTEST** to **Internal Pull Requests**
17. Hit Save down at the bottom

***

# Setting up Docker Files in local repo
Docker needs a few files in your local repo to function. below will show each file you need, how to setup them up, and what they do
### Dockerfile
The Dockerfile is the instructions that run to setup the docker container
1. In the root of your local repo type `sudo nano Dockerfile`
2. In the file add the following code
```bash
FROM ubuntu:xenial

COPY . /src
WORKDIR /src
```

### docker-compose.test.yml
This file points to your test file that will pass or fail your build
1. In the root of your local repo type `sudo nano docker-compose.test.yml`
2. In the file add the following code
```python
sut:
  build: .
  command: bash ./run-tests.sh
```

### run-tests.sh
This file points to the python file with your tests in it
1. In the root of your local repo type `sudo nano run-test.sh`
2. In the file add the following code
```bash
#!/bin/bash

echo "Running Flask Unit Tests"

python3 project_test.py
```

### project_test.py
This file has your tests for docker in it The first time docker runs this it should fail, if it passes double check all of the code is correct
1. In the root of your local repo type `sudo nano project_test.py`
2. In the file add the following code
```python
import unittest

import flask_server

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_server.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Chech that the page contians the desired phrase
        assert b'Hello World' in rv.data

if __name__ == '__main__':
    unittest.main()
```
This will check if the home page has **hello world** somewhere on it.

# Adding the Dockerfile
After this section the tests still won't pass, but it shouldn't fail as early...

Since the Dockerfile is the instructions on how to setup the container we need to add some code to it so it sets up the server correctly
The first time you run the test it will take a bit longer, however docker caches commands, so the second time should be faster.
One catch is that if one line in the Dockerfile changes all lines after it will not use the cached version.

1. in the root of the repo type `sudo nano Dockerfile`
2. directly after the first line add this code
```
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
```
The entire file should look like this
```
FROM ubuntu:xenial

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

COPY . /src
WORKDIR /src

```
This will install most of the packages you need


# Flask
Flask is the backend to the web server. it is written in python. For some more info on flask checkout [http://flask.pocoo.org/](http://flask.pocoo.org/)
For now we will set this up to pass our test that we setup

1. in the root of the repo type `sudo nano flask_server.py`
2. add this code to the file
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def mainRoute():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
```
3. You are also going to have to add another line to you Dockerfile
4. You should know how to edit files at this point... edit the Docker file and add the line below smoewhere above `COPY . /src` and below `RUN apt-get install...`

```
RUN pip3 install Flask
```
If you notice we are installing Flask with pip3. This is because Flask is a python app
