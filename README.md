
# Тестовое задание для компании "Тензор" - автотестирование

Целью данного проекта было создание автотеста, способного провести тест по трем заданным сценариям.

## Установка и запуск проекта

### 1. Склонировать репозиторий
Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone <URL репозитория>
cd <название репозитория>
```

### 2. Создать и активировать виртуальное окружение для проекта:
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Запустить тесты
```
pytest tests/*.py
```

### Для запуска тестов с отчетом
```
pytest -s -v --alluredir results
allure serve results
```



