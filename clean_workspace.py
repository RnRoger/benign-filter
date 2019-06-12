import os

def main():
    """Remove all old files"""
    for n in ["18","21","y"]:
        try:
            os.remove(f"data/{n}.json")
            os.remove(f"data/{n}done.txt")
            os.remove(f"data/{n}report.html")
            os.remove(f"data/{n}ensembl.json")
        except:
            pass


if __name__ == "__main__":
    main()