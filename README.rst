=======================
CBVadmin Materialize UI
=======================

Template pack for CBVadmin using MaterializeCSS framework

Require following existing django packages.

- materialize_css_forms

Installing and configuring
==========================

``pip install cbvadmin-materialize-ui``

Add the following to django settings.py for automatic configuration

.. code-block:: python

    from cbvadmin_materialize_ui.settings import update_cbvadmin_settings
    ...
    update_cbvadmin_settings(locals())

Or do manual config

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'cbvadmin_materialize_ui',
        'materialize_css_forms'
    ]
    ...
    CBVADMIN_TEMPLATE_PACK': 'materialize',
    CRISPY_TEMPLATE_PACK': 'materialize_css_forms',
    CRISPY_ALLOWED_TEMPLATE_PACKS': ('materialize_css_forms',)
