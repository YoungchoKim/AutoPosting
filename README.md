### AutoPosting
- AutoPosting was developed to automatically post the contents of a repository linked to Leethub to tistory.
- Using llm, we post a summary of the Leetcode problem, how to approach the problem, time complexity of the code, and code explanation.


![AutoPostingStructure_](https://github.com/user-attachments/assets/d37b097c-06ea-41b3-a92c-847ffc2c4485)



### Post Table
```
mysql> desc Post;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int          | NO   | PRI | NULL    | auto_increment |
| problem_name | varchar(256) | NO   |     | NULL    |                |
| daily_date   | datetime     | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```

### config_template.json
- need to rename config.json
```json
{
  "tistory": {
    "username": "",   # your kakao id for tistory login
    "password": "",   # your kakao password for tistory login
    "tistory_url": "" # your tistory url. ex) xxx.tistory.com
  },
  "database": {
    "host": "",          # your mysql address ex) localhost
    "port": 0,           # ex) 3306
    "user": "",          # your mysql id
    "password": "",      # your mysql password
    "database_name": ""  # your database name
  },
  "github": {
    "owner": "", # github username. It is in your github link.
    "repo": "",  # repository should be connected to Leethub 
    "token": ""  # your github token. It is related to API request limits.
  }
}
```
