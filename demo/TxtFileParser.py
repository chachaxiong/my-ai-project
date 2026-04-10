from pathlib import Path


class TxtFileParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

    def read_lines(self) -> list[str]:
        if not self.file_path.exists():
            raise FileNotFoundError(f"文件不存在: {self.file_path}")

        if self.file_path.suffix.lower() != ".txt":
            raise ValueError(f"只支持解析 .txt 文件: {self.file_path}")

        with self.file_path.open("r", encoding="utf-8") as file:
            return file.readlines()

    def print_lines(self) -> None:
        for line_number, line in enumerate(self.read_lines(), start=1):
            print(f"第{line_number}行: {line.rstrip()}")


if __name__ == "__main__":
    sample_path = "example.txt"
    parser = TxtFileParser(sample_path)
    parser.print_lines()
