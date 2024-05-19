<h1 align="center">Фреймворк для автоматизации тестирование сайта Школы Английского языка "INTER NATION"</h1>


***
***Особенности проекта***  
-Оповещения о тестовых прогонах в Telegram  
-Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы  
-Сборка проекта в Jenkins  
-Отчеты Allure Report  
-Интеграция с Allure TestOps
-Запуск web/UI автотестов в Selenoid.


***
***Список проверок, реализованных в web/UI автотестах***

-Отображение главной страницы  
-Автоскролинг при нажатии кнопки в шапке сайте  
-Проверка возможности оставить заявку для обратной связи  
-Автоматизация авторизации для студентов школы  
-Проверка страницы вакансии  

***


***Используемый стэк***  
<p align="left">
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" />
<img align="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40" />
<img align="center" src="resources/images/allure.png" height="40" width="40" />
<img align="center" src="resources/images/selene.png" height="40" width="40" />
<img align="center" src="resources/images/selenoid.png" height="40" width="40" />
<img align="center" src="resources/images/telegram.png" height="40" width="40" />

***  
***Запуск тестов***  
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
***

***Примеры запуска***  

История запуска тестов и автоотчеты

<img align="center" src="resources/images/allure_history.png"/>  

***
Пример выполнение автоотеста

<img align="center" src="resources/images/allure_run.png"/>  

***
***Нотификация в телеграмме*** 

<img align="center" src="resources/images/telegram_notification.png"/>  

***

***Видео*** 

<img align="center" src="resources/images/test_video.gif"/>  

***