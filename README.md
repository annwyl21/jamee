# Friends (JAMEE created by Jaya, Abigail, Michelle, Eyasmin & Ellen)
A website / dashboard for personal financial tracking and managements of debt repayment.

- Install the requirements
```bash
pip install -r requirements.txt
```
- Create the database in MySql using the script: `application/static/scripts/jamee_user_database.sql`
- Run the app.py file to start the site locally
```bash
python -m flask run
```

# Problem-Solving

- Is flask started?
- Have you got the correct databse, no duplicates or old versions of the database?
    - Our Database code is held in Static/ Scripts
        - run `teardown_script.sql` to drop old versions of the database
        - run `jamee_user_database.sql` to rebuild the new database

