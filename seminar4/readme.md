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
hadoop@mts-hse-de-course-team-1-4:/usr/local/hadoop$ mapred streaming -file 2023-10-18 20:22:13,720 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
2023-10-18 20:22:18,895 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-18 20:22:20,882 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-18 20:22:22,094 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1697652284772_0014
2023-10-18 20:22:25,231 INFO mapred.FileInputFormat: Total input files to process : 1
2023-10-18 20:22:25,537 INFO mapreduce.JobSubmitter: number of splits:9
2023-10-18 20:22:26,844 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1697652284772_0014
2023-10-18 20:22:26,844 INFO mapreduce.JobSubmitter: Executing with tokens: []
2023-10-18 20:22:27,638 INFO conf.Configuration: resource-types.xml not found
2023-10-18 20:22:27,639 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2023-10-18 20:22:28,185 INFO impl.YarnClientImpl: Submitted application application_1697652284772_0014
2023-10-18 20:22:28,317 INFO mapreduce.Job: The url to track the job: http://mts-hse-de-course-team-1-1.msk.internal:8088/proxy/application_1697652284772_0014/
2023-10-18 20:22:28,318 INFO mapreduce.Job: Running job: job_1697652284772_0014
2023-10-18 20:23:00,076 INFO mapreduce.Job: Job job_1697652284772_0014 running in uber mode : false
2023-10-18 20:23:00,077 INFO mapreduce.Job:  map 0% reduce 0%
2023-10-18 20:23:46,111 INFO mapreduce.Job:  map 1% reduce 0%
2023-10-18 20:23:50,528 INFO mapreduce.Job:  map 2% reduce 0%
2023-10-18 20:23:52,915 INFO mapreduce.Job:  map 4% reduce 0%
2023-10-18 20:23:54,332 INFO mapreduce.Job:  map 5% reduce 0%
2023-10-18 20:23:56,420 INFO mapreduce.Job:  map 8% reduce 0%
2023-10-18 20:23:58,492 INFO mapreduce.Job:  map 9% reduce 0%
2023-10-18 20:23:59,504 INFO mapreduce.Job:  map 10% reduce 0%
2023-10-18 20:24:02,664 INFO mapreduce.Job:  map 14% reduce 0%
2023-10-18 20:24:04,838 INFO mapreduce.Job:  map 15% reduce 0%
2023-10-18 20:24:08,040 INFO mapreduce.Job:  map 18% reduce 0%
2023-10-18 20:24:10,059 INFO mapreduce.Job:  map 20% reduce 0%
2023-10-18 20:24:11,088 INFO mapreduce.Job:  map 22% reduce 0%
2023-10-18 20:24:14,356 INFO mapreduce.Job:  map 24% reduce 0%
2023-10-18 20:24:15,368 INFO mapreduce.Job:  map 26% reduce 0%
2023-10-18 20:24:16,444 INFO mapreduce.Job:  map 27% reduce 0%
2023-10-18 20:24:17,468 INFO mapreduce.Job:  map 29% reduce 0%
2023-10-18 20:24:20,694 INFO mapreduce.Job:  map 31% reduce 0%
2023-10-18 20:24:21,708 INFO mapreduce.Job:  map 33% reduce 0%
2023-10-18 20:24:24,028 INFO mapreduce.Job:  map 35% reduce 0%
2023-10-18 20:24:27,077 INFO mapreduce.Job:  map 37% reduce 0%
2023-10-18 20:24:28,267 INFO mapreduce.Job:  map 38% reduce 0%
2023-10-18 20:24:29,303 INFO mapreduce.Job:  map 39% reduce 0%
2023-10-18 20:24:32,404 INFO mapreduce.Job:  map 40% reduce 0%
2023-10-18 20:24:34,688 INFO mapreduce.Job:  map 41% reduce 0%
2023-10-18 20:24:35,933 INFO mapreduce.Job:  map 42% reduce 0%
2023-10-18 20:24:39,352 INFO mapreduce.Job:  map 43% reduce 0%
2023-10-18 20:24:40,544 INFO mapreduce.Job:  map 44% reduce 0%
2023-10-18 20:24:44,992 INFO mapreduce.Job:  map 45% reduce 0%
2023-10-18 20:24:47,344 INFO mapreduce.Job:  map 46% reduce 0%
2023-10-18 20:24:49,585 INFO mapreduce.Job:  map 48% reduce 0%
2023-10-18 20:24:51,643 INFO mapreduce.Job:  map 50% reduce 0%
2023-10-18 20:24:53,940 INFO mapreduce.Job:  map 51% reduce 0%
2023-10-18 20:24:55,106 INFO mapreduce.Job:  map 54% reduce 0%
2023-10-18 20:24:56,223 INFO mapreduce.Job:  map 55% reduce 0%
2023-10-18 20:24:59,812 INFO mapreduce.Job:  map 57% reduce 0%
2023-10-18 20:25:00,972 INFO mapreduce.Job:  map 58% reduce 0%
2023-10-18 20:25:02,124 INFO mapreduce.Job:  map 60% reduce 0%
2023-10-18 20:25:06,637 INFO mapreduce.Job:  map 62% reduce 0%
2023-10-18 20:25:07,952 INFO mapreduce.Job:  map 63% reduce 0%
2023-10-18 20:25:27,943 INFO mapreduce.Job:  map 67% reduce 0%
2023-10-18 20:26:28,581 INFO mapreduce.Job:  map 68% reduce 0%
2023-10-18 20:26:31,912 INFO mapreduce.Job:  map 68% reduce 22%
2023-10-18 20:26:35,148 INFO mapreduce.Job:  map 73% reduce 22%
2023-10-18 20:26:40,510 INFO mapreduce.Job:  map 75% reduce 22%
2023-10-18 20:26:41,520 INFO mapreduce.Job:  map 77% reduce 22%
2023-10-18 20:26:46,939 INFO mapreduce.Job:  map 81% reduce 22%
2023-10-18 20:26:52,574 INFO mapreduce.Job:  map 82% reduce 22%
2023-10-18 20:26:53,707 INFO mapreduce.Job:  map 85% reduce 22%
2023-10-18 20:27:01,442 INFO mapreduce.Job:  map 86% reduce 22%
2023-10-18 20:27:14,246 INFO mapreduce.Job:  map 90% reduce 22%
2023-10-18 20:27:19,720 INFO mapreduce.Job:  map 93% reduce 26%
2023-10-18 20:27:26,060 INFO mapreduce.Job:  map 95% reduce 26%
2023-10-18 20:27:32,924 INFO mapreduce.Job:  map 97% reduce 26%
2023-10-18 20:27:38,584 INFO mapreduce.Job:  map 98% reduce 30%
2023-10-18 20:27:44,684 INFO mapreduce.Job:  map 100% reduce 30%
2023-10-18 20:27:51,146 INFO mapreduce.Job:  map 100% reduce 33%
2023-10-18 20:28:35,025 INFO mapreduce.Job:  map 100% reduce 59%
2023-10-18 20:28:41,273 INFO mapreduce.Job:  map 100% reduce 67%
2023-10-18 20:31:56,691 INFO mapreduce.Job:  map 100% reduce 100%
2023-10-18 20:32:01,922 INFO mapreduce.Job: Job job_1697652284772_0014 completed successfully
2023-10-18 20:32:03,544 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=909678579
                FILE: Number of bytes written=1383448828
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=1153467121
                HDFS: Number of bytes written=51
                HDFS: Number of read operations=32
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters 
                Killed map tasks=3
                Launched map tasks=12
                Launched reduce tasks=1
                Data-local map tasks=12
                Total time spent by all maps in occupied slots (ms)=1319927
                Total time spent by all reduces in occupied slots (ms)=372055
                Total time spent by all map tasks (ms)=1319927
                Total time spent by all reduce tasks (ms)=372055
                Total vcore-milliseconds taken by all map tasks=1319927
                Total vcore-milliseconds taken by all reduce tasks=372055
                Total megabyte-milliseconds taken by all map tasks=1351605248
                Total megabyte-milliseconds taken by all reduce tasks=380984320
        Map-Reduce Framework
                Map input records=31628381
                Map output records=31628381
                Map output bytes=407715128
                Map output materialized bytes=470971944
                Input split bytes=774
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
                GC time elapsed (ms)=13766
                CPU time spent (ms)=215440
                Physical memory (bytes) snapshot=3519528960
                Virtual memory (bytes) snapshot=27350528000
                Total committed heap usage (bytes)=2635071488
                Peak Map Physical memory (bytes)=390709248
                Peak Map Virtual memory (bytes)=2758836224
                Peak Reduce Physical memory (bytes)=659202048
                Peak Reduce Virtual memory (bytes)=2757586944
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


```

Результат:
sum	11854895632930
max	691190
min	0
count	31628381


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



