#Requirements#

python
python-pip



#Instalation#

**Clone the repository**

**Install python libraries**

`pip install -r requirements.txt`



#Configuration#

Edit the `settings.py_dist` file and configure the parameters

*server*: The server ip or address

*port*: The elasticsearh port

*indices*: An array with the indices to backup

*repository_name*: The name of the repository **The repository must exists in elasticsearch, this script don't create it**

*snapshots_to_store*: The number of snapshot to store **When the current amount of snapshots exceeds, the script deletes the first snapshots**

Rename the file `settings.py_dist` to `settings.py`



#Usage#

Execute the script `esbackup.py`

Add the scrip execution in a cron job.
