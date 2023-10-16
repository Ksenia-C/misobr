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

Замер ресурсов записали на видео: https://drive.google.com/file/d/15aMC3XyDOc7Jyu1nuhe5pQuJBnzrB8pE/view?usp=sharing

# Запуск MapReduce на Hadoop Standalone:
```bash
hadoop@mts-hse-de-course-team-1-4:/usr/local/hadoop$ mapred streaming -file /home/hadoop/sem4/mapper.py    -mapper  "python3 /home/hadoop/sem4/mapper.py" -file /home/hadoop/sem4/reducer.py   -reducer  "python3 /home/hadoop/sem4/reducer.py" -input /sem4/very_big_file.csv -output /sem4/result238472023-10-11 18:22:27,606 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [/home/hadoop/sem4/mapper.py, /home/hadoop/sem4/reducer.py] [/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar] /tmp/streamjob16648459089395060725.jar tmpDir=null
2023-10-11 18:22:28,548 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-11 18:22:28,817 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-11 18:22:29,006 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1696807012168_0117
2023-10-11 18:22:29,370 INFO mapred.FileInputFormat: Total input files to process : 1
2023-10-11 18:22:29,436 INFO mapreduce.JobSubmitter: number of splits:9
2023-10-11 18:22:29,645 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1696807012168_0117
2023-10-11 18:22:29,645 INFO mapreduce.JobSubmitter: Executing with tokens: []
2023-10-11 18:22:29,769 INFO conf.Configuration: resource-types.xml not found
2023-10-11 18:22:29,769 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2023-10-11 18:22:29,837 INFO impl.YarnClientImpl: Submitted application application_1696807012168_0117
2023-10-11 18:22:29,863 INFO mapreduce.Job: The url to track the job: http://mts-hse-de-course-team-1-4.msk.internal:8088/proxy/application_1696807012168_0117/
2023-10-11 18:22:29,864 INFO mapreduce.Job: Running job: job_1696807012168_0117
2023-10-11 18:22:37,084 INFO mapreduce.Job: Job job_1696807012168_0117 running in uber mode : false
2023-10-11 18:22:37,085 INFO mapreduce.Job:  map 0% reduce 0%
2023-10-11 18:23:00,330 INFO mapreduce.Job:  map 4% reduce 0%
2023-10-11 18:23:02,341 INFO mapreduce.Job:  map 9% reduce 0%
2023-10-11 18:23:03,347 INFO mapreduce.Job:  map 18% reduce 0%
2023-10-11 18:23:05,481 INFO mapreduce.Job:  map 28% reduce 0%
2023-10-11 18:23:07,491 INFO mapreduce.Job:  map 31% reduce 0%
2023-10-11 18:23:08,499 INFO mapreduce.Job:  map 33% reduce 0%
2023-10-11 18:23:09,505 INFO mapreduce.Job:  map 38% reduce 0%
2023-10-11 18:23:11,517 INFO mapreduce.Job:  map 41% reduce 0%
2023-10-11 18:23:13,614 INFO mapreduce.Job:  map 43% reduce 0%
2023-10-11 18:23:14,619 INFO mapreduce.Job:  map 45% reduce 0%
2023-10-11 18:23:15,625 INFO mapreduce.Job:  map 50% reduce 0%
2023-10-11 18:23:16,672 INFO mapreduce.Job:  map 55% reduce 0%
2023-10-11 18:23:17,678 INFO mapreduce.Job:  map 61% reduce 0%
2023-10-11 18:23:18,682 INFO mapreduce.Job:  map 63% reduce 0%
2023-10-11 18:23:19,688 INFO mapreduce.Job:  map 67% reduce 0%
2023-10-11 18:23:38,187 INFO mapreduce.Job:  map 78% reduce 0%
2023-10-11 18:23:39,194 INFO mapreduce.Job:  map 90% reduce 0%
2023-10-11 18:23:41,204 INFO mapreduce.Job:  map 90% reduce 26%
2023-10-11 18:23:45,331 INFO mapreduce.Job:  map 99% reduce 26%
2023-10-11 18:23:46,334 INFO mapreduce.Job:  map 100% reduce 26%
2023-10-11 18:23:47,424 INFO mapreduce.Job:  map 100% reduce 33%
2023-10-11 18:23:59,572 INFO mapreduce.Job:  map 100% reduce 67%
2023-10-11 18:24:35,815 INFO mapreduce.Job:  map 100% reduce 100%
2023-10-11 18:24:35,821 INFO mapreduce.Job: Job job_1696807012168_0117 completed successfully
2023-10-11 18:24:35,952 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=909678579
                FILE: Number of bytes written=1383449628
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1153467193
                HDFS: Number of bytes written=51
                HDFS: Number of read operations=32
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters 
                Killed map tasks=1
                Launched map tasks=10
                Launched reduce tasks=1
                Data-local map tasks=10
                Total time spent by all maps in occupied slots (ms)=322284
                Total time spent by all reduces in occupied slots (ms)=75173
                Total time spent by all map tasks (ms)=322284
                Total time spent by all reduce tasks (ms)=75173
                Total vcore-milliseconds taken by all map tasks=322284
                Total vcore-milliseconds taken by all reduce tasks=75173
                Total megabyte-milliseconds taken by all map tasks=330018816
                Total megabyte-milliseconds taken by all reduce tasks=76977152
        Map-Reduce Framework
                Map input records=31628381
                Map output records=31628381
                Map output bytes=407715128
                Map output materialized bytes=470971944
                Input split bytes=846
                Combine input records=0
                Combine output records=0
                Reduce input groups=1
                Reduce shuffle bytes=470971944
                Reduce input records=31628381
                Reduce output records=4
                Spilled Records=92718403
                Shuffled Maps =9
                Failed Shuffles=0
                Merged Map outputs=9
                GC time elapsed (ms)=2326
                CPU time spent (ms)=171910
                Physical memory (bytes) snapshot=3293085696
                Virtual memory (bytes) snapshot=27377545216
                Total committed heap usage (bytes)=2192572416
                Peak Map Physical memory (bytes)=358715392
                Peak Map Virtual memory (bytes)=2758479872
                Peak Reduce Physical memory (bytes)=645013504
                Peak Reduce Virtual memory (bytes)=2757877760
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=1153466347
        File Output Format Counters 
                Bytes Written=51
2023-10-11 18:24:35,952 INFO streaming.StreamJob: Output directory: /sem4/result23847


```

# Запуск MapReduce на кластере Hadoop:
```bash
$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-file  /home/hadoop/sem4/mapper.py -mapper mapper.py \
-file  /home/hadoop/sem4/reducer.py -reducer reducer.py \
-input /sem4/very_big_file.csv \
-output /sem4/output
2023-10-14 13:29:56,039 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [/home/hadoop/sem4/mapper.py, /home/hadoop/sem4/reducer.py, /tmp/hadoop-unjar8020407589170180434/] [] /tmp/streamjob4246296754301022721.jar tmpDir=null
2023-10-14 13:29:56,895 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-14 13:29:57,056 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-14 13:29:57,301 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1696807012168_0274
2023-10-14 13:29:57,743 INFO mapred.FileInputFormat: Total input files to process : 1
2023-10-14 13:29:57,805 INFO mapreduce.JobSubmitter: number of splits:9
2023-10-14 13:29:57,981 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1696807012168_0274
2023-10-14 13:29:57,981 INFO mapreduce.JobSubmitter: Executing with tokens: []
2023-10-14 13:29:58,125 INFO conf.Configuration: resource-types.xml not found
2023-10-14 13:29:58,126 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2023-10-14 13:29:58,175 INFO impl.YarnClientImpl: Submitted application application_1696807012168_0274
2023-10-14 13:29:58,202 INFO mapreduce.Job: The url to track the job: http://mts-hse-de-course-team-1-4.msk.internal:8088/proxy/application_1696807012168_0274/
2023-10-14 13:29:58,204 INFO mapreduce.Job: Running job: job_1696807012168_0274
2023-10-14 13:30:05,355 INFO mapreduce.Job: Job job_1696807012168_0274 running in uber mode : false
2023-10-14 13:30:05,356 INFO mapreduce.Job:  map 0% reduce 0%
2023-10-14 13:30:28,876 INFO mapreduce.Job:  map 10% reduce 0%
2023-10-14 13:30:30,888 INFO mapreduce.Job:  map 19% reduce 0%
2023-10-14 13:30:32,898 INFO mapreduce.Job:  map 24% reduce 0%
2023-10-14 13:30:33,904 INFO mapreduce.Job:  map 30% reduce 0%
2023-10-14 13:30:36,036 INFO mapreduce.Job:  map 33% reduce 0%
2023-10-14 13:30:37,042 INFO mapreduce.Job:  map 38% reduce 0%
2023-10-14 13:30:39,081 INFO mapreduce.Job:  map 40% reduce 0%
2023-10-14 13:30:40,187 INFO mapreduce.Job:  map 42% reduce 0%
2023-10-14 13:30:42,256 INFO mapreduce.Job:  map 46% reduce 0%
2023-10-14 13:30:43,362 INFO mapreduce.Job:  map 51% reduce 0%
2023-10-14 13:30:44,389 INFO mapreduce.Job:  map 56% reduce 0%
2023-10-14 13:30:45,494 INFO mapreduce.Job:  map 64% reduce 0%
2023-10-14 13:30:46,503 INFO mapreduce.Job:  map 67% reduce 0%
2023-10-14 13:31:03,142 INFO mapreduce.Job:  map 78% reduce 0%
2023-10-14 13:31:05,279 INFO mapreduce.Job:  map 85% reduce 0%
2023-10-14 13:31:06,290 INFO mapreduce.Job:  map 92% reduce 0%
2023-10-14 13:31:08,390 INFO mapreduce.Job:  map 92% reduce 26%
2023-10-14 13:31:11,402 INFO mapreduce.Job:  map 100% reduce 26%
2023-10-14 13:31:14,430 INFO mapreduce.Job:  map 100% reduce 33%
2023-10-14 13:31:20,464 INFO mapreduce.Job:  map 100% reduce 49%
2023-10-14 13:31:26,563 INFO mapreduce.Job:  map 100% reduce 67%
2023-10-14 13:32:00,522 INFO mapreduce.Job:  map 100% reduce 100%
2023-10-14 13:32:00,526 INFO mapreduce.Job: Job job_1696807012168_0274 completed successfully
2023-10-14 13:32:00,616 INFO mapreduce.Job: Counters: 55
	File System Counters
		FILE: Number of bytes read=909678579
		FILE: Number of bytes written=1383448888
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=1153467193
		HDFS: Number of bytes written=51
		HDFS: Number of read operations=32
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters
		Killed map tasks=1
		Launched map tasks=10
		Launched reduce tasks=1
		Data-local map tasks=10
		Total time spent by all maps in occupied slots (ms)=303812
		Total time spent by all reduces in occupied slots (ms)=73274
		Total time spent by all map tasks (ms)=303812
		Total time spent by all reduce tasks (ms)=73274
		Total vcore-milliseconds taken by all map tasks=303812
		Total vcore-milliseconds taken by all reduce tasks=73274
		Total megabyte-milliseconds taken by all map tasks=311103488
		Total megabyte-milliseconds taken by all reduce tasks=75032576
	Map-Reduce Framework
		Map input records=31628381
		Map output records=31628381
		Map output bytes=407715128
		Map output materialized bytes=470971944
		Input split bytes=846
		Combine input records=0
		Combine output records=0
		Reduce input groups=1
		Reduce shuffle bytes=470971944
		Reduce input records=31628381
		Reduce output records=4
		Spilled Records=92718403
		Shuffled Maps =9
		Failed Shuffles=0
		Merged Map outputs=9
		GC time elapsed (ms)=3426
		CPU time spent (ms)=169710
		Physical memory (bytes) snapshot=3538952192
		Virtual memory (bytes) snapshot=27396435968
		Total committed heap usage (bytes)=2489319424
		Peak Map Physical memory (bytes)=415518720
		Peak Map Virtual memory (bytes)=2770235392
		Peak Reduce Physical memory (bytes)=659099648
		Peak Reduce Virtual memory (bytes)=2760605696
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters
		Bytes Read=1153466347
	File Output Format Counters
		Bytes Written=51
2023-10-14 13:32:00,619 INFO streaming.StreamJob: Output directory: /sem4/output
```

Прочитаем результат
```bash
$ hadoop fs -getmerge /sem4/output output.txt
$ cat output.txt
sum	11854895632930
max	691190
min	0
count	31628381
```



