killall -9 gunicorn
sleep 3
/home/bret/code/microblog/venv/bin/gunicorn -b localhost:8000 -w 2 microblog:app
