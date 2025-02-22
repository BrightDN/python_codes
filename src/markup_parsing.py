import re

def extract_markdown_images(text):
    """Extracts all properly formatted Markdown images from text.
    
    Args:
        text (str): The Markdown text to parse
        
    Returns:
        list[tuple]: A list of tuples, each containing (alt_text, url)
        If no images are found, returns an empty list
        
    Examples:
        >>> text = "![alt text](image.jpg)" # Valid image
        >>> extract_markdown_images(text)
        [('alt text', 'image.jpg')]

        >>> text = "![alt text www.example.com)"   # invalid image syntax
        >>> extract_markdown_image(text)
        []
    """
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex, text)
    cleaned_matches = [(text.strip(), clean_url(url)) for text, url in matches]
    return cleaned_matches

def extract_markdown_links(text):
    """Extracts all properly formatted Markdown links from text.
    
    Args:
        text (str): The Markdown text to parse
        
    Returns:
        list[tuple]: A list of tuples, each containing (clickable text, url)
        If no links are found, returns an empty list
        
    Examples:
        >>> text = "[click me](www.example.com)"  # valid link
        >>> extract_markdown_links(text)
        [('click me', 'www.example.com')]

        >>> text = "[click me www.example.com)"   # invalid link syntax
        >>> extract_markdown_links(text)
        []
    """
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_regex, text)
    cleaned_matches = [(text.strip(), clean_url(url)) for text, url in matches]
    return cleaned_matches

def clean_url(url):
    return re.sub(r'\s+', '', url)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    