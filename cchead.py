import argparse
import sys


def read_file(filename):
    """ Read a file"""
    with open(filename, 'rb') as f:
        return f.read()
    
def get_output_lines(input_lines, content_byte) -> str:
    """Get the output of the first number of lines of the content"""
    output_content = ''
    content_str = content_byte.decode('utf-8').strip().split('\n')
    num_lines = min(input_lines, len(content_str)) 
    for i, line in enumerate(content_str[:num_lines]):
        output_content += line + '\n' if i < num_lines-1 else line

    return output_content

def get_output_bytes(input_bytes, content_byte) -> str:
    """Get the output of the first number of bytes of the content"""
    num_bytes = min(input_bytes, len(content_byte))
    return content_byte[:num_bytes].decode('utf-8')
    
def main():
    """Main flow"""
    parser = argparse.ArgumentParser(
        description="cchead command"
    )

    parser.add_argument('filename', nargs='?', default=None,
                        help="file to read")
    parser.add_argument('-n', '--lines', type=int, default=10,
                        help="Display the first n lines")
    parser.add_argument('-c', '--bytes', type=int, default=None,
                        help="Display the num first bytes")
    
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
    
    
    if args.bytes:
        output_content = get_output_bytes(args.bytes, content_byte)
    elif args.lines:
        output_content = get_output_lines(args.lines, content_byte)

    print(output_content)

if __name__ == '__main__':
    main()