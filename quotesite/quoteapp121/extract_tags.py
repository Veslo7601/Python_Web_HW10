from django import template

register = template.Library()


def tags(q_tags):
    return ', '.join([str(tag) for tag in q_tags.all()])

register.filter('tags', tags)