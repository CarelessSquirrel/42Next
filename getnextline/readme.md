This project has been created as a part of the 42 curriculum by: jabettin.


## Description ##
GNL is a program that should "split" sentences in a text file when it finds a delimiter.
In the case of GNL, this delimiter is the newline character.
The sentences after finding a newline will be split underneath one another, just like in regular writing.
It does so by looping through the entire array looking for the provided delimiter, which in this case has been set to be the newline character.


## Instructions
The compiling will happen with the three standard flags, -Wall -Wextra -Werror and is typed as follows:
`cc -Werror -Wall -Wextra ./main.c ./get_next_line.c ./get_next_line_utils.c -D BUFFER_SIZE=4 -o test`
After which it can be ran using **./test**.


## Resources ##
For this project i used the information by LAnnur-s from the website Medium.
`https://medium.com/@lannur-s/gnl-c3cff1ee552b`
I also used valgrind and francinette for testing purposes, and to look for any memory leaks.





You call `get_next_line(fd)` for the first time:

1. **Initial Setup**

   * A **static pointer `remainder`** is declared. Right now, it’s `NULL`.
   * A **buffer** of size `BUFFER_SIZE + 1` (5 bytes) is allocated to store data read from the file.
   * `bytes_read` is set to 1 so we can enter the read loop.

---

2. **First Read (first 4 bytes)**

   * `read(fd, buffer, 4)` reads `"hell"` from the file.
   * `buffer[4] = '\0'` → buffer is now `"hell"`.
   * `join_free(remainder, buffer)` is called:

     * `remainder` is `NULL`, so only `buffer` is copied.
     * A new string `"hell"` is allocated and returned.
     * `remainder` now points to `"hell"`.
     * `buffer` is freed inside `join_free`.
   * **Check for newline**: `ft_strchr(remainder, '\n')` → no newline yet.
   * Loop continues.

3. **Second Read (next 4 bytes)**

   * `read(fd, buffer, 4)` reads `"o\nWo"`.
   * `buffer[4] = '\0'` → buffer is `"o\nWo"`.
   * `join_free(remainder, buffer)` is called:

     * `remainder` is `"hell"`, `buffer` is `"o\nWo"`.
     * A new string `"hello\nWo"` is allocated.
     * `remainder` is updated to point to `"hello\nWo"`.
     * `buffer` is freed.
   * **Check for newline**: `ft_strchr(remainder, '\n')` → newline found at index 5 (`"hello\n"`).
   * Loop exits.

4. **Extract the Line**

   * `extract_line(&remainder)` is called.
   * `nl_ptr = ft_strchr(remainder, '\n')` → points to the `\n` in `"hello\nWo"`.
   * `len = nl_ptr - *remainder + 1 = 5 - 0 + 1 = 6` → we want 6 characters including newline.
   * `line = ft_substr(remainder, 0, 6)` → line is `"hello\n"`.
   * `update_remainder(remainder, 6)` is called:

     * `old = "hello\nWo"`, `start = 6`.
     * `old[6]` is `'W'` → not null.
     * `ft_substr(old, 6, ft_strlen(old) - 6)` → substring from index 6 to end → `"Wo"`.
     * `remainder` is updated to `"Wo"`.
   * Return `"hello\n"` from `get_next_line`.

5. **Second Call to `get_next_line(fd)`**

   * `remainder = "Wo"` from previous call.
   * Buffer is allocated again.
   * `read(fd, buffer, 4)` → reads `"rld\n"` (next 4 bytes).
   * `buffer[4] = '\0'` → buffer is `"rld\n"`.
   * `join_free(remainder, buffer)` → `"Wo"` + `"rld\n"` → `"World\n"`.
   * Check for newline → found at index 5.
   * `extract_line(&remainder)`:

     * `len = 6` → `"World\n"` is extracted.
     * `update_remainder("World\n", 6)` → nothing left → remainder = `NULL`.
   * Return `"World\n"`.

6. **Third Call to `get_next_line(fd)`**

   * `remainder = NULL`.
   * `read(fd, buffer, 4)` → reads `"42"` (last bytes).
   * `buffer[2] = '\0'` → buffer = `"42"`.
   * `join_free(remainder, buffer)` → remainder = `"42"`.
   * Check for newline → not found.
   * `read(fd, buffer, 4)` → returns 0 (EOF).
   * `extract_line(&remainder)`:

     * No newline, copy entire remainder → `"42"`.
     * Free remainder → remainder = `NULL`.
   * Return `"42"`.

7. **Fourth Call to `get_next_line(fd)`**

   * `remainder = NULL`.
   * `read(fd, buffer, 4)` → returns 0 (EOF).
   * `get_next_line` returns `NULL` → end of file reached.



### Key concepts/syntax of this GNL project ##

* **`buffer`**: Temporary array where each chunk of the file is read. Freed after each iteration.
* **`remainder`**: Persistent storage across calls, holds data that was read but not yet returned as a line.
* **`nl_ptr`**: Pointer inside `remainder` to the first occurrence of `\n`.
* **`extract_line`**: Takes a line from `remainder` up to and including `\n`, updates remainder to only leftover data.
* **`update_remainder`**: Removes the extracted part from `remainder`.
* **Static `remainder`**: Enables `get_next_line` to “remember” leftover data between multiple calls.

