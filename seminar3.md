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
До помещения файлов в HDFS затрачиваемые ресурсы были следующими

На NameNode:
![Снимок экрана от 2023-10-10 20-23-40](https://github.com/Ksenia-C/misobr/assets/50082204/3e6e8cff-fb87-4371-86aa-4c2786546515)

На DataNode:
![image](https://github.com/Ksenia-C/misobr/assets/50082204/7b295dda-d764-481b-8aa1-6619bb4de040)


Помещаем гигабайтный файл в hadoop fs:

```bash
hadoop fs -put table.csv /hadoop_table.csv
```

Изменение ресурсов

На NameNode:
![image](https://github.com/Ksenia-C/misobr/assets/50082204/4a2c212b-2f30-44c7-8f49-afb454c39614)

Как видим DISK везде увеличился на размер файла

На DataNode:
![Снимок экрана от 2023-10-10 21-00-55](https://github.com/Ksenia-C/misobr/assets/50082204/a45bccf1-4284-438d-8a25-85cceef914a4)

Как видим, DISK везде увеличился на размер файла

Помещаем много файлов суммарным весом в гигабайт в hadoop fs:

```bash
hadoop fs -put many_files /hadoop_many_files
```

Изменение ресурсов

На NameNode:
![image](https://github.com/Ksenia-C/misobr/assets/50082204/a3d2108c-6454-44cd-a5bf-1e53b65dd268)

Как видим DISK везде увеличился на размер папки с файлами

На DataNode:
![image](https://github.com/Ksenia-C/misobr/assets/50082204/a5a55d26-a7e2-4b59-b9bc-c0664d355a8b)

Как видим DISK везде увеличился на размер папки с файлами, а также возросло количество блоков

Результаты можно увидеть в UI: http://77.105.185.69:9870/explorer.html#/
