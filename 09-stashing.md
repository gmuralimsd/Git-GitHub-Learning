# What is Git Stash?
Git Stash is a Git feature that temporarily saves your uncommitted changes and makes your working directory clean.
Later, you can bring those changes back.`  OR  `
Git Stash temporarily hides your unfinished work so you can work on something else.

---

### Why do we use Git Stash?

- Work is not finished
- Need to switch branches
- Need to fix urgent bugs
- Don't want to create unnecessary commits
- Want a clean working directory

---

Before going to Create Stash cretae file and modefy it 
```
echo "Welcome to Git" > readme.txt

```
Now modefy it 
```
echo "Welcome to Git and GitHub" > readme.txt

```
Now check the status
```
git status

```
Output
```
modified: readme.txt
```
---
Now stash them. for that we have to commands 
```
git stash                                          -----it stash all without msg------
git stash push -m "Login page changes"             -----it stash all with msg------

```
**Output**
```
Saved working directory and index state
```

*Now check status.*
```
git status
```

*Output*
```
nothing to commit, working tree clean

Your changes are safely stored.
```
---
This command is used to check the all stashes
```
git stash list
```
***Output***
```
stash@{0}: On main: Login page changes

stash@{1}: On main: Navbar update
```
stash@{0}  ----> Means newest stash

stash@{1}  ----> Means older stash

stash@{2}  ----> Means even older stash

---
### This command is used to restores the latest stash.
```
git stash apply
```
**output**
```
readme.txt     ← Restored

```

> After
> git stash apply
> The stash still exists.

Example
```
git stash list
```

***Output***
```
stash@{0}

It is not deleted.
```
Apply Specific Stash
```
git stash apply stash@{0}
git stash apply stash@{1}
git stash apply stash@{2}
```

Thes command does to things ar a time
- Restores the stash
- Deletes the stash
  
```
git stash pop
```
For delete a specific stash
```
git stash drop stash@{0}
```
for delete all stash at a time
```
git stash clear
```
***Output***
```
All stashes removed
```
# Git stash work flow
```
 Modify Files

      ↓

  git stash

      ↓

Working directory
 becomes clean

      ↓

Switch Branch

      ↓

Complete another
     task

      ↓

  Come back

      ↓

git stash apply
     or
git stash pop

      ↓

Continue work
```
