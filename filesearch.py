import os
import fnmatch

def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

if __name__ == "__main__":
    assert recursive_glob("./temp", "*.py") == []
    assert recursive_glob("./temp", "*.txt") == ["./temp/1.txt", "./temp/123/456/789.txt"]
    assert recursive_glob("./temp/123/456","*.txt") == ["./temp/123/456/789.txt"]
    print ("Tests passed")