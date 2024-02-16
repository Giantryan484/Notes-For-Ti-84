# Ti-BASIC Notes Generator

## Overview

This Python script automates the generation of Ti-BASIC files for displaying notes on TI-84 calculators. It is designed to take multiple text files as input, each containing notes on different subjects, and generates a single Ti-BASIC program. This program allows users to view their notes directly on their TI-84 calculators through a simple menu-driven interface.

The script processes each text file, formats the content into pages and lines according to the display constraints of the TI-84 calculator, and generates Ti-BASIC code that can be transferred to a TI-84 calculator for study and reference purposes.

## Prerequisites

- Python 3.x installed on your computer.
- A TI-84 (or compatible) calculator to transfer and run the generated Ti-BASIC code.
- Some method to compile and transfer the file to your calculator (I personally use a combination of TokensIDE and TiLP)

## How to Use It

1. **Prepare Your Notes**: Create text files containing the notes you want to display on your TI-84 calculator. Each text file represents a different subject or category of notes.

2. **Run the Script**: Use the command line to navigate to the directory containing the script and your notes files. Run the script with the following syntax:

    ```bash
    python3 generateTICode.py output_file.txt input_file1.txt [input_file2.txt ...]
    ```

    - `output_file.txt` is the name of the Ti-BASIC program file that will be generated.
    - `input_file1.txt`, `input_file2.txt`, ... are the text files containing your notes.

3. **Compile the Output file to `.8xp`**: This can be done in a wide variety of ways, but personally I use the [TokensIDE](https://www.ticalc.org/archives/files/fileinfo/433/43315.html) code editor.

4. **Transfer the Ti-BASIC (`.8xp`) Program to Your Calculator**: Again, there's dozens of ways to do this. Personally I use [TiLP](http://lpg.ticalc.org/prj_tilp/), but [TI Connect](https://education.ti.com/en/products/computer-software/ti-connect-sw) is a more user-friendly alternative.

5. **View Your Notes**: Run the transferred Ti-BASIC program on your calculator. Use the menu to navigate to the different subjects and pages of notes.

## An Example

If you have three sets of notes named `Math.txt`, `Chemistry.txt`, and `Physics.txt`, run the script like this:

```bash
python3 generateTICode.py NOTES.txt Math.txt Chemistry.txt Physics.txt
```

This will create a `NOTES.txt` file containing the Ti-BASIC code. Compile and transfer `NOTES.8xp` to your calculator to access your notes.

## Contributing

Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.
