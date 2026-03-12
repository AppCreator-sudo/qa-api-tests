# QA API Tests (Python + pytest)

Набор автотестов для публичного API *ReqRes.in*.  
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
   venv\Scripts\activate для Windows
   source venv/bin/activate для Linux, macOS
   pip install -r requirements.txt
3. *Запустить тесты*
   pytest --html=report.html -v