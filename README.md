git-test
========

This is a repo for testing git features.

See [Usage](#Usage) for instructions.

Current Branch: `submodule`
------------------------

###### Created: 4/30/2020

This branch is for testing the submodule feature of git.

### Submodule Instructions

1. `git submodule add <url>` (url must me https://github.com/... for GitHub to recognize and link properly)
1. Commit changes
1. To update submodules:
    - `git submodule update` with these flags (if needed):
        - `--init` initializes and clones submodule to local repo (needed after cloning repo with submodules)
        - `--recursive` recursively updated nested submodules
        - `--remote` updates submodule to most recent commit on remote branch rather than specified submodule commit
        - `--checkout`, `--merge`, `--rebase`: see `update` option in [option list](#Options) below
        - Note: `git submodule update` without `--remote` updates the submodule to a specified commit in the index, not the most recent commit
        - See `git help submodule` for more info
    - `git submodule foreach <command>` may be helful
        - Example: `git submodule foreach git pull origin master`
1. To remove submodules:
    1. `git rm <submodule>`
    1. `rm -rf .git/modules/<submodule>`
    1. `git config -f .git/config --remove-section submodule.<submodule>`
1. To switch to a branch with different status:
    - `git checkout --recurse-submodules <branch>`
    - Optional: `git config submodule.recurse true` to always use `--recurse-submodules`

### `.gitmodules` Options:

#### Sample `.gitmodules` entry:

```
[submodule "<submodule>"]
    path = <submodule>
    url = <url-to-submodule>
```

#### Options:

Edit with `git config -f .gitmodules submodule.<submodule>.<option> <value>`

- `branch`: Which branch is tracked by the submodule for updates with `--remote` (defaults to `master`)
- `update`: What happens when `git submodue update` happens
    - `checkout`: Default. Checks out most recent commit (detached HEAD)
    - `merge`: Merge remote into submodule. (Note: if branch is checked out before update HEAD will not be detached)
    - `rebase`: Rebase onto remote. (Note: if branch is checked out before update HEAD will not be detached)
- `ignore`: Which files in the submodule repo are ignored by the main repo
    - `none`: Default. No change are ignored
    - `all`: Any changes are ignored
    - `dirty`: Uncommitted changes are ignored but committed changes are shown
    - `untracked`: Only untracked files are ignored. All tracked changes are shown

### Helpful Links

- [Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [Working with submodules](https://github.blog/2016-02-01-working-with-submodules/)
- [Why is my Git Submodule HEAD detached from master?](https://stackoverflow.com/a/55570998/10865303)
- [How do I remove a submodule?](https://stackoverflow.com/a/21211232/10865303)
- [GitHub Tutorial to Manage Project with SubRepositories](https://github.com/EmaroLab/docs/wiki/GitHub-Tutorial-to-Manage-Project-with-SubRepositories)
- [Update Git submodule to latest commit on origin](https://stackoverflow.com/questions/5828324/)

Branch Key
----------

Branch Name | Description
----------- | -----------
`master`    | Base set of files. Used as a base for testing branches.
`submodule` | Testing git submodules.

Usage
-----

Use branches to manage different tests.

`master` should be updated to represent a good base, and new branches should be created for each new test.

### Instructions

1. Edit `README.md` on the `master` branch
    1. Add the new branch to the table
    1. Commit these changes on `master`
1. Create a new branch with `git checkout -b <name>`
1. Edit `README.md` on the new branch
    1. Update the current branch name
    1. Update the description
1. Do whatever testing is needed
1. Update `README.md` on the new branch to have descriptions of the testing that was done.

### Files

- `countries/`: Contains text files listing countries by continent
- `README.md`: Contains general information about the repo and current branch
- `countries.csv`: CSV file containing raw country data
- `country_sorter.py`: Python script that sorts countries from `countries.CSV` into continent text files in `countries/`
- `iso_8859-1.txt`: Contains a list of characters defined by ISO 8859-1
- `primes.py`: Python script that prints all primes under the given input
- `sample.txt`: Contains sample text from a GitHub Gist by bawejakunal
