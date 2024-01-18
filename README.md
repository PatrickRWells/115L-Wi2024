## 115L Assignments

This repository contains code and information for submitting and grading assignments in the Phy 115L Lab Class at U.C. Davis in Winter 2024. 

## Instutions for Submitting Assignments

This quarter, we will be using GitHub to submit assignments. GitHub is a collaborative coding platform that is used throughout academia and industry alike. It based on `git`, which is a tool for tracking changes made to your code and allowing you to go back to old versions if needed.

This guide assumes you already understand the of git and GitHub. It will not discuss how to actually put your code on github. For an introduction to how to use `git` and Github, see [this video](https://www.youtube.com/watch?v=8Dd7KRpKeaE)

If you have any questions. Please feel free to reach out to me on Canvas or come to my office hours.

These instructions will be the same for all the assignment in this course.

**1. Create a Private Repository**

Github repositories can be public or private. As you may expect, public repositories can be seen by anyone, while your private repositories can only be seen by you and anyone else you grant access.

You will be submitting your code for this class by posting it in a private GitHub repository and then sharing it with me. I recommend you create the repository *before* you start writing your solutions, and commit as you go. You can name the repo whatever you want, but I'd recommend something that makes it clear what the repo is for. 

If you're creating your repository directly on GitHub.com, there is a Public/Private repository option below the "description" field. If you're creating a repository using the GitHub Desktop client, there is a "keep this code private" checkbox when you do the first publish.

**2. Add your Solutions, and some other stuff**

Make sure to add solutions for all the assignments to the repository. Additionally, you should add file named "pyproject.toml" with the following information:

```toml
[project]
assignment-name = "My Assignment Name Here"
author = "Your Name Here"
dependencies = [
	"numpy",
	"scipy",
	"some-other-library"
]
```
A toml file can be be read by directly into a python dictionary. If you browse python projects on GitHub, you'll find that many (perhaps most!) of them will include a file like this that contains information about the project, and is used to create packages you can download with `pip`. I will be using this file when I grade to keep track of whose code is whose.

The "dependencies" list should contain any external libraries that your code needs to run. This includes libraries like "numpy" or "scipy," but *not* modules that are in the python standard library. If you're not sure, you can find a list of python standard library modules on [this page](https://docs.python.org/3/library/index.html)


**3. Add me as a collaborator on your repository**

Since your library is private, you will need to add me as a collaborator so that I can access it. For instructions on how to do this, see [this article](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository#)

My username on GitHub is [PatrickRWells](https://github.com/PatrickRWells)

**4. Submit your repository URL on Canvas**

GitHub does send me an email when you add me as a collaborator, but emails are hard to work with (from a code perspective).  From the repository home page on GitHub, click the ![[Screenshot 2024-01-18 at 12.44.26.png]] button and copy the link provided there. It should end with ".git"

Find the assignment on Canvas, and submit the url to the assignment.

Last Update: Jan 18, 12:50 PM
