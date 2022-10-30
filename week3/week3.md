## Questions
1. Install Git;
1. Create an account on Github (or use an existing if you want);
1. Set up a local repository in your project folder;
2. Create folder `homework/week3`;
3. Within it, create the following two folders and two files:

```bash
data/
text/
notes.txt
functions.py
```

and exclude folder `data/` from being tracked;

## Solutions
```
#create two folders and two files
mkdir data/
mkdir text/
echo '' > notes.txt
echo '' > functions.py

#exclude data/ from being tracked
touch .gitignore
vi .gitignore

```

## Questions
1. Add and commit everything;
1. Add line reading 'THIS IS FINE' to `notes.txt`, commit the new version with message 'a fine change';
1. Change that line to 'THIS IS GOOD', commit the new version with message 'a good change' *overwriting the previous commit* as if it never happened (make sure `git log` does not show 'a fine change');
1. Change that line to 'THIS IS BAD', save the file and close the editor to make it impossible to use `Ctrl+Z`;
1. Try to restore `notes.txt` to the state where it reads 'THIS IS GOOD';
1. Change that line to 'THIS IS THE BEST' and delete file `functions.py`, commit your changes giving your commit a name such as 'first-working';
1. Undo the previous commit using `git revert`, makes sure `functions.py` does exist and the line reads 'THIS IS GOOD';
1. Create a remote repo on Github/Bitbucket and link your local repo to it;
1. Push all the commits to the remote;
1. Try to revert `notes.txt` to the state where it reads 'THIS IS FINE' keeping all the other changes in place;
1. Commit everything pending and push to the remote;
1. Commit and push the previous homework.


## Solutions
1. Add and commit everything;
```
git add.
git commit -m "initial commit"
```

2.Add line reading 'THIS IS FINE' to `notes.txt`, commit the new version with message 'a fine change';
```
vi notes.txt
git add notes.txt
git commit -m "a fine change"
```

3. Change that line to 'THIS IS GOOD', commit the new version with message 'a good change' *overwriting the previous commit* as if it never happened (make sure `git log` does not show 'a fine change');
```
vi notes.txt
git add notes.txt
git commit --amend -m "a good change"
#check
git log
```
4. Change that line to 'THIS IS BAD', save the file and close the editor to make it impossible to use `Ctrl+Z`;
```
vi notes.txt
#close the editor
```
5. Try to restore `notes.txt` to the state where it reads 'THIS IS GOOD';
```
git restore notes.txt
```
6. Change that line to 'THIS IS THE BEST' and delete file `functions.py`, commit your changes giving your commit a name such as 'first-working';
```
#change the line to "THIS IS THE BEST"
vi notes.txt

#delete file 'functions.py'
rm functions.py

#commit changes and giving the commit a name
git add .
git commit -m "first-working"
```

7. Undo the previous commit using `git revert`, makes sure `functions.py` does exist and the line reads 'THIS IS GOOD';
```
git revert 
```
8. Create a remote repo on Github/Bitbucket and link your local repo to it;
9. Push all the commits to the remote;
```
git remote add origin <url>
git push -u origin master
```
10. Try to revert `notes.txt` to the state where it reads 'THIS IS FINE' keeping all the other changes in place;
```
git log
git revert <sha> notes.txt
```
11. Commit everything pending and push to the remote;
```
git add .
git commit -m "final commit"
git push -u orgin master
```
12. Commit and push the previous homework.
