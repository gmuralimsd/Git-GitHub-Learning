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

How to Resolve
Option 1: Keep current branch
<h1>Welcome to My Website</h1>
Option 2: Keep feature branch
Option 3: Combine both
<h1>Welcome to My Website - Hello Everyone</h1>
Save the file

Then stage it

git add index.html

Finish the merge

git commit -m "Resolved merge conflict"
Push changes
git push origin main
Conflict Resolution Flow
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
4. Abort Merge
What is Abort Merge?

If a merge goes wrong or you don't want to continue, you can cancel the merge and return to the state before the merge started.

Command
git merge --abort
Example

Start merging

git merge feature

Git reports conflicts.

You decide not to continue.

Run

git merge --abort

Git restores the branch to its previous state.

When to Use
You merged the wrong branch.
Too many conflicts.
You want to try again later.
You don't want to resolve the conflicts now.
Important Commands
Purpose	Command
Merge branch	git merge feature
Check current branch	git branch
Switch branch	git switch main
View merge conflicts	Open the conflicted file
Stage resolved file	git add <file>
Complete merge	git commit -m "Resolved merge conflict"
Abort merge	git merge --abort
Push merged code	git push origin main
Interview Questions
1. What is a merge in Git?

Answer: Merge combines changes from one branch into another branch.

2. What is a merge conflict?

Answer: A merge conflict occurs when the same part of the same file is modified in different branches and Git cannot automatically combine the changes.

3. How do you merge a branch?
git switch main
git merge feature
4. How do you resolve a merge conflict?

Answer: Open the conflicted file, choose or combine the correct changes, remove the conflict markers (<<<<<<<, =======, >>>>>>>), save the file, then run:

git add .
git commit -m "Resolved merge conflict"
5. How do you cancel a merge?
git merge --abort
Easy Formula to Remember
Merge = Combine two branches.
Conflict = Same line changed in both branches.
Resolve = Edit the file, keep the correct code, git add, then git commit.
Abort = Cancel the merge using git merge --abort.
