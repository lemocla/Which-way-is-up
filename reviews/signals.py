"""
Signal to update artwork rating by calculating ratings average
for a specified artwork when review is created, updated and deleted.
"""
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from reviews.models import Review


@receiver(post_save, sender=Review)
def update_rating_on_save(sender, instance, **kwargs):
    """
    Update artwork's average rating on review is created/updated.
    """
    if instance.artwork:
        instance.artwork.calculate_average_rating()


@receiver(pre_delete, sender=Review)
def update_rating_on_delete(sender, instance, **kwargs):
    """
    Update artwork's average rating when a review is deleted.
    """
    if instance.artwork and hasattr(instance, 'calc_average_rating'):
        instance.artwork.calc_average_rating()
