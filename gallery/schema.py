import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from gallery.models import GalleryImage


class ImageType(DjangoObjectType):
    class Meta:
        model = GalleryImage


class Query(ObjectType):
    image = graphene.Field(ImageType, id=graphene.Int())
    images = graphene.List(ImageType)

    def resolve_image(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return GalleryImage

        return None

    def resolve_images(self, info, **kwargs):
        return GalleryImage.objects.all()


class ImageInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    thumbnail = graphene.String()
    width = graphene.Int()
    height = graphene.Int()


class CreateImage(graphene.Mutation):
    class Aruguments:
        input = ImageInput(required=True)

    ok = graphene.Boolean()
    image = graphene.Field(ImageType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        image_instance = GalleryImage(title=input.title, thumbnail=input.thumbnail)
        image_instance.save()
        return CreateImage(ok=ok, image=image_instance)


class Mutation(graphene.ObjectType):
    create_image = CreateImage.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)