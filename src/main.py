import os
import sys
from textnode import *
from helper import *


def copy_static_to_public():
    print("copying static files to public folder")
    if not os.path.exists('docs'):
        os.mkdir('docs')
    os.system("rm -rf docs/*")
    os.system("cp -r static/* docs")
    

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception('No title found in markdown')


def generate_page(basepath, from_path, template_path, dest_path):
    with open(from_path, 'r') as f:
        markdown = f.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    with open(template_path, 'r') as f:
        template = f.read()
    template = re.sub(r"\{\{\s*Title\s*\}\}", title, template)
    template = re.sub(r"\{\{\s*Content\s*\}\}", content, template)
    template = re.sub(r'href="/', f'href="{basepath}/', template)
    template = re.sub(r'src="/', f'src="{basepath}/', template)
    
    with open(dest_path, 'w') as f:
        f.write(template)


def generate_page_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    print(f'Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}')
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item.replace('.md', '.html'))
        if os.path.isdir(from_path):
            os.mkdir(f'{dest_dir_path}/{item}')
            generate_page_recursive(basepath, from_path, template_path, dest_path)
        elif item.endswith('.md'):
            generate_page(basepath, from_path, template_path, dest_path)


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = ''
    copy_static_to_public()
    generate_page_recursive(basepath, 'content/', 'template.html', 'docs/')


main()
