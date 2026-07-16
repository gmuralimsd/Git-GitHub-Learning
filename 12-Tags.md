# What is a Tag ?

A Tag is a permanent label given to a specific commit.

Tags are two types 

1. Lightweight Tag
2. Annotated Tag

Create tag and atach to the commite
```
git log --oneline
git tag v1.0
git tag v1.0 2f8b1ad

```
*output*

```
v1.0
```

2. Annotated Tag
Definition


Create Annotated Tag
```
git tag -a v1.0 -m "First Stable Release"

```

-a = Create Annotated Tag

-m = Message

View Tag Details
```
git show v1.0
```
**output**
```
tag v1.0
Tagger: Murali
Date:
Thu Jul 16
First Stable Release
commit 7c45d21...
```

By defoult tags are not fush to the remote repository we need to push 

**Push One Tag**

```
git push origin v1.0
```

**Push All Tags**

```
git push origin --tags

```

**Verify Remote Tags**

```
git ls-remote --tags origin

```

use this command for delete tags both local and remote 

```

git tag -d v1.0

git push origin --delete v1.0

```
Now the tag is removed from GitHub as well.
