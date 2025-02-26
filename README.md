# Git Assignment - Harjeet

## Overview
This repository contains Python scripts for various computational tasks, including arithmetic operations, geometric calculations, and Git version control workflows. It is part of my Git assignment for HeroVired and showcases version control best practices, collaboration, and branching strategies.

## Repository Structure
- **calculator.py**: A Python script that performs basic arithmetic operations, including addition, subtraction, multiplication, and division, along with a square root function.
- **geometry-calc.py**: A Python script for geometric calculations, including area computations for circles and rectangles.
- **git_lfs.txt**: A text file containing detailed steps for Git LFS tracking.
- **large_file.bin**: A large binary file tracked using Git LFS.
- **.gitattributes**: A Git configuration file that specifies how Git LFS should handle certain files.
- **README.md**: This file, providing details about the repository.

## Branches Overview
- **main**: The primary branch containing stable releases.
- **dev**: A development branch where new features and bug fixes are tested before merging into main.
- **lfs**: A branch dedicated to handling large files using Git LFS.
- **feature/sqrt**: A branch for implementing the square root function in "calculator.py".
- **geometry-calculator**: Serves as the main feature branch where different sub-features (circle area and rectangle area calculations) are developed and merged.
- **feature/circle-area**: A branch for implementing the area calculation of a circle in "geometry-calc.py".
- **feature/rectangle-area**: A branch for implementing the area calculation of a rectangle in "geometry-calc.py".

## Workflow Steps

### **1️⃣CalculatorPlus Implementation**
1. **Create the Repository**
   - Create a GitHub repository named `git_assignment_HeroVired` and clone it locally.

2. **Create a Development Branch and add the provided code**
   - Switch to the `dev` branch.

3. **Merge with Main and Release Version 1**
   - Merge `dev` into `main` and create a v1.0 release.
   - Add any of your classmates as collaborators.

4. **Implement Square Root Feature**
   - Create a new branch `feature/sqrt` and implement the square root function.
   - Uncomment and implement the `square_root` function in `calculator.py`.
   - Commit your changes in the local branch `feature/sqrt`.

5. **Bug Fixation**
   - Switch to the `dev` branch.
   - Modify the `divide` function to prevent division by zero.
   - Implement the fix in the `dev` branch and merge it.
   - Create a pull request to push the changes to the `main` branch from `dev`.

6. **Feature Addition and Release Version 2**
   - Switch to the `feature/sqrt` branch.
   - Merge the updated changes from `dev` branch to `feature/sqrt` branch and fix the conflicts if any.
   - Create a pull request to push the changes to the `feature/sqrt` branch from `dev`.
   - Merge `dev` into `main` and create a v2.0 release.

### **2️⃣Handling Large Files with Git LFS**
1. **Create a Branch for Git LFS**
   - Switch to a new branch `lfs`:
     ```sh
     git checkout -b lfs
     ```
2. **Install and Set Up Git LFS**<br>
   - Download and install the Git command line extension. 
     ```sh
     https://github.com/git-lfs/git-lfs/releases/download/v3.6.1/git-lfs-windows-v3.6.1.exe
     ```
   - Once downloaded and installed, set up Git LFS for your user account and select the file types you'd like Git LFS to manage (or directly edit your .gitattributes)
     ```sh
     git lfs install
     git lfs track "*.bin"
     git add .gitattributes
     ```
3. **Upload Large Files and Push Features**
   - Add and commit a file over 200MB.
   - Implement, commit, and push all the changes or requirements into the current branch.
     ```sh
     git add .
     git commit -m "Add design file"
     git push origin lfs
     ```
   - Merge into `main` once you are done.

### **3️⃣Geometry Calculator with Git Stash**
1. **Create a main feature branch geometry-calculator**
   - Switch to the `geometry-calculator` branch.
     
2. **Create Feature Branches from the main feature branch "geometry-calculator"**
   - `feature/circle-area` for circle area calculations.
   - `feature/rectangle-area` for rectangle area calculations.

3. **Use Git Stash**
   - Before switching branches, stash incomplete changes:
     ```sh
     git stash
     ```
   - Retrieve the stashed changes when resuming work:
     ```sh
     git stash pop
     ```

4. **Commit and Push Features**
   - Implement, commit, and push both features.
   - Create pull requests for `dev`.
   - Merge into `main` upon approval.

## Scripts Execution Steps with Output Screenshots Reference

- **calculator.py Output [Question 1]**
![image](https://github.com/user-attachments/assets/f092fb5b-7cc8-486f-9cc4-e7e3dd5db48c)
![image](https://github.com/user-attachments/assets/7c2e9609-f26c-4f77-b7c4-e4cd4eddf5e4)


- **git lfs output [Question 2]**
![Screenshot 2025-02-25 224028](https://github.com/user-attachments/assets/bf86c59c-e1ed-4096-9317-e76632e8cb89)


- **calculator.py Output [Question 3]**
![image](https://github.com/user-attachments/assets/134f9ad7-5d32-4afb-8bfa-bac07dbee38d)


## Fellow Collaborators
Thanks to my collaborators for their support in this assignment:
- @tanujbhatia24
- @minnathdhani
- @shraddhabhat06

## Contribution
To contribute:
1. Fork the repository.
2. Create a feature branch from the dev branch.
3. Commit your changes.
4. Push to your branch and open a Pull Request.

