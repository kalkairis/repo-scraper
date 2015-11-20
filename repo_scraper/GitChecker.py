from repo_scraper import git
from repo_scraper.DiffChecker import DiffChecker
import subprocess

class GitChecker:
    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions
    def file_traverser(self):
        #Checkout master
        subprocess.call(['git', 'checkout', 'master'])
        #Get all commits, reverse the list to get them in chronological order
        commits = git.list_commits()[::-1]
        #Go to the first commit
        subprocess.call(['git', 'checkout', commits[0]])
        #Run folder checker on first commit

        #Checkout master
        subprocess.call(['git', 'checkout', 'master'])
        #Generate commit pairs (each commit with the previous one)
        commit_pairs = zip(commits[:-1], commits[1:])
        for pair in commit_pairs:
            #print 'getting diff for %s %s' % pair
            files_diff = git.diff_for_commit_to_commit(*pair)
            for f in files_diff:
                #print 'gichecker: %s' % f['filename']+' in '+pair[1]
                yield DiffChecker(pair, f['filename'], f['content'], f['error'], self.allowed_extensions).check()