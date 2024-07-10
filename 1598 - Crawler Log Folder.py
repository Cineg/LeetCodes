class Folder:
    def __init__(self, name: str, parent=None):
        self.parent: Folder | None = parent
        self.name: str = name


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        folder: Folder = Folder("root")

        for log in logs:
            if log == "../":
                folder = folder.parent if folder.parent else folder
            elif log == "./":
                continue
            else:
                nfolder: Folder = Folder(log, folder)
                folder = nfolder

        count: int = 0
        while folder.name != "root":
            folder = folder.parent
            count += 1

        return count


def main() -> None:
    sol = Solution()
    logs: list[str] = [
        "./",
        "c1/",
        "pj5/",
        "e5/",
        "y6/",
        "../",
        "u4/",
        "a5/",
        "../",
        "nq5/",
        "../",
        "m2/",
        "w0/",
        "./",
        "./",
        "uf5/",
        "z8/",
        "../",
        "z8/",
        "r7/",
        "ez6/",
        "u4/",
        "it2/",
        "./",
        "../",
        "./",
        "tb9/",
        "o4/",
    ]
    res: int = sol.minOperations(logs)
    print(res)


if __name__ == "__main__":
    main()
