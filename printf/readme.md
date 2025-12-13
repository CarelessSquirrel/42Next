`This project has been created as a part of the 42 curriculum by:` <jabettin>.


## Description ##
ft_printf as a program, should- almost exactly replicate the behavior of printf from the standard input, output library, or just: <stdio.h>. With a few exceptions, which are stated in the subject file of ft_printf.
Printf's functionality at it's core could simply be summarized as follows: We want to keep looping through the format string until we find a delimiter. 
In the case of printf, this delimiter is the `'%'`. When this delimiter is found, the next step is to read one index past the delimiter, to identify the `format specifier`. The format specifier tells printf what datatype the user wants being printed. i.e: *`%s`* or *`%i`*.


## Instructions ##
Because ft_printf makes use of a Makefile, as required by the subject file. The first step is to write `make` in your terminal.
Now we can compile. This will happen with the three standard flags: -Wall -Wextra -Werror and is typed as follows:
`cc -Werror -Wall -Wextra libftprintf.a main.c -o test`
After which it can be ran using **./test**.
To get rid of the `.a` and `.o` file(s) after having used `make`
you can either write: `make clean` which will get rid of all the `.o` files, but leaves the **libftprintf.a**
If you also want to clean that file make sure to use the following command: `make fclean`. **make fclean will also get rid of any `.o` files**



## Resources ##
For this project i used information from the Gitbook posted by <Laura> from: `https://42-cursus.gitbook.io/guide/1-rank-01/ft_printf`
Aswell as the Wikipedia page on the standard C library function printf from: `https://en.wikipedia.org/wiki/Printf`
Aswell as AI to write the flow of my ft_printf down below.


## Key concepts/syntax of this ft_printf project ##


**Be aware of the fact that, before turning this code in, you might, or will have to remove one of the following file(s): main.c, test**