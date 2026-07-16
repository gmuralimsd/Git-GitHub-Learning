# Merge Conflicts
### What is a Merge Conflict?

A merge conflict happens when Git cannot decide which changes to keep because

the same part of the same file was changed in different branches.

Git asks you to choose the correct version.

***Example**

Suppose `index.html `contains
```
<h1>Welcome</h1>
```
On main branch

You change it to
```
<h1>Welcome to My Website</h1>
```
Commit it.

On **feature** branch

You change the same line to
```
<h1>Hello Everyone</h1>
```
Commit it.

Now return to the `main` branch 
```
git merge feature
```
Git cannot decide which heading is correct.

***Result:***
```
CONFLICT (content): Merge conflict in index.html
Automatic merge failed.
3. Resolve Conflicts
```
Git marks the conflicting file like this:
```
Meaning
<<<<<<< HEAD

Current branch (main)

=======

Separator

>>>>>>> feature
```
Incoming changes from the feature branch

# How do you resolve a merge conflict?

Answer: Open the conflicted file, choose or combine the correct changes, 

remove the conflict markers (<<<<<<<, =======, >>>>>>>), save the file, then run:
```
git add .
git commit -m "Resolved merge conflict"
```
flow chart

```
Merge Branch
      │
      ▼
Conflict Found
      │
      ▼
Open File
      │
      ▼
Edit the File
(Remove <<<<<<< ======= >>>>>>>)
      │
      ▼
Save File
      │
      ▼
git add .
      │
      ▼
git commit
      │
      ▼
git push
```

### How do you cancel a merge?
```
git merge --abort

```

Abort = Cancel the merge using git merge --abort.
