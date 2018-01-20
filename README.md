
# Log Analysis

## This project answers to the following questions using sql

* Most popular articles of all time
* Most popular authors of all time
* Date on which more than 1% requests lead to errors

## To know answers follow the instructions

**_Meeting the Requirements_**
---
1. **Configure virtual machine using vagrant**
* Download vagrant from [here](https://www.vagrantup.com/downloads.html)
* Download configuration files from [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* Extract those files in a folder then open git bash in the folder.
* Run `vagarant up` in git bash.
* Then run `winpty vagrant ssh` or `vagrant ssh` to login.
* Now you have up and runnig postgresql in your system with python3 and newly created database **_news_**.

2. **Tables and necessary python libraries.**
* cd into vagrant by running `cd /vagrant`.
* Run `sudo apt-get install psycopg2` if not installed.
* To create all the necessary tables download the `newsdata.sql` file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
* Then run this command `psql -d news -f newsdata.sql`.

**_Run Log Analysis_**
---
1. **Clone or download the zip file of the repository.**
1. **Extract the files in a folder.**
1. **Open git bash in the folder.**
1. **Now to obtain the analysis run `python3 reporting_tool.py` or `.\reporting_tool.py`.**
1. **Open the following text files to see the output.**
* `popular_articles.txt`
* `popular_authors.txt`
* `status.txt`