# # What is Git Ignore?

Git Ignore is a feature that tells Git to ignore specific files and folders.
### Why do we use .gitignore?

Some files are:
- Temporary
- Automatically generated
- Personal
- Secret
These should not be uploaded to GitHub


***To ignore a single file, you need to add the file name to the .gitignore file.***

```
nano .gitignore
password.txt
Ctrl + O → Enter
Ctrl + X
```

***Ignore a file inside a folder***
```
vi .gitignore
folde/file
config/database.txt
```
***If file is at staged area git cann't ignore the file or folder***
for the use below command 
```
git rm --cached password.txt
git commit -m "Stop tracking password.txt"
```
Now git will ignore the file 

**to gitignore multiple file at a time**
Create a file with a name of `.gitignore` and type bellow 
```
# Ignore log files
*.log

# Ignore Python cache
__pycache__/

# Ignore virtual environment
venv/

# Ignore environment file
.env
```
