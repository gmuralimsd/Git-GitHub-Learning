# Git Commands Cheat Sheet

A complete list of commonly used Git commands with examples.

---

# 1. Check Git Version

```bash
git --version
```

Example:
```bash
git --version
```

Output:
```
git version 2.50.1
```

---

# 2. Configure Username

```bash
git config --global user.name "Murali"
```

Example:

```bash
git config --global user.name "John Doe"
```

---

# 3. Configure Email

```bash
git config --global user.email "murali@gmail.com"
```

Example:

```bash
git config --global user.email "john@gmail.com"
```

---

# 4. Check Configuration

```bash
git config --list
```

---

# 5. Initialize Git Repository

```bash
git init
```

Example:

```bash
mkdir MyProject
cd MyProject
git init
```

---

# 6. Check Repository Status

```bash
git status
```

---

# 7. View Files

```bash
dir
```

Linux/Mac:

```bash
ls
```

---

# 8. Add Single File

```bash
git add index.html
```

---

# 9. Add Multiple Files

```bash
git add file1.txt file2.txt
```

---

# 10. Add All Files

```bash
git add .
```

---

# 11. Commit Changes

```bash
git commit -m "Initial Commit"
```

---

# 12. View Commit History

```bash
git log
```

Short Version

```bash
git log --oneline
```

---

# 13. Rename Branch

```bash
git branch -M main
```

---

# 14. View Branches

```bash
git branch
```

---

# 15. Create New Branch

```bash
git branch dev
```

---

# 16. Switch Branch

```bash
git checkout dev
```

OR

```bash
git switch dev
```

---

# 17. Create and Switch Branch

```bash
git checkout -b feature
```

OR

```bash
git switch -c feature
```

---

# 18. Merge Branch

```bash
git checkout main
git merge dev
```

---

# 19. Delete Branch

```bash
git branch -d dev
```

Force Delete

```bash
git branch -D dev
```

---

# 20. Connect GitHub Repository

```bash
git remote add origin https://github.com/username/repository.git
```

Check Remote

```bash
git remote -v
```

---

# 21. Change Remote URL

```bash
git remote set-url origin https://github.com/username/newrepo.git
```

---

# 22. Push Code

First Time

```bash
git push -u origin main
```

Next Time

```bash
git push
```

---

# 23. Clone Repository

```bash
git clone https://github.com/username/repository.git
```

---

# 24. Download Latest Changes

```bash
git pull origin main
```

---

# 25. Fetch Changes

```bash
git fetch
```

---

# 26. Compare Changes

```bash
git diff
```

---

# 27. Show Staged Changes

```bash
git diff --staged
```

---

# 28. Remove File from Staging

```bash
git restore --staged filename.txt
```

---

# 29. Restore File

```bash
git restore filename.txt
```

---

# 30. Remove File

```bash
git rm filename.txt
```

---

# 31. Remove Cached File

```bash
git rm --cached filename.txt
```

---

# 32. Create Tag

```bash
git tag v1.0
```

---

# 33. List Tags

```bash
git tag
```

---

# 34. Push Tag

```bash
git push origin v1.0
```

---

# 35. Stash Changes

```bash
git stash
```

View Stash

```bash
git stash list
```

Restore

```bash
git stash pop
```

---

# 36. Show Remote Repository

```bash
git remote -v
```

---

# 37. Remove Remote

```bash
git remote remove origin
```

---

# 38. Check Current Branch

```bash
git branch --show-current
```

---

# 39. Show Commit Details

```bash
git show
```

---

# 40. Reset Last Commit (Keep Changes)

```bash
git reset --soft HEAD~1
```

---

# 41. Reset Last Commit (Delete Changes)

```bash
git reset --hard HEAD~1
```

---

# 42. Revert Commit

```bash
git revert HEAD
```

---

# 43. Clean Untracked Files

```bash
git clean -f
```

---

# 44. Show Working Tree

```bash
git status
```

---

# 45. Show Repository Information

```bash
git remote show origin
```

---

# Complete Git Workflow

## Step 1

```bash
git init
```

## Step 2

```bash
git add .
```

## Step 3

```bash
git commit -m "Initial Commit"
```

## Step 4

```bash
git branch -M main
```

## Step 5

```bash
git remote add origin https://github.com/username/repository.git
```

## Step 6

```bash
git push -u origin main
```

---

# Daily Git Workflow

```bash
git status
git add .
git commit -m "Updated project"
git push
```

---

# Clone Existing Repository

```bash
git clone https://github.com/username/repository.git

cd repository

git pull

git add .

git commit -m "Added new feature"

git push
```

---

# Useful Shortcuts

| Command | Description |
|----------|-------------|
| git status | Check repository status |
| git add . | Stage all files |
| git commit -m "msg" | Commit changes |
| git push | Upload code |
| git pull | Download latest changes |
| git clone URL | Download repository |
| git log --oneline | Short commit history |
| git branch | Show branches |
| git checkout branch | Switch branch |
| git merge branch | Merge branch |
| git stash | Save temporary work |
| git fetch | Download updates |
| git diff | Compare changes |
| git remote -v | Show remote URL |
| git tag | List tags |

---

# Common Git Command Sequence

```bash
git status
git add .
git commit -m "Added new feature"
git push
```
