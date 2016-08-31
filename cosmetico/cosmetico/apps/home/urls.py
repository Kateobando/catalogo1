from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('cosmetico.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		

		url(r'^cosmetico/(?P<id_prod>.*)/$', 'single_cosmetic_view', name = 'vista_single_cosmetico'),
		url(r'^marca/(?P<id_prod>.*)/$', 'single_marca_view', name = 'vista_single_marca'),
		url(r'^categoria/(?P<id_prod>.*)/$', 'single_categoria_view', name = 'vista_single_categoria'),
		url(r'^color/(?P<id_prod>.*)/$', 'single_color_view', name = 'vista_single_color'),
		url(r'^ingredientes/(?P<id_prod>.*)/$', 'single_ingredientes_view', name = 'vista_single_ingredientes'),
		url(r'^advertencias/(?P<id_prod>.*)/$', 'single_advertencias_view', name = 'vista_single_advertencias'),	


		url(r'^cosmeticos/$', 'cosmeticos_view', name = 'vista_cosmeticos'),
		url(r'^cosmeticos/page/(?P<pagina>.*)/$', 'cosmeticos_view', name = 'vista_cosmeticos'),


		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		
		url(r'^registro/$','register_view',name='vista_registro'),

)