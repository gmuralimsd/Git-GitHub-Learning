# What is a Branch?

A branch in git is simple a moveble pointer to a spesific commit it allows to u diverse from main line of development ans work in isolation 
without effecting the main code until you ready

or 

A branch is a separate line of development in Git.

It lets you work on new features, fix bugs, or test ideas without changing the main project.


A branch is a copy of your project where you can work safely without affecting the main branch.

## Why Do We Use Branches?

- Add new features safely
- Fix bugs without affecting the main project
- Test new ideas
- Allow many developers to work at the same time
- Keep the main project stable


# 1. What is Branching?

Branching means creating a separate line of development in a Git repository.

A branch lets you work on new features or fix bugs without affecting the main project.

Think of it as making a copy of your work where you can safely make changes.

**Example**
```
Main Project
     │
     │
     ▼
    main

Create a branch:

        main
          │
          │
     ─────┼─────
          │
    feature-login
```

### What is a Branch?

- A branch is a pointer to the latest commit.
- Every branch has its own commits.
- When you create a branch, Git does not copy the entire project.
- It simply creates another pointer.

Current branch is `main`


**Create Branch**

```
git branch< branch-name >

Example

git branch login
```

You are still on main.

***Check***
```
git branch
```
Output

*main
 
 login


### Show all branches
```
git branch -a

```

**Move from one branch to another.**

```
git switch <branch-name>

Example

git switch login

```

Create and switch together
```
git switch -c <branch-name>
git checkout -b <branch-name>

```

Rename another branch
```
git branch -m <old-name> <new-name>

Example

git branch -m main login
```

for delete a Branch
```
git branch -d <login>

```
Git checks whether the branch is merged.

If merged

Deleted branch login.

Force delete
```
git branch -D login
```

We Cannot delete current branch

```
git branch -d main

Switch first

git switch login

Then

git branch -d main
```

### Merge Branch

Merge means combine one branch into another.

At the time of merging we must switch to `main` branch  
```
git switch main

git merge login
```

# All Commands Togethe
```
# Check current branch
git branch

# Create a new branch
git branch login

# Switch to the new branch
git switch login

# Make changes to your files

# Check status
git status

# Stage changes
git add .

# Commit changes
git commit -m "Added login button"

# Switch back to main
git switch main

# Merge the login branch
git merge login

# View commit history
git log --oneline

# Delete the merged branch
git branch -d login

```
# Why is it called "Three-Way-Merge"?

- Git compares three commits:
   - The common ancestor (where the branches split)
    - The latest commit on the current branch
    - The latest commit on the branch being merged

Using these three points, Git decides how to combine the changes.


## What is commit id ?

1. A commit is a saved snapshot of your project at a specific point in time.
2. It stores all the changes you have added to the staging area.
3. Every commit has a unique ID (hash) to identify it.
4. A commit should include a clear message describing the changes.
5. Create a commit using the command: `git commit -m "Your commit message"`


**# use this command for all commits**

```git log
```

output

```
commit ae628ab9ff55ece8c984580f976f0d07bf6dad1e (HEAD -> main, origin2/main, origin/main)
Author: gmurali <gmurali.msd@gmail.com>
Date:   Wed Jul 15 09:28:02 2026 +0000

    modefied

commit 03b432f02fa4c193961a85d4a6f793d7b0e919c6
Author: gmurali <gmurali.msd@gmail.com>
Date:   Wed Jul 15 09:07:56 2026 +0000

    added readme

commit 1f56b29f6f08a3ea13368aadc893800d9ab7f437
Author: gmurali <gmurali.msd@gmail.com>
Date:   Wed Jul 15 08:52:20 2026 +0000

    first commit
```

**# use this command for all compresh commits**
```
git log --online
```

output

```
ae628ab (HEAD -> main, origin2/main, origin/main) modefied
03b432f added readme
1f56b29 first commit
```

**# use this command for latest commit**

```
commit ae628ab9ff55ece8c984580f976f0d07bf6dad1e (HEAD -> main, origin2/main, origin/main)
Author: gmurali <gmurali.msd@gmail.com>
Date:   Wed Jul 15 09:28:02 2026 +0000

    modefied
```
