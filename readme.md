## Проект команды номер 1
## Состав группы:
Копылов Олег

Карнаухов Арсений

Жукова Дарья

Петренко Ксения

Сазонов Михаил


## Инструкция

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
   
