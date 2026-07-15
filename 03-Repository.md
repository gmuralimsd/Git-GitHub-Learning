# 1. What is a Repository?
A Repository (Repo) is a place where Git stores your project files and keeps track of every

change you make or 
A repository is a folder that contains your project and its history.

### Why is it needed?

- Stores project files
- Tracks every change
- Allows teamwork
- Lets you go back to older versions
- Keeps project safe

# 2. Local Repository

A Local Repository is a repository stored on your own computer.


It is the project that exists only on your laptop or desktop.


### Why is it needed?
- Work offline
- Save changes
- Test code safely
- Fast development

# 3. Remote Repository

A Remote Repository is a repository stored on the internet.

### Why is it needed?
- Share code
- Backup project
- Work with team
- Access from anywhere



# 4. Initialize Repository (git init)

git init creates a new Git repository.

It tells Git "Start tracking this project."


```bash
Project/
│
├── index.html
└── style.css
```
**Syntax**

```bash
git init
```

This command creates a new Git repository

```
Project/
│
├── .git
├── index.html
└── style.css
```

# 5. Clone Repository (git clone)

git clone copies an existing repository from a remote server (such as GitHub) to your computer.

It downloads a project from GitHub to your computer.

***Syntax***
```
git clone <repository-url>
```
**Example**
```
git clone https://github.com/gmuralimsd/Git-GitHub-Learning/edit/master/03-Repository.md

```
