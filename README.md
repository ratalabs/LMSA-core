## Blackboard Assistant

This is a full service web-based automation application for the Blackboard Learn LMS.
It can currently handle all content management and information editing tasks.


## For The Developers:

#### Modules

* [analytics](https://github.com/smccaffrey/BlackboardAssistant/tree/master/analytics) - Handles all analytical tasks
* [automation](https://github.com/smccaffrey/BlackboardAssistant/tree/master/automation) - WebDriver automation framework for Blackboard Learn
* [scraper](https://github.com/smccaffrey/BlackboardAssistant/tree/master/scraper) - XML/HTML ingestion engine for dynamically scraping web pages

### Prerequisites

What things you need to install the software and how to install them

```
...in progress
```

# Developer Installation
Get your copy of the repository and setup the dev environment.
## Clone
```
  $ git clone https://github.com/smccaffrey/BlackboardAssistant.git <directory>
```

## Virtual Environment Setup

```
  $ pip install virtualenv
  $ pip install virtualenvwrapper
  $ export WORKON_HOME=~/Envs
  $ source /usr/local/bin/virtualenvwrapper.sh
```
#### Create and Activate virtualenv
```
  $ mkvirtualenv v-env-name
  $ workon v-env-name
```
#### Create directory for app

```
  (v-env-name) $ mkdir my-project
  (v-env-name) $ cd my-project
```
#### Now that we have a project and are inside v-env-name install Flask
```
  (v-env-name) $ pip install Flask
```
#### Now run the application
```
  ~/my-project $ export FLASK_APP=run.py
  ~/my-project $ flask run
    * Serving Flask app "run"
    * Running on https://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Useful commands

#### Shows all dependencies installed by Flask
```
  $ pip freeze
```
#### Push dependencies to requirements
```
  $ pip freeze > requirements.txt
```

## Running the tests

This process is currently under production and will be completed soon

### Break down into end to end tests

Explain what these tests test and why

```
...in progress
```

### And coding style tests

Explain what these tests test and why

```
...in progress
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Selenium](http://selenium-python.readthedocs.io/) - The framework used

## Contributing

Currently under private development

## Versioning


## Authors

* **Sam McCaffrey** - *Project Lead* - [smccaffrey](https://github.com/smccaffrey)

See also the list of [contributors](https://github.com/smccaffrey/blackboard_automation/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* selenium-python
* etc
