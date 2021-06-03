from django.urls import path

# # from . import views
from .views import Bloglistview,Blogdetail,Createtview,updatetview,deleteview,AddcommentViews,AddCategoryView, CategoryView
# HomeView, mainview


urlpatterns = [

	#Leave as empty string for base url
	path('', Bloglistview.as_view(), name="home"),
	path('create/', Createtview.as_view(), name="create"),
	path('category/', AddCategoryView.as_view(), name="addcategory"),
    path('Blogdetail/<int:pk>/', Blogdetail.as_view(), name="Blogdetail"),
    path('Blogdetail/edit/<int:pk>/', updatetview.as_view(), name="updatetview"),
	path('Blogdetail/<int:pk>/delete', deleteview.as_view(), name="deletepost"),
	path('Blogdetail/<int:pk>/add_comment/', AddcommentViews.as_view(), name="add_comment"),
	path('category/<str:cats>/', CategoryView, name="category"),
	# the cats is short form for category



]