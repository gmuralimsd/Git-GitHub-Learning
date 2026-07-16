# Cherry Pick

Copy one specific commit from one branch and apply it to another branch.
Instead of merging the entire branch, you copy only the commit you need.


### Why use Cherry Pick?

**Imagine:**

Feature branch has 20 commits.
Only 1 commit fixes an important bug.

See commit IDs

git log --oneline

**output**

8a3b2f1 Added Login

4d8e123 Fixed Navbar

6f912ab Updated README

Copy commit ID

Switch to target branch

git checkout main

Run Cherry Pick
```
git cherry-pick 4d8e123
````
Done.

That commit now exists in main.

If Conflict Happens

Fix the conflict.

Then

git add .
git cherry-pick --continue

Cancel Cherry Pick

git cherry-pick --abort

# Rebase
What is Rebase?

Rebase means:

Move your branch on top of another branch.

Instead of creating a merge commit, Git replays your commits.

Before Rebase
main

A --- B --- C

feature

      D --- E

Meanwhile

main

A --- B --- C --- F

Your feature branch is behind.

Instead of Merge

git merge main

Use

git rebase main

Git does

A --- B --- C --- F --- D --- E

Notice

There is no merge commit.

History becomes clean.

Syntax
git checkout feature

git rebase main
Why use Rebase?

Advantages

Cleaner history
No unnecessary merge commits
Easier to understand project history
Preferred before Pull Requests in many companies
If Conflict Happens

Resolve conflict

git add .

Continue

git rebase --continue

Cancel

git rebase --abort
