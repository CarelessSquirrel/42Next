`This project has been created as a part of the 42 curriculum by: jabettin`


## Description ##
ft_printf as a program, should- almost exactly replicate the behavior of printf from the standard input, output library, or just: <stdio.h>. With a few exceptions, which are stated in the subject file of ft_printf. This ft_printf does **NOT** include the bonus excercise
Printf at its core, could be simply summarized as follows: printf works by iterating over the format string character by character. When a `%` character is encountered, it signals the start of a format instruction. The character following % is interpreted as a `format specifier`, which determines how the next argument from the `variadic argument list` should be processed and printed. For example: *`%s`*, *`%d`*. All other characters are printed directly to the standard output


## Instructions ##
Because ft_printf makes use of a Makefile, as required by the subject file. The first step is to write `make` in your terminal.
Now we can compile. This will happen with the three standard flags: -Wall -Wextra -Werror and is typed as follows:
`cc -Werror -Wall -Wextra libftprintf.a main.c -o test`
After which it can be ran using **./test**.
To get rid of the `.a` and `.o` file(s) after having used `make`
you can either write: `make clean` which will get rid of all the `.o` files, but leaves the **libftprintf.a**
If you also want to clean that file make sure to use the following command: `make fclean`. **make fclean will also get rid of any `.o` files**



## Resources ##
For this project i used information from the Gitbook posted by Laura from: `https://42-cursus.gitbook.io/guide/1-rank-01/ft_printf`
Aswell as the Wikipedia page on the standard C library function printf from: `https://en.wikipedia.org/wiki/Printf`
Aswell as AI to write the flow of my ft_printf down below.



## Flow of ft_printf ##

You call 
`ft_printf("Hello %s, number: %d, hex: %x\n", "world", 42, 42);`


1. **Initial Setup**

* `ft_printf` is called with:

  * `format = "Hello %s, number: %d, hex: %x\n"`
  * Variadic arguments: `"world"`, `42`, `42`
* A `va_list args` is initialized using `va_start`.
* Index `i` is set to `0`.
* `count` is set to `0` to track the total number of characters written.

---

2. **Iterating Through the Format String**

The function loops through the format string character by character.

 Characters before `%`

* Characters `'H'`, `'e'`, `'l'`, `'l'`, `'o'`, and `' '` are encountered.
* Each character is written directly using `write(1, &format[i], 1)`.
* `count` is incremented for each printed character.

At this point:

* Output: `"Hello "`
* `count = 6`

3. **Encountering `%`**

* `format[i] == '%'` is detected.
* Index `i` is incremented to look at the format specifier.
* `format[i] == 's'`, so `handle_conversion('s', args)` is called.

4. **Handling the Conversion (`%s`)**

Inside `handle_conversion`:

* `va_arg(args, char *)` retrieves `"world"` from the argument list.
* `print_str("world")` is called:

  * The string length is calculated (`5`)
  * `"world"` is written using `write`
  * `5` is returned

Back in `ft_printf`:

* `count += 5`

At this point:

* Output: `"Hello world"`
* `count = 11`

5. **Continuing After the Conversion**

* The loop continues.
* Literal characters `", number: "` are written one by one.
* `count` is updated accordingly.

At this point:

* Output: `"Hello world, number: "`

6. **Handling `%d` (Decimal Integer)**

* `%` is found again.
* `handle_conversion('d', args)` is called.
* `va_arg(args, int)` retrieves `42`.

Inside `print_decimal(42)`:

* The number is positive → no minus sign printed.
* `ft_putnbr_unsigned(42, 10, "0123456789")` is called.
* Digits are printed recursively (`'4'`, then `'2'`).
* `2` characters are written and counted.

7. **Handling `%x` (Hexadecimal)**

* `%x` is encountered.
* `va_arg(args, unsigned int)` retrieves `42`.

Inside `print_hex(42, 0)`:

* `ft_putnbr_unsigned(42, 16, "0123456789abcdef")` is called.
* The number is printed as `"2a"`.
* `2` characters are written.

8. **End of Format String**

* Remaining characters (including `\n`) are printed normally.
* The loop exits when `format[i] == '\0'`.
* `va_end(args)` is called.
* `count` is returned.

Final output: Hello world, number: 42, hex: 2a



## Key concepts / syntax of this ft_printf project ##

* **`format` string**: The template string that controls output. Regular characters are printed directly, `%` introduces a conversion.
* **`va_list args`**: Holds the variadic arguments passed to `ft_printf`. Arguments are consumed in order using `va_arg`.
* **`%` specifier**: Signals that the next character determines how the next argument should be printed.
* **`handle_conversion`**: Dispatches the correct print function based on the format specifier (`c`, `s`, `d`, `x`, etc.).
* **Conversion functions** (`print_str`, `print_decimal`, `print_hex`, …): Each handles a specific data type and returns the number of characters written.
* **`ft_putnbr_unsigned`**: Core number-printing helper that converts numbers to any base using recursion.
* **`count`**: Tracks and accumulates the total number of characters written, matching the behavior of the real `printf`.
* **Direct `write` calls**: All output is written directly to file descriptor `1` (stdout), without buffering.

---
**`Be aware of the fact that, before turning this code in, you might, or will have to remove one of the following file(s): main.c, test`**