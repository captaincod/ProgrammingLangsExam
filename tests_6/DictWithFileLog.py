from datetime import datetime


def now():
    return datetime.utcnow()


class DictWithFileLog(dict):

    def __init__(self, path, *args, **kwargs):
        self.f = open(path, "a+")
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        self._write_line(f"get item '{key}'")
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self._write_line(f"set item '{key}' with value '{value}'")
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        self._write_line(f"del item '{key}'")
        return super().__delitem__(key)

    def _write_line(self, line):
        self.f.write(f"{now()}: {line}\n")

    def log(self):
        self.f.seek(0)
        return self.f.readlines()

