# Selenium-Python-Study-Project
Проект по итогам курса "Автоматизация тестирования с помощью Selenium и Python"


Подготовка окружения:

1. Создайте отдельный публичный репозиторий с осмысленным названием на GitHub.
2. Склонируйте его к себе на локальную машину.
3. Добавьте туда файл conftest.py из предыдущего модуля. Убедитесь дополнительно, что там есть параметр для задания языка интерфейса, по умолчанию равный "en"
4. Добавьте в репозиторий файл requirements.txt из предыдущего модуля. 
5. Создайте файл пустой файл `__init__.py`, чтобы работали относительные импорты.
6. Создайте файл `test_main_page.py` и добавьте в него тест из предыдущего модуля: 
```python
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
```

* Убедитесь, что тест работает, с помощью следующей команды:
```
pytest -v --tb=line --language=en test_main_page.py
```
Здесь и далее мы будем использовать эту команду для запуска. В этой команде мы использовали опцию `PyTest --tb=line`, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста. Так вам будет проще разобраться в том, как выглядят сообщения об ошибках. 
* Добавьте все новые файлы в Git командой `git add *`
* Проверьте, что нужные файлы попали в планируемый коммит: `git status`
* Зафиксируйте изменения коммитом с осмысленным сообщением: `git commit -m "write your message"`
* По желанию добавьте описание репозитория с описанием вашего тестового проекта 