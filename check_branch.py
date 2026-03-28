import subprocess

def get_git_branch():
    try:
        # Run the command and capture its output
        branch_name = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=subprocess.STDOUT, text=True).strip()
        return branch_name
    except subprocess.CalledProcessError:
        return "Error: Not a git repository or detached HEAD"

current_branch = get_git_branch()
print(f"Current Git branch: {current_branch}")
