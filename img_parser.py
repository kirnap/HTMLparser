from bs4 import BeautifulSoup


def open_html_document_in_beautifulsoup(input_doc):
    """

    :param input_doc:
    :return: BeautifulSoup instance
    """
    return BeautifulSoup(open(input_doc), 'html5lib')


def find_p_tags(document):
    """
    Finds the p_tags in the document as a list

    """
    return document.findAll('p')


def insert_img_tag_after_p_tag(p_tag_list):
    """
    Takes p_tag list as an input and finds the img tags in each p tag in list and insert immediately after
    the parent p tag in the document

    """
    for p_tag in p_tag_list:
        for tag in p_tag.findChildren():
            if tag.name == 'img':
                p_tag.insert_after(tag)


def find_img_tags(document):
    """
    Returns the img_tags in the document as a list

    """
    return document.findAll('img')


def normalize_img_tags(img_list):
    """

    Takes img tag  and if the style attribute of a given tag has a width value of 590, then
    width value becomes 710 and the height value decomposed

    """

    for img in img_list:
        # Check the img tag has an attribute of style
        if 'style' in img.attrs:
            if 'width:590px' in img.attrs['style']:
                img.attrs['style'] = "width:710px;"
        # Check the img tag has an attribute of width and height other than style
        if 'width' in img.attrs:
            if '590' in img.attrs['width']:
                img.attrs['width'] = '710'
                if 'height' in img.attrs:
                    del img.attrs['height']


if __name__ == '__main__':
    input_document = raw_input('Please enter full path of your html document: ')
    html_doc = open_html_document_in_beautifulsoup(input_document)
    img_tags = find_img_tags(html_doc)
    normalize_img_tags(img_tags)

    # p_tags_in_html_doc = find_p_tags(html_doc)
    # insert_img_tag_after_p_tag(p_tags_in_html_doc)

    result = open('result.html', 'w')
    result.write(html_doc.prettify())
    result.close()





