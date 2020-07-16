### Conda environment
Create conda environment and install for local running and debugging
``` bash
conda update -n base conda --yes
conda create -n personalsite
conda activate personalsite
conda install -n personalsite --yes --file env/requirements_conda.txt
pip install -r env/requirements_noconda.txt

```

### Local Docker
``` bash
docker build -t bluemania/personalsite .
docker run -p 5000:5000 -e PORT=5000 --rm bluemania/personalsite

```
```bash
docker stop $(docker ps -a -q)
```


### Push Docker

``` bash
heroku login
docker build -t bluemania/personalsite .
heroku container:login
docker tag bluemania/personalsite registry.heroku.com/nickjenkins/web
docker push registry.heroku.com/nickjenkins/web
heroku container:release web -a nickjenkins

```

### SSL
www.nickjenkins.com.au  
fathomless-whale-h7m0nr3r05sfqntdtuajxbkm.herokudns.com  
heroku certs:auto:enable -a nickjenkins  

### SEO resources
Google SEO
http://flask.pocoo.org/snippets/108/

# TODOs

* Understand dockerfiles and docker-compose better. I want to be able to run docker and have files update (and for flask to reset), then, easily changeover for prod
* I want to abstract out the article source information to how the site displays the blogs better. Currently doing hardcoded files that are provided along with docker, but i want to be able to point to any file sources (S3 bucket, or an email inbox)
* Fix up code display
* Automatically link to related articles based on tags
* Create an RSS feed
* Pagination

Code highlighting https://highlightjs.org/usage/


### Within Articles
Linking of other articles
Image handling

### Done
Disqus
Filtering
