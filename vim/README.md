# Vim

## TL;DR: to exit vim hit `esc` to enter "normal mode" followed by `:q!` and hit `enter`

## What is Vim?

[Vim](https://www.vim.org/)'s official site will tell you it is a "highly configurable text editor".

## Why Vim?

simply because it makes me feel really cool while coding! However, there are
many features that Vim a viable option as your text editor of choice.

* highly portable as its included in Linux and macOS
* fast and efficient as it can be fully navigated with your keyboard
* supports a wide array of plug-ins that greatly enhance the vim's
  functionality 

## Modes

The first thing to understand about Vim is its different modes. 

* Normal mode
	* Vim's default when started
	* Keyboard input will not write to the file, but rather, have special
	  commands assigned to them. These commands are explained further below.
* Insert mode
	* Enter Insert mode by pressing `i` when in Normal mode 
	* More in line with what you'd expect from a text editor. What you type
	  should appear on screen.
* Visual mode
	* Enter Visual mode by pressing `v` when in Normal mode
	* Select text akin to how a mouse would behave
	* There are three subtypes to visual mode: visual, block-visual, and
	  linewise-visual
* Command mode
	* Enter Command mode by pressing `:` when in Normal mode
	* Read about the available commands using `:h` or `:help`
* Replace mode
	* Enter Replace mode by pressing `R` when in Normal mode
	* Starting with your cursor placement, whatever you type will replace
	  existing text

## Text Editing

> To being, I'll organize this the same way as `vimtutor` and rewrite it in a more cohesive manner afterwards

| Command     | Description |
| ----------- | ----------- |
| j | move cursor down one line         |
| k | move cursor up one line                |
| h | move cursor to the left one character  |
| l | move cursor to the right one character |

The j, k, h, l keys act much like like the arrow keys typically do on a keyboard.

## Resources Used

* [vimtutor](https://linux.die.net/man/1/vimtutor)
* [Vim Editor Modes Explained](https://www.freecodecamp.org/news/vim-editor-modes-explained/) 

