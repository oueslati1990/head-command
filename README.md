# head-command

A Python implementation of the Unix `head` command. This tool displays the first part of files, allowing you to view the beginning of one or more files or standard input.

## Features

- Display the first N lines of files (default: 10 lines)
- Display the first N bytes of files
- Support for multiple files with automatic headers
- Read from standard input when no files are provided
- Error handling for missing or inaccessible files

## Installation

```bash
pip install .
```

After installation, you can use the `cchead` command directly from your terminal.

## Usage

### Display first 10 lines (default)
```bash
cchead test.txt
```

### Display first N lines
```bash
cchead -n 5 test.txt
cchead --lines 5 test.txt
```

### Display first N bytes
```bash
cchead -c 100 test.txt
cchead --bytes 100 test.txt
```

### Process multiple files
```bash
cchead -n 20 test.txt test2.txt
```

### Read from standard input
```bash
cat test.txt | cchead -n 5
echo "Hello, World!" | cchead
```

## Testing

Run the test suite:
```bash
python cchead_tests.py
```

## License

MIT License - see LICENSE file for details.

## Author

Mohamed Oueslati