alice:
- set up
```
  mkdir week4 
```
- in 'test-alice' create file 'functions.txt', write 'THIS LINE IS OK' in it, add+commit+push
```
 code .\week4\functions.txt
 git add .
 git commit -m "alice create functions.txt"
 git push
 ```

bob:
- pull (nb branch)
```
git pull
```
- change line #1 to 'THIS LINE IS BAD'
- pull (nothing changes)
```
git pull
```
- add+commit+push
```
 git add .
 git commit -m "bob change line #1"
 git push
 ```

alice:
- add another line 'THIS #2 LINE IS OK', change line #1 to 'THIS LINE IS STILL OK'
- pull (should fail, need to commit the changes first)
```
git pull

error: Your local changes to the following files would be overwritten by merge:
        week4/test-alice/functions.txt
Please commit your changes or stash them before you merge.
```
- add+commit
```
 git add .
 git commit -m "alice change line #1 and #2"
 ```
- pull, resolve conflicts by accepting line 1 from bob and line 2 from self
```
git pull
```
- commit+push
```
 git add .
 git commit -m "alice resolve conflict"
 git push
 ```

bob:
- git log to see identity of commits
```
git log
```
- pull (should see two lines)
```
git pull
```
- want to continue working on the first line until it is ok
- create a new branch 'feature-1'
```
git branch feature-1
git checkout feature-1
```
- change line #1 to 'THIS LINE WAS BAD BUT NOW IS OK'
- add+commit+push
```
 git add .
 git commit -m "bob new branch"
 git push
 ```

alice:
- pull without switching branches (nothing changes)
```
git pull
```

bob:
- change line #1 to 'THIS LINE IS FINALLY OK'
- add+commit+push
```
 git add .
 git commit -m "bob finally ok"
 git push
 ```
- open pull request
```
git pull
```

alice:
- checkout
```
git checkout feature-1
```
- merge branch into main
```
git checkout feature-1
git pull
git checkout Homework
git merge feature-1
```
- push
```
git push
```

bob:
- pull
```
git pull
```