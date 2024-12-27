# ВИ система и аналитика + визуализация - ClickHouse

## 1. Тема: ВИ система и аналитика + визуализация - ClickHouse

---

- **Цель**:  
  Данная работа направлена на исследование интеграции ClickHouse с Grafana для эффективной визуализации и анализа, с акцентом на применение в системах бизнес-аналитики (BI).

---

## 2. Содержание

### 2.1 Введение

**Обзор**:  
В современном мире больших данных существует растущий спрос на сбор, управление, анализ и визуализацию огромных объемов данных, будь то для обеспечения безопасности или для поддержки бизнес-стратегий. Системы бизнес-аналитики (BI) играют ключевую роль в упрощении этих задач, обеспечивая повышенную безопасность, эффективность и выводы, на основе которых можно принимать решения.

Эта работа сосредоточена на интеграции ClickHouse, высокопроизводительного хранилища данных для онлайн-аналитической обработки (OLAP) запросов, с Grafana, открытой платформой для мониторинга, визуализации и оповещений по метрикам.

**Исследовательский вопрос**:  
Какую роль играют Grafana и ClickHouse в бизнес-аналитике, и как их интеграция может улучшить процесс анализа данных и визуализации?

### 2.2 Актуальность

#### 2.2.1 Архитектура и технологии

**Обзор архитектуры BI системы**:  
Архитектура бизнес-аналитики (BI) относится к совокупности технологий, процессов и инструментов, используемых для сбора, хранения, управления и анализа данных с целью поддержки бизнес-решений. Архитектурные слои BI спроектированы для преобразования сырых данных в полезную информацию, используя комбинацию управления данными, анализа данных и их визуализации [2].

**Ключевые компоненты**:

1. **Слой источников данных (ClickHouse)**:

   - **ClickHouse** — это открытая колонкоориентированная СУБД для онлайн-аналитической обработки, позволяющая пользователям в реальном времени генерировать аналитические отчеты с использованием SQL-запросов.
   - ClickHouse оптимизирован для быстрых запросов и агрегаций, что делает его идеальным выбором для задач BI, требующих мгновенных аналитических выводов.

2. **Слой обработки данных**:

   - Этот слой включает очистку, преобразование и обработку данных перед визуализацией. Он может включать процессы ETL (Извлечение, Преобразование, Загрузка) или прямые запросы из ClickHouse.
   - SQL-возможности ClickHouse можно использовать для выполнения преобразования данных, агрегации, фильтрации и суммирования на этом уровне.

3. **Слой визуализации (Grafana)**:

   - **Grafana** напрямую подключается к ClickHouse и отвечает за отображение данных в удобной для пользователя форме: через визуализации, панели мониторинга и отчеты.
   - Grafana поддерживает широкий спектр визуальных элементов, таких как графики временных рядов, таблицы и панели реального времени, что делает ее идеальной для отслеживания ключевых показателей (KPI) и мониторинга бизнес-тенденций.

4. **Слой оповещений и мониторинга**:
   - Grafana также предоставляет возможность настройки оповещений и мониторинга, позволяя пользователям устанавливать пороговые значения и отправлять уведомления, если метрики превышают заданные лимиты.
   - Эта функция гарантирует, что заинтересованные стороны BI смогут принимать своевременные и основанные на данных решения.

**Поток данных**:

1. **Загрузка данных**:  
   Для примера используется [тестовый набор данных BETH](https://www.kaggle.com/datasets/katehighnam/beth-dataset/data?select=labelled_testing_data.csv), который хранится в ClickHouse.

2. **Запрос и обработка данных**:  
   Для предварительной обработки данных и их вставки в ClickHouse используются кастомные скрипты на Python. ClickHouse обрабатывает данные с использованием SQL-запросов, применяя фильтры, преобразования и агрегации в соответствии с требованиями BI.

3. **Визуализация**:  
   Grafana в реальном времени извлекает данные из ClickHouse и отображает их через настраиваемые панели для анализа трендов, мониторинга KPI и оценки бизнес-результатов.

4. **Оповещения и мониторинг**:  
   Оповещения срабатывают при наступлении определённых условий, и уведомления отправляются заинтересованным сторонам для быстрого решения критических вопросов.

**Архитектурная диаграмма:**

```mermaid
stateDiagram-v2
   s1: Тренировочный набор данных BETH
    s2: Предварительная обработка данных с помощью Python
    s3: ClickHouse
    s4: Grafana
    u1: BI аналитики
    u2: Эксперты по безопасности
    u3: и т.д.
    [*] --> s1

	s1 --> s2
	s2 --> s3
	s3 --> s4
	s4 --> u1
	s4--> u2
	s4--> u3
```

### 2.3. Проектирование системы

#### 2.3.1. Реализация и тестирование

#### 2.3.1.1 Установка ClickHouse

ClickHouse предлагает хорошо документированный процесс установки, который можно найти [здесь](https://clickhouse.com/docs/ru/install). В данной работе мы демонстрируем установку ClickHouse как на Linux, так и на macOS. Для этого раздела мы сосредоточимся на установке на macOS.

Чтобы установить ClickHouse на macOS, выполните следующие шаги:

1. **Скачать ClickHouse:**

   - Самый простой способ загрузить ClickHouse локально — выполнить следующую команду:

   ```bash
   curl https://clickhouse.com/ | sh

   ```

2. **Запуск сервера ClickHouse:**

- После установки запустите сервер ClickHouse, выполнив следующую команду:

```bash
   ./clickhouse server
```

!['Shows ClickHouse server running'](src/reports/01.png)

![Shows ClickHouse service started on Linux](src/reports/02.png)

> Примечание: Для повышения безопасности рекомендуется изменить пароль по умолчанию и добавить пользователя после первоначальной настройки.

---

#### 2.3.1.2 Установка Grafana

!['Shows ClickHouse server running'](src/reports/03.png)
!['Shows ClickHouse server running'](src/reports/04.png)
!['Shows ClickHouse server running'](src/reports/05.png)
!['Shows ClickHouse server running'](src/reports/07.png)

#### 2.3.2 Вставка данных

Для вставки данных в ClickHouse мы используем собственные [скрипты](src/scripts/click_house.py). Другим вариантом является выполнение следующей команды для вставки данных:

1. Для создания таблицы:

```sql
CREATE TABLE ids.labelled_testing_data (timestamp Float64,processId UInt64,threadId UInt64,parentProcessId UInt64,userId UInt64,mountNamespace UInt64,processName String,hostName String,eventId UInt64,eventName String,stackAddresses Array(Int128),argsNum UInt64,returnValue Int64,sus Int64,evil UInt64)ENGINE = MergeTree() ORDER BY timestamp
```

2. Чтобы добавить данные

```bash
clickhouse-client -query "INSERT INTO ids.labelled_testing_data FORMAT CSV" < labelled_testing_data.csv
```
!['Shows ClickHouse server running'](src/reports/10.png)
!['Shows ClickHouse server running'](src/reports/09.png)
!['Shows ClickHouse server running'](src/reports/11.png)
!['Shows ClickHouse server running'](src/reports/11_1.png)

!['Shows ClickHouse server running'](src/reports/12.png)

---
#### 2.3.3 Визуализация данных в Grafana


!['Shows ClickHouse server running'](src/reports/12_1.png)
!['Shows ClickHouse server running'](src/reports/13.png)
!['Shows ClickHouse server running'](src/reports/14.png)
!['Shows ClickHouse server running'](src/reports/15.png)
!['Shows ClickHouse server running'](src/reports/16.png)
!['Shows ClickHouse server running'](src/reports/17.png)
!['Shows ClickHouse server running'](src/reports/18.png)
!['Shows ClickHouse server running'](src/reports/19.png)
## список литературы

1. What is business intelligence? [electronic resource]. URL: https://www.ibm.com/topics/business-intelligence (date of reference: 23.12.2024).
2. Understanding Business Intelligence Architecture: A Comprehensive Guide [electronic resource]. URL: https://www.sprinkledata.com/blogs/understanding-business-intelligence-architecture-a-comprehensive-guide (date of reference: 23.12.2024).
3. Grafana: инструмент для удобной визуализации метрик мониторинга [electronic resource]. URL: https://cloud.vk.com/blog/grafana-instrument-udobnoy-vizualizatsii-metrik-monitoringa/ (date of reference: 23.12.2024).
# bi_clickhouse_grafana
