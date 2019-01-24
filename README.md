# Achievement First Coding Exercise

Python script to use [Github v3 API](https://developer.github.com/v3/repos/) for displaying the public repositories associated with the user.

If the user has any public repositories associated with their account the program outputs the name and True/False if the repo is forked and archived.

If there are no public repos for a user or the user does not exists, the program states respectively.

## Installation
- Python 3.x
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install library requirements for this program.

```bash
pip install -U -r requirements.txt
```

## Usage

python test.py user

where user is the Github username of the user you want to search for.

```python
>python test.py android
+-----+---------------------+-------+----------+
| SNo |         Name        |  Fork | Archived |
+-----+---------------------+-------+----------+
|  1  |     android-ktx     | False |   True   |
|  2  | android-studio-poet | False |  False   |
|  3  |     android-test    | False |  False   |
|  4  |  android.github.io  | False |  False   |
|  5  |         KEEP        |  True |  False   |
|  6  |    kotlin-guides    | False |   True   |
|  7  |       snippets      | False |  False   |
|  8  |        xAnd11       | False |  False   |
+-----+---------------------+-------+----------+

>python test.py vaibhav19sharma
+-----+---------------------------+-------+----------+
| SNo |            Name           |  Fork | Archived |
+-----+---------------------------+-------+----------+
|  1  | achievementFirst_exercise | False |  False   |
|  2  |      blogify-frontend     | False |  False   |
|  3  |         CS460_660         |  True |  False   |
|  4  |        cs506-f18-a3       |  True |  False   |
|  5  |           CS660           | False |  False   |
|  6  |           CS_660          | False |   True   |
|  7  |       CustomListView      | False |  False   |
|  8  |           dbApp           | False |  False   |
|  9  |           dpApp           | False |  False   |
|  10 |        estuary-api        |  True |  False   |
|  11 |    JARVIS-on-Messenger    |  True |  False   |
|  12 |            Java           |  True |  False   |
|  13 |       LocationSearch      | False |  False   |
|  14 |          logette          | False |  False   |
|  15 |         NumberGame        | False |  False   |
|  16 |      PhotoShare-CS660     |  True |  False   |
|  17 |           Python          |  True |  False   |
|  18 |           RefEd           | False |  False   |
|  19 |      Twitter-Scraping     | False |  False   |
|  20 | vaibhav19sharma.github.io | False |  False   |
|  21 |      youtube-analysis     | False |  False   |
+-----+---------------------------+-------+----------+

>python test.py asasdasdasdasdasd
User not found
```
