### create directory temp/;
```
mkdir temp
```

### change working directory to temp/ (assuming temp/ exists);
```
cd temp
```

### write 'hello world' to file called hello.txt;
```
echo "hello world" > hello.txt
```

### list all files and folders in the parent folder of temp/;
```
ls -la ..
```

### list all currently processes running;
```
ps -A
```

### kill process with ID 666;
```
kill 666
```

### write the contents of environment variable to file $PATHpath.txt;
```
echo $PATH >> path.txt
```

### find file 'hello.txt' in the parent of the current directory;
```
ls .. | grep hello.txt
```

### find all files in your home directory and subdirectories;
```
ls -R | grep '\.png$'
```

### find where the executable of command is located;
```
whereis echo
```

### find text 'Select all processes' in the manual of command (that is, in the output of command psman ps);
```
man ps | grep "Select all processes"
```

### write the last 20 commands you've executed to file .commands.txt
```
history 20 >> commands.txt
```