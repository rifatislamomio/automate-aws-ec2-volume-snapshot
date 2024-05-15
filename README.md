## Automate EC2 volume creation process

***Steps for simply running this script on any machine:***

_Configure AWS credentials using AWS CLI [(if not configured already)](https://docs.aws.amazon.com/cli/latest/reference/configure/)._

  ```
# install pipenv  (if not already exists)
pip install pipenv

# install dependencies
pipenv install

# run the script
python script.py
```

### Setting Up The Cron Job
For EC2 volume creation automation process, we have to create a Cron job so that the script runs after a certain time automatically.

**Step-0:** Install necessary packages or tools in Linux machine using following command

    sudo apt update
    
    # installing cron
    sudo apt install cron
    
    sudo systemctl enable cron
	
**Step-01:** Run this following command to create a `.cron` file

    sudo nano /etc/cron.d/snapshot.cron

**Step-02:** Write this inside the file

    # script will run in every 20 minutes
    */20 * * * *   ubuntu (user)  python /path/to/script.py
    
    # script will run after system reboot
    @reboot       ubuntu (user) python /path/to/script.py
Custom cron expressions can be generated from [here](https://crontab.guru/).
