---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# How-To: Project Work

This document explains the practical details of how to do project work in IN1910. How to work on Git and hand in is described first, how to collaborate on projects is described at the bottom.

## Working on the project in Git

### Project Repositories

For each of the four projects in IN1910, you will do your work in a specific Git repository. **We make these repos for you** and give you the specific URL and editing rights in the project text.

### Delivering your project

In your repository you will create a branch called `release`. To hand in your project should make a pull request into this branch. If you are unsure how to make a pull request, checkout the [hello world example on GitHub](https://guides.github.com/activities/hello-world/#pr) or the [lecture video about git](https://youtu.be/pz-ZiALcnwk). You can also read more about pull request [here](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

In addition to making a pull request, we ask that you hand in your README.md file to Devilry (https://devilry.ifi.uio.no). We ask you to do this because we use Devilry for grading each project and as a backup in case any issues arise with the Git repo.

### Using the README-file

Your project repositories should all contain a file called `README.md`, which you should also upload to Devilry when you are finished. This file should contain the following information
* The name/URL of your repository
* Short explanation of any technical issues you ran into, if any
* Any other information you want your grader to know.

In addition to these, the README can be extended to include more information about your project work if desired. You can read more about readme files on GitHub [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-readmes). A cool project to use if you want a nice looking README file is <https://readme.so/editor>.

### Create a .gitignore

All repositories should contain a `.gitignore` file, you can create one using the following website
* <https://gitignore.io>

Good things to add to your gitignore are Python, Jupyter, C++, your OS (e.g., Windows/macOS/Linux) and your editor (e.g., VisualStudioCode or SublimeText)

### Commit often and make good commit messages

Every time you are done implementing a specific task, or fix an error, you should make a commit. The message should precisely shortly describe what changes to the code each commit represents. Think about your commits as the history of what you did. Many and good commits will make it easier for your grader to understand what you have done, and it will be easier for you to look back at your project work before the oral exam as well.

Also remember to push to GitHub often. By pushing you ensure an external backup of your work, in case anything happens to your local copy or computer. In addition, if you are collaborating, pushing is the only way for your partner to see or use your changes.

Finally, when you are collaborating, remember to use `git pull` before you start working. This way you get the most up-to-date version of the code, in case your partner has pushed any changes you are unaware of.


## Teamwork in IN1910

For the first project (Project 0) has to be done individually. You can of course discuss and help each other, but you should write your own code and submit your own work. For the remaining three projects however (Project 1, 2, and 3) you can work in pairs if you wish. This means you will get a joint Git repository, work on the code together and submit together. Here we explain how to find a partner if you wish to collaborate, and some tips for collaborating.

### Finding your team (or how to work alone)

You can choose if you want to do Projects 1, 2, and 3 alone, with a specific partner, or with a randomly chosen from the same group session that you are in (as far as possible). You can reach your partner by email by sending an email to `username@mail.uio.no` (or `username@ulrik.uio.no`) (where you swap username with the username of your partner. You can also try to get in touch with your partner on https://mattermost.uio.no/ifi-in1910. See below on what to do if you are struggling to establish contact with your partner.

In good time before the project we will publish a web form (nettskjema) you can fill in to let us know if you want to collaborate or work alone, and if you have a specific partner in mind or if we should find one for you. The deadline for making this request is 1 week before the project is handed out. See [Project Work, Grading and Exam](../info/exam.md) for more info.

### Unable to get in contact with your partner
If you have tried to contact your assigned partner, e.g by sending him/her an email, but haven't gotten any response within two (working) days, then we will try to find you a new partner. See [Project Work, Grading and Exam](../info/exam.md) for more info.


### Issues with the team work
If you encounter any issues with the teamwork, please send an email to [johanbir@ifi.uio.no](mailto:johanbir@ifi.uio.no) so we can try to resolve it.

## Advice on Collaborating
We encourage working in pairs in IN1910, because it is a good way to learn more about how to collaborate on software development in Git. Please do note however, that the final oral exam, which revolves mostly about the project work, is individual. At the exam you can be asked about any parts of the projects. Thus, even when collaborating, you do need to collaborate on all parts of the projects and strive to understand all aspects of the code. In other words, don't simply split the project down the middle and never talk together, that is not a good way to collaborate. Instead, we suggest you use the Agile software development *pair programming*.

### Pair programming

In the [pair programming](https://en.wikipedia.org/wiki/Pair_programming) technique, two programmers collaborate using a single computer. One person is the "driver", who is actually writing the code, while the other is the "navigator". The navigator helps the driver by catching errors, giving advice, asking helpful questions. The goal is that the driver can have a narrow focus on technical details while the navigator can have a bigger picture view of the code and the project as a whole. The two roles should be switched frequently, at least every 30 minutes. You can for example use the Pomodoro technique and swap every break (work for 25 minutes, take a 5 minute break, rinse and repeat).

Pair programming is a popular technique as it leads to fewer errors in code and it is a great way for programmers to exchange knowledge and learn from each other. Using pair programming will also ensure that both team members are contributing to all parts of the project and you will work on discussing and talking about the project work and your code, which will be a very good preparation for the final oral exam.

Pair programming can be done in person, or remotely via Zoom. When working remotely, the person doing the programming can share their screen while the other watches with active discussion and instruction along the way. Whether you work locally or remotely, every time you switch role you will most likely switch machines. To do this efficiently and seamlessly, simply have the driver commit and push and the other person pull before you resume work with flipped roles.
