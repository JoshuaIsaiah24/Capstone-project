URLs you can test:

path('restaurant/menu/', include('restaurant.urls')),
path('restaurant/booking/', include(router.urls)),

Also:

path('menu/', views.MenuItemsView.as_view(), name="menu"),
path('menu/<int:pk>', views.SingleMenuItemsView.as_view()),
path('api-token-auth/', obtain_auth_token, name='api_token_auth'),