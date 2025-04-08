import subprocess


def initialize_repository():
    print("Initializing git repository...")
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)


def main():
    initialize_repository()


if __name__ == "__main__":
    main()
