from parler.managers import TranslatableManager, TranslatableQuerySet
from polymorphic.managers import PolymorphicManager
from polymorphic.query import PolymorphicQuerySet


class ArtworkQuerySet(TranslatableQuerySet, PolymorphicQuerySet):
    pass

class ArtworkManager(PolymorphicManager, TranslatableManager):
    queryset_class = ArtworkQuerySet