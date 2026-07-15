# 1. GitHub Introduction
### What is GitHub?

GitHub is a website where you store Git repositories online.

**Website:**
```
https://github.com
```
### Why use GitHub?
1. Backup your code
2. Share code
3. Work with teams
4. Track changes
5. Open Source projects
6. Portfolio for jobs

# What is a Remote Repository? (github)


A Remote Repository is a Git repository that is stored online instead of on your computer.

- Store your code safely on the internet.
- Share your project with others.
- Work with a team.
- Access your code from anywhere.

***Architecture***
```
          Internet
             │
             ▼
   Remote Repository (GitHub)
             ▲
             │
     git push / git pull
             │
             ▼
      Local Repository
       (my Computer)

```



# 3. Create Remote Repository

A Remote Repository is usually created on GitHub.


**Step 1**
```
https://github.com
```
**Step 2**
```
Login to GitHub.
```
**Step 3**
```
click on
New Repository
```
**Step 4**
```
Enter

Repository Name
Ex : Git-Learning
Choose
Public
or
Private
```
**Step 5**
```
Click
Create Repository
Done!
```

Now you have a Remote Repository.

# 4. Connect Local Repository to GitHub

- echo "# practice-" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/gmuralimsd/practice-.git
- git push -u origin main


### this commands use for pull the project
- git remote add origin https://github.com/gmuralimsd/practice-.git
- git branch -M main
- git push -u origin main
