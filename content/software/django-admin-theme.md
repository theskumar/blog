Title: Quickly add custom branding to Django admin site
Slug: quickly-update-django-admin
Date: 2018-03-06 17:18:33
Tags: django, theming, admin
Category: 
Author: Saurabh Kumar
Lang: en
Summary: How to quickly customize django admin theme.

This is a quick 2mins guide to add custom branding to your Django Admin Site.

**Step-1:** Create a `admin/base_site.html` file inside your templates directory. 
**Step-2:** Copy/Paste the following snippet in that file.

```jinja
<!-- yoursite/templates/admin/base_site.html -->

{% extends "admin/base_site.html" %}
{% block extrastyle %}
<style>
  :root {
    --primary-color: #1d1d1b;
    --primary-color-faded: #585853;
    --secondary-color: #4dffba;
  }

  ::selection {
    background: var(--secondary-color);
    color:var(--primary-color);
    opacity:1
  }

  ::-moz-selection {
    background: var(--secondary-color);
    color:var(--primary-color);
    opacity:1
  }
  body {
    font-family:
          -apple-system,
          BlinkMacSystemFont,
          'Segoe UI',
          Roboto,
          Helvetica,
          Arial,
          sans-serif,
          'Apple Color Emoji',
          'Segoe UI Emoji',
          'Segoe UI Symbol';
  }
  #branding h1, #branding h1 a:link, #branding h1 a:visited {
    color: #ffffff;
    font-weight: 400;
  }

  #header {
    background: var(--primary-color);
  }
  .module h2, .module caption, .inline-group h2 {
    background-color: var(--primary-color-faded);
  }
  div.breadcrumbs {
    background: var(--primary-color-faded);
  }
  a:link, a:visited {
    color: var(--primary-color-faded);
  }
  .selector-chosen h2 {
    background: var(--primary-color-faded) !important;
  }
  .button, input[type=submit], input[type=button], .submit-row input, a.button {
    background: var(--primary-color-faded);
  }
  .button.default, input[type=submit].default, .submit-row input.default {
    background: var(--primary-color);
  }
  .button:active, input[type=submit]:active, input[type=button]:active, .button:focus, input[type=submit]:focus, input[type=button]:focus, .button:hover, input[type=submit]:hover, input[type=button]:hover {
    background: var(--primary-color-faded);
    opacity: 0.8;
  }
  .button.default:active, input[type=submit].default:active, .button.default:focus, input[type=submit].default:focus, .button.default:hover, input[type=submit].default:hover {
    background: var(--primary-color);
    opacity: 0.8;
  }
</style>
{% endblock %}
```

**Step-3:** Now modify the following css variables in the above file as per your brand colors.

```scss
:root {
    --primary-color: #1d1d1b;
    --primary-color-faded: #585853;
    --secondary-color: #4dffba;
}
```

**Step-4:** Reload your admin site and you should see updated theme!

!!! tip "Take Away"
    CSS Variables is a powerful feature you can use to add custom themes.

---