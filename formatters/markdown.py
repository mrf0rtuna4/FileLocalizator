import markdown

def localize_markdown(file_path, localization_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    markdown_html = markdown.markdown(markdown_text)

    for key, value in localization_dict.items():
        markdown_html = markdown_html.replace(key, value)

    return markdown_html