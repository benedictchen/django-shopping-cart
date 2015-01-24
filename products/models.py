from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=100.00, validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return unicode(reverse('detail', kwargs=kwargs))

    def __unicode__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='product/images/')
    is_featured = models.BooleanField(default=False)
    is_thumbnail = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return ''.join([self.product.title, ' (image #', unicode(self.id), ') '])


VARIATION_CATEGORIES = (
    ('size', 'Size'),
    ('color', 'Color'),
    ('package', 'Package'),
)


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def all_sizes(self):
        return self.all().filter(category='size')

    def all_colors(self):
        return self.all().filter(category='color')

    def variation_by_category(self):
        return [(category[0], self.filter(category=category[0])) for category in VARIATION_CATEGORIES]


class Variation(models.Model):
    """A variation on a particular product"""
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=VARIATION_CATEGORIES, default=VARIATION_CATEGORIES[0])
    image = models.ForeignKey(ProductImage, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100,
                                validators=[MinValueValidator(0)], null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __unicode__(self):
        return ' | ' + self.title + ' | <' + self.category + '> of ' + self.product.title
