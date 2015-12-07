import copy

from bs4 import BeautifulSoup
from bs4 import NavigableString


def open_html_document_in_beautifulsoup(input_doc):
    """

    :param input_doc:
    :return: BeautifulSoup instance
    """
    return BeautifulSoup(open(input_doc), 'html5lib')


def find_container_p_tags(document):
    """
    Finds the p_tags containing <img> in the document as a list

    """
    ret = []

    for p_tag in document.findAll('p'):
        if has_img_tag(p_tag):
            ret.append(p_tag)
    return ret


def beautify_content(doc, p_tag):
    """
    First insert all the elements after the current p_tags in order and then destroy the current tag
    :param doc:
    :param p_tag:
    :return: None
    """
    p_tag_contents = p_tag.contents
    current = p_tag
    for i in range(len(p_tag_contents)):
        item = copy.copy(p_tag_contents[i])
        if isinstance(item, NavigableString):
            new_element = doc.new_tag('p')
            new_element.string = item
            current.insert_after(new_element)
            current = current.next_sibling
        else:
            current.insert_after(item)
            current = current.next_sibling
    p_tag.decompose()


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


def has_img_tag(tag):
    ret = False
    for child_tag in tag.findChildren():
        if child_tag.name == 'img':
            return True
    return ret


if __name__ == '__main__':
    input_document = raw_input('Please enter full path of your html document: ')
    html_doc = open_html_document_in_beautifulsoup(input_document)
    img_tags = find_img_tags(html_doc)
    normalize_img_tags(img_tags)
    for tag in find_container_p_tags(html_doc):
        beautify_content(html_doc, tag)


    result = open('result.html', 'w')
    result.write(html_doc.prettify())
    result.close()





