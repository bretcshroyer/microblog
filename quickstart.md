# I don't want to read the whole mega-tutuorial, I just want to get this running

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux

install and activate venv

### Install the requirements:
pip intall -r requirements.txt

update /app/.env

### add FLASK_APP to your default profile
echo "export FLASK_APP=microblog.py" >> ~/.profile