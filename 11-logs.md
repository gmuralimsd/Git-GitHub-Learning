# What is git log?
git log displays the history of commits in your repository.
```
echo "Welcome" >> app.txt
git add .
git commit -m "Added welcome message"
```
*Now check history.*
```
git log
```
**Output**
```
commit b73d6c1a72c....
Author: Murali
Date: Tue Jul 16
    Added welcome message
```
`git log` Show full history

*for One line history*

```
git log --oneline
```

**Output**

```
b73d6c1 Added welcome message
4b6e7e9 First commit
```

*It shows Last 3 commits*

```
git log -3
```

*Show changes in each commit*

```
git log -p
```

*Show statistics*

```
git log --stat
```

**output**

```
app.txt | 2 ++
```

# Commit Hash
Every commit has a unique ID.

Git generates it automatically.

```
git log --oneline
```

*Example*

```
6bc912f Fixed login
5f8d1ab Added login page
```

Check commit hash

```
git show 6bc912f
```

**output**

```

8fd45c90b4f80ad5e22b4d71d90cfa14c12ef562

```

This commands r=are used to draw a gragh

```
git log --graph 
git log --graph --oneline --all
```

`git reflog` records every change to where `HEAD` points in your local repository.

```
git reflog
git reflog -5
```
