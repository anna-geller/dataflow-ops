from prefect.filesystems import GitHub

gh = GitHub(repository="https://github.com/anna-geller/dataflow-ops.git")
gh.save("main")
# await gh.get_directory()
