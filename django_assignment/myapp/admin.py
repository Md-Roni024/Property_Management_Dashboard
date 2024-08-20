# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Location, Amenity, Property, Image
# import os

# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'latitude', 'longitude', 'create_date', 'update_date')
#     search_fields = ('name', 'type')
#     list_filter = ('type','create_date','update_date')
#     list_per_page = 16
#     actions = ['update_properties']


# class AmenityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'create_date', 'update_date')
#     search_fields = ('name',)
#     list_per_page = 16
#     list_filter = ('create_date','update_date')
#     actions = ['update_properties']


# # class PropertyAdmin(admin.ModelAdmin):
# #     list_display = ('get_image_urls', 'title', 'description','price','room_type','rating','create_date', 'update_date', 'get_location_names', 'get_amenity_names')
# #     search_fields = ('title', 'description','rating')
# #     list_filter = ('amenities','room_type','create_date','update_date')
# #     list_per_page = 16

# #     def get_location_names(self, obj):
# #         return ", ".join([loc.name for loc in obj.locations.all()])
# #     get_location_names.short_description = 'Locations'

# #     def get_amenity_names(self, obj):
# #         return ", ".join([amenity.name for amenity in obj.amenities.all()])
# #     get_amenity_names.short_description = 'Amenities'

# #     def get_image_urls(self, obj):
# #         image = obj.images.first()
# #         if image:
# #             image_path = os.path.join(
# #                 image.image.url
# #             )
# #             print(f"Image URL: {image_path}")
# #             return format_html(
# #                 '<img src="{}" width="150" height="150" style="margin-right: 5px;">',
# #                 image_path
# #             )
# #         return "No image"

# #     def get_list_display_links(self, request, list_display):
# #         return ('title',) if 'title' in list_display else None


# class PropertyAdmin(admin.ModelAdmin):
#     list_display = (
#         'get_image_urls', 'title', 'description', 'price', 'room_type', 
#         'rating', 'create_date', 'update_date', 'get_location_names', 
#         'get_amenity_names'
#     )
#     search_fields = ('title', 'description', 'rating')
#     list_filter = ('amenities', 'room_type', 'create_date', 'update_date')
#     list_per_page = 16

#     def get_location_names(self, obj):
#         return ", ".join([loc.name for loc in obj.locations.all()])
#     get_location_names.short_description = 'Locations'

#     def get_amenity_names(self, obj):
#         return ", ".join([amenity.name for amenity in obj.amenities.all()])
#     get_amenity_names.short_description = 'Amenities'

#     def get_image_urls(self, obj):
#         image = obj.images.first()
#         if image:
#             image_path = image.image.url
#             return format_html(
#                 '<img src="{}" width="150" height="150" style="margin-right: 5px;">',
#                 image_path
#             )
#         return "No image found"
#     get_image_urls.short_description = 'Image Preview'

#     def formfield_for_dbfield(self, db_field, request, **kwargs):
#         if db_field.name == 'images':  # Assuming 'images' is a field on your Property model
#             kwargs['widget'] = admin.widgets.AdminFileWidget()  # You may need to adjust based on your actual field
#         return super().formfield_for_dbfield(db_field, request, **kwargs)

#     def get_list_display_links(self, request, list_display):
#         return ('title',) if 'title' in list_display else None

        
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('property', 'image_thumbnail', 'create_date', 'update_date')
#     search_fields = ('property__title',)
#     list_per_page = 16
#     list_filter = ('create_date', 'update_date')
#     def image_thumbnail(self, obj):
#         return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
    
#     image_thumbnail.short_description = 'Image Thumbnail'


# admin.site.register(Location, LocationAdmin)
# admin.site.register(Amenity, AmenityAdmin)
# admin.site.register(Property, PropertyAdmin)
# admin.site.register(Image, ImageAdmin)

# New Test
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Location, Amenity, Property, Image
# from django import forms
# from django.contrib.admin.widgets import AdminFileWidget

# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'latitude', 'longitude', 'create_date', 'update_date')
#     search_fields = ('name', 'type')
#     list_filter = ('type', 'create_date', 'update_date')
#     list_per_page = 16

# class AmenityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'create_date', 'update_date')
#     search_fields = ('name',)
#     list_filter = ('create_date', 'update_date')
#     list_per_page = 16

# class PropertyAdminForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance.pk:
#             # Optionally, you can filter queryset for better admin experience
#             self.fields['locations'].queryset = Location.objects.all()
#             self.fields['amenities'].queryset = Amenity.objects.all()

# class PropertyAdmin(admin.ModelAdmin):
#     form = PropertyAdminForm
#     list_display = (
#         'get_image_urls', 'title', 'description', 'price', 'room_type', 
#         'rating', 'create_date', 'update_date', 'get_location_names', 
#         'get_amenity_names'
#     )
#     search_fields = ('title', 'description', 'rating')
#     list_filter = ('amenities', 'room_type', 'create_date', 'update_date')
#     list_per_page = 16

#     def get_location_names(self, obj):
#         return ", ".join([loc.name for loc in obj.locations.all()])
#     get_location_names.short_description = 'Locations'

#     def get_amenity_names(self, obj):
#         return ", ".join([amenity.name for amenity in obj.amenities.all()])
#     get_amenity_names.short_description = 'Amenities'

#     def get_image_urls(self, obj):
#         images = obj.images.all()
#         if images:
#             image_tags = [
#                 format_html(
#                     '<img src="{}" width="150" height="150" style="margin-right: 5px;">',
#                     image.image.url
#                 ) for image in images
#             ]
#             return format_html(''.join(image_tags))
#         return "No image found"
#     get_image_urls.short_description = 'Image Preview'

#     def formfield_for_dbfield(self, db_field, request, **kwargs):
#         if db_field.name == 'images':
#             kwargs['widget'] = AdminFileWidget()  # Ensures file widgets are displayed properly
#         return super().formfield_for_dbfield(db_field, request, **kwargs)

#     def get_list_display_links(self, request, list_display):
#         return ('title',) if 'title' in list_display else None

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('image_thumbnail', 'property', 'create_date', 'update_date')
#     search_fields = ('property__title',)
#     list_filter = ('create_date', 'update_date')
#     list_per_page = 16

#     def image_thumbnail(self, obj):
#         return format_html('<img src="{}" width="60" height="60" />', obj.image.url) if obj.image else "No Image"
#     image_thumbnail.short_description = 'Image Thumbnail'

# admin.site.register(Location, LocationAdmin)
# admin.site.register(Amenity, AmenityAdmin)
# admin.site.register(Property, PropertyAdmin)
# admin.site.register(Image, ImageAdmin)


#Work
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Location, Amenity, Property, Image
# from django import forms
# from django.contrib.admin.widgets import AdminFileWidget
# from .forms import ImageForm


# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'latitude', 'longitude', 'create_date', 'update_date')
#     search_fields = ('name', 'type')
#     list_filter = ('type', 'create_date', 'update_date')
#     list_per_page = 16

# class AmenityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'create_date', 'update_date')
#     search_fields = ('name',)
#     list_filter = ('create_date', 'update_date')
#     list_per_page = 16

# class PropertyAdminForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance.pk:
#             self.fields['locations'].queryset = Location.objects.all()
#             self.fields['amenities'].queryset = Amenity.objects.all()

# class PropertyAdmin(admin.ModelAdmin):
#     form = PropertyAdminForm
#     list_display = (
#         'get_image_urls', 'title', 'description', 'price', 'room_type', 
#         'rating', 'create_date', 'update_date', 'get_location_names', 
#         'get_amenity_names'
#     )
#     search_fields = ('title', 'description', 'rating')
#     list_filter = ('amenities', 'room_type', 'create_date', 'update_date')
#     list_per_page = 16

#     def get_location_names(self, obj):
#         return ", ".join([loc.name for loc in obj.locations.all()])
#     get_location_names.short_description = 'Locations'

#     def get_amenity_names(self, obj):
#         return ", ".join([amenity.name for amenity in obj.amenities.all()])
#     get_amenity_names.short_description = 'Amenities'

#     def get_image_urls(self, obj):
#         images = obj.images.all()
#         if images:
#             image_tags = [
#                 format_html(
#                     '<img src="{}" width="150" height="150" style="margin-right: 5px;">',
#                     image.image.url
#                 ) for image in images
#             ]
#             return format_html(''.join(image_tags))
#         return "No image found"
#     get_image_urls.short_description = 'Image Preview'

#     def formfield_for_dbfield(self, db_field, request, **kwargs):
#         if db_field.name == 'images':
#             kwargs['widget'] = AdminFileWidget()  # Ensures file widgets are displayed properly
#         return super().formfield_for_dbfield(db_field, request, **kwargs)

#     def get_list_display_links(self, request, list_display):
#         return ('title',) if 'title' in list_display else None

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('property','image_thumbnail', 'create_date', 'update_date')
#     search_fields = ('property__title',)
#     list_filter = ('create_date', 'update_date')
#     list_per_page = 16

#     def image_thumbnail(self, obj):
#         return format_html('<img src="{}" width="60" height="60" />', obj.image.url) if obj.image else "No Image"
#     image_thumbnail.short_description = 'Image Thumbnail'

# admin.site.register(Location, LocationAdmin)
# admin.site.register(Amenity, AmenityAdmin)
# admin.site.register(Property, PropertyAdmin)
# admin.site.register(Image, ImageAdmin)


#Work

from django.contrib import admin
from .models import Location, Amenity, Property, Image
from django.utils.html import format_html
from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.forms import BaseInlineFormSet


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'latitude', 'longitude', 'create_date', 'update_date')
    search_fields = ('name', 'type')
    list_filter = ('type', 'create_date', 'update_date')
    list_per_page = 16

class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'update_date')
    search_fields = ('name',)
    list_filter = ('create_date', 'update_date')
    list_per_page = 16


# Define an inline formset for Image model
class ImageInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initialization code here if needed

class ImageInline(admin.TabularInline):
    model = Image
    formset = ImageInlineFormSet
    extra = 0  # Number of empty forms to display initially
    can_delete = True
    fields = ('image',)

class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['locations'].queryset = Location.objects.all()
            self.fields['amenities'].queryset = Amenity.objects.all()

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    inlines = [ImageInline]  # Add the ImageInline to the PropertyAdmin
    list_display = (
        'get_image_urls', 'title', 'description', 'price', 'room_type', 
        'rating', 'create_date', 'update_date', 'get_location_names', 
        'get_amenity_names'
    )
    search_fields = ('title', 'description', 'rating')
    list_filter = ('amenities', 'room_type', 'create_date', 'update_date')
    list_per_page = 16

    def get_location_names(self, obj):
        return ", ".join([loc.name for loc in obj.locations.all()])
    get_location_names.short_description = 'Locations'

    def get_amenity_names(self, obj):
        return ", ".join([amenity.name for amenity in obj.amenities.all()])
    get_amenity_names.short_description = 'Amenities'

    def get_image_urls(self, obj):
        images = obj.images.all()
        if images:
            image_tags = [
                format_html(
                    '<img src="{}" width="150" height="150" style="margin-right: 5px;">',
                    image.image.url
                ) for image in images
            ]
            return format_html(''.join(image_tags))
        return "No image found"
    get_image_urls.short_description = 'Image Preview'

    def get_list_display_links(self, request, list_display):
        return ('title',) if 'title' in list_display else None

class ImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image_thumbnail', 'create_date', 'update_date')
    search_fields = ('property__title',)
    list_filter = ('create_date', 'update_date')
    list_per_page = 16

    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="60" height="60" />', obj.image.url) if obj.image else "No Image"
    image_thumbnail.short_description = 'Image Thumbnail'

admin.site.register(Location, LocationAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Image, ImageAdmin)