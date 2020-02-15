# CV API

## Summary
An Curriculum Vitae (Resume) API 

_Note: If you have any questions or comments you can always DM me on the twitter @rbocchinfuso._

### Why
- Just for fun.
- Because I can.
- Inflight boredom and shitty United WiFi.
- Because we learn by doing.
- Because we live in an API driven world.
- The motivation for the CV API is a long story, but the key reason that I decided to build this was really driven by a desire to create a gate for those looking to inspect my CV. I wanted a way to inspect the inspector without having to do the inspection. More details on my motivations can be gleamed from a blog I published here: http://bit.ly/372imHl

### How
- Create a JSON structure to store CV details.
    - Thank you to https://jsonresume.org/ for providing an existing standard.
- Build API with Python and Flash
- Package and containerize API
- Automate deployment

#### Tooling
- **Plan**
	- Evernote:  https://evernote.com/
	- Trello:  https://trello.com/b/9t66HNJq/cv-api
- **Platform**
	- Linux:  Ubuntu 18.04.3 LTS
	- Python:  Anaconda 3 ( https://www.anaconda.com/distribution/)
	- Docker:  https://www.docker.com/
- **Code/Develop**
	- Codeanywhere (IDE):  https://codeanywhere.com/
		- My IDE of choice
			- I like a consistent work from anywhere experience.
			- Part of my productivity regiment.
	- autopep8:  https://pypi.org/project/autopep8/
	- Postman:  https://www.getpostman.com/
		- API testing and documentation
	- JSON Editor Online:  https://jsoneditoronline.org/
		- Great tool for editing and validating JSON.
- **Version**
	- GItHub:  https://github.com/rbocchinfuso/cv-api.git
	- DockerHub:  https://hub.docker.com/
- **Build**
	- Docker Compose:  https://docs.docker.com/compose/
	- Watchtower:  https://containrrr.github.io/watchtower/
- **Test**
	- pytest:  https://docs.pytest.org/en/latest/
	- Postman:  https://www.getpostman.com/
	- lgtm:  https://lgtm.com/
- **Deploy**
	- Docker:  https://www.docker.com/
- **Monitor**
	- Site24x7:  https://www.site24x7.com/
	- Sentry:  https://sentry.io/
	- UptimeRobot:  https://uptimerobot.com/
	- Logdna:  https://logdna.com/
	- Slack:  https://slack.com/
	- Telegram:  https://telegram.org/

### What
- Deploys nginx docker container and exposes port 80
- Builds cv-api docker container from source, exposed port 5000 and creates revese proxy to cv-api from nginx contianer using virtual hostname "cv.bocchinfuso.net"
- Allows user with bearer token make a REST GET for CV data
	- [Run CV API GET Request](https://reqbin.com/c-xyo316m9) 
```curl -H "Accept: application/json" -H "Authorization: Bearer Gj4TUbT209T0YEbmxwSZ9MgdC7AtRr6D" http://cv.bocchinfuso.net/app/api/v1.0/cv```
	- [Read the full API documentation](https://documenter.getpostman.com/view/916401/SWLe6nU9?version=latest#1421c1f4-b5cb-42fd-9188-fc0b168c65d7)

### Todo
- Integrate automated testing into the pipeline
- Add reqeust logging
- Add REST PUT for user initiated requests
- Add Pushover push notifications on REST PUT
- Integrate Sentry for error logging

## Requirements
- [Flask](https://github.com/pallets/flask)
- [Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth)
- [ConfigParser](https://docs.python.org/3/library/configparser.html)

## Usage

### Make Request
- [Run CV API GET Request](https://reqbin.com/c-xyo316m9) 
```curl -H "Accept: application/json" -H "Authorization: Bearer Gj4TUbT209T0YEbmxwSZ9MgdC7AtRr6D" http://cv.bocchinfuso.net/app/api/v1.0/cv```
- [Read the full API documentation](https://documenter.getpostman.com/view/916401/SWLe6nU9?version=latest#1421c1f4-b5cb-42fd-9188-fc0b168c65d7)

### Get my CV API from Docker Hub for local use

### Deploy for Personal Use
- Download code from GitHub for personal use
	```
	git clone https://github.com/rbocchinfuso/cv-api.git
	```
- Note:  If you don't have Git installed you can also just grab the zip: https://github.com/rbocchinfuso/cv-api/archive/master.zip

- Modify the cv.json file
- Modify the config.ini (if desired, e.g. you want to update the auth token)
- Build and deploy (attached)
	```
	docker-compose up --build
	```
- Build and deploy (detached)
	```
	docker-compose up -d --build
	```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ツ

## History
-  version 0.1 (initial release) - 2020/01/21
-  version 0.2 (readme.md updates) - 2020/02/15

## Credits
Rich Bocchinfuso <<rbocchinfuso@gmail.com>>

## License
MIT License

Copyright (c) [2020] [Richard J. Bocchinfuso]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.