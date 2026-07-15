# Git instalation in ubuntu instance
### **Step 1: Create a directory**
   - Create a folder with a name of project
   - And change the directory
     ```bash
     sudo apt update -y
     mkdir <folder-name>
     cd <folder-name>
     ```

### **Step 2: install git**
   - Install git and check the version 
     ```bash
     sudo apt install git 
     git --version
     ```
---
# Configuration
### **Step 1: Set User Information**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.editor "editor name"
```

**example**
```bash
git config --global user.name "gmurali"
git config --global user.email "gmurali.msd@gmail.com"
git config --global core.editor "vs code"
```

---

### **Step 2: Check Configuration**

```bash
git config --global --list
```

**output**
```bash
user.name=gmurali
user.email=gmurali.msd@gmail.com
core.editor=vs code
```

### **Step 3: Remove Configuration**

```bash
git config --global --unset user.name
git config --global --unset user.email
git config --global --unset core.editor
```
