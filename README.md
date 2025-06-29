# Система анализа видео с БПЛА на базе YOLOv4-tiny

Система автоматического обнаружения и трекинга объектов на видеозаписях с беспилотных летательных аппаратов (БПЛА) с веб-интерфейсом.

## 📌 Основные возможности

- 🎯 Детекция объектов (люди, транспорт и др.) с помощью YOLOv4-tiny
- 📹 Обработка видеофайлов с БПЛА
- 🔍 Упрощенный трекинг объектов между кадрами
- 🌐 Веб-интерфейс для загрузки видео и просмотра результатов
- 📊 Галерея обнаруженных объектов с метаданными

## 🛠 Технологический стек

- **Язык программирования**: Python 3.8+
- **Модель детекции**: YOLOv4-tiny
- **Библиотеки**: OpenCV (DNN модуль), NumPy
- **Веб-фреймворк**: Flask
- **Интерфейс**: HTML, Bootstrap

## ⚙️ Установка и запуск

Установите зависимости:
```bash
pip install -r requirements.txt
```

Скачайте веса YOLOv4-tiny, если не получилось скачать здесь:
```bash
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights -P model/
```

Откройте в браузере: [http://localhost:5000](http://localhost:5000)

## 📊 Моя работа 

– Общая схема взаимодействия компонентов системы

![image](https://github.com/user-attachments/assets/f00d3b61-3f93-4b47-b668-a15cb21b45cf)

– Блок-схема этапов анализа видеоданных

![image](https://github.com/user-attachments/assets/234b98f8-e0c2-4d2f-ab7a-4f4edae5ed1a)

– Главная страница веб-интерфейса для загрузки видео и выбора классов объектов

![image](https://github.com/user-attachments/assets/c4ad812c-eb3a-41a2-856a-127b1369cd07)

- Пример успешной детекции человека на видео с БПЛА
- 
![image](https://github.com/user-attachments/assets/6c7152eb-c2c2-4c51-80a0-87ff3b89adca)

- Фрагмент галереи обнаруженных объектов с информацией о трекинге

![image](https://github.com/user-attachments/assets/1e6b0bdd-9b9a-45e0-8f45-922a7542477c)

