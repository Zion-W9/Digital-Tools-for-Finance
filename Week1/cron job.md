For this task, we use the sudo command to temporarily elevate the user's privileges, allowing users to complete sensitive tasks without logging in as the root user.

To execute script runner.sh 'hello'" every second day at 17:00, we use crontab execute scheduled commands.
```
sudo crontab -e <your_username>
0 17 */5 * * ./runner.sh 'hello' >/dev/null 2>&1
```

