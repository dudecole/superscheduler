# Super Scheduler
This is a basic scheduler to help Superintendent's of Builders be 
able to track their regular schedules, jobs, and their contractors
schedules.  

Concept is when one contractor is delayed, anything scheduled after
will automatically adjust the new date, while also excluding weekends. 


Create Virtual Env:   

    $ virtualenv .env

Activate Virtual Env

    $ source .env/bin/activate

Install requirements

    $ pip install -r requirements.txt

Run Super Scheduler

`$ python superscheduler.py`
