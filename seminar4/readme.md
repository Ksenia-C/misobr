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
hadoop@mts-hse-de-course-team-1-1:~$ hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar -file  /home/hadoop/sem4/mapper.py -mapper mapper.py -file  /home/hadoop/sem4/reducer.py -reducer reducer.py -input /sem4/table.csv -output /sem4/output
2023-10-18 21:22:19,720 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
packageJobJar: [/home/hadoop/sem4/mapper.py, /home/hadoop/sem4/reducer.py, /tmp/hadoop-unjar18274763974910523532/] [] /tmp/streamjob9505827619949035830.jar tmpDir=null
2023-10-18 21:22:25,100 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-18 21:22:26,316 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
2023-10-18 21:22:28,107 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1697652284772_0017
2023-10-18 21:22:30,984 INFO mapred.FileInputFormat: Total input files to process : 1
2023-10-18 21:22:31,259 INFO mapreduce.JobSubmitter: number of splits:9
2023-10-18 21:22:32,923 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1697652284772_0017
2023-10-18 21:22:32,923 INFO mapreduce.JobSubmitter: Executing with tokens: []
2023-10-18 21:22:33,393 INFO conf.Configuration: resource-types.xml not found
2023-10-18 21:22:33,397 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2023-10-18 21:22:34,221 INFO impl.YarnClientImpl: Submitted application application_1697652284772_0017
2023-10-18 21:22:34,403 INFO mapreduce.Job: The url to track the job: http://mts-hse-de-course-team-1-1.msk.internal:8088/proxy/application_1697652284772_0017/
2023-10-18 21:22:34,404 INFO mapreduce.Job: Running job: job_1697652284772_0017
2023-10-18 21:23:05,069 INFO mapreduce.Job: Job job_1697652284772_0017 running in uber mode : false
2023-10-18 21:23:05,070 INFO mapreduce.Job:  map 0% reduce 0%
2023-10-18 21:23:53,232 INFO mapreduce.Job:  map 1% reduce 0%
2023-10-18 21:23:54,252 INFO mapreduce.Job:  map 2% reduce 0%
2023-10-18 21:23:55,288 INFO mapreduce.Job:  map 4% reduce 0%
2023-10-18 21:23:56,295 INFO mapreduce.Job:  map 5% reduce 0%
2023-10-18 21:23:59,439 INFO mapreduce.Job:  map 6% reduce 0%
2023-10-18 21:24:00,449 INFO mapreduce.Job:  map 7% reduce 0%
2023-10-18 21:24:01,454 INFO mapreduce.Job:  map 9% reduce 0%
2023-10-18 21:24:02,460 INFO mapreduce.Job:  map 10% reduce 0%
2023-10-18 21:24:03,465 INFO mapreduce.Job:  map 11% reduce 0%
2023-10-18 21:24:07,104 INFO mapreduce.Job:  map 13% reduce 0%
2023-10-18 21:24:08,276 INFO mapreduce.Job:  map 14% reduce 0%
2023-10-18 21:24:09,636 INFO mapreduce.Job:  map 16% reduce 0%
2023-10-18 21:24:11,831 INFO mapreduce.Job:  map 17% reduce 0%
2023-10-18 21:24:12,838 INFO mapreduce.Job:  map 18% reduce 0%
2023-10-18 21:24:13,917 INFO mapreduce.Job:  map 19% reduce 0%
2023-10-18 21:24:15,256 INFO mapreduce.Job:  map 21% reduce 0%
2023-10-18 21:24:25,303 INFO mapreduce.Job:  map 22% reduce 0%
2023-10-18 21:24:26,449 INFO mapreduce.Job:  map 26% reduce 0%
2023-10-18 21:24:35,312 INFO mapreduce.Job:  map 28% reduce 0%
2023-10-18 21:24:40,164 INFO mapreduce.Job:  map 29% reduce 0%
2023-10-18 21:24:53,155 INFO mapreduce.Job:  map 30% reduce 0%
2023-10-18 21:24:54,537 INFO mapreduce.Job:  map 31% reduce 0%
2023-10-18 21:25:03,231 INFO mapreduce.Job:  map 33% reduce 0%
2023-10-18 21:25:32,860 INFO mapreduce.Job:  map 35% reduce 0%
2023-10-18 21:25:42,656 INFO mapreduce.Job:  map 36% reduce 0%
2023-10-18 21:26:14,136 INFO mapreduce.Job:  map 38% reduce 0%
2023-10-18 21:26:19,004 INFO mapreduce.Job:  map 39% reduce 0%
2023-10-18 21:26:20,952 INFO mapreduce.Job:  map 40% reduce 0%
2023-10-18 21:27:26,759 INFO mapreduce.Job:  map 41% reduce 0%
2023-10-18 21:27:28,872 INFO mapreduce.Job:  map 42% reduce 0%
2023-10-18 21:27:30,268 INFO mapreduce.Job:  map 48% reduce 0%
2023-10-18 21:27:48,434 INFO mapreduce.Job:  map 52% reduce 0%
2023-10-18 21:27:52,315 INFO mapreduce.Job:  map 53% reduce 0%
2023-10-18 21:28:34,676 INFO mapreduce.Job:  map 55% reduce 0%
2023-10-18 21:28:49,096 INFO mapreduce.Job:  map 67% reduce 0%
2023-10-18 21:30:19,626 INFO mapreduce.Job:  map 68% reduce 0%
2023-10-18 21:30:22,852 INFO mapreduce.Job:  map 69% reduce 15%
2023-10-18 21:30:26,120 INFO mapreduce.Job:  map 71% reduce 15%
2023-10-18 21:30:28,154 INFO mapreduce.Job:  map 72% reduce 15%
2023-10-18 21:30:29,160 INFO mapreduce.Job:  map 73% reduce 22%
2023-10-18 21:30:32,189 INFO mapreduce.Job:  map 74% reduce 22%
2023-10-18 21:30:34,878 INFO mapreduce.Job:  map 77% reduce 22%
2023-10-18 21:30:36,991 INFO mapreduce.Job:  map 78% reduce 22%
2023-10-18 21:30:40,138 INFO mapreduce.Job:  map 79% reduce 22%
2023-10-18 21:30:52,440 INFO mapreduce.Job:  map 80% reduce 22%
2023-10-18 21:30:53,622 INFO mapreduce.Job:  map 81% reduce 22%
2023-10-18 21:30:58,852 INFO mapreduce.Job:  map 82% reduce 22%
2023-10-18 21:31:00,000 INFO mapreduce.Job:  map 85% reduce 22%
2023-10-18 21:31:20,620 INFO mapreduce.Job:  map 90% reduce 22%
2023-10-18 21:31:24,818 INFO mapreduce.Job:  map 91% reduce 22%
2023-10-18 21:31:31,831 INFO mapreduce.Job:  map 91% reduce 26%
2023-10-18 21:31:37,853 INFO mapreduce.Job:  map 92% reduce 26%
2023-10-18 21:31:42,919 INFO mapreduce.Job:  map 94% reduce 26%
2023-10-18 21:31:45,252 INFO mapreduce.Job:  map 95% reduce 26%
2023-10-18 21:31:49,390 INFO mapreduce.Job:  map 97% reduce 26%
2023-10-18 21:31:51,412 INFO mapreduce.Job:  map 98% reduce 26%
2023-10-18 21:31:55,530 INFO mapreduce.Job:  map 98% reduce 30%
2023-10-18 21:31:56,548 INFO mapreduce.Job:  map 100% reduce 30%
2023-10-18 21:32:02,136 INFO mapreduce.Job:  map 100% reduce 33%
2023-10-18 21:32:45,527 INFO mapreduce.Job:  map 100% reduce 41%
2023-10-18 21:32:52,796 INFO mapreduce.Job:  map 100% reduce 67%
2023-10-18 21:36:21,672 INFO mapreduce.Job:  map 100% reduce 100%
2023-10-18 21:36:26,708 INFO mapreduce.Job: Job job_1697652284772_0017 completed successfully
2023-10-18 21:36:29,271 INFO mapreduce.Job: Counters: 55
	File System Counters
		FILE: Number of bytes read=909678579
		FILE: Number of bytes written=1383448808
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
		Total time spent by all maps in occupied slots (ms)=2659178
		Total time spent by all reduces in occupied slots (ms)=408202
		Total time spent by all map tasks (ms)=2659178
		Total time spent by all reduce tasks (ms)=408202
		Total vcore-milliseconds taken by all map tasks=2659178
		Total vcore-milliseconds taken by all reduce tasks=408202
		Total megabyte-milliseconds taken by all map tasks=2722998272
		Total megabyte-milliseconds taken by all reduce tasks=417998848
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
		GC time elapsed (ms)=25511
		CPU time spent (ms)=217070
		Physical memory (bytes) snapshot=3444862976
		Virtual memory (bytes) snapshot=27344171008
		Total committed heap usage (bytes)=2940207104
		Peak Map Physical memory (bytes)=442413056
		Peak Map Virtual memory (bytes)=2767519744
		Peak Reduce Physical memory (bytes)=655290368
		Peak Reduce Virtual memory (bytes)=2762584064
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
2023-10-18 21:36:29,271 INFO streaming.StreamJob: Output directory: /sem4/output

```

Результат:

```bash
hadoop@mts-hse-de-course-team-1-1:~$ hadoop fs -getmerge /sem4/output output.txt
hadoop@mts-hse-de-course-team-1-1:~$ cat output.txt
sum	11854895632930
max	691190
min	0
count	31628381
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



