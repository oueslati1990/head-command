import argparse
import sys
from typing import Dict


def read_file(filename):
    """ Read a file"""
    with open(filename, 'r') as f:
        return f.read()
    
def get_output_lines(input_lines, content_str) -> str:
    """Get the output of the first number of lines of the content"""
    output_content = ''
    content = content_str.strip().split('\n')
    num_lines = min(input_lines, len(content)) 
    for i, line in enumerate(content[:num_lines]):
        output_content += line + '\n' if i < num_lines-1 else line

    return output_content

def get_output_bytes(input_bytes, content_str) -> str:
    """Get the output of the first number of bytes of the content"""
    num_bytes = min(input_bytes, len(content_str))
    return content_str[:num_bytes]
    
def main():
    """Main flow"""
    parser = argparse.ArgumentParser(
        description="cchead command"
    )

    parser.add_argument('filenames', nargs='*', default=None,
                        help="file to read")
    parser.add_argument('-n', '--lines', type=int, default=10,
                        help="Display the first n lines")
    parser.add_argument('-c', '--bytes', type=int, default=None,
                        help="Display the num first bytes")
    
    args = parser.parse_args()

    try:
        content_dict:Dict[str, str] = {}
        if args.filenames:
            for f in args.filenames:
                content_dict[f] = read_file(f)
        else:
            content_dict["stdin"] = sys.stdin.buffer.read().decode('utf-8')
    except FileNotFoundError:
        print(f'file {f} does not exist', file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f'You are not permitted to access this file {f}', file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"{args.filename}: {e}", file=sys.stderr)
        sys.exit(1) 

    output_content = ''
        
    if args.bytes:
        for name, content in content_dict.items():
            if name != "stdin" and len(content_dict) > 1:
                output_content += f"==> {name} <==\n"
            output_content += get_output_bytes(args.bytes, content) + "\n\n"
        
    elif args.lines:
        for name, content in content_dict.items():
            if name != "stdin" and len(content_dict) > 1:
                output_content += f"==> {name} <==\n"
            output_content += get_output_lines(args.lines, content) + "\n\n"

    print(output_content)

if __name__ == '__main__':
    main()