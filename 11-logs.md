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
