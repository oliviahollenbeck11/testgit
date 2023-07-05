from git import Repo

#TODO: Enter your name
name = ???

#TODO: Enter the folder name you made with 'mkdir.' If you haven't done that yet, go back!
foldername = ???

#TODO: Change this to your repo location. Mine is '/home/pi/BWSI_Code/FlatSatChallenge'
repo_name = ???

#function for uploading to Github. Note the input has a default value
def git_push(commit_message = 'New commit'):
    repo = Repo(repo_name)
    repo.git.add(repo_name + '/Images/')
    repo.index.commit(commit_message)
    print('made the commit')
    origin = repo.remote('origin')
    print('added remote')
    origin.push()
    print('pushed changes')
        

#Run it!
new_file = repo_name + '/Images/' + foldername + '/' + name + '.txt'
f = open(new_file,'w')
f.write('%s' % name)
f.close()

git_push('%s is testing git!' %name)
