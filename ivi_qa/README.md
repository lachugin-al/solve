# ivi_qa

Setup:
python3 -m venv venv
source venv/bin/activate
pip3 install -U pip
pip3 install -r requirements.txt

Запуск тестов:
pytest --browser="chrome" --url="https://google.com"