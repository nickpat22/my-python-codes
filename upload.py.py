import subprocess

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Updated files"], check=True)
subprocess.run(["git", "push"], check=True)

print("Uploaded successfully!")