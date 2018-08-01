# Suppose we represent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory
# subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1
# contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2
# contains a second-level sub-directory subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path
# to a file within our file system. For example, in the second example above, the
# longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is
# 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the
# length of the longest absolute path to a file in the abstracted file system.
# If there is no file in the system, return 0.
#
# Note:
#
# The name of a file contains at least a period and an extension.
#
# The name of a directory or sub-directory will not contain a period.


def longest_file_path(filesystem):
    length = 0
    dirs = {}
    lines = filesystem.split('\n')
    # we go through each line and calculate its total length.
    # we check if it's the new max (if it's a file)
    # or add it to the dictionary of directories, together with its
    # total length, so it doesn't need to be calculated again.
    # this way is efficient because the parent directory of the file/directory
    # is always in an earlier line.
    for i, s in enumerate(lines):
        level = s.count('\t')
        total_length = find_total_length(s, level, dirs)
        if '.' in s:
            length = max(length, total_length)
        else:
            dirs.update({i: (total_length, level)})
    return length


def find_total_length(s, level, dirs):
    own_length = len(s) - level
    if level == 0:
        return own_length
    else:
        parent_index = max(
            [i for i, (_, lev) in dirs.items() if lev == level - 1])
        parent_length = dirs[parent_index][0]
        return own_length + parent_length + 1
