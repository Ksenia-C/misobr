# Запуск MapReduce без Hadoop:

```bash
$ time cat sem4/very_big_file.csv | python3 sem4/mapper.py | python3 sem4/reducer.py
sum	11854895632930
max	691190
min	0
count	31628381

real	0m43.102s
user	1m0.576s
sys	0m2.628s
```

Замер ресурсов записали на видео: 
