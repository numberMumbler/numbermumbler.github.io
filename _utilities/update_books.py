#! /usr/bin/env python3
"""
generate the recently read book data
"""
import os
from xml.dom import minidom
import json
import requests
import argparse


_GOODREADS_URL_TEMPLATE = 'https://www.goodreads.com/review/list/{user_id}.xml' \
    '?key={key}&v=2&shelf=read&sort=date_read&order=d&per_page={n}&page=1'


def get_recent_books(user_id, count=10):
    """
    get basic data for recently read books
    """
    goodreads_xml = get_goodreads_recently_read(user_id, count)
    dom = minidom.parseString(goodreads_xml)
    results = []
    for book_node in dom.getElementsByTagName("book"):
        book = {'title': get_text(book_node, 'title'),
                'title_without_series': get_text(book_node, 'title_without_series'),
                'link': get_text(book_node, 'link'),
                'image_url': get_text(book_node, 'image_url')}
        results.append(book)
    return results


def get_text(root_node, tag_name):
    """
    get the text from a node's children
    """
    values = []
    nodes = root_node.getElementsByTagName(tag_name)
    while len(nodes):
        node = nodes.pop(0)
        if node.nodeType == node.TEXT_NODE:
            values.append(node.data.strip())
        elif node.hasChildNodes():
            nodes.extend(node.childNodes)
    return ''.join(values)


def get_goodreads_recently_read(user_id, count):
    """
    get recently read books from Goodreads API
    """
    url = _GOODREADS_URL_TEMPLATE.format(key=get_key(), user_id=user_id, n=count)
    response = requests.get(url)
    assert response.status_code == 200
    return response.content


def write_json_file(data, file_path):
    """
    write the data to a file as json
    """
    with open(file_path, 'w') as out_file:
        json.dump(data, out_file, sort_keys=True, indent=2, separators=(',', ': '))


def get_key():
    """
    return Goodreads API key
    """
    return os.environ['GOODREADS_KEY']


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("goodreads_id", help="Goodreads user ID", type=int)
    parser.add_argument("out_path", help="where to write the data", type=str)
    return parser.parse_args()


def main():
    args = get_args()
    book_data = get_recent_books(args.goodreads_id)
    write_json_file(book_data, args.out_path)


if __name__ == '__main__':
    main()
