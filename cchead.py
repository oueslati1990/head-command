import argparse
import sys


def read_file(filename):
    """ Read a file"""
    with open(filename, 'r') as f:
        return f.read()
    
def main():
    """Main flow"""
    parser = argparse.ArgumentParser(
        description="cchead argument parser"
    )

    parser.add_argument('filename', nargs='?', default=None,
                        help="file to read")
    args = parser.parse_args()

    try:
        content = ''
        if args.filename:
            content = read_file(args.filename)
        else:
            content = sys.stdin.buffer.read()
    except FileNotFoundError:
        print(f'file {args.filename} does not exist', file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f'You are not permitted to access this file {args.filename}', file=sys.stderr)
        exit(1) 

    print(content)

if __name__ == '__main__':
    main()