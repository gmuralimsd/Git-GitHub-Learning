# #.Cherry Pick

Copy one specific commit from one branch and apply it to another branch.
Instead of merging the entire branch, you copy only the commit you need.


### Why use Cherry Pick?
Feature branch has 20 commits.
Only 1 commit fixes an important bug.
```
git log --oneline
```
**output**

8a3b2f1 Added Login

4d8e123 Fixed Navbar

6f912ab Updated README


Run Cherry Pick
```
git cherry-pick 4d8e123
````

> If Conflict Happens
> Fix the conflict.

Then
```
git add .
git cherry-pick --continue
```
Cancel Cherry Pick
```
git cherry-pick --abort
```
# #.Rebase
Move your branch on top of another branch.

Instead of creating a merge commit, Git replays your commits.

```
git checkout feature

git rebase main
```

> If Conflict Happens
> Resolve conflict
```
git add .
git rebase --continue
```

Cancel
```
git rebase --abort
```
