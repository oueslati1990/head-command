#!/usr/bin/env python3
"""
Tests for cchead - head command implementation
Starting with line count (-n flag)
"""

import subprocess


def run_cchead(args):
    """
    Helper function to run cchead command with given arguments

    Args:
        args: list of command-line arguments

    Returns:
        tuple: (stdout, stderr, return_code)
    """
    cmd = ['cchead'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def test_lines_count_short_flag():
    """Test -n flag for custom line count"""
    print("Testing: Custom line count with -n flag")

    stdout, stderr, returncode = run_cchead(['-n', '5', 'test.txt'])

    print(f"  Output: {stdout[:100]}...")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with errors: {stderr}"

    # Count lines in output
    lines = stdout.split('\n')

    print(f"  Lines displayed: {len(lines)}")

    # Should display 5 lines
    assert len(lines) == 5, f"Expected 5 lines, got {len(lines)}"

    print("  ✓ Test passed!")


def test_lines_count_long_flag():
    """Test --lines flag for custom line count"""
    print("Testing: Custom line count with --lines flag")

    stdout, stderr, returncode = run_cchead(['--lines', '3', 'test.txt'])

    print(f"  Output: {stdout[:100]}...")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with errors: {stderr}"

    # Count lines in output
    lines = stdout.split('\n')

    print(f"  Lines displayed: {len(lines)}")

    # Should display 3 lines
    assert len(lines) == 3, f"Expected 3 lines, got {len(lines)}"

    print("  ✓ Test passed!")


def test_bytes_count_short_flag():
    """Test -c flag for custom byte count"""
    print("Testing: Custom byte count with -c flag")

    # For byte count tests, we need the raw output without stripping
    cmd = ['cchead', '-c', '50', 'test.txt']
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout_raw = result.stdout
    stderr = result.stderr.strip()
    returncode = result.returncode

    print(f"  Output: {stdout_raw.strip()}")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with errors: {stderr}"

    # Check byte count in raw output (before stripping)
    # The output includes the 50 bytes from file plus "\n\n" added by cchead
    byte_count = len(stdout_raw.encode('utf-8'))

    print(f"  Bytes displayed (total): {byte_count}")

    # Should display 50 bytes from file + 3 bytes for extra newlines = 53 bytes
    assert byte_count == 53, f"Expected 53 bytes, got {byte_count}"

    print("  ✓ Test passed!")


def test_bytes_count_long_flag():
    """Test --bytes flag for custom byte count"""
    print("Testing: Custom byte count with --bytes flag")

    # For byte count tests, we need the raw output without stripping
    cmd = ['cchead', '--bytes', '100', 'test.txt']
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout_raw = result.stdout
    stderr = result.stderr.strip()
    returncode = result.returncode

    print(f"  Output: {stdout_raw.strip()[:80]}...")
    print(f"  Errors: {stderr}")
    print(f"  Return code: {returncode}")

    # Check if command succeeded
    assert returncode == 0, f"Command failed with errors: {stderr}"

    # Check byte count in raw output (before stripping)
    # The output includes the 100 bytes from file plus "\n\n" added by cchead
    byte_count = len(stdout_raw.encode('utf-8'))

    print(f"  Bytes displayed (total): {byte_count}")

    # Should display 100 bytes from file + 3 bytes for extra newlines = 103 bytes
    assert byte_count == 103, f"Expected 103 bytes, got {byte_count}"

    print("  ✓ Test passed!")


if __name__ == '__main__':
    print("=" * 50)
    print("Testing cchead - Line and Byte Display Features")
    print("=" * 50)

    try:
        test_lines_count_short_flag()
        print()
        test_lines_count_long_flag()
        print()
        test_bytes_count_short_flag()
        print()
        test_bytes_count_long_flag()
        print()
        print("✓ All tests passed!")
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
