# Cyber Care Task_2

### Intro

Joining two files together.

### How to use it:

```
git clone https://github.com/LeonMilosevic/cc_task_2.git
```

```
pip install -r requirements.txt
```

```
python main.py
```

### Pipeline Walkthrough:

Extract:

- Extract both files from source<br />
&darr;
- Ensure Data Quality checks for fetched data.<br />
&darr;
- Document Data Quality findings in logs dir<br />

Transform:

- Apply transformations needed per business requirements.<br />

Load:
- Dump result as csv file in storage dir. <br />

### Expected Results:

- CSV file with merged data from two files, where we kept the last updated ticker per id and brand_id.