from django.contrib import admin

from .models import (Favorite, Follow, Ingredient, IngredientInRecipe,
                     Purchase, Recipe, Tag)


class IngredientInRecipeAdmin(admin.TabularInline):
    """ Класс для отображения таблицы c ингредиентами в админке рецепта. """
    model = IngredientInRecipe
    fk_name = 'recipe'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'favorited')
    list_filter = ('author', 'name', 'tags')
    exclude = ('ingredients',)

    inlines = [
        IngredientInRecipeAdmin,
    ]

    def favorited(self, obj):
        favorited_count = Favorite.objects.filter(recipe=obj).count()
        return favorited_count

    favorited.short_description = 'В избранном'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('^name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(Follow)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')


@admin.register(IngredientInRecipe)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


# admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(IngredientInRecipe, RecipeIngredientAdmin)
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Purchase, PurchaseAdmin)
# admin.site.register(Favorite, FavoriteAdmin)
# admin.site.register(Follow, SubscriptionAdmin)
