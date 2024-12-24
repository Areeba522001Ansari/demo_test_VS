import os
import subprocess
import tempfile
from pathlib import Path
import difflib

def clone_repo_at_commit(github_url, commit_id, target_dir):
    """Clone the repository at a specific commit."""
    try:
        print(f"Cloning repository for commit {commit_id}...")
        subprocess.run(["git", "clone", github_url, target_dir], check=True)
        subprocess.run(["git", "checkout", commit_id], cwd=target_dir, check=True)
        print(f"Cloned repository at commit {commit_id} into {target_dir}")
        return target_dir
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository at commit {commit_id}: {e}")
        return None

def get_recent_commits(github_url):
    """Fetch recent commit IDs for the default branch."""
    try:
        temp_dir = tempfile.mkdtemp()
        subprocess.run(["git", "clone", "--depth", "2", github_url, temp_dir], check=True)
        # Get the commit IDs
        result = subprocess.run(
            ["git", "log", "--pretty=%H"], cwd=temp_dir, capture_output=True, text=True
        )
        commits = result.stdout.splitlines()
        if len(commits) < 2:
            print("Warning: The repository has fewer than two commits.")
        return commits
    except subprocess.CalledProcessError as e:
        print("Error fetching commits:", e)
        return []

def find_common_files(dir1, dir2):
    """Identify files with the same name in two directories."""
    files1 = {file.name for file in Path(dir1).rglob("*") if file.is_file()}
    files2 = {file.name for file in Path(dir2).rglob("*") if file.is_file()}
    return files1.intersection(files2)

def compare_files(file1_path, file2_path):
    """Compare two files and show the differences."""
    with open(file1_path, "r") as f1, open(file2_path, "r") as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    diff = difflib.unified_diff(
        file1_lines, file2_lines, fromfile="Commit 1", tofile="Commit 2", lineterm=""
    )
    diff_output = "\n".join(diff)
    if diff_output:
        print("Differences found between the files:")
        print(diff_output)
    else:
        print("The selected files are identical.")

if __name__ == "__main__":
    github_url = input("Enter the GitHub repository URL: ")

    # Step 1: Fetch recent commits
    commits = get_recent_commits(github_url)
    if not commits:
        print("Failed to fetch commits. Exiting...")
        exit(1)

    if len(commits) < 2:
        print("The repository has fewer than two commits. Comparison cannot proceed.")
        exit(1)

    print(f"Recent commits:\n1. {commits[0]}\n2. {commits[1]}")

    # Step 2: Clone repo at each commit
    dir1 = tempfile.mkdtemp()
    dir2 = tempfile.mkdtemp()
    clone_repo_at_commit(github_url, commits[0], dir1)
    clone_repo_at_commit(github_url, commits[1], dir2)

    # Step 3: Find common files
    common_files = find_common_files(dir1, dir2)
    if not common_files:
        print("No common files found between the two commits.")
    else:
        print("Common files found:")
        for idx, file in enumerate(common_files, start=1):
            print(f"{idx}. {file}")

        # Step 4: Select files for comparison
        selected_file = input("Enter the name of the file to compare: ")
        file1_path = Path(dir1) / selected_file
        file2_path = Path(dir2) / selected_file

        if file1_path.exists() and file2_path.exists():
            # Step 5: Compare files
            compare_files(file1_path, file2_path)
        else:
            print("The selected file does not exist in one or both commits.")
