# Выполнение задания к семинару 3.

## Состав группы:

Копылов Олег

Карнаухов Арсений

Жукова Дарья

Петренко Ксения

Сазонов Михаил

Богачева Анна

## Выполнение

Создали большой файл, локально весящий 1.22 ГБ: https://drive.google.com/file/d/1VIjdrTvM-cJm_UG-kdRxPjJpx8hxvXVg/view?usp=sharing

И 1000 небольших файлов, суммарно весящих 1.1 ГБ: https://drive.google.com/drive/folders/1Wrsrukajh9RGzKCjBv7BZy-PdqawX9gR?usp=sharing

Перемещаем файлы на мастерный сервер:

```bash
scp table.csv team1@77.105.185.69:/home/team1/table.csv
scp -r many_files team1@77.105.185.69:/home/team1/many_files
```
