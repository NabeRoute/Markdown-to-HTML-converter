import markdown
import sys

def convert_markdown_to_html(markdown_path, html_path):
    try:
        with open(markdown_path, "r", encoding='utf-8') as markdown_file:
            markdown_text = markdown_file.read()
        
        html = markdown.markdown(markdown_text)

        with open(html_path, "w", encoding='utf-8') as html_file:
            html_file.write(html)
        
        print(f"Markdown file {markdown_path} has been converted to HTML and saved to {html_path}.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 file-converter.py <inputfile.md> <outputfile.html>")
        sys.exit(1)
    
    markdown_path = sys.argv[1]
    html_path = sys.argv[2]

    convert_markdown_to_html(markdown_path, html_path)