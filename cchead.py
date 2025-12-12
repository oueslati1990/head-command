import argparse
import sys


def read_file(filename):
    """ Read a file"""
    with open(filename, 'rb') as f:
        return f.read()
    
def main():
    """Main flow"""
    parser = argparse.ArgumentParser(
        description="cchead command"
    )

    parser.add_argument('filename', nargs='?', default=None,
                        help="file to read")
    parser.add_argument('-n', '--lines', type=int, default=10,
                        help="Display the first n lines")
    
    args = parser.parse_args()

    try:
        content_byte = b''
        if args.filename:
            content_byte = read_file(args.filename)
        else:
            content_byte = sys.stdin.buffer.read()
    except FileNotFoundError:
        print(f'file {args.filename} does not exist', file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f'You are not permitted to access this file {args.filename}', file=sys.stderr)
        exit(1) 

    output_content = ''
    content_str = content_byte.decode('utf-8').strip().split('\n')
    num_lines = min(args.lines, len(content_str)) 
    for i, line in enumerate(content_str[:num_lines]):
        output_content += line + '\n' if i < num_lines-1 else line

    print(output_content)

if __name__ == '__main__':
    main()