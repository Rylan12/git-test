git-test
========

This is a repo for testing git features.

See [Usage](#Usage) for instructions.

Current Branch: `master`
------------------------

###### Created: 4/30/2020

This contains a base set of files that can be used for testing.

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
