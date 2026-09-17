import subprocess

repo_url = "https://github.com/nickpat22/my-python-codes.git"
file = "new.py"

# Initialize Git
subprocess.run(["git", "init"])

# Connect local folder to GitHub
subprocess.run(["git", "remote", "add", "origin", repo_url])

# Add file
subprocess.run(["git", "add", file])

# Commit
subprocess.run(["git", "commit", "-m", "Upload file"])

# Push to GitHub
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])

print("File uploaded successfully!")