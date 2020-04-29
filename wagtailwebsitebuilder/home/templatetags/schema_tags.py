from django import template
from django.utils.safestring import mark_safe

from home.schemas import Person, Product, Thing, Offer

register = template.Library()


@register.simple_tag(takes_context=True)
def person_schema(context):
    data = context['value']
    organisation = context['settings']['multisite']['Organisation'].schema
    image = None
    if data['image']:
        image = '{}{}'.format(
            context['request'].site.root_url,
            data['image'].get_rendition('original').url)

    url = data['url'].url if data['url'] else None

    person = Person(
        data['email'],
        organisation,
        name=data['name'],
        description=data['description'],
        image=image,
        url=url)
    return mark_safe(person.as_json)


@register.simple_tag(takes_context=True)
def product_schema(context):
    data = context['value']
    organisation = context['settings']['multisite']['Organisation'].schema
    image = None
    if data['image']:
        image = '{}{}'.format(
            context['request'].site.root_url,
            data['image'].get_rendition('original').url)

    url = data['url'].url if data['url'] else None

    price = data['price']
    price_currency = data['price_currency']
    sku = '{} | {}'.format(
        data['name'],
        organisation.name)

    product = Product(
        Thing(name=data['audience_type'], description=''),  # audience
        organisation,  # manufacturer
        organisation,  # brand
        sku=sku,
        offer=Offer(price, price_currency),
        name=data['name'],
        description=data['description'],
        image=image,
        url=url)
    return mark_safe(product.as_json)
