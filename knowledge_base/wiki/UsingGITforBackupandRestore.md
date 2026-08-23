---
title: "Using GIT for Backup and Restore"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Using_GIT_for_Backup_and_Restore"
type: wiki
categories: FHS, Business
author: Fraser Highland Shoppe Wiki
---

 You will need a GIT server - I am using github.
 username ksfraser, email kevin@ksfraser.com
 password is in the KeePass

==Git Commands==
*git remote add origin https://github.com/ksfraser/etc.git
*git push -v origin master
*git push -v origin master
*git checkout -b scan
*git pull -v scan master
*git branch -a
*git branch
*git add *
*git commit
*git push -v

===Testing Github and SSH keys===
*ssh -vT git@github.com


==Server Side==
#Create your repository

==Client Side==
#cd {DIR}
#git init
#git add .
#git commit -a -m "Yes, this is server"

==Backup Script==
21 December 2017

#put my files into a Git repository.
#use feature of Git called bundles to make incremental backups.
#(optionally)use GPG to encrypt the bundles, and then upload them to a cloud hosting site.


 git bundle create master.bundle master
then it will create a single file, called master.bundle, which contains all of the commits on the master branch. If you’re creating a backup of the master branch, then you just need to copy that bundle somewhere safe.

incremental backups means create a bundle that only has the changes since the last backup. This is a very similar process.

 git bundle create start-to-master.bundle start..master
This will create a bundle that has everything in master, except anything that is also in start. If start.bundle was the last backup, then I can recover my repository if I have both start.bundle and start-to-master.bundle.

===Script===
#!/bin/bash

# This will make the script as a whole exit when it first encounters
# an error.
set -e

echo "Starting file backup"

# This is the directory that I'm backing up.
FILE_DIR='/home/justin/mail/'
# It will create the bundles in this subdirectory. Make sure you've
# added this subdirectory to your .gitignore file.
BACKUP_DIR='backup-cf/'

cd $FILE_DIR

# If there aren't any backups yet, create the folder. This will be the
# first backup, and also the first time after you restore from a
# backup.
if [ ! -d "$BACKUP_DIR" ]
then
    echo "Backup directory does not exist. Creating it"
    mkdir -p $BACKUP_DIR
fi

# Create an automated commit of the latest changes, but only if
# there's something to commit.
git add -A
if [ "`git diff --cached --name-only`" ]
then
    git commit -m "Automated commit from backup util"
fi

# Garbage collection so the backup doesn't grow HUGE
git gc

# I'm calling the commits here checkpoints, because I can't help in my
# head thinking of it as saving my progress in a game. It's really
# just the id of the last commit.
CURRENT_CHECKPOINT=`git rev-parse --verify HEAD`
# Notice that the filename contains a timestamp, such that if I want
# these in chronological order I can sort by filename.
BUNDLE_NAME="mail."`date +%Y%m%d%H%M%S`"."$CURRENT_CHECKPOINT".bundle"
BUNDLE=$BACKUP_DIR$BUNDLE_NAME

# This is the most recently created bundle. I'm keeping all of the
# bundles in the backup folder so that I can do this.
LAST_BUNDLE=`find $BACKUP_DIR -name '*.bundle' | sort -r | head -n 1`
if [ "$LAST_BUNDLE" == "" ]
then
    # There was no previous bundle, so this bundle just gets all of
    # the commits.
    echo "first backup bundle"
    git bundle create "$BUNDLE" HEAD
else
    # There's a previous bundle, so we can exclude the commits from
    # that bundle.
    echo "basing backup on previous bundle, $LAST_BUNDLE"
    LAST_CHECKPOINT=`git bundle list-heads $LAST_BUNDLE | cut -d' ' -f1`
    echo "last commit was $LAST_CHECKPOINT"
    if [ "$CURRENT_CHECKPOINT" != "$LAST_CHECKPOINT" ]
    then
        git bundle create "$BUNDLE" $LAST_CHECKPOINT..HEAD
    else
        echo "nothing new to backup"
    fi
fi

# If there wasn't anything new in the bundle, we wouldn't have created
# it. So only if there's something new, then we need to upload.
if [ -f "$BUNDLE" ]
then
    # I encrypt the bundle using my GPG public key.
    echo "Encrypting bundle"
    gpg -r justin -e "$BUNDLE"

    # Rsync the gpg file over to Cloudfiles! Because of the fickle
    # nature of network connections, this is the point which is most
    # likely to fail. If the network is down, Rsync will fail to
    # upload it, and so Rsync won't delete it. The next time the
    # script runs, when it gets here, it will upload the bundle that
    # didn't make it last time.
    rsync -avz --remove-source-files --ignore-existing \
          $BACKUP_DIR/*.bundle.gpg \
          username@bucketname.cloudfiles.co.za:jw-backups/.
fi

echo "Finished backup utility"

===Restoring===
No backup strategy is complete without some way to recover the backed up data. Here is my script to do that.

#!/bin/bash

set -e

# To recover the backups, first we need to get the backups
mkdir /tmp/backup

# The --protect-args part here makes sure the * is actually sent to
# the CloudFiles server, and our local bash doesn't try to expand
# it. Our local bash can't figure out all the files on CloudFiles.
rsync -avz --progress --protect-args \
      "username@bucketname.cloudfiles.co.za:jw-backups/*.bundle.gpg" \
      /tmp/backup/

# This will prompt you for your private key password. Most Linux
# distributions come with gpg-agent, so you'll only need to enter the
# password once.
gpg --decrypt-files /tmp/backup/*.bundle.gpg

# This is where we're restoring to. Change as necessary.
mkdir recovery
cd recovery

# This is the git trick. It's just doing a fetch from each Git bundle,
# in order (remember the filenames have a datestamp in them), and
# calling the end of the last one the master branch.
git init
find /tmp/backup/ -name '*.bundle' | sort | xargs -n1 -I'{}' git fetch {}
git checkout -B master FETCH_HEAD


===Limitations===
The way that I’m using Git in this script assumes that there aren’t ever any branches. Since I let the script do everything with Git here, and don’t use it as a Git repository otherwise, this is a fair assumption. If you’re planning on backing up an active Git repository, you can do that with bundles, but you’ll need to consider which branches you’re interested in.

Git is very good at finding the changes in text files. If the files that you’re working with are not text files, like images, audio, video, or other binary formats, you may find that your Git repository starts to get large over time. For these sorts of files, there may be better options than using Git. Thankfully, Git does work exceptionally well for things like my emails.

The cryptography in this blog is a relatively simplistic approach to prevent people from reading the data in the backups. It would still be theoretically possible for an attacker to do nasty things like replacing the backups with something completely different without you knowing. If you’re feeling extra paranoid, you could look into also using a GPG private key to sign the bundles before uploading them.



[[Category: Business]]
[[Category: Infrastructure]]
[[Category: FHS]]
[[Category: KSFII]]

===Truncate History using Rebase===
 https://passingcuriosity.com/2017/truncating-git-history/
*git checkout --orphan temp e41d7f633c45c46bd42e97cecf93204191d9e4c9
*git commit -m "Truncate history"
*git rebase --onto temp e41d7f633c45c46bd42e97cecf93204191d9e4c9 master

More complete

*git checkout --orphan temp $1 # create a new branch without parent history
*git commit -m "Truncated history" # create a first commit on this branch
*git rebase --onto temp $1 master # now rebase the part of master branch that we want to keep onto this branch
*git branch -D temp # delete the temp branch
 The following 2 commands are optional - they keep your git repo in good shape.
*git prune --progress # delete all the objects w/o references
*git gc --aggressive # aggressively collect garbage; may take a lot of time on large repos

===Truncate using SHALLOW===

*git rev-parse HEAD~1200 > .git/shallow
*git fsck --unreachable
*git filter-branch -- --all
*git gc --prune --aggresive

===Truncate using Checkout===
If you want to keep the upstream repository with full history, but local smaller checkouts, do a shallow clone with 
*git clone --depth=1 [repo].
After pushing a commit, you can do
*git fetch --depth=1 to prune the old commits. This makes the old commits and their objects unreachable.
*git reflog expire --expire-unreachable=now --all. To expire all old commits and their objects
*git gc --aggressive --prune=all to remove the old objects
See also [https://stackoverflow.com/q/9819185/873282 How to remove local git history after a commit]?.

==MySQL==
 https://www.viget.com/articles/backup-your-database-in-git/
mkdir -p /path/to/backup cd /path/to/backup mysqldump -u [user] -p[pass] --skip-extended-insert [database] > [database].sql git init git add [database].sql git commit -m "Initial commit" 

0 * * * * cd /path/to/backup && \ mysqldump -u [user] -p[pass] --skip-extended-insert [database] > [database].sql && \ git commit -am "Updating DB backup" 

You may want to add another entry to run git gc every day or so in order to keep disk space down and performance up.

Now that you have all of your data in a git repo, you’ve got a lot of options. Easily view activity on your site with git whatchanged -p. Update your staging server to the latest data with git clone ssh://[hostname]/path/to/backup. Add a remote on Github and get offsite backups with a simple git push.