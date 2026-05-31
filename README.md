# Scrapy Parser PEP

Scrapy-паук для парсинга сайта [Python Enhancement Proposals](https://peps.python.org/). Собирает информацию обо всех PEP, их статусах и формирует два CSV-файла с результатами.

## Возможности

- Обход списка всех PEP на главной странице `peps.python.org`
- Извлечение номера, названия и статуса каждого PEP
- Сохранение детального CSV-файла со всеми PEP
- Подсчёт количества PEP по каждому статусу и запись сводного CSV-файла


## Технологии

- Python 3.12+
- Scrapy 2.5.1
- pytest 6.2.5
- flake8 4.0.1

## Установка и запуск

```bash
# Клонирование репозитория
git clone https://github.com/Dmtrii-Zverev/scrapy_parser_pep.git
cd scrapy_parser_pep

# Создание и активация виртуального окружения
python3.12 -m venv .venv
source .venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск паука
scrapy crawl pep
```

Результаты появятся в `pep_parse/results/`.

## Структура проекта

```
scrapy_parser_pep/
├── pep_parse/                    # Основной пакет Scrapy-проекта
│   ├── spiders/
│   │   └── pep.py                # PepSpider — главный паук
│   ├── items.py                  # PepParseItem — модель данных
│   ├── pipelines.py              # PepParsePipeline — подсчёт статусов
│   ├── middlewares.py            # Стандартные middleware (без изменений)
│   ├── settings.py               # Настройки Scrapy
│   └── constants.py              # Константы путей
├── tests/                        # Набор тестов
│   ├── test_pep.py               # Тесты PepSpider
│   ├── test_items.py             # Тесты PepParseItem
│   ├── test_pipelines.py         # Тесты PepParsePipeline
│   ├── test_settings.py          # Тесты настроек
│   ├── test_files.py             # Тесты выходных файлов
│   ├── test_main.py              # Интеграционный тест
│   └── conftest.py               # Фикстуры pytest
├── pyproject.toml                # Метаданные проекта
├── requirements.txt              # Pinned-зависимости
├── scrapy.cfg                    # Конфигурация Scrapy
└── pytest.ini                    # Настройки pytest
```

## Выходные файлы

| Файл | Описание |
|------|----------|
| `pep_<timestamp>.csv` | Все PEP с колонками: `number`, `name`, `status` |
| `status_summary_<timestamp>.csv` | Сводка по статусам с колонками: `Статус`, `Количество` и итоговой строкой `Total` |

## Тестирование

```bash
pytest -vv
flake8
```

## Лицензия

MIT
