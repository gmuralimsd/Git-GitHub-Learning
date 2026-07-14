# What is Git?

Git is a Version Control System (VCS) tool that records every change you make to your project so you can track, manage, and restore your work whenever needed.

## Why is Git used?
- Without Git:

  - If you accidentally delete a file, it may be lost.
  - If you make a mistake, you cannot easily return to an older version.
  - If multiple developers work on the same project, files can be overwritten.

- With Git:

  - Every change is saved.
  - You can restore previous versions.
  - Multiple developers can work together safely.
  - You know who changed what and when.


## What is Version Control System (VCS)?

 - VCS stands for Version Control System.
- It is a software tool that tracks changes made to files and source code.
- It stores different versions of a project over time.
- It allows you to restore previous versions if needed.
- It helps multiple developers work together without overwriting each other's changes.
- It keeps a complete history of who changed what and when.
- It is mainly used in software development and DevOps.

### Examples of VCS
1. Git ✅ (Most popular)
2. SVN (Subversion)
3. CVS
4. Mercurial


## Types of Version Control System (VCS)

There are 3 main types of Version Control Systems.

**1. Local Version Control System (LVCS)**
   - Stores versions only on your local computer.
   - Used by one user.
   - No collaboration with others.
   - If your computer crashes, you may lose all version history.

**2. Centralized Version Control System (CVCS)**
- Stores the project in one central server.
- Multiple developers connect to the same server.
- Users must connect to the server to get or upload changes.
- If the server goes down, work may be interrupted.

**3. Distributed Version Control System (DVCS)**
- Every developer has a complete copy of the repository.
- Developers can work offline.
- Changes are shared with a remote repository (such as GitHub) when ready.
- Faster, more reliable, and the most widely used today.

## Git Architecture

          Working Directory (local)
                 │
              git add
                 │
                 ▼
            Staging Area
                 │
             git commit
                 │
                 ▼
           Local Repository
                 │
             git push
                 │
                 ▼
        Remote Repository (GitHub)
