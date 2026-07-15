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

* main
  login

* means current branch.

List Branches

Command

git branch

Example

* main
  login
  payment
  profile

Current branch

* main

Show all branches

git branch -a

Shows

Local branches
Remote branches

Example

* main
  login
  remotes/origin/main
  remotes/origin/login
Switch Branch

Move from one branch to another.

Command

git switch branch-name

Example

git switch login

Older command

git checkout login

Before switching

* main
  login

After

  main
* login

Shortcut

Create and switch together

git switch -c login

Older method

git checkout -b login
Rename Branch

Current branch

git branch -m new-name

Example

login

Rename

git branch -m login-page

Result

login-page

Rename another branch

git branch -m old-name new-name

Example

git branch -m login authentication
Delete Branch

Delete merged branch

git branch -d login

Git checks whether the branch is merged.

If merged

Deleted branch login.

Force delete

git branch -D login

Use only if you really want to delete unmerged work.

Cannot delete current branch

Wrong

git branch -d main

Switch first

git switch login

Then

git branch -d main
Merge Branch

Merge means combine one branch into another.

Example

main

A → B

login

A → B → C → D

Merge

git switch main
git merge login

Result

main

A → B → C → D
Merge Process
Step 1

Current project

main

A → B
Step 2

Create branch

main

A → B

      \
       login
Step 3

Work on login

main

A → B

      \
       C → D
Step 4

Merge

main

A → B → C → D
Fast Forward Merge
What is it?

A Fast Forward Merge happens when the target branch has not changed after the new branch was created.

Git simply moves the branch pointer forward.

No merge commit is created.

Example

main

A → B

Create login

A → B

        \
         C → D

Main has no new commits.

Merge

git switch main
git merge login

Result

A → B → C → D

Git simply moves main to the latest commit.

Visualization

Before

main

A → B

        \
         C → D

After

main

A → B → C → D

No extra merge commit.

Advantages

Clean history
Simple
Easy to understand
No unnecessary merge commit
Three-Way Merge
What is it?

A Three-Way Merge happens when both branches have new commits after they split.

Git combines the histories and creates a new merge commit.

Example

Start

A → B

Create branch

main

A → B

        \
         login

Developer 1 on main

A → B → E

Developer 2 on login

A → B → C → D

Now merge.

Git creates a merge commit.

          C → D
         /      \
A → B → E ------- M

M is the merge commit.

Command

git switch main
git merge login

Why is it called "Three-Way"?

Git compares three commits:

The common ancestor (where the branches split)
The latest commit on the current branch
The latest commit on the branch being merged

Using these three points, Git decides how to combine the changes.
