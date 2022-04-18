# Setup git repositories
In this instructions, we will be achieving 3 objectives:
1. Setup a folder that is solely for keeping a clean version of class materials
2. Setup a repo that will contain your edited version of class materials
3. Setup a repo for lab assignments


## Contents

# Setup a clean folder of class materials

### 1. Copy the git URI 
from https://git.generalassemb.ly/DSI-SG-master-list/DSIF-SG-3

<img src="assets\copy_git_uri.png" width="600"/>


### 2. Create a folder to contain the files
In this example, I will use `~/original_materials` as the path.

Open a terminal (mac) / git bash (windows) and navigate to the folder:
```
~$ cd ~/original_materials
```
_note: don't type ~ or $. ~ means user's root location_

### 3. Clone the repo
In the folder, clone the repo
```
~/original_materials $ git clone https://git.generalassemb.ly/DSI-SG-master-list/DSIF-SG-3.git .
```

Explanation:
- `clone` tells git to copy all the files from the URI and also setup the source link (explanation below)
- `.` at the end means clone to current directory (otherwise it will create a new folder called materials)


The repo is now cloned. We can check where it's linked to by typing:
```
~/original_materials $ cd DSIF-SG-3
~/original_materials $ git remote -v
```
you should see the 2 lines:<br>
`origin  https://git.generalassemb.ly/DSI-SG-master-list/DSIF-SG-3.git (fetch)`<br>
`origin  https://git.generalassemb.ly/DSI-SG-master-list/DSIF-SG-3.git (push)`

Explanation:
- `remote` means remote server
- `-v` means version flag
- we are asking git to show us where is the remote server location
- `origin` is a shorthand name for the remote repository that a project was originally cloned from
- `(fetch)` indicates where we will be retrieving the files from for new updates
- `(push)` indicates where we will be sending the files to if we want to make an update (in this case we won't be)

### 4. Update changes in future
**To retreive future updates** type the 2 commands:
```
~/original_materials $ git fetch
~/original_materials $ git pull
```
Explanation:
- `fetch` tells git to retreive the latest meta-data (aka information) of the origin
- `pull` tells git to retreive the actual files based on the meta-data
- we must always perform these 2 steps in sequence



# Setup a repo for our own materials

### 1. Create your github repo
goto: https://git.generalassemb.ly/<br>
you should be logged into your account

click "new" repo button

<img src="assets\new_repo_btn.png" width="600"/>

In this example I will name the repo `my_materials`, then click "create repository"

<img src="assets\create_repo.png" width="600"/>

In the next page, you will find your git uri that looks like 
<br>`https://git.generalassemb.ly/maheshkumarpaik/my_materials.git`<br>
**Please don't copy mine but use your own URI instead**

### 2. Clone the repo to your local device
Create a new folder for your own version of materials<br>
In this example I will use `~/my_materials`

Navigate to your folder
```
$ cd ~/my_materials
```

Then clone YOUR repo
```
~/my_materials $ git clone https://git.generalassemb.ly/maheshkumarpaik/my_materials.git .
```
**Please don't copy mine but use your own URI instead**

This folder is now linked to the github repo. Any file changes inside will be tracked and can be saved to github.

Now you can move whatever files you have been working on previously into this folder.

### 3. Adding your credentials into git's configuration
Before we are able to write anything to github, we need to provide our email and username credentials. This is a process you will only be needing to do once ever.

to view what is currently in our config:
```
$ git config --global --list
```
you might see something like:<br>
`user.email=your@email.com`<br>
`user.name=YourGitUserName`

If you do, that means your credentials already exist. Otherwise, we will need to add it with the following lines:
```
$ git config --global user.name "YourGitUserName"
$ git config --global user.email your@email.com
```


### 4. Pushing changes from your device to github
After changing the files, to send the changes to your github repo, we need 3 steps. I like to think of it as sending a rocket to space. We put all the materials at a staging area, then we decide on the mission name, and finally blast it into space.

1. Add all the files to staging
```
~/my_materials $ git add .
```
- `add` means add the files to staging
- `.` means all files


2. Commit the files in staging
```
~/my_materials $ git commit -m "my first commit"
```
- `commit` means commiting all the changes to a checkpoint
- `-m` flag means "message". we're giving it a description
- `"my first commit"` is the description we attach to the commit. It should describe the changes like "updated readme" or "fixed xx bug"

3. Push the files to github
```
~/my_materials $ git push origin master
```
OR A SHORTER VERSION ()
```
~/my_materials $ git push
```
- `push` means pushing the files to github
- `origin` is the shorthand for `https://git.generalassemb.ly/maheshkumarpaik/my_materials.git` URI
- `master` means master branch. Branching is an intermidiate topic for another day. find out more at https://learngitbranching.js.org/

# Setup a repo for Lab assignments

Your labs will be reviewed regularly as part of the course requirements. I will need you to setup a serparate repo that will be shared with the Instructors and TAs.

Repeat the above steps to create another repo called `Labs`. Ideally, the folder is seperate and outside of your `my_materials` folder. You can push the labs the same way as above. You will also need to grant the team access to the repo for us to view it.

<img src="assets\add_collaborator.png" width="600"/>

Go to `settings` tab on top, then on the left, go to `Collaborators` and add Shilpa, Peter and Mark 
- shilpa-ga
- petermah
- mt2395

Once you have done that, fill up this form: https://forms.gle/sB3nC6qQunTsPaev8

fyi, we will repeat this process for project submissions in the future.
