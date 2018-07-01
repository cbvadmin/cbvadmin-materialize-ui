required_settings = {
    'CBVADMIN_TEMPLATE_PACK': 'materialize',
    'CRISPY_TEMPLATE_PACK': 'materialize_css_forms',
    'CRISPY_ALLOWED_TEMPLATE_PACKS': ('materialize_css_forms',)
}


def update_cbvadmin_settings(settings):
    settings.update(required_settings)
    return settings
