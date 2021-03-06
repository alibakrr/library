from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Adı")
    last_name = models.CharField(max_length=50, verbose_name="Soyadı")
    birthday = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Doğum Tarihi")

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class WishAuthor(Author):
    pass


class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name="Adı")

    def __str__(self):
        return self.name


class WishPublisher(Publisher):
    pass


class BaseBook(models.Model):
    title = models.CharField(max_length=50, verbose_name="Kitap Adı", default='')

    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.title


class Book(BaseBook):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               verbose_name="Yazar")
    content = RichTextField(verbose_name="İçerik")
    book_image = models.FileField(blank=True, null=True,
                                  verbose_name="Kitaba Fotoğraf Ekleyebilirsiniz.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  default=None)


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             verbose_name="Kitap", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']


class FavouriteBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT,
                             verbose_name="Kitap")
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class WishBook(BaseBook):
    author = models.ForeignKey(WishAuthor, on_delete=models.CASCADE,
                               verbose_name="Yazar", default=None)
    publisher = models.ForeignKey(WishPublisher, on_delete=models.CASCADE,
                                  default=None)
