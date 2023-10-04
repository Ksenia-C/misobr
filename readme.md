## Проект команды номер 1
## Состав группы:
Копылов Олег

Карнаухов Арсений

Жукова Дарья

Петренко Ксения

Сазонов Михаил


## Инструкция

### Подготовка операционной системы

Выполните следующие команды (команды приведены для Ubuntu).

1. Обновление пакетов

``apt update && apt upgrade``

2. Настройка брандмауэра

``iptables -I INPUT -p tcp --dport 9870 -j ACCEPT``


``iptables -I INPUT -p tcp --dport 8020 -j ACCEPT``


``iptables -I INPUT -p tcp --match multiport --dports 9866,9864,9867 -j ACCEPT``


где порт:

9870 — веб-интерфейс для управления.

8020 — RPC адрес для клиентских подключений.

9866 — DataNode (передача данных).

9864 — DataNode (http-сервис).

9867 — DataNode (IPC-сервис).


Для сохранения правил используем утилиту netfilter-persistent:

``apt install iptables-persistent``

``netfilter-persistent save``


3. Настройка hosts
На серверах добавить в файл hosts следующее:

``vi /etc/hosts`` – с помощью  этой команды добавляем

_Добавляемый текст:_

**#127.0.1.1 haddop1**

**192.168.1.15 haddop1**

**192.168.1.20 haddop2**

**192.168.1.25 haddop3**
   

### Установка Java

Hadoop разработан на языке программирования Java, поэтому на наших серверах должна быть установлена данная платформа.

Выполняем команду:

``apt install default-jdk``
Готово. Смотрим версию установленной java:

``java -version``
Мы должны увидеть что-то похожее на:

**openjdk version "11.0.13" 2021-10-19**

**OpenJDK Runtime Environment (build 11.0.13+8-Ubuntu-0ubuntu1.20.04)**

**OpenJDK 64-Bit Server VM (build 11.0.13+8-Ubuntu-0ubuntu1.20.04, mixed mode, sharing)**

### Установка Hadoop

Установка выполняется вручную — необходимо скачать бинарник с сайта разработчика и разместить на сервере, создать файлы с переменными окружения и настроить автозапуск с помощью systemd. Данные действия выполняем на всех серверах. Также необходимо обеспечить возможность подключения по ssh ко всем серверам кластера.

#### Загрузка исходника

Переходим на страницу загрузки Hadoop и кликаем по ссылке для скачивания нужной версии программного обеспечения.
Копируем ссылку на загрузку архива и, используя эту ссылку, загружаем на наши серверы архив:

``wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz``


### Установка и настройка среды

Создадим каталог, в который поместим файлы приложения:

``mkdir /usr/local/hadoop``

Распаковываем содержимое загруженного архива в созданный каталог:

``tar -zxf hadoop-*.tar.gz -C /usr/local/hadoop --strip-components 1``

Создаем пользователя hadoop:

``useradd hadoop -m``

И зададим ему пароль:

``passwd hadoop``

Задаем в качестве владельца каталога hadoop созданного пользователя:

``chown -R hadoop:hadoop /usr/local/hadoop``

Создаем файл с профилем:

``_vi /etc/profile.d/hadoop.sh``

_Добавляемый текст:_

**export HADOOP_HOME=/usr/local/hadoop**

**export HADOOP_HDFS_HOME=$HADOOP_HOME**

**export HADOOP_MAPRED_HOME=$HADOOP_HOME**

**export HADOOP_COMMON_HOME=$HADOOP_HOME**

**export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native**

**export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"**

**export YARN_HOME=$HADOOP_HOME**

**export PATH="$PATH:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin"**

Выше задаются системные переменные, требующиеся для работы hadoop:

_HADOOP_HOME_ — путь, где находятся файлы hadoop.

_HADOOP_HDFS_HOME_ — директория распределенной файловой системы HDFS.

_HADOOP_MAPRED_HOME_ — необходима для возможности отправки задания MapReduce с помощью MapReduce v2 в YARN.

_HADOOP_COMMON_HOME_ — путь хранения файлов для модуля common.

_HADOOP_COMMON_LIB_NATIVE_DIR_ — место размещения библиотеки native-hadoop.

_HADOOP_OPTS_ — дополнительные опции запуска.

_YARN_HOME_ — путь размещения файлов модуля YARN.

_PATH_ — дополняет общую переменную PATH, где хранятся пути хранения бинарников для запуска приложений.

Теперь откроем файл:

``vi /usr/local/hadoop/etc/hadoop/hadoop-env.sh``


Находим:

``# export JAVA_HOME=``
Меняем на:

``export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64``

_Замечение:_
Выше прописали актуальный путь до файлов openjdk.


### Проверка настройки среды
