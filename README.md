# Flask Starter Template

This flask starter template includes everything you need to start your own app 
including auth, database, **and security**, to get up and started quickly.

Uses CSRF tokens and CSP headers to protect your website from injection. It also
does all of this stuff: [https://github.com/GoogleCloudPlatform/flask-talisman](https://github.com/GoogleCloudPlatform/flask-talisman)

###### I hope to add more, like an admin and user dashboard prebuilt in.
## Setup & Installation

Make sure you have the latest version of Python installed. Built in 3.11.

```bash
git clone https://github.com/Neceros/flask-starter.git
cd flask-starter
```

Set up your virtual environment. It's easy, and you should do it for every project, 
as it will save you many headaches later on from a bloated python.

**Make sure the virtual environment is outside your project folder**:

```bash
python3 -m venv /flask-apps/venv/flask-starter
source /flask-apps/venv/flask-starter/bin/activate
```
The first line creates the environment and the second line activates it.

If you are using Windows you can put it anywhere like: `python3 -m venv c:\flask-apps\venv\flask-starter`

Please see [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) if you need help with venv.


Now that you are inside the project folder and the virtual environment, install the required
packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

You are ready to begin. Everything should be setup and ready to run right this moment. Just start adding your application code!

#### TODO:
* Add database models: products, posts, tracks, downloads, etc

## Running The App

```bash
python main.py
```

## Viewing The App

**Go to** [http://127.0.0.1:5000](http://127.0.0.1:5000)
