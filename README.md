# beginner_website
This is a website I am making partially for webdev practice, and also to put a bunch of web development related notes onto.

## Setup
I am using [pdm](https://github.com/pdm-project/pdm) as my package manager, so you can install it by running `pip install pdm` and then `pdm install` to install all the dependencies.

Alternatively, you can `pip install -r requirements.txt` instead.

I have also configured a run command for pdm which is `pdm run`. `pdm start` will also run the site but installs dependencies first. Otherwise just run the `index.py` file for prod build and `app.py` for flask debug