# QA API Tests (Python + pytest)

Набор автотестов для публичного API *jsonplaceholder*.  
Проект создан для демонстрации навыков автоматизации на python.

## Стек
- Python 3.10+
- pytest (фикстуры, параметризация, маркеры)
- requests (HTTP-запросы)
- Git

## Как запустить

1. *Клонировать репозиторий*
   bash:
   git clone https://github.com/ТВОЙ_НИК/qa-api-tests.git
   cd qa-api-tests
2. *Выполнить*
   python -m venv venv
   venv\Scripts\activate для Windows

   python -m venv venv
   source venv/bin/activate для Linux, macOS
   pip install -r requirements.txt
3. *Запустить тесты*
   pytest --html=report.html -v