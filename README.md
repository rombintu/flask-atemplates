
# Запуск
```
git clone https://github.com/rombintu/flask-atemplates.git
cd flask-atemplates
cp .env.bak .env
python3 -m poetry install
python3 src/server/model.py  
mkdir -p src/server/static/downloads 
flask run
```
## Необходимое ПО
- python3
- pip3
- poetry

## Удалить шаблон
```
python3 src/server/deleter.py
```