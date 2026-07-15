
# What is File Lifecycle?

File Lifecycle is the journey of a file from the time you create it until it is permanently saved in Git.

# 1. Working Directory

The Working Directory is the folder where you create, edit, rename, and delete files.

It is the place where you normally work.

**syntax**
```
mkdir < file-name >
```
**Example**
```
mkdir index.html
```
# 2. Untracked Files

An Untracked File is a new file that Git does not know about yet.

index.html

Git has never tracked this file.

# 3. Staging Area

The Staging Area is a temporary place where Git keeps files that are ready to be committed.

**Syntax**
```
git add <file-name>
```

***Example***
```
git add index.html
```
Now the file moves to the Staging Area.


# 4. Local Repository

The Local Repository is where Git permanently saves your project history on your computer.

Every commit is stored here.

**Syntax**
```
git commit -m "Added homepage"
```

Now Git saves the file permanently.

# 5. Tracked Files

A Tracked File is a file that Git already knows about.

Git watches every change made to it.

***Example***
```
git add app.py
git commit -m "Added app.py"

```

Now app.py becomes a tracked file.

# 6. Modified File

A Modified File is a tracked file that has been changed after the last commit.

Git knows the file has changed, but the changes are not yet staged.

# 7. Staged Files

A Staged File is a modified file that has been added to the Staging Area.

It is ready to be committed.

**Example**
```
git add index.html

```

Now the file is staged.


# Complete File Lifecycle

```
New File {mkdir index.html}
          │
    Untracked File 
          │
          ▼
git add {git add index.html}
          │
      Staged File
          │
          ▼
git commit {git commit -m "msg"}
          │
    Tracked File
          │
          ▼
Edit File {vi index.html}
          │
     Modified File
          │
          ▼
git add {git add index.html}
          │    
     Staged File
          │
          ▼
git commit {git commit -m "msg"}
          │
Tracked File (Updated)
```
