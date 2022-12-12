class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name: str, parent: 'Folder' = None) -> None:
        self.name = name
        self.files = []
        self.folders = []
        if not parent:
            self.parent = self

    def add_file(self, file: File) -> None:
        # check file not in folder
        for f in self.files:
            if f.name == file.name:
                return
        self.files.append(file)

    def add_folder(self, folder: 'Folder') -> None:
        # check folder not in folder
        for f in self.folders:
            if f.name == folder.name:
                return
        self.folders.append(folder)
        folder.parent = self

    def get_size(self) -> int:
        size = 0
        for f in self.files:
            size += f.size
        for f in self.folders:
            size += f.get_size()
        return size


class FileSystem:
    def __init__(self) -> None:
        self.root = Folder('/')
        self.current = self.root

    def cd(self, path: str) -> None:
        if path == '/':
            self.current = self.root
            return

        folders = path.split('/')
        if folders[0] == '':
            folders = folders[1:]
            self.current = self.root
        for folder in folders:
            if folder == '..':
                self.current = self.current.parent
            else:
                for f in self.current.folders:
                    if f.name == folder:
                        self.current = f
                        break
                else:
                    raise Exception('No such folder')

    def add_file(self, name: str, size: int) -> None:
        self.current.add_file(File(name, size))

    def add_folder(self, name: str) -> None:
        self.current.add_folder(Folder(name))


def solve(lines):
    fs  = FileSystem()
    for line in lines:
        line = line.strip()

        if line:
            if line.startswith('$ cd '):
                path = line[5:]
                fs.cd(path)
            elif line.startswith('$ ls'):
                continue
            elif line.startswith('dir '):
                path = line[4:]
                fs.add_folder(path)
            else:
                size, name = line.split()
                size = int(size)
                fs.add_file(name, size)
    
    ans = float('inf')

    MAX = 70000000
    MIN = 30000000
    available = MAX - fs.root.get_size()

    queue = [fs.root]
    while queue:
        folder = queue.pop(0)
        size = folder.get_size()
        if available + size >= MIN:
            ans = min(ans, size)
        for f in folder.folders:
            queue.append(f)

    print(ans)

def main():
    with open('input.txt') as f:
        solve(f.readlines())

if __name__ == '__main__':
    main()