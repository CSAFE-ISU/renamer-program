# renamer-program
Simple program for renaming images

See the `environment.yml` file for a list of dependencies. If you're using
Anaconda, you can use it to create a virtual environment including those
packages using `conda env create` in the root directory, then activating
it with `source activate renamer-env`.

## To contribute
- Fork the repo on GitHub.
- Clone your fork.
- Create a new branch with `git checkout -b <my_branchname>`.
- Make your changes.
- Commit your changes.
- Push back to your fork on GitHub with `git push origin my_branchname`.
- From GitHub, open a pull request to have your changes merged with the
  master branch.

## To test
- Clone the repo.
- Navigate to the root directory.
- Run `python renamer.py test_images/` and have fun renaming files!
- Run `python renamer.py -h` to see documenation and options.