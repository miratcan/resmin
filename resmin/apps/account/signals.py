from django.dispatch import Signal, receiver

from apps.account.tasks import follower_count_changed_callback_task

follower_count_changed = Signal()


@receiver(follower_count_changed)
def follower_count_changed_callback(sender, **kwargs):
	follower_count_changed_callback_task.delay(sender)