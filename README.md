### Conda environment

conda update -n base conda --yes
conda create personal
activate personal
conda install -n personal --yes --file environment/requirements_conda.txt
pip install -r environment/requirements_noconda.txt



docker build -t bluemania/personalsite .
docker run -p 5000:5000 -e PORT=5000 --rm bluemania/personalsite


docker build -t bluemania/personalsite .
heroku login
heroku container:login
docker tag bluemania/personalsite registry.heroku.com/nickjenkins/web
docker push registry.heroku.com/nickjenkins/web
heroku container:release web -a nickjenkins


Google SEO
http://flask.pocoo.org/snippets/108/


# TODOs
Google site analytics for SEO connect
Github for code, versioning

RSS
Disqus

Getting started scripts
Code highlighting https://highlightjs.org/usage/
CONTENT!



www.nickjenkins.com.au
fathomless-whale-h7m0nr3r05sfqntdtuajxbkm.herokudns.com
heroku certs:auto:enable -a nickjenkins

# Articles todo
Code highlighting
Tags
Link to other articles (use article text)
Image handling
Pagination
Filtering

