### Conda environment

conda update -n base conda --yes
conda create personal
activate personal
conda install -n personal --yes --file environment/requirements_conda.txt
pip install -r environment/requirements_noconda.txt


### Local Docker
docker build -t bluemania/personalsite .
docker run -p 5000:5000 -e PORT=5000 --rm bluemania/personalsite

### Push Docker
docker build -t bluemania/personalsite .
heroku login
heroku container:login
docker tag bluemania/personalsite registry.heroku.com/nickjenkins/web
docker push registry.heroku.com/nickjenkins/web
heroku container:release web -a nickjenkins

### SSL
www.nickjenkins.com.au
fathomless-whale-h7m0nr3r05sfqntdtuajxbkm.herokudns.com
heroku certs:auto:enable -a nickjenkins

### SEO resources
Google SEO
http://flask.pocoo.org/snippets/108/

# TODOs
x CONTENT!
x Tags - working for filters etc
x Formatting of articles
 - video
 
Sitemap
Related articles based on tags
RSS
Pagination
Code highlighting https://highlightjs.org/usage/
Comment count on links

### Within Articles
Linking of other articles
Image handling

### Done
Disqus
Filtering


