import sys
import os
import textwrap

def process_file(file_path):
    pages = []
    with open(file_path, 'r') as file:
        # Split content by newlines to preserve intended paragraph breaks
        paragraphs = file.read().replace('"', "''").split('\n')
        for paragraph in paragraphs:
            if paragraph:  # Check if paragraph is not empty
                # Wrap each paragraph individually, respecting the 30 character limit
                wrapped_paragraph = textwrap.wrap(paragraph, width=30, replace_whitespace=False, break_long_words=True)
                pages.extend(wrapped_paragraph)
            else:
                # Preserve paragraph breaks as empty lines
                pages.append("")
    # Organize wrapped lines into pages of up to 10 lines each
    page_chunks = [pages[i:i + 10] for i in range(0, len(pages), 10)]
    return page_chunks

def generate_ti_basic_code(output_file_path, input_file_paths):
    template_start = "ClrHome\nClrDraw\nGridOff\nAxesOff\nLbl B\nMenu(\"NOTES\","

    template_end = """
Lbl E
ClrHome
ClrDraw
AxesOn
Return
"""

    sections = []
    menu_items = []
    label_char = ord('Q')  # Start with label Q because earlier characters may be used

    for file_path in input_file_paths:
        file_name = os.path.splitext(os.path.basename(file_path))[0].capitalize()
        pages = process_file(file_path)
        page_count = len(pages)
        menu_items.append(f'"{file_name}",{chr(label_char)}')
        section = f'\n\n"Section for {file_name}"\nLbl {chr(label_char)}\n0→P\nWhile P<{page_count}\n'
        for i, page in enumerate(pages):
            section += f'  If P={i}:Then\n  ClrDraw\n'
            for j, line in enumerate(page):
                section += f'  Text({j*6},0,"{line}")\n'
            section += '  End\n'
        section += """
  0→K
  While not(K=34 or K=25 or K=45)
    getKey→K
  End
  
  If K=25 and P:P-1→P
  If K=34:P+1→P
  If K=45:""" + f"{page_count}→P\nEnd\nGoto B"
        sections.append(section)
        label_char += 1

    menu_items.append('"Exit",E')
    
    full_code = template_start + ','.join(menu_items) + ")" + ''.join(sections) + template_end
    
    # Specify UTF-8 encoding to support "→"
    with open(output_file_path, "w", encoding='utf-8') as output_file:
        output_file.write(full_code)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 generateTICode.py output_file.txt input_file1.txt [input_file2.txt ...]")
    else:
        output_file_path = sys.argv[1]
        input_file_paths = sys.argv[2:]
        generate_ti_basic_code(output_file_path, input_file_paths)
        print(f"Ti-BASIC code generated and saved to {output_file_path}.")