import os
import subprocess
import tempfile
from pathlib import Path

def clone_github_repo(github_url):
    """Clone the GitHub repository and return the path to the cloned directory."""
    try:
        # Create a temporary directory to clone the repo
        temp_dir = tempfile.mkdtemp()
        print(f"Cloning the repository into {temp_dir}...")
        subprocess.run(["git", "clone", github_url, temp_dir], check=True)
        return temp_dir
    except subprocess.CalledProcessError as e:
        print("Error cloning the repository:", e)
        return None

def find_python_files(repo_path):
    """Find and list all Python files in the repository."""
    py_files = list(Path(repo_path).rglob("*.py"))
    if not py_files:
        print("No Python files found in the repository.")
    else:
        print(f"Found {len(py_files)} Python file(s):")
        for file in py_files:
            print(f"- {file}")
    return py_files

if __name__ == "__main__":
    # Example GitHub URL (replace with your own)
    github_url = input("Enter the GitHub repository URL: ")

    # Clone the repository
    repo_path = clone_github_repo(github_url)

    if repo_path:
        # List Python files in the repository
        python_files = find_python_files(repo_path)
        if python_files:
            print("Ready to proceed with further processing of these files!")
        else:
            print("No further processing as no Python files are found.")
